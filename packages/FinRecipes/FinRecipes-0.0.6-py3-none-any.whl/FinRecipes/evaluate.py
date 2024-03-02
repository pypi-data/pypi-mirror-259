import numpy as np
# from empyrical import max_drawdown, alpha_beta
from six import iteritems
import pandas as pd
from copy import deepcopy

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import pyfolio
from pyfolio import timeseries
import config

APPROX_BDAYS_PER_MONTH = 21
APPROX_BDAYS_PER_YEAR = 252

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52
QTRS_PER_YEAR = 4

DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'
YEARLY = 'yearly'

ANNUALIZATION_FACTORS = {
    DAILY: APPROX_BDAYS_PER_YEAR,
    WEEKLY: WEEKS_PER_YEAR,
    MONTHLY: MONTHS_PER_YEAR,
    QUARTERLY: QTRS_PER_YEAR,
    YEARLY: 1
}

nanmean = np.nanmean
nanmin = np.nanmin
nanstd = np.nanstd

def _to_pandas(ob):
    if isinstance(ob, (pd.Series, pd.DataFrame)):
        return ob

    if ob.ndim == 1:
        return pd.Series(ob)
    elif ob.ndim == 2:
        return pd.DataFrame(ob)
    else:
        raise ValueError(
            'cannot convert array of dim > 2 to a pandas structure',
        )

def _aligned_series(*many_series):
    head = many_series[0]
    tail = many_series[1:]
    n = len(head)
    if (isinstance(head, np.ndarray) and
            all(len(s) == n and isinstance(s, np.ndarray) for s in tail)):
        # optimization: ndarrays of the same length are already aligned
        return many_series

    # dataframe has no ``itervalues``
    return (
        v
        for _, v in iteritems(pd.concat(map(_to_pandas, many_series), axis=1))
    )

def beta_aligned(returns, factor_returns, risk_free=0.0, out=None):
    # Cache these as locals since we're going to call them multiple times.
    nan = np.nan
    isnan = np.isnan

    returns_1d = returns.ndim == 1
    if returns_1d:
        returns = np.asanyarray(returns)[:, np.newaxis]

    if factor_returns.ndim == 1:
        factor_returns = np.asanyarray(factor_returns)[:, np.newaxis]

    N, M = returns.shape

    if out is None:
        out = np.full(M, nan)
    elif out.ndim == 0:
        out = out[np.newaxis]

    if len(returns) < 1 or len(factor_returns) < 2:
        out[()] = nan
        if returns_1d:
            out = out.item()
        return out

    # Copy N times as a column vector and fill with nans to have the same
    # missing value pattern as the dependent variable.
    #
    # PERF_TODO: We could probably avoid the space blowup by doing this in
    # Cython.

    # shape: (N, M)
    independent = np.where(
        isnan(returns),
        nan,
        factor_returns,
    )

    # Calculate beta as Cov(X, Y) / Cov(X, X).
    # https://en.wikipedia.org/wiki/Simple_linear_regression#Fitting_the_regression_line  # noqa
    #
    # NOTE: The usual formula for covariance is::
    #
    #    mean((X - mean(X)) * (Y - mean(Y)))
    #
    # However, we don't actually need to take the mean of both sides of the
    # product, because of the folllowing equivalence::
    #
    # Let X_res = (X - mean(X)).
    # We have:
    #
    #     mean(X_res * (Y - mean(Y))) = mean(X_res * (Y - mean(Y)))
    #                             (1) = mean((X_res * Y) - (X_res * mean(Y)))
    #                             (2) = mean(X_res * Y) - mean(X_res * mean(Y))
    #                             (3) = mean(X_res * Y) - mean(X_res) * mean(Y)
    #                             (4) = mean(X_res * Y) - 0 * mean(Y)
    #                             (5) = mean(X_res * Y)
    #
    #
    # The tricky step in the above derivation is step (4). We know that
    # mean(X_res) is zero because, for any X:
    #
    #     mean(X - mean(X)) = mean(X) - mean(X) = 0.
    #
    # The upshot of this is that we only have to center one of `independent`
    # and `dependent` when calculating covariances. Since we need the centered
    # `independent` to calculate its variance in the next step, we choose to
    # center `independent`.

    ind_residual = independent - nanmean(independent, axis=0)

    covariances = nanmean(ind_residual * returns, axis=0)

    # We end up with different variances in each column here because each
    # column may have a different subset of the data dropped due to missing
    # data in the corresponding dependent column.
    # shape: (M,)
    np.square(ind_residual, out=ind_residual)
    independent_variances = nanmean(ind_residual, axis=0)
    independent_variances[independent_variances < 1.0e-30] = np.nan

    np.divide(covariances, independent_variances, out=out)

    if returns_1d:
        out = out.item()

    return out

def alpha_beta_aligned(returns,
                       factor_returns,
                       risk_free=0.0,
                       period=DAILY,
                       annualization=None,
                       out=None):
    
    if out is None:
        out = np.empty(returns.shape[1:] + (2,), dtype='float64')

    b = beta_aligned(returns, factor_returns, risk_free, out=out[..., 1])
    alpha_aligned(
        returns,
        factor_returns,
        risk_free,
        period,
        annualization,
        out=out[..., 0],
        _beta=b,
    )

    return out

def annualization_factor(period, annualization):
    if annualization is None:
        try:
            factor = ANNUALIZATION_FACTORS[period]
        except KeyError:
            raise ValueError(
                "Period cannot be '{}'. "
                "Can be '{}'.".format(
                    period, "', '".join(ANNUALIZATION_FACTORS.keys())
                )
            )
    else:
        factor = annualization
    return factor

def _adjust_returns(returns, adjustment_factor):
    if isinstance(adjustment_factor, (float, int)) and adjustment_factor == 0:
        return returns
    return returns - adjustment_factor

def alpha_aligned(returns,
                  factor_returns,
                  risk_free=0.0,
                  period=DAILY,
                  annualization=None,
                  out=None,
                  _beta=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:], dtype='float64')

    if len(returns) < 2:
        out[()] = np.nan
        if returns.ndim == 1:
            out = out.item()
        return out

    ann_factor = annualization_factor(period, annualization)

    if _beta is None:
        _beta = beta_aligned(returns, factor_returns, risk_free)

    adj_returns = _adjust_returns(returns, risk_free)
    adj_factor_returns = _adjust_returns(factor_returns, risk_free)
    alpha_series = adj_returns - (_beta * adj_factor_returns)

    out = np.subtract(
        np.power(
            np.add(
                nanmean(alpha_series, axis=0, out=out),
                1,
                out=out
            ),
            ann_factor,
            out=out
        ),
        1,
        out=out
    )

    if allocated_output and isinstance(returns, pd.DataFrame):
        out = pd.Series(out)

    if returns.ndim == 1:
        out = out.item()

    return out

def alpha_beta(returns,
               factor_returns,
               risk_free=0.0,
               period=DAILY,
               annualization=None,
               out=None):
    returns, factor_returns = _aligned_series(returns, factor_returns)

    return alpha_beta_aligned(
        returns,
        factor_returns,
        risk_free=risk_free,
        period=period,
        annualization=annualization,
        out=out,
    )

def cum_returns(returns, starting_value=0, out=None):
    if len(returns) < 1:
        return returns.copy()

    nanmask = np.isnan(returns)
    if np.any(nanmask):
        returns = returns.copy()
        returns[nanmask] = 0

    allocated_output = out is None
    if allocated_output:
        out = np.empty_like(returns)

    np.add(returns, 1, out=out)
    out.cumprod(axis=0, out=out)

    if starting_value == 0:
        np.subtract(out, 1, out=out)
    else:
        np.multiply(out, starting_value, out=out)

    if allocated_output:
        if returns.ndim == 1 and isinstance(returns, pd.Series):
            out = pd.Series(out, index=returns.index)
        elif isinstance(returns, pd.DataFrame):
            out = pd.DataFrame(
                out, index=returns.index, columns=returns.columns,
            )

    return out

def max_drawdown(returns, out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])

    returns_1d = returns.ndim == 1

    if len(returns) < 1:
        out[()] = np.nan
        if returns_1d:
            out = out.item()
        return out

    returns_array = np.asanyarray(returns)

    cumulative = np.empty(
        (returns.shape[0] + 1,) + returns.shape[1:],
        dtype='float64',
    )
    cumulative[0] = start = 100
    cum_returns(returns_array, starting_value=start, out=cumulative[1:])

    max_return = np.fmax.accumulate(cumulative, axis=0)

    nanmin((cumulative - max_return) / max_return, axis=0, out=out)
    if returns_1d:
        out = out.item()
    elif allocated_output and isinstance(returns, pd.DataFrame):
        out = pd.Series(out)

    return out

def cum_returns_final(returns, starting_value=0):
    if len(returns) == 0:
        return np.nan

    if isinstance(returns, pd.DataFrame):
        result = (returns + 1).prod()
    else:
        result = np.nanprod(returns + 1, axis=0)

    if starting_value == 0:
        result -= 1
    else:
        result *= starting_value

    return result

def annual_return(returns, period=DAILY, annualization=None):
    if len(returns) < 1:
        return np.nan

    ann_factor = annualization_factor(period, annualization)
    num_years = len(returns) / ann_factor
    # Pass array to ensure index -1 looks up successfully.
    ending_value = cum_returns_final(returns, starting_value=1)

    return ending_value ** (1 / num_years) - 1

def cagr(returns, period=DAILY, annualization=None):
    return annual_return(returns, period, annualization)


def annual_volatility(returns, period=DAILY, alpha=2.0,
                      annualization=None):
    """
    Determines the annual volatility of a strategy.

    Parameters
    ----------
    returns : :py:class:`pandas.Series`
        Daily returns of the strategy, noncumulative.
        See full explanation in :func:`~empyrical.stats.cum_returns`.
    period : :class:`str`, optional
        Defines the periodicity of the 'returns' data for purposes of
        annualizing. Value ignored if `annualization` parameter is specified.
        See full explanation in :func:`~empyrical.stats.annual_return`.
    alpha : :class:`float`, optional
        Scaling relation (Levy stability exponent).
    annualization : :class:`int`, optional
        Used to suppress default values available in `period` to convert
        returns into annual returns. Value should be the annual frequency of
        `returns`.

    Returns
    -------
    :class:`float`
        Annual volatility.
    """

    if len(returns) < 2:
        return np.nan

    ann_factor = annualization_factor(period, annualization)

    volatility = returns.std() * (ann_factor ** (1.0 / alpha))

    return volatility

def half_yearly_volatility(returns, period=DAILY, alpha=2.0,
                      annualization=None):
    """
    Determines the annual volatility of a strategy.

    Parameters
    ----------
    returns : :py:class:`pandas.Series`
        Daily returns of the strategy, noncumulative.
        See full explanation in :func:`~empyrical.stats.cum_returns`.
    period : :class:`str`, optional
        Defines the periodicity of the 'returns' data for purposes of
        annualizing. Value ignored if `annualization` parameter is specified.
        See full explanation in :func:`~empyrical.stats.annual_return`.
    alpha : :class:`float`, optional
        Scaling relation (Levy stability exponent).
    annualization : :class:`int`, optional
        Used to suppress default values available in `period` to convert
        returns into annual returns. Value should be the annual frequency of
        `returns`.

    Returns
    -------
    :class:`float`
        Annual volatility.
    """

    if len(returns) < 2:
        return np.nan

    # ann_factor = annualization_factor(period, annualization)
    ann_factor = 126

    volatility = returns.std() * (ann_factor ** (1.0 / alpha))

    return volatility

def sharpe_ratio_six(returns,
                 risk_free=0,
                 period=DAILY,
                 annualization=None,
                 out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])

    return_1d = returns.ndim == 1

    if len(returns) < 2:
        out[()] = np.nan
        if return_1d:
            out = out.item()
        return out

    returns_risk_adj = np.asanyarray(_adjust_returns(returns, risk_free))
    ann_factor = annualization_factor(period, annualization)

    np.multiply(
        np.divide(
            nanmean(returns_risk_adj, axis=0),
            nanstd(returns_risk_adj, ddof=1, axis=0),
            out=out,
        ),
        np.sqrt(len(returns)),
        out=out,
    )
    if return_1d:
        out = out.item()

    return out

def sharpe_ratio(returns,
                 risk_free=0,
                 period=DAILY,
                 annualization=None,
                 out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])

    return_1d = returns.ndim == 1

    if len(returns) < 2:
        out[()] = np.nan
        if return_1d:
            out = out.item()
        return out

    returns_risk_adj = np.asanyarray(_adjust_returns(returns, risk_free))
    ann_factor = annualization_factor(period, annualization)

    np.multiply(
        np.divide(
            nanmean(returns_risk_adj, axis=0),
            nanstd(returns_risk_adj, ddof=1, axis=0),
            out=out,
        ),
        np.sqrt(ann_factor),
        out=out,
    )
    if return_1d:
        out = out.item()

    return out

def downside_risk(returns,
                  required_return=0,
                  period=DAILY,
                  annualization=None,
                  out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])

    returns_1d = returns.ndim == 1

    if len(returns) < 1:
        out[()] = np.nan
        if returns_1d:
            out = out.item()
        return out

    ann_factor = annualization_factor(period, annualization)

    downside_diff = np.clip(
        _adjust_returns(
            np.asanyarray(returns),
            np.asanyarray(required_return),
        ),
        np.NINF,
        0,
    )

    np.square(downside_diff, out=downside_diff)
    nanmean(downside_diff, axis=0, out=out)
    np.sqrt(out, out=out)
    np.multiply(out, np.sqrt(ann_factor), out=out)

    if returns_1d:
        out = out.item()
    elif isinstance(returns, pd.DataFrame):
        out = pd.Series(out, index=returns.columns)
    return out


def sortino_ratio(returns,
                  required_return=0,
                  period=DAILY,
                  annualization=None,
                  out=None,
                  _downside_risk=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])

    return_1d = returns.ndim == 1

    if len(returns) < 2:
        out[()] = np.nan
        if return_1d:
            out = out.item()
        return out

    adj_returns = np.asanyarray(_adjust_returns(returns, required_return))

    ann_factor = annualization_factor(period, annualization)

    average_annual_return = nanmean(adj_returns, axis=0) * ann_factor
    annualized_downside_risk = (
        _downside_risk
        if _downside_risk is not None else
        downside_risk(returns, required_return, period, annualization)
    )
    np.divide(average_annual_return, annualized_downside_risk, out=out)
    if return_1d:
        out = out.item()
    elif isinstance(returns, pd.DataFrame):
        out = pd.Series(out)

    return out

# class performance_evaluation():
#     def __init__(self, baseline_list, startDate, endDate):
#         self.baseline_list = baseline_list
#         self.startDate = startDate
#         self.endDate = endDate
               
#     def baseline_evaluation(self):

#         print("==============Get Baseline Stats===========")
#         baseline_returns = dict()
#         for baseline in self.baseline_list:
            
#             print("\n for", baseline)
#             baseline_df = get_baseline(
#                     ticker=baseline, start=self.startDate, end=self.endDate  # '^GSPC'
#                 )

#             baseline_returns[baseline] = get_daily_return(baseline_df, value_col_name="close").fillna(0)
#             # baseline_returns_list.append(baseline_returns)

#             stats = backtest_stats(baseline_df, value_col_name = 'close')

#         return baseline_returns



def get_daily_return(df, value_col_name="account_value"):
    df = deepcopy(df)
    df["daily_return"] = df[value_col_name].pct_change(1)
    df["date"] = pd.to_datetime(df["date"],utc=True)
    df.set_index("date", inplace=True, drop=True)
    # df.index = df.index.tz_localize("YN")
    return pd.Series(df["daily_return"], index=df.index)


def convert_daily_return_to_pyfolio_ts(df):
    strategy_ret = df.copy()
    strategy_ret["date"] = pd.to_datetime(strategy_ret["date"])
    strategy_ret.set_index("date", drop=False, inplace=True)
    strategy_ret.index = strategy_ret.index.tz_localize("UTC")
    del strategy_ret["date"]
    return pd.Series(strategy_ret["daily_return"].values, index=strategy_ret.index)


def backtest_stats(account_value, value_col_name="account_value"):
    dr_test = get_daily_return(account_value, value_col_name=value_col_name)
    perf_stats_all = timeseries.perf_stats(
        returns=dr_test,
        positions=None,
        transactions=None,
        turnover_denom="AGB",
    )
    print(perf_stats_all)
    return perf_stats_all


def backtest_plot(
    account_value,
    baseline_start='2022-03-01',
    baseline_end='2022-10-16',
    baseline_ticker="^DJI",
    value_col_name="account_value",
):
    df = deepcopy(account_value)
    df["date"] = pd.to_datetime(df["date"])
    test_returns = get_daily_return(df, value_col_name=value_col_name)

    baseline_df = get_baseline(
        ticker=baseline_ticker, start=baseline_start, end=baseline_end
    )

    baseline_df["date"] = pd.to_datetime(baseline_df["date"], format="%Y-%m-%d")
    baseline_df = pd.merge(df[["date"]], baseline_df, how="left", on="date")
    baseline_df = baseline_df.fillna(method="ffill").fillna(method="bfill")
    baseline_returns = get_daily_return(baseline_df, value_col_name="close")

    with pyfolio.plotting.plotting_context(font_scale=1.1):
        pyfolio.create_full_tear_sheet(
            returns=test_returns, benchmark_rets=baseline_returns, set_context=False
        )


def get_baseline(ticker, start, end):
    return YahooDownloader(
        start_date=start, end_date=end, ticker_list=[ticker]
    ).fetch_data()


def trx_plot(df_trade, df_actions, ticker_list):
    df_trx = pd.DataFrame(np.array(df_actions["transactions"].to_list()))
    df_trx.columns = ticker_list
    df_trx.index = df_actions["date"]
    df_trx.index.name = ""

    for i in range(df_trx.shape[1]):
        df_trx_temp = df_trx.iloc[:, i]
        df_trx_temp_sign = np.sign(df_trx_temp)
        buying_signal = df_trx_temp_sign.apply(lambda x: x > 0)
        selling_signal = df_trx_temp_sign.apply(lambda x: x < 0)

        tic_plot = df_trade[
            (df_trade["tic"] == df_trx_temp.name)
            & (df_trade["date"].isin(df_trx.index))
        ]["close"]
        tic_plot.index = df_trx_temp.index

        plt.figure(figsize=(10, 8))
        plt.plot(tic_plot, color="g", lw=2.0)
        plt.plot(
            tic_plot,
            "^",
            markersize=10,
            color="m",
            label="buying signal",
            markevery=buying_signal,
        )
        plt.plot(
            tic_plot,
            "v",
            markersize=10,
            color="k",
            label="selling signal",
            markevery=selling_signal,
        )
        plt.title(
            f"{df_trx_temp.name} Num Transactions: {len(buying_signal[buying_signal == True]) + len(selling_signal[selling_signal == True])}"
        )
        plt.legend()
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=25))
        plt.xticks(rotation=45, ha="right")
        plt.show()

# def visualize(prices, long_ticks, short_ticks, total_reward,dates, name_string):
#     plt.figure(figsize=(15,6))
#     plt.cla()
#     plt.plot(dates,prices)
#     plt.plot(dates[short_ticks], prices[short_ticks], 'ro')
#     plt.plot(dates[long_ticks], prices[long_ticks], 'go')

#     for i in range(len(long_ticks)):
#         buy = long_ticks[i]
#         sell = short_ticks[i] if i < len(short_ticks) else len(prices)-1

#         if prices[sell] > prices[buy]:
#             plt.axvspan(dates[buy], dates[sell], color='green', alpha = 0.3)
#         else:
#             plt.axvspan(dates[buy], dates[sell], color='red', alpha = 0.3)

#     # plt.suptitle(
#     #     "Total Reward: %.6f" % total_reward + ' ~ ' +
#     #     "CAGR: %.2f" % cagr(prices, long_ticks, short_ticks, len(prices))
#     # )

#     stmp = datetime.now().strftime("%H-%M-%S")

#     plt.savefig(figdir + '/' + ticker + stmp + name_string + '.jpeg',bbox_inches='tight')
#     # plt.show()



if __name__ == "__main__":
    returns = pd.read_csv("Results/df_daily_return.csv")
    # returns = np.array([0, .44, .03, -.4, -.06, -.02])
    # print()
    returns = np.array(returns['daily_return'])
    benchmark_returns = np.array([.02, .02, .03, -.35, -.05, -.01])

    # calculate the max drawdown
    max_drawdown = max_drawdown(returns)
    CAGR = cagr(returns)

    Sharpe_ratio = sharpe_ratio(returns)
    Sotino_ratio = sortino_ratio(returns)
    # calculate alpha and beta
    alpha, beta = alpha_beta(returns, benchmark_returns)
    print(alpha,beta)
    print(Sharpe_ratio,CAGR)

