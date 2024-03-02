import pandas as pd
import numpy as np

def buy_hold_portfolio_return(df_tics, df_indices = None, with_indices = False,dropna = True,fillna = False):

    ''' Created on Date: 2023-11-07
    This function return the porfolio return of equal weight portfolio
    also compare the returns with indices'''

    n_tickers = len(df_tics.tic.unique())
    df_tics_close = pd.pivot_table(df_tics, values='close',index='date',columns='tic')
    if dropna:
        df_tics_returns = df_tics_close.pct_change().dropna()
    if fillna:
        df_tics_returns = df_tics_close.pct_change().fillna(0)
    equal_weights = np.full(n_tickers, 1 / n_tickers)
    portfolio_returns = df_tics_returns.dot(equal_weights)
    portfolio_returns = pd.DataFrame(portfolio_returns,columns=['Buy_Hold_returns'])

    if with_indices:
        df_index_close = pd.pivot_table(df_indices, values='close',index='date',columns='tic')
        if dropna:
            df_index_returns = df_index_close.pct_change().dropna()
        if fillna:
            df_index_returns = df_index_close.pct_change().fillna(0)

        # df_index_returns = df_index_close.pct_change()    #.fillna(0)
        portfolio_returns = portfolio_returns.merge(df_index_returns,how='left',on = 'date')
        # cumulative_returns = (portfolio_returns + 1).cumprod()
    
    return portfolio_returns