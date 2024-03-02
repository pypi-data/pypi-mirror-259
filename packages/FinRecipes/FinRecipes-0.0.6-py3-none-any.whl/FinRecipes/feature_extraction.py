import os
import pandas as pd
from stockstats import StockDataFrame as Sdf
from scipy.stats import kurtosis
from scipy.stats import skew
import numpy as np
import quandl
# import config_ms
# import config_po as config
import progressbar
import time
# import talib
# from lib.dc_finta import TA
from .utils import data_split
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# from finrl.meta.preprocessor.preprocessors import data_split

# disable all warnings
# import warnings
# warnings.filterwarnings("ignore")

def kurtosis_Comp(data, ndays=60):
    colName = 'kurt'
    kurt = pd.Series(data['close'].pct_change().rolling(
        ndays).kurt(), name=colName)
    data = data.join(kurt)
    return data

def skew_Comp(data, ndays=60):
    colName = 'skew'
    skew = pd.Series(data['close'].pct_change().rolling(
        ndays).skew(), name=colName)
    data = data.join(skew)
    return data

def cci(data, ndays):
  colName = 'cci_'+str(ndays)
  data['TP'] = (data['high'] + data['low'] + data['close']) / 3 
  data['sma'] = data['TP'].rolling(ndays).mean()
  data['mad'] = data['TP'].rolling(ndays).apply(lambda x: pd.Series(x).mad())
  data[colName] = (data['TP'] - data['sma']) / (0.015 * data['mad']) 
  return data

# Returns ATR values
def atr(high, low, close, n=14):
    tr = np.amax(np.vstack(((high - low).to_numpy(), (abs(high - close)).to_numpy(), (abs(low - close)).to_numpy())).T, axis=1)
    return pd.Series(tr).rolling(n).mean().to_numpy()

# Simple Moving Average 
def sma(data, ndays): 
    colName = 'sma_'+str(ndays)
    SMA = pd.Series(data['close'].rolling(ndays).mean(), name = colName) 
    data = data.join(SMA) 
    return data

# Exponentially-weighted Moving Average (also called EMA)
def ema(data, ndays): 
    colName =  'ema_' + str(ndays)
    EMA = pd.Series(data['close'].ewm(span = ndays, min_periods = ndays - 1).mean(), 
                 name = colName) 
    data = data.join(EMA) 
    return data

def macd(data):
  # Get the 12-day EMA of the closing price
  k = data['close'].ewm(span=12, adjust=False, min_periods=12).mean()
  # Get the 26-day EMA of the closing price
  d = data['close'].ewm(span=26, adjust=False, min_periods=26).mean()
  # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
  macd = k - d
  # print(macd)
  # Get the 9-Day EMA of the MACD for the Trigger line
  macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
  # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
  macd_h = macd - macd_s
  # Add all of our new values for the MACD to the dataframe
  data['macd'] = macd
  data['macd_h'] = macd_h
  data['macd_s'] = macd_s

  return data

# Compute the Bollinger Bands 
def bbands(data, n):
    MA = data['close'].rolling(window=n).mean()
    SD = data['close'].rolling(window=n).std()
#     data['MiddleBand'] = MA
    data['boll_ub'] = MA + (2 * SD) 
    data['boll_lb'] = MA - (2 * SD)
    return data

# Returns RSI values
def rsi(data, periods = 14):
    colName = 'rsi_'+str(periods)
    close = data['close']
    close_delta = close.diff()
    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()

    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    data[colName] = rsi
    return data

def volatility_compute(df_tic,lookback_tech_indicator=252):

    df_tic['volatility']= df_tic['close'].pct_change().rolling(lookback_tech_indicator).std()*(252**0.5)
    return df_tic

def volatility_percent(df_tics_raw,startDate,Q_start,Q_end,tickers_list):
    # uniqueDates = df_tics_raw.date.unique()
    # df_tics_raw_dates = pd.DataFrame(uniqueDates,columns=['date'])

    # interestRates = pd.read_csv(path_interest,header='infer')
    # interestRates = interestRates.rename(columns = {'DATE':'date','DTB3':'Interest_rate'})       #['date','Interest_rate']
    # interestRates['date'] = pd.to_datetime(interestRates['date'] , infer_datetime_format=True)      # change datatype of date column
    
    # interestRates = df_tics_raw_dates.merge(interestRates, on='date', how='left')
    # interestRates = interestRates[(interestRates['date']>=startDate) & (interestRates['date']<=Q_end)]
    # interestRates = interestRates.replace('.', np.nan).ffill()
    # interestRates['Interest_rate'] = interestRates.Interest_rate.apply(lambda x: float(x)/100)     # change datatype of str to
    # interestRates.rename(columns={'Interest_rate':'rate'},inplace=True)

    # if Q_end != interestRates.date.iloc[-1]:
    #     raise ValueError('ERROR: 3Months_US_treasury_bill_rate.csv is not updated.')

    #%% add volatility and interest rate to the dataframe
    uniqueDates = df_tics_raw.date.unique()
    df_dates = pd.DataFrame(uniqueDates,columns=['date'])
    print('Unique dates count = ',len(uniqueDates))
    df_tics = []
    volatility_window_size = 60    # for annual volatility

    for tic in tickers_list:
        df_tic_raw = df_tics_raw[df_tics_raw.tic == tic]
        df_tic = df_dates.merge(df_tic_raw, on='date', how='left')
        print(tic,'|| Length of data:',len(df_tic_raw),'|| missing values:',df_tic.close.isna().sum())
        # df_tic = df_tic.merge(interestRates,how='left', on='date')
        df_tic['tic'] = tic
        df_tic = df_tic.fillna(method='bfill').fillna(method='ffill')
        # df_tic = df_tic.fillna(method='bfill', axis=0)
        df_tic['volatility']= df_tic['close'].pct_change().rolling(volatility_window_size).std()*(252**0.5)
        df_tic = df_tic[(df_tic['date']>=startDate) & (df_tic['date']<=Q_end)]
        df_tics.append(df_tic)

    df = pd.concat(df_tics)
    df.reset_index(drop=True,inplace=True)
    df = df[(df.date>=startDate) & (df.date <= Q_end)]
    df = df.dropna()
    if (df.isnull().sum() != 0).any():
        raise Exception("Check df, there are null values")

    return df

def append_macro_data(df_tic):
    path_local_datasets = os.path.normpath(os.getcwd() + os.sep + os.pardir+ os.sep + os.pardir+ os.sep + os.pardir)
    filepath_macro_data = path_local_datasets+'\Database\Macro_data\df_macro_18-12-2022.h5'
    df_macro_data = pd.read_hdf(filepath_macro_data, "df",mode = 'r')
    df_macro_data.rename(columns={'DATE':'date'},inplace=True)
    df_tic = df_tic.merge(df_macro_data,on='date', how='left')
    return df_tic


def append_PCR_data(df_tic, api_key):
    quandl.ApiConfig.api_key = api_key
    df_tic_PCR = quandl.get('QOA/MSFT', start_date=df_tic['date'].iloc[0], end_date=df_tic['date'].iloc[-1])
    df_tic_PCR.reset_index(inplace = True)
    df_tic_PCR.rename(columns={'Date':'date'},inplace=True)
    df_tic = df_tic.merge(df_tic_PCR,on='date', how='left')
    return df_tic

def add_features(df_tics_raw,features_list,lookback_tech_indicator, train_startDate,valid_startDate,trade_startDate,trade_endDate,norm_flag):
    tickers_list = df_tics_raw.tic.unique().tolist()
    uniqueDates = df_tics_raw.date.unique()
    df_dates = pd.DataFrame(uniqueDates, columns=['date']).sort_values(by='date')
    print('Unique dates count = %d\n'%(len(uniqueDates)))
    df_tics = []
    for tic in tickers_list:
        df_tic = df_tics_raw[df_tics_raw.tic == tic]
        df_tic = df_dates.merge(df_tic, on='date', how='left')
        print("%5s,   length = %6d,   null values filled = %6d "%(tic, len(df_tic),df_tic['close'].isna().sum()))
        df_tic = skew_Comp(df_tic,lookback_tech_indicator)
        df_tic = kurtosis_Comp(df_tic,lookback_tech_indicator)
        df_tic = append_macro_data(df_tic)
        df_tic = append_PCR_data(df_tic)
        # df_tic = volatility_compute(df_tic,lookback_tech_indicator=60)
        # print(tic)
        # print(df_tic['close'].index[df_tic['close'].apply(np.isnan)])
        # print(df_tic['skew'].index[df_tic['skew'].apply(np.isnan)])
        # df_tic = rsi(df_tic,10)
        df_tic = df_tic.fillna(method='bfill').fillna(method='ffill')
        df_tics.append(df_tic)
    df = pd.concat(df_tics)
    # df = df[(df['date'] >= df_dates.iloc[60].values[0])].reset_index(drop=True)
    print('\nShape of dataframe =',df.shape)

    if norm_flag == True:
        train = data_split(df, train_startDate, valid_startDate).reset_index(drop=True)
        valid = data_split(df, valid_startDate, trade_startDate).reset_index(drop=True)
        trade = data_split(df, trade_startDate, trade_endDate).reset_index(drop=True)
        train_norm = []
        valid_norm = []
        trade_norm = []
        mean_var = dict()
        for i, tic in enumerate(train.tic.unique()):
            df_tic_train = train[train.tic == tic]
            df_tic_valid = valid[valid.tic == tic]
            df_tic_trade = trade[trade.tic == tic]

            mean_var_dict = dict()
            # mean_var_dict['tic'] = tic
            for j,indicator in enumerate(features_list):
                mu = df_tic_train[indicator].mean()
                sd = df_tic_train[indicator].std()

                mean_var_dict[indicator] = (mu,sd)
                
                df_tic_train[indicator] = (df_tic_train[indicator] - mu)/sd
                df_tic_valid[indicator] = (df_tic_valid[indicator] - mu)/sd
                df_tic_trade[indicator] = (df_tic_trade[indicator] - mu)/sd

            if tic == 'BRK-B':
                tic = 'BRK.B'
            mean_var[tic] = mean_var_dict

            train_norm.append(df_tic_train)
            valid_norm.append(df_tic_valid)
            trade_norm.append(df_tic_trade)
            
        train_norm = pd.concat(train_norm)
        valid_norm = pd.concat(valid_norm)
        trade_norm = pd.concat(trade_norm)
        df = pd.concat([train_norm,valid_norm, trade_norm],ignore_index=True)
    
    return df, mean_var

def add_features_portfolio(df_tics_raw,features_list,lookback_tech_indicator, train_startDate, trade_startDate,trade_endDate,norm_flag):
    tickers_list = df_tics_raw.tic.unique().tolist()
    uniqueDates = df_tics_raw.date.unique()
    df_dates = pd.DataFrame(uniqueDates, columns=['date']).sort_values(by='date')
    print('Unique dates count = %d\n'%(len(uniqueDates)))
    df_tics = []
    for tic in tickers_list:
        df_tic = df_tics_raw[df_tics_raw.tic == tic]
        df_tic = df_dates.merge(df_tic, on='date', how='left')
        print("%5s,   length = %6d,   null values filled = %6d "%(tic, len(df_tic),df_tic['close'].isna().sum()))
        df_tic = skew_Comp(df_tic,lookback_tech_indicator)
        df_tic = kurtosis_Comp(df_tic,lookback_tech_indicator)
        # df_tic = volatility_compute(df_tic,lookback_tech_indicator=60)
        # print(tic)
        # print(df_tic['close'].index[df_tic['close'].apply(np.isnan)])
        # print(df_tic['skew'].index[df_tic['skew'].apply(np.isnan)])
        # df_tic = rsi(df_tic,10)
        df_tic = df_tic.fillna(method='bfill').fillna(method='ffill')
        df_tics.append(df_tic)
    df = pd.concat(df_tics)
    # df = df[(df['date'] >= df_dates.iloc[60].values[0])].reset_index(drop=True)
    print('\nShape of dataframe =',df.shape)

    if norm_flag == True:
        train = data_split(df, train_startDate, trade_startDate).reset_index(drop=True)
        # valid = data_split(df, valid_startDate, trade_startDate).reset_index(drop=True)
        trade = data_split(df, trade_startDate, trade_endDate).reset_index(drop=True)
        train_norm = []
        valid_norm = []
        trade_norm = []
        mean_var = dict()
        for i, tic in enumerate(train.tic.unique()):
            df_tic_train = train[train.tic == tic]
            # df_tic_valid = valid[valid.tic == tic]
            df_tic_trade = trade[trade.tic == tic]

            mean_var_dict = dict()
            # mean_var_dict['tic'] = tic
            for j,indicator in enumerate(features_list):
                mu = df_tic_train[indicator].mean()
                sd = df_tic_train[indicator].std()

                mean_var_dict[indicator] = (mu,sd)
                
                df_tic_train[indicator] = (df_tic_train[indicator] - mu)/sd
                # df_tic_valid[indicator] = (df_tic_valid[indicator] - mu)/sd
                df_tic_trade[indicator] = (df_tic_trade[indicator] - mu)/sd

            if tic == 'BRK-B':
                tic = 'BRK.B'
            mean_var[tic] = mean_var_dict

            train_norm.append(df_tic_train)
            # valid_norm.append(df_tic_valid)
            trade_norm.append(df_tic_trade)
            
        train_norm = pd.concat(train_norm)
        # valid_norm = pd.concat(valid_norm)
        trade_norm = pd.concat(trade_norm)
        df = pd.concat([train_norm,trade_norm],ignore_index=True)
    
    return df, mean_var

def add_features_not_required(df_tics_raw,features_list,lookback_tech_indicator, train_startDate,valid_startDate,trade_startDate,trade_endDate,norm_flag):
    tickers_list = df_tics_raw.tic.unique().tolist()
    uniqueDates = df_tics_raw.date.unique()
    df_dates = pd.DataFrame(uniqueDates, columns=['date']).sort_values(by='date')
    print('Unique dates count = %d\n'%(len(uniqueDates)))
    df_tics = []
    for tic in tickers_list:
        df_tic = df_tics_raw[df_tics_raw.tic == tic]
        df_tic = df_dates.merge(df_tic, on='date', how='left')
        print("%5s,   length = %6d,   null values filled = %6d "%(tic, len(df_tic),df_tic['close'].isna().sum()))
        df_tic = skew_Comp(df_tic,lookback_tech_indicator)
        df_tic = kurtosis_Comp(df_tic,lookback_tech_indicator)
        # df_tic = rsi(df_tic,10)
        df_tic = df_tic.fillna(method='bfill').fillna(method='ffill')
        df_tics.append(df_tic)
    df = pd.concat(df_tics)
    # df = df[(df['date'] >= df_dates.iloc[60].values[0])].reset_index(drop=True)
    print('\nShape of dataframe =',df.shape)

    if norm_flag == True:
        train = data_split(df, train_startDate, valid_startDate).reset_index(drop=True)
        valid = data_split(df, valid_startDate, trade_startDate).reset_index(drop=True)
        trade = data_split(df, trade_startDate, trade_endDate).reset_index(drop=True)
        train_norm = []
        valid_norm = []
        trade_norm = []
        for i, tic in enumerate(train.tic.unique()):
            df_tic_train = train[train.tic == tic]
            df_tic_valid = valid[valid.tic == tic]
            df_tic_trade = trade[trade.tic == tic]

            for indicator in features_list:
                mu = df_tic_train[indicator].mean()
                sd = df_tic_train[indicator].std()

                df_tic_train[indicator] = (df_tic_train[indicator] - mu)/sd
                df_tic_valid[indicator] = (df_tic_valid[indicator] - mu)/sd
                df_tic_trade[indicator] = (df_tic_trade[indicator] - mu)/sd

            train_norm.append(df_tic_train)
            valid_norm.append(df_tic_valid)
            trade_norm.append(df_tic_trade)
            
        train_norm = pd.concat(train_norm)
        valid_norm = pd.concat(valid_norm)
        trade_norm = pd.concat(trade_norm)
        df = pd.concat([train_norm,valid_norm, trade_norm],ignore_index = True)
    
    return df

class Feature_extraction_old:
    def __init__(self, df_tics_raw, lookback = None):
        if lookback == None:
            self.lookback = 60
        else:
            self.lookback = lookback

        self.df = df_tics_raw
    
    def kurtosis_Comp(self, data, ndays=60):
        colName = 'kurt'
        kurt = pd.Series(data['close'].pct_change().rolling(
            ndays).kurt(), name=colName)
        data = data.join(kurt)
        return data

    def skew_Comp(self, data, ndays=60):
        colName = 'skew'
        skew = pd.Series(data['close'].pct_change().rolling(
            ndays).skew(), name=colName)
        data = data.join(skew)
        return data
    
# tickers_list = df_tics_raw.tic.unique().tolist()
#     uniqueDates = df_tics_raw.date.unique()
#     # df_dates = pd.DataFrame(uniqueDates, columns=['date']).sort_values(by='date')
#     print('Unique dates count = %d\n'%(len(uniqueDates)))
#     df_tics = []
#     for tic in tickers_list:
#         df_tic = df_tics_raw[df_tics_raw.tic == tic]
#         # df_tic = df_dates.merge(df_tic, on='date', how='left')
#         print("%5s,   length = %6d,   null values filled = %6d "%(tic, len(df_tic),df_tic['close'].isna().sum()))
#         df_tic = skew_Comp(df_tic,lookback_tech_indicator)
#         df_tic = kurtosis_Comp(df_tic,lookback_tech_indicator)
#         # df_tic = rsi(df_tic,10)
#         df_tic = df_tic.fillna(method='bfill').fillna(method='ffill')
#         df_tics.append(df_tic)
#     df = pd.concat(df_tics)
#     # df = df[(df['date'] >= df_dates.iloc[60].values[0])].reset_index(drop=True)
#     print('\nShape of dataframe =',df.shape)

    def add_technical_indicators(self, strt_date, split_dt, tech_indicator_list, normalize):
        """
		calculate technical indicators
		use stockstats package to add technical indicators
		:param data: (df) pandas dataframe
		:return: (df) pandas dataframe
        Sdf: StockDataFrame library
		"""
        df = self.df.copy()
        df = df.sort_values(by=["tic", "date"])
        stock = Sdf.retype(df.copy())
        unique_ticker = stock.tic.unique()

        for indicator in tech_indicator_list:
            indicator_df = pd.DataFrame()
            for i in range(len(unique_ticker)):
                if indicator == 'skew':
                    df_tic = df[df.tic == unique_ticker[i]]
                    df_tic = self.skew_Comp(df_tic, self.lookback)
                    indicator_df = indicator_df.append(df_tic[["tic", "date", indicator]], ignore_index=True)
                elif indicator == 'kurt':
                    df_tic = df[df.tic == unique_ticker[i]]
                    df_tic = self.kurtosis_Comp(df_tic, self.lookback)
                    indicator_df = indicator_df.append(df_tic[["tic", "date", indicator]], ignore_index=True)
                else:
                    temp_indicator = stock[stock.tic == unique_ticker[i]][indicator]
                    temp_indicator = pd.DataFrame(temp_indicator)
                    temp_indicator["tic"] = unique_ticker[i]
                    temp_indicator["date"] = df[df.tic == unique_ticker[i]]["date"].to_list()
                    indicator_df = indicator_df.append(temp_indicator, ignore_index=True)

            df = df.merge(indicator_df[["tic", "date", indicator]], on=["tic", "date"], how="left")
        df = df.sort_values(by=['date', 'tic'],ignore_index=True)
        # df.index = df.date.factorize()[0]
        df = df.fillna(method="bfill").fillna(method="ffill")

        df_tics_list  = []
        if normalize == True:
            for i,tic in enumerate(df.tic.unique()):
                df_tic = df[df.tic == tic]
                df_tic['date'] = pd.to_datetime(df_tic.date)
                df_train = df_tic[(df_tic['date'] >= strt_date) & (df_tic['date'] <= split_dt)]
                
                for indicator in tech_indicator_list:
                    mn = df_train[indicator].mean()
                    sd = df_train[indicator].std()
                    # print(mn, sd)
                    df_tic[indicator] = (df_tic[indicator] - mn)/sd

                    # df.loc[df.tic==tic, indicator] = df_tic[indicator].values
                # df_tic = df_tic.fillna(method="ffill").fillna(method="bfill")
                df_tics_list.append(df_tic)
                print('Number of nan values for',tic,df_tic.isna().sum().sum())

            df = pd.concat(df_tics_list)

        # df = df.fillna(method="ffill").fillna(method="bfill")
        df = df.sort_values(by=['date', 'tic'],ignore_index=True)
        # df.index = df.date.factorize()[0]
        return df

    def compute_returns(self, df):

        # add covariance matrix as states
        df=df.sort_values(['date','tic'],ignore_index=True)
        df.index = df.date.factorize()[0]

        cov_list = []
        return_list = []

        # look back is 60 days
        # lookback=60
        for i in range(self.lookback,len(df.index.unique())):
            data_lookback = df.loc[i-self.lookback:i,:]
            price_lookback=data_lookback.pivot_table(index = 'date',columns = 'tic', values = 'close')
            return_lookback = price_lookback.pct_change().dropna()

            # a = return_lookback.iloc[:5]
            # a = a.append(return_lookback.iloc[19])
            # a = a.append(return_lookback.iloc[59])

            a = return_lookback.iloc[0:1]
            a = a.append(return_lookback.iloc[40:41])
            a = a.append(return_lookback.iloc[55:])

            return_list.append(a)

        df_cov = pd.DataFrame({'date':df.date.unique()[self.lookback:], 'return_list':return_list})
        df = df.merge(df_cov, on='date')
        df = df.sort_values(['date','tic']).reset_index(drop=True)
        df['date'] = pd.to_datetime(df.date)

        # return return_list
        return df

    def get_features(self, strt_date, split_dt, tech_indicator_list, normalize=True):

        # ''' ------- Get last index of training set for feature extraction -----------------'''
        # unique_dates = sorted(df.date.unique())
        # train_dt = [dt for dt in unique_dates if dt < split_dt]
        # lim = len(train_dt)

        df = self.add_technical_indicators(strt_date, split_dt, tech_indicator_list, normalize)

        # return_list = self.compute_returns(df)

        # df_cov = pd.DataFrame({'date':df.date.unique()[lookback:], 'return_list':return_list})
        # df = df.merge(df_cov, on='date')
        # df = df.sort_values(['date','tic']).reset_index(drop=True)

        df = self.compute_returns(df, self.lookback)
        return df


class Feature_Engineer:
    """Provides methods for preprocessing the stock price data
    Attributes
    ----------
        use_technical_indicator : boolean
            we technical indicator or not
        tech_indicator_list : list
            a list of technical indicator names (modified from neofinrl_config.py)
        use_turbulence : boolean
            use turbulence index or not
        user_defined_feature:boolean
            use user defined features or not

    Methods
    -------
    preprocess_data()
        main method to do the feature engineering

    # stockstats technical indicator column names, check https://pypi.org/project/stockstats/ for different names
    """

    def __init__(
        self,
        use_ohlcv_features = False,
        use_vix=False,
        use_turbulence=False,
        use_stat_feature = False,
        use_market_feature = False,
        use_technical_indicator = False,
        use_technical_indicator_talib = False,
        use_user_defined_feature = False,
        use_norm_features = False,
        tech_indicator_list = [],
        stat_feature_list = [],
        market_feature_list = [],
        user_defined_feature_list = [],
        norm_feature_list = [],
        path_data = None,
        state_lookback = 60,
        features_norm_type = 'zscore',
        results_dir = "results",
        date_str = "",
        ):

        self.use_technical_indicator = use_technical_indicator
        self.use_technical_indicator_talib = use_technical_indicator_talib
        self.tech_indicator_list = tech_indicator_list
        self.use_vix = use_vix
        self.use_turbulence = use_turbulence
        self.use_user_defined_feature = use_user_defined_feature
        self.user_defined_feature_list = user_defined_feature_list
        self.use_stat_feature = use_stat_feature
        self.use_market_feature = use_market_feature
        self.stat_feature_list = stat_feature_list
        self.market_feature_list = market_feature_list
        self.path_vix_data = path_data
        self.norm_feature_list = norm_feature_list
        self.use_norm_features = use_norm_features
        self.state_lookback = state_lookback
        self.final_feature_list = []
        self.features_norm_type = features_norm_type
        self.scaler_model_path =  results_dir + '/scaler_models/'     
        self.date_str = date_str  
        
        if not os.path.exists("./" + self.scaler_model_path):
            os.makedirs("./" + self.scaler_model_path)

    def prepare_features_and_targets(self, df, features_col, target_col, delayed = -1):
        df_tics = []
        for tic in df.tic.unique().tolist():
            df_tic = df[df.tic == tic]
            df_tic[target_col] = df_tic[target_col].shift(delayed)
            df_tic = df_tic.dropna()
            df_tics.append(df_tic)
            
        df_tics = pd.concat(df_tics, ignore_index = True)
        df_tics = df_tics.reset_index(drop = True)
        return df_tics

    def prepare_features_and_add_targets(self, df, features_col, target_col, delayed = -1):
        df_tics = []
        for tic in df.tic.unique().tolist():
            df_tic = df[df.tic == tic]
            df_tic['target'] = df_tic[target_col].shift(delayed)
            df_tic = df_tic.dropna()
            df_tics.append(df_tic)
            
        df_tics = pd.concat(df_tics, ignore_index = True)
        df_tics = df_tics.reset_index(drop = True)
        return df_tics

    def add_lagged_features(self, df_processed, features_list, lag_period = 5):
        features = features_list.copy()
        # Create lagged features
        for feature in features:
            for lag in range(1, lag_period + 1):
                df_processed[f'{feature}_lag_{lag}'] = df_processed[feature].shift(lag)
                features_list.append(f'{feature}_lag_{lag}')
        return df_processed, features_list

    def add_daily_features(self, df):
        """main method to do the feature engineering
        @:param config: source dataframe
        @:return: a DataMatrices object
        """
        # clean data
        # df = self.clean_data(df)

        # add technical indicators using stockstats
        if self.use_technical_indicator:
            df = self.add_technical_indicator(df)
            # print("Successfully added technical indicators")

        # add technical indicators using talib
        if self.use_technical_indicator_talib:
            df = self.add_technical_indicator_talib(df)
            # print("Successfully added technical indicators")

        # add vix for multiple stock
        if self.use_vix:
            df = self.add_vix(df)
            # print("Successfully added vix")

        # add turbulence index for multiple stock
        if self.use_turbulence:
            df = self.add_turbulence(df)
            # print("Successfully added turbulence index")

        # add user defined feature
        if self.use_user_defined_feature:
            df = self.add_user_defined_feature(df)
            # print("Successfully added user defined features")

        # add statistics feature
        if self.use_stat_feature:
            df = self.add_stat_feature(df)
            # print("Successfully added stat features: skew and kurtosis")

        if self.use_market_feature:
            df = self.add_market_feature(df)
            # print("Successfully added market features")

        # fill the missing values at the beginning and the end
        # df = df.fillna(method="ffill").fillna(method="bfill")
        print("After feature extraction, ffill and bfill, the number of null value are %4d."%(df.isna().sum().sum()))
        return df, self.final_feature_list

    def add_weekly_features(self, df):
        """main method to do the feature engineering
        @:param config: source dataframe
        @:return: a DataMatrices object
        """
        # clean data
        # df = self.clean_data(df)

        # add technical indicators using stockstats
        if self.use_technical_indicator:
            df = self.add_technical_indicator(df)
            print("Successfully added technical indicators")

        # add technical indicators using talib
        if self.use_technical_indicator_talib:
            df = self.add_technical_indicator_talib(df)
            print("Successfully added technical indicators")

        # add vix for multiple stock
        if self.use_vix:
            df = self.add_vix(df)
            print("Successfully added vix")

        # add turbulence index for multiple stock
        if self.use_turbulence:
            df = self.add_turbulence(df)
            print("Successfully added turbulence index")

        # add user defined feature
        if self.use_user_defined_feature:
            df = self.add_user_defined_feature(df)
            print("Successfully added user defined features")

        # add statistics feature
        if self.use_stat_feature:
            df = self.add_stat_feature(df)
            print("Successfully added stat features: skew and kurtosis")

        if self.use_market_feature:
            df = self.add_market_feature(df)
            print("Successfully added market features")

        # fill the missing values at the beginning and the end
        # df = df.fillna(method="ffill").fillna(method="bfill")
        print("After feature extraction, ffill and bfill, the number of null value are %4d."%(df.isna().sum().sum()))        
        return df, self.final_feature_list

    def add_market_feature(self,data):

        df = data.copy()
        df = df.sort_values(by=["tic", "date"])
        # stock = Sdf.retype(df.copy())
        # unique_ticker = stock.tic.unique()
        df_QOA = pd.read_csv('datasets/QOA/' + df.tic.unique()[0] + '.csv')
        df_QQQ = pd.read_csv('datasets/QQQ/' + df.tic.unique()[0] + '.csv')

        df_market_feature = df_QOA.merge(df_QQQ, on = ['Date'])
        df_market_feature.rename(columns = {'Date': 'date'}, inplace= True)
        df_market_feature['date'] = pd.to_datetime(df_market_feature['date'], utc = True)
        # df_market_feature['date'] = pd.to_datetime(df_market_feature['date'])
        # df['date'] = df['date'].apply(lambda x: x.date())
        # df['date'] = pd.to_datetime(df['date'])
        
        for indicator in self.market_feature_list:
            if indicator in df_market_feature.columns.to_list()[1:]:
                df = df.merge(df_market_feature[['date',indicator]], on = ['date'])
                self.final_feature_list.append(indicator)
                print(f'{indicator} is added to the dataframe')
            else:
                print(f'{indicator} is not available, check your database')
            

            

        
        df = df.sort_values(by=["date", "tic"])
        return df
            


        # if len(qoa_features) > 0:
        #     qoa_df = pd.read_csv('datasets/QOA/' + ticker[0] + '.csv')
        #     qoa_df

        # features = features + qoa_features

        # if len(qoa_features) > 0:
        #     for ftr in qoa_features:
        #         df[ftr] = qoa_df[ftr].fillna(method ='ffill')

    def norm_features_single(self, df,train_start_date,train_end_date):
        if self.use_norm_features == True:
            scaler = StandardScaler()
            scaler.fit(df[(df['date'] >= train_start_date) & (df['date'] <= train_end_date)][self.final_feature_list])
            df[self.final_feature_list] = pd.DataFrame(scaler.transform(df[self.final_feature_list]))
            print('\nFeatures are normalized for single ticker')
            return df
        else:
            return df, None
        

    def scale_features_sklearn(self, df_tics, train_start_date, train_end_date,save_scale_models = False):
        if self.norm_feature_list == 'all':
            self.norm_feature_list = self.final_feature_list
        
        df_tics.index = df_tics['date'].factorize()[0]
        self.tickers_list = df_tics['tic'].unique().tolist()
        df_tics_list = []

        for tic in self.tickers_list:
            df_tic = df_tics[df_tics['tic'] == tic]

            if self.features_norm_type == 'zscore':
                scaler = StandardScaler()
            elif self.features_norm_type == 'min-max':
                scaler = MinMaxScaler()
                
            scaler.fit(df_tic[(df_tic['date'] >= train_start_date) & (df_tic['date'] <= train_end_date)][self.norm_feature_list])
            df_tic[self.norm_feature_list] = pd.DataFrame(scaler.transform(df_tic[self.norm_feature_list]))
            
            if save_scale_models:
                pickle.dump(scaler, open(self.scaler_model_path + '/' + self.date_str + '_scaler_' + tic + ".pkl", 'wb'))
            
            df_tics_list.append(df_tic)
        
        df_tics = pd.concat(df_tics_list)
        print(f'Features Scaled: {self.features_norm_type}')
        return df_tics
        
    def reorder_features(self,df):
        features = ['Price_Change','volume_pctchg','Price_Change','RSI','Price_Change','MACD','Price_Change','ADX',
                 'Price_Change','PPO','Price_Change','CMO','Price_Change','ROC','Price_Change','SMA_10_20','Price_Change','close_SKEW_20',
                 'Price_Change','volume_SKEW_20','Price_Change','PcrOi10','Price_Change','IvCall10']
        df = df[['date','tic','close','Price_Change','volume_pctchg','Price_Change','RSI','Price_Change','MACD','Price_Change','ADX',
                 'Price_Change','PPO','Price_Change','CMO','Price_Change','ROC','Price_Change','SMA_10_20','Price_Change','close_SKEW_20',
                 'Price_Change','volume_SKEW_20','Price_Change','PcrOi10','Price_Change','IvCall10']]
        
        return df,features

    def norm_features(self, df,train_start_date,train_end_date):
        if self.use_norm_features == True:
            if self.norm_type == 'zscore':
                if self.norm_feature_list == 'all':
                    self.norm_feature_list = self.final_feature_list
                    
                train = data_split(df, train_start_date,train_end_date).reset_index(drop=True)
                mean_var_train = dict()
                df_tic_list = []
                for i, tic in enumerate(train.tic.unique()):
                    df_tic_train = train[train.tic == tic]
                    df_tic = df[df.tic == tic]
                    mean_var_dict = dict()
                    # mean_var_dict['tic'] = tic
                    for j,indicator in enumerate(self.norm_feature_list):
                        mu = df_tic_train[indicator].mean()
                        sd = df_tic_train[indicator].std()
                        mean_var_dict[indicator] = (mu,sd)
                        df_tic[indicator] = (df_tic[indicator] - mu)/sd
                    
                    if '-' in tic:
                        tic = tic.replace('-', '.')

                    mean_var_train[tic] = mean_var_dict
                    # df_tic_list = pd.concat([df_tic_list,df_tic],ignore_index = True)
                    df_tic_list.append(df_tic)
    
                df_norm = pd.concat(df_tic_list)
                # df_norm = df_tic_list
                print('Features are normalized sucessfully')
                return df_norm, mean_var_train
            
            elif self.norm_type == 'min-max':
                if self.norm_feature_list == 'all':
                    self.norm_feature_list = self.final_feature_list
                    
                train = data_split(df, train_start_date,train_end_date).reset_index(drop=True)
                mean_var_train = dict()
                df_tic_list = []
                for i, tic in enumerate(train.tic.unique()):
                    df_tic_train = train[train.tic == tic]
                    df_tic = df[df.tic == tic]
                    mean_var_dict = dict()
                    # mean_var_dict['tic'] = tic
                    for j,indicator in enumerate(self.norm_feature_list):
                        mu = df_tic_train[indicator].mean()
                        sd = df_tic_train[indicator].std()
                        mean_var_dict[indicator] = (mu,sd)
                        df_tic[indicator] = (df_tic[indicator] - mu)/sd
                    
                    if '-' in tic:
                        tic = tic.replace('-', '.')

                    mean_var_train[tic] = mean_var_dict
                    # df_tic_list = pd.concat([df_tic_list,df_tic],ignore_index = True)
                    df_tic_list.append(df_tic)
    
                df_norm = pd.concat(df_tic_list)
                # df_norm = df_tic_list
                print('Features are normalized sucessfully')
                return df_norm, mean_var_train

                print('not implemented yet')
                return df, None

        else:
            return df, None

    def add_drl_states_subham(self, df):
        df = df.sort_values(['date', 'tic'], ignore_index=True)
        df.index = df.date.factorize()[0]
        time.sleep(1)     # for jupyter notebook printing
        state_list = []
        bar = progressbar.ProgressBar(maxval=len(df.index.unique()), \
        widgets=[progressbar.Bar(u'█', '[', ']'), ' ', '(',progressbar.Percentage(), ' ',progressbar.AdaptiveETA(), ')'])
        bar.start()
        for i in range(self.state_lookback, len(df.index.unique())):
            df_temp = []
            data_lookback = df.loc[i-self.state_lookback:i, :]                    # in df.loc include last index unlike numpy index
            price_lookback = data_lookback.pivot_table(index='date', columns='tic', values='close')
            return_lookback = price_lookback.pct_change().dropna()

            # pd.concat([df_temp,return_lookback.iloc[0:1]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[40:41]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[55:]], ignore_index = True)

            df_temp.append(return_lookback.iloc[0:1])                          # in df.iloc not include last index like numpy index
            df_temp.append(return_lookback.iloc[40:41])
            df_temp.append(return_lookback.iloc[55:])

            if self.use_technical_indicator:
                for tech_indicator in self.tech_indicator_list:
                    tech_indicator_val = data_lookback.pivot_table(index='date', columns='tic', values=tech_indicator)
                    tech_indicator_val = tech_indicator_val.iloc[-1, :].tolist()    # last day tech indicator
                    tech_indicator_val = pd.DataFrame([tech_indicator_val], columns=return_lookback.columns)

                    df_temp.append(tech_indicator_val)
            
            if self.use_stat_feature:
                for stat_feature in self.stat_feature_list:
                    stat_feature_val = data_lookback.pivot_table(index='date', columns='tic', values=stat_feature)
                    stat_feature_val = stat_feature_val.iloc[-1, :].tolist()       # # last day stat feature
                    stat_feature_val = pd.DataFrame([stat_feature_val], columns=return_lookback.columns)

                    df_temp.append(stat_feature_val)
            
            df_temp = pd.concat(df_temp)
            state_list.append(df_temp)
            
            bar.update(i+1)
            time.sleep(0.001)
        bar.finish()

        df_state = pd.DataFrame({'date': df.date.unique()[self.state_lookback:], 'cov_list': state_list})
        df = df.merge(df_state, on='date')            # ,how="left")         uncomment if need all dates but it will include NaN    
        df = df.sort_values(['date', 'tic']).reset_index(drop=True)
        
        return df

    def add_drl_states(self, df):
        df = df.sort_values(['date', 'tic'], ignore_index=True)
        df.index = df.date.factorize()[0]
        time.sleep(0.001)     # for jupyter notebook printing
        state_list = []
        bar = progressbar.ProgressBar(maxval=len(df.index.unique()), \
        widgets=[progressbar.Bar(u'█', '[', ']'), ' ', '(',progressbar.Percentage(), ' ',progressbar.AdaptiveETA(), ')'])
        bar.start()
        for i in range(self.state_lookback, len(df.index.unique())):
            df_temp = []
            data_lookback = df.loc[i-self.state_lookback:i, :]                    # in df.loc include last index unlike numpy index
            price_lookback = data_lookback.pivot_table(index='date', columns='tic', values='close')
            return_lookback = price_lookback.pct_change().dropna()

            # pd.concat([df_temp,return_lookback.iloc[0:1]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[40:41]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[55:]], ignore_index = True)

            # df_temp.append(return_lookback.iloc[0:1])                          # in df.iloc not include last index like numpy index
            # df_temp.append(return_lookback.iloc[40:41])
            # df_temp.append(return_lookback.iloc[55:])

            if self.use_technical_indicator:
                for tech_indicator in self.tech_indicator_list:
                    tech_indicator_val = data_lookback.pivot_table(index='date', columns='tic', values=tech_indicator)
                    tech_indicator_val = tech_indicator_val.iloc[-1, :].tolist()    # last day tech indicator
                    tech_indicator_val = pd.DataFrame([tech_indicator_val], columns=return_lookback.columns)

                    df_temp.append(tech_indicator_val)
            
            if self.use_stat_feature:
                for stat_feature in self.stat_feature_list:
                    stat_feature_val = data_lookback.pivot_table(index='date', columns='tic', values=stat_feature)
                    stat_feature_val = stat_feature_val.iloc[-1, :].tolist()       # # last day stat feature
                    stat_feature_val = pd.DataFrame([stat_feature_val], columns=return_lookback.columns)

                    df_temp.append(stat_feature_val)

            if self.use_user_defined_feature:
                for user_feature in self.user_defined_feature_list:
                    user_feature_val = data_lookback.pivot_table(index='date', columns='tic', values=user_feature)
                    user_feature_val = user_feature_val.iloc[-1, :].tolist()    # last day tech indicator
                    user_feature_val = pd.DataFrame([user_feature_val], columns=return_lookback.columns)

                    df_temp.append(user_feature_val)

            if self.use_vix:
                vix_val = data_lookback.pivot_table(index='date', columns='tic', values='vix')
                vix_val = vix_val.iloc[-1, :].tolist()    # last day vix_val
                vix_val = pd.DataFrame([vix_val], columns=return_lookback.columns)

                df_temp.append(vix_val)
            
            df_temp = pd.concat(df_temp)
            state_list.append(df_temp)
            
            bar.update(i+1)
            time.sleep(0.001)
        bar.finish()

        df_state = pd.DataFrame({'date': df.date.unique()[self.state_lookback:], 'cov_list': state_list})
        df = df.merge(df_state, on='date')            # ,how="left")         uncomment if need all dates but it will include NaN    
        df = df.sort_values(['date', 'tic']).reset_index(drop=True)
        
        return df
    
    def add_drl_states_weekly(self, df):
        df = df.sort_values(['date', 'tic'], ignore_index=True)
        df.index = df.date.factorize()[0]
        time.sleep(1)     # for jupyter notebook printing
        state_list = []
        bar = progressbar.ProgressBar(maxval=len(df.index.unique()), \
        widgets=[progressbar.Bar(u'█', '[', ']'), ' ', '(',progressbar.Percentage(), ' ',progressbar.AdaptiveETA(), ')'])
        bar.start()
        for i in range(self.state_lookback, len(df.index.unique())):
            df_temp = []
            data_lookback = df.loc[i-self.state_lookback:i, :]                    # in df.loc include last index unlike numpy index
            price_lookback = data_lookback.pivot_table(index='date', columns='tic', values='close')
            return_lookback = price_lookback.pct_change().dropna()

            # pd.concat([df_temp,return_lookback.iloc[0:1]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[40:41]], ignore_index = True)
            # pd.concat([df_temp,return_lookback.iloc[55:]], ignore_index = True)

            # df_temp.append(return_lookback.iloc[0:1])                          # in df.iloc not include last index like numpy index
            # df_temp.append(return_lookback.iloc[40:41])
            # df_temp.append(return_lookback.iloc[55:])
            df_temp.append(return_lookback)

            if self.use_technical_indicator:
                for tech_indicator in self.tech_indicator_list:
                    tech_indicator_val = data_lookback.pivot_table(index='date', columns='tic', values=tech_indicator)
                    tech_indicator_val = tech_indicator_val.iloc[-1, :].tolist()    # last day tech indicator
                    tech_indicator_val = pd.DataFrame([tech_indicator_val], columns=return_lookback.columns)

                    df_temp.append(tech_indicator_val)
            
            if self.use_stat_feature:
                for stat_feature in self.stat_feature_list:
                    stat_feature_val = data_lookback.pivot_table(index='date', columns='tic', values=stat_feature)
                    stat_feature_val = stat_feature_val.iloc[-1, :].tolist()       # # last day stat feature
                    stat_feature_val = pd.DataFrame([stat_feature_val], columns=return_lookback.columns)

                    df_temp.append(stat_feature_val)
            
            df_temp = pd.concat(df_temp)
            state_list.append(df_temp)
            
            bar.update(i+1)
            time.sleep(0.001)
        bar.finish()

        df_state = pd.DataFrame({'date': df.date.unique()[self.state_lookback:], 'cov_list': state_list})
        df = df.merge(df_state, on='date')            # ,how="left")         uncomment if need all dates but it will include NaN    
        df = df.sort_values(['date', 'tic']).reset_index(drop=True)
        
        return df

    def kurtosis_Comp(self, data, ndays=60):
        colName = 'kurt'
        kurt = pd.Series(data['close'].pct_change().rolling(
            ndays).kurt(), name=colName)
        data = data.join(kurt)
        return data

    def skew_Comp(self, data, ndays=60):
        colName = 'skew'
        skew = pd.Series(data['close'].pct_change().rolling(ndays).skew(), name=colName)
        data = data.join(skew)
        return data

    def add_stat_feature(self, df, lookback = 60):
        unique_ticker = df.tic.unique()

        for stat_feature in self.stat_feature_list:
            df_tics = []
            
            for i in range(len(unique_ticker)):
                df_tic = df[df.tic == unique_ticker[i]]
                
                if stat_feature == 'skew':
                    df_tic = self.skew_Comp(df_tic, ndays=lookback)
                    df_tic = df_tic.fillna(method="ffill").fillna(method="bfill")
                    # df_tics = pd.concat([df_tics,df_tic], ignore_index = True)
                    df_tics.append(df_tic)
                    # df_tics = df_tics.append(df_tic[["tic", "date", stat_feature]], ignore_index=True)
                
                elif stat_feature == 'kurt':
                    df_tic = self.kurtosis_Comp(df_tic,ndays=lookback)
                    df_tic = df_tic.fillna(method="ffill").fillna(method="bfill")
                    # df_tics = pd.concat([df_tics,df_tic], ignore_index = True)
                    df_tics.append(df_tic)
                    # df_tics = df_tics.append(df_tic[["tic", "date", stat_feature]], ignore_index=True)

            # df = df.merge(df_tics[["tic", "date", stat_feature]], on=["tic", "date"], how="left")
            df = pd.concat(df_tics)
            self.final_feature_list.append(stat_feature)
            print(f'{stat_feature} is added to the dataframe')
        df = df.sort_values(by=['date', 'tic'],ignore_index=True)
        # df.index = df.date.factorize()[0]
        # df = df.fillna(method="ffill").fillna(method="bfill")
        return df

    def clean_data(self, data):
        """
        clean the raw data
        deal with missing values
        reasons: stocks could be delisted, not incorporated at the time step
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df = data.copy()
        df = df.sort_values(["date", "tic"], ignore_index=True)
        df.index = df.date.factorize()[0]
        merged_closes = df.pivot_table(index="date", columns="tic", values="close")
        merged_closes = merged_closes.dropna(axis=1)
        tics = merged_closes.columns
        df = df[df.tic.isin(tics)]
        # df = data.copy()
        # list_ticker = df["tic"].unique().tolist()
        # only apply to daily level data, need to fix for minute level
        # list_date = list(pd.date_range(df['date'].min(),df['date'].max()).astype(str))
        # combination = list(itertools.product(list_date,list_ticker))

        # df_full = pd.DataFrame(combination,columns=["date","tic"]).merge(df,on=["date","tic"],how="left")
        # df_full = df_full[df_full['date'].isin(df['date'])]
        # df_full = df_full.sort_values(['date','tic'])
        # df_full = df_full.fillna(0)
        return df

    def add_technical_indicator(self, data):
        """
        calculate technical indicators
        use stockstats package to add technical inidactors
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df = data.copy()
        df = df.sort_values(by=["tic", "date"])
        stock = Sdf.retype(df.copy())
        unique_ticker = stock.tic.unique()

        for indicator in self.tech_indicator_list:
            indicator_df = pd.DataFrame()
            for i in range(len(unique_ticker)):
                try:
                    temp_indicator = stock[stock.tic == unique_ticker[i]][indicator]
                    temp_indicator = pd.DataFrame(temp_indicator)
                    temp_indicator["tic"] = unique_ticker[i]
                    temp_indicator["date"] = df[df.tic == unique_ticker[i]][
                        "date"
                    ].to_list()
                    temp_indicator = temp_indicator.fillna(method="ffill").fillna(method="bfill")
                    # indicator_df = indicator_df.append(
                    #     temp_indicator, ignore_index=True
                    # )
                    indicator_df = pd.concat([indicator_df,temp_indicator], ignore_index = True)
                except Exception as e:
                    print(e)
            df = df.merge(
                indicator_df[["tic", "date", indicator]], on=["tic", "date"], how="left"
            )
            print(f'{indicator} is added to the dataframe')
            self.final_feature_list.append(indicator)
        df = df.sort_values(by=["date", "tic"])
        return df
        # df = data.set_index(['date','tic']).sort_index()
        # df = df.join(df.groupby(level=0, group_keys=False).apply(lambda x, y: Sdf.retype(x)[y], y=self.tech_indicator_list))
        # return df.reset_index()

    def add_technical_indicator_talib(self, data):
        """
        calculate technical indicators
        use stockstats package to add technical inidactors
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df = data.copy()
        df = df.sort_values(by=["tic", "date"])
        # stock = Sdf.retype(df.copy())
        # unique_ticker = stock.tic.unique()

        for indicator in self.tech_indicator_list:
            # for indicator in self.tech_indicator_list:

            if indicator == 'RSI':
                df[indicator] = TA.RSI(df)

            elif indicator == 'ADX':
                df[indicator] = TA.ADX(df)

            elif indicator == 'SMA_10':
                df[indicator] = TA.SMA(df, period = 10)
            elif indicator == 'SMA_20':
                df[indicator] = TA.SMA(df, period = 20)
            elif indicator == 'SMA_30':
                df[indicator] = TA.SMA(df, period = 30)

            elif indicator == 'HT_TRENDLINE':
                df[indicator] = talib.HT_TRENDLINE(df['close'])

            elif indicator == 'KAMA':
                df[indicator] = TA.KAMA(df)

            elif indicator == 'MACD':
                # df[indicator] = TA.MACD(df)['MACD']
                df[indicator] = TA.MACD(df)[0]

            elif indicator == 'MACD_signal':
                # df[indicator] = TA.MACD(df)['SIGNAL']
                df[indicator] = TA.MACD(df)[1]

            elif indicator == 'MFI':
                df[indicator] = TA.MFI(df)

            elif indicator == 'ROC':
                df[indicator] = TA.ROC(df)

            elif indicator == 'STOCHRSI':
                df[indicator] = TA.STOCHRSI(df)

            elif indicator == 'WILLR':
                df[indicator] = talib.WILLR(df['close'])
            

            
            ############# reversal ####################################
            # elif indicator == 'OBV':
            #     df[indicator] = talib.OBV(df['volume'])

            # elif indicator == 'MINUS_DI':
            #     df[indicator] = talib.MINUS_DI(df[['high', 'low', 'close']])

            ############# oscillation #############################
            elif indicator == 'PPO':
                df[indicator] = TA.PPO(df)['PPO']

            elif indicator == 'ATR':
                df[indicator] = TA.ATR(df)

            elif indicator == 'HT_DCPERIOD':
                df[indicator] = talib.HT_DCPERIOD(df['close'])

            elif indicator == 'APO':
                df[indicator] = talib.APO(df['close'])

            elif indicator == 'CMO':
                df[indicator] = TA.CMO(df)

            elif indicator == 'ADOSC':
                df[indicator] = talib.ADOSC(df['close'])


            # elif indicator == 'SKEW_10':
            #     df[indicator] = TA.SKEW(df, period = 10)
            # elif indicator == 'SKEW_20':
            #     df[indicator] = TA.SKEW(df, period = 20)
            
            elif indicator == 'OBV':
                df[indicator] = TA.OBV(df)

            # df = df.merge(
            #     indicator_df[["tic", "date", indicator]], on=["tic", "date"], how="left"
            # )
            self.final_feature_list.append(indicator)
            print(f'{indicator} is added to the dataframe')
        df = df.sort_values(by=["date", "tic"])
        return df
        # df = data.set_index(['date','tic']).sort_index()
        # df = df.join(df.groupby(level=0, group_keys=False).apply(lambda x, y: Sdf.retype(x)[y], y=self.tech_indicator_list))
        # return df.reset_index()

    def add_user_defined_feature(self, data):
        """
         add user defined features
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df_local = data.copy()
        df_local = df_local.sort_values(by=["tic", "date"])
        stock = Sdf.retype(df_local.copy())
        unique_ticker = stock.tic.unique()

        # for indicator in self.user_defined_feature_list:
        #     indicator_df = pd.DataFrame()
        #     for i in range(len(unique_ticker)):
        #         try:
        #             temp_indicator = stock[stock.tic == unique_ticker[i]]['close'].pct_change(5)
        #             temp_indicator = pd.DataFrame(temp_indicator)
        #             temp_indicator["tic"] = unique_ticker[i]
        #             temp_indicator["date"] = df[df.tic == unique_ticker[i]][
        #                 "date"
        #             ].to_list()
        #             temp_indicator = temp_indicator.fillna(method="ffill").fillna(method="bfill")
        #             # indicator_df = indicator_df.append(
        #             #     temp_indicator, ignore_index=True
        #             # )
        #             indicator_df = pd.concat([indicator_df,temp_indicator], ignore_index = True)
        #         except Exception as e:
        #             print(e)
        #     df = df.merge(
        #         indicator_df[["tic", "date", indicator]], on=["tic", "date"], how="left"
        #     )
        #     print(f'{indicator} is added to the dataframe')
        #     self.final_feature_list.append(indicator)
        # df = df.sort_values(by=["date", "tic"])
        # return df
        # df = data.set_index(['date','tic']).sort_index()
        # df = df.join(df.groupby(level=0, group_keys=False).apply(lambda x, y: Sdf.retype(x)[y], y=self.tech_indicator_list))
        # return df.reset_index()



        # df["daily_return"] = df.close.pct_change(1)


        # df['return_lag_1']=df.close.pct_change(2)
        # df['return_lag_2']=df.close.pct_change(3)
        # df['return_lag_3']=df.close.pct_change(4)
        # df['return_lag_4']=df.close.pct_change(5)
        for indicator in self.user_defined_feature_list:
            indicator_df = pd.DataFrame()
            for i in range(len(unique_ticker)):
                df = stock[stock.tic == unique_ticker[i]]

                if indicator == 'close':
                    temp_indicator = df['close']

                elif indicator == 'close_1_roc':
                    temp_indicator = df['close'].pct_change()

                elif indicator == 'close_2_roc':
                    temp_indicator = df['close'].pct_change(2)

                elif indicator == 'close_3_roc':
                    temp_indicator = df['close'].pct_change(2)

                elif indicator == 'close_4_roc':
                    temp_indicator = df['close'].pct_change(4)

                elif indicator == 'close_5_roc':
                    temp_indicator = df['close'].pct_change(5)

                elif indicator == 'close_21_roc':
                    temp_indicator = df['close'].pct_change(21)

                elif indicator == 'volume':
                    temp_indicator = df['volume']

                elif indicator == 'volume_pctchg':
                    temp_indicator = df['volume'].pct_change()

                elif indicator == 'SMA_10_20':
                    temp_indicator = TA.SMA(df, period = 10) - TA.SMA(df, period = 20)

                elif indicator == 'SMA_20_30':
                    temp_indicator = TA.SMA(df, period = 20) - TA.SMA(df, period = 30)

                elif indicator == 'close_SKEW_10':
                    temp_indicator = TA.SKEW(df, period = 10)

                elif indicator == 'close_SKEW_20':
                    temp_indicator = TA.SKEW(df, period = 20)

                elif indicator == 'volume_SKEW_10':
                    temp_indicator = TA.SKEW(df, period = 10, column = 'volume')

                elif indicator == 'volume_SKEW_20':
                    temp_indicator = TA.SKEW(df, period = 20, column = 'volume')

                elif 'volatility' in indicator:
                    temp_variable = indicator.split('_')

                    if len(temp_variable) == 3:
                        [ind_name, lookback, technique] = indicator.split('_')
                        if technique == 'SMA':
                            temp_indicator = df['close'].pct_change().dropna().rolling(window=int(lookback)).std()* np.sqrt(252)

                    if len(temp_variable) == 2:
                        [ind_name, lookback] = indicator.split('_')
                        temp_indicator = df['close'].pct_change().dropna().rolling(window=int(lookback)).std()*np.sqrt(252)

                temp_indicator = pd.DataFrame(temp_indicator)
                temp_indicator = temp_indicator.rename(columns = {'close': indicator})
                temp_indicator["tic"] = unique_ticker[i]
                temp_indicator = temp_indicator.reset_index()
                # temp_indicator["date"] = df_local[df_local.tic == unique_ticker[i]]["date"].to_list()

                # temp_indicator = temp_indicator.fillna(method="ffill").fillna(method="bfill")
                indicator_df = pd.concat([indicator_df,temp_indicator], ignore_index = True)
            
            df_local = df_local.merge(indicator_df[["tic", "date", indicator]], on=["tic", "date"], how="left")
            print(f'{indicator} is added to the dataframe')
            self.final_feature_list.append(indicator)

        df_local = df_local.sort_values(by=["date", "tic"])
        return df_local

    def add_vix(self, data):
        """
        add vix from yahoo finance
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df = data.copy()

        file_ext = os.path.splitext(self.path_vix_data)[-1]
        if file_ext == '.csv':
            df_tics_daily = pd.read_csv(self.path_vix_data)
        elif file_ext == '.h5':
            df_tics_daily = pd.read_hdf(self.path_vix_data, "df",mode = 'r')



        df_vix = df_tics_daily[df_tics_daily['tic']=="^VIX"]

        vix = df_vix[["date", "close"]]
        vix.columns = ["date", "vix"]
        vix.set_index('date',inplace=True)
        # NY = "America/New_York"
        # vix.index = pd.to_datetime(vix.index).tz_localize(NY)
        df = df.merge(vix, on="date")
        df = df.sort_values(["date", "tic"]).reset_index(drop=True)
        self.final_feature_list.append('vix')
        print(f'vix is added to the dataframe')
        return df

    def add_turbulence(self, data):
        """
        add turbulence index from a precalcualted dataframe
        :param data: (df) pandas dataframe
        :return: (df) pandas dataframe
        """
        df = data.copy()
        turbulence_index = self.calculate_turbulence(df)
        df = df.merge(turbulence_index, on="date")
        df = df.sort_values(["date", "tic"]).reset_index(drop=True)
        return df

    def calculate_turbulence(self, data):
        """calculate turbulence index based on dow 30"""
        # can add other market assets
        df = data.copy()
        df_price_pivot = df.pivot(index="date", columns="tic", values="close")
        # use returns to calculate turbulence
        df_price_pivot = df_price_pivot.pct_change()

        unique_date = df.date.unique()
        # start after a year
        start = 252
        turbulence_index = [0] * start
        # turbulence_index = [0]
        count = 0
        for i in range(start, len(unique_date)):
            current_price = df_price_pivot[df_price_pivot.index == unique_date[i]]
            # use one year rolling window to calcualte covariance
            hist_price = df_price_pivot[
                (df_price_pivot.index < unique_date[i])
                & (df_price_pivot.index >= unique_date[i - 252])
            ]
            # Drop tickers which has number missing values more than the "oldest" ticker
            filtered_hist_price = hist_price.iloc[
                hist_price.isna().sum().min() :
            ].dropna(axis=1)

            cov_temp = filtered_hist_price.cov()
            current_temp = current_price[[x for x in filtered_hist_price]] - np.mean(
                filtered_hist_price, axis=0
            )
            # cov_temp = hist_price.cov()
            # current_temp=(current_price - np.mean(hist_price,axis=0))

            temp = current_temp.values.dot(np.linalg.pinv(cov_temp)).dot(
                current_temp.values.T
            )
            if temp > 0:
                count += 1
                if count > 2:
                    turbulence_temp = temp[0][0]
                else:
                    # avoid large outlier because of the calculation just begins
                    turbulence_temp = 0
            else:
                turbulence_temp = 0
            turbulence_index.append(turbulence_temp)
        try:
            turbulence_index = pd.DataFrame(
                {"date": df_price_pivot.index, "turbulence": turbulence_index}
            )
        except ValueError:
            raise Exception("Turbulence information could not be added.")
        return turbulence_index

class Feature_Engineer_old:
    def __init__(self, tickers_list, features_list, frequency = 'daily'):
        self.features_list = [item for item in features_list if item['frequency'] == frequency]
        self.feature_names = [f['name'] for f in self.features_list]
        self.tickers_list = tickers_list
        # df_features_detail = pd.DataFrame(features_list) 
        # df_features_detail = df_features_detail[df_features_detail['frequency']==frequency]

    def add_technical_features(self, df_tics):
        df_tics_list = []

        for tic in self.tickers_list:
            df_tic = df_tics[df_tics['tic'] == tic]
            df_tic = df_tic.copy()

            # ftr_list = []
            for feature in self.features_list:
                if feature['type'] in ['tech', 'ohlcv']:
                    ftr = feature['name']

                    if '_' in ftr and ftr.split('_')[1] == 'pctchng':
                        col = ftr.split('_')[0]
                        time = int(ftr.split('_')[-1])
                        df_tic[ftr] = df_tic[col].pct_change(time)

                    # elif '_' in ftr and ftr.split('_')[1] == 'SKEW':
                    #     col = ftr.split('_')[0]
                    #     time = int(ftr.split('_')[-1])
                    #     df_tic[ftr] = TA.SKEW(df_tic, period = time, column= col)

                    # elif '_' in ftr and ftr.split('_')[1] == 'KURT':
                    #     col = ftr.split('_')[0]
                    #     time = int(ftr.split('_')[-1])
                    #     df_tic[ftr] = TA.KURT(df_tic, period = time, column= col)

                    # elif '_' in ftr and ftr.split('_')[1] == 'VOL':
                    #     col = ftr.split('_')[0]
                    #     time = int(ftr.split('_')[-1])
                    #     df_tic[ftr] = TA.VOL(df_tic, period = time, column= col)

                    # elif ftr == 'RSI':
                    #     df_tic[ftr] = TA.RSI(df_tic)

                    elif '_' in ftr and ftr.split('_')[0] == 'RSI':
                        time = int(ftr.split('_')[-1])
                        df_tic[ftr] = TA.RSI(df_tic, period = time)

                    # elif ftr == 'MACD':
                    #     df_tic[ftr] = TA.MACD(df_tic)[0]

                    # elif ftr == 'MACD_signal':
                    #     df_tic[ftr] = TA.MACD(df_tic)[1]

                    # elif ftr == 'MACD_cross':
                    #     df_tic[ftr] = TA.MACD(df_tic)[0] - TA.MACD(df_tic)[1]

                    # elif ftr == 'KAMA':
                    #     df_tic[ftr] = TA.KAMA(df_tic)
                    
                    # elif ftr == 'MFI':
                    #     df_tic[ftr] = TA.MFI(df_tic)


                    elif '_' in ftr and ftr.split('_')[0] == 'ROC':
                        time = int(ftr.split('_')[-1])
                        df_tic[ftr] = TA.ROC(df_tic, period = time)

                    elif ftr == 'STOCHRSI':
                        df_tic[ftr] = TA.STOCHRSI(df_tic)    
                    
                    elif ftr == 'ADX':
                        df_tic[ftr] = TA.ADX(df_tic)

                    elif ftr == 'BBWIDTH':
                        df_tic[ftr] = (TA.BBANDS(df_tic)[0] - TA.BBANDS(df_tic)[1])/TA.BBANDS(df_tic)[0] 

                    elif ftr == 'CCI':
                        df_tic[ftr] = TA.CCI(df_tic)

                    # elif ftr == 'WILLIAMS':
                    #     df_tic[ftr] = TA.WILLIAMS(df_tic)

                    # elif ftr == 'CHAIKIN':
                    #     df_tic[ftr] = TA.CHAIKIN(df_tic)

                    # elif ftr == 'UO':
                    #     df_tic[ftr] = TA.UO(df_tic)
                    
                    # elif ftr == 'PPO':
                    #     df_tic[ftr] = TA.PPO(df_tic)[0]

                    elif '_' in ftr and ftr.split('_')[0] == 'PPO':
                        fast = int(ftr.split('_')[1])
                        slow = int(ftr.split('_')[2])
                        df_tic[ftr] = TA.PPO(df_tic, period_fast = fast, period_slow=slow)[0]

                    elif ftr == 'OBV':
                        df_tic[ftr] = TA.OBV(df_tic)

                    print(f"{ftr} added for {tic}")

            df_tic = df_tic.fillna(method='ffill').fillna(method='bfill')
            df_tics_list.append(df_tic)

        df_tics = pd.concat(df_tics_list) 
        return df_tics
    
    def add_options_features(self, df_tics):
        self.tickers_list = df_tics['tic'].unique().tolist()
        df_options_features_tics = pd.read_hdf('datasets1/df_options_feature.h5')

        df_tics_list = []

        for tic in self.tickers_list:
            df_tic = df_tics[df_tics['tic'] == tic]
            ftr_list = []

            for feature in self.features_list:   
                if feature['type'] == 'options':
                    ftr = feature['name']
                    ftr_list.append(ftr)

            df_options_features_tic =  df_options_features_tics[ df_options_features_tics['tic']==tic]
            # df_options_features = pd.read_hdf('datasets/IVPCR_data/' + tic + '.h5')
            # df_options_features = df_options_features.reset_index()
            # df_options_features = df_options_features.rename(columns = {'Date':'date'})
            df_options_features_tic['date'] = pd.to_datetime(df_options_features_tic['date'])
            df_options_features_tic = df_options_features_tic[['date'] + ftr_list]
            df_tic = df_tic.merge(df_options_features_tic, on='date', how='left')
            df_tic = df_tic.fillna(method='ffill').fillna(method='bfill')
            # print("After feature extraction, ffill and bfill, the number of null value are %4d."%(df_tic.isna().sum().sum())) 
            df_tics_list.append(df_tic)

        df_tics = pd.concat(df_tics_list)
        return df_tics
    
    def lag_features(self,df_tics):
        self.tickers_list = df_tics['tic'].unique().tolist()
        df_tics_list = []

        for tic in self.tickers_list:
            df_tic = df_tics[df_tics['tic'] == tic]

            for feature in self.features_list:
                if feature['lagged']:
                    ftr = feature['name']
                    df_tic[ftr] = df_tic[ftr].shift(periods=1)
            
            df_tic = df_tic.fillna(method='ffill').fillna(method='bfill')
            # print("After feature extraction, ffill and bfill, the number of null value are %4d."%(df_tic.isna().sum().sum())) 
            df_tics_list.append(df_tic)

        df_tics = pd.concat(df_tics_list)
        return df_tics
    
    
    # def scale_features_sklearn(self, df_tics):
    #     df_tics.index = df_tics['date'].factorize()[0]
    #     self.tickers_list = df_tics['tic'].unique().tolist()
    #     df_tics_list = []
    #     train_start_idx = df_tics[df_tics['date'] == self.TRAIN_START_DATE].index[0]
    #     train_end_idx = df_tics[df_tics['date'] == self.TRAIN_END_DATE].index[0]

    #     # trade_start_idx = df_tics[df_tics['date'] == self.TRADE_START_DATE].index.item()
    #     # trade_end_idx = df_tics[df_tics['date'] == self.TRADE_END_DATE].index.item()

    #     for tic in self.tickers_list:
    #         df_tic = df_tics[df_tics['tic'] == tic]
    #         # scaler = StandardScaler()
    #         scaler = MinMaxScaler()
    #         scaler.fit(df_tic.loc[train_start_idx : train_end_idx][self.feature_names])
    #         df_tic[self.feature_names] = pd.DataFrame(scaler.transform(df_tic[self.feature_names]))
            
    #         pickle.dump(scaler, open("scaler_models/scaler_"+tic+".pkl", 'wb'))

    #         df_tics_list.append(df_tic)
        
    #     df_tics = pd.concat(df_tics_list)
    #     return df_tics
    
    def scale_features_minmax(self, df_tics):
        df_tics = df_tics.sort_values(by=['date','tic'])
        df_tics.index = df_tics['date'].factorize()[0]
        df_min_max = pd.DataFrame(self.features_list)[['name','min','max']].set_index("name").T
        df_tics[self.feature_names] = (df_tics[self.feature_names]-df_min_max.loc['min'])/(df_min_max.loc['max']-df_min_max.loc['min'])

        return df_tics


