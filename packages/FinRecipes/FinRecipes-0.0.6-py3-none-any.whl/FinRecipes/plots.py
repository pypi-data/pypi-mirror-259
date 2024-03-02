import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import empyrical as ep
import matplotlib.dates as mdates
import os

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
# yf.pdr_override()
import matplotlib.pyplot as plt

def plot_train_val_test(df,
                        total_training_period,
                        trading_period,
                        validation_start_index1,
                        validation_start_index2,
                        validation_start_index3,
                        validation_period1,
                        validation_period2,
                        validation_period3,
                        validation_period4,
                        figdir,
                        ):
    
    ticker = df.tic.unique()[0]
    # %matplotlib inline
    plt.style.use('ggplot')
    fig, (ax,ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=6, ncols=1, figsize=(15,14))

    ax.plot(df['date'][total_training_period[0]: trading_period[1]+1], df['close'][total_training_period[0]: trading_period[1]+1], color = 'black')

    # validation 1
    if validation_start_index1 != None:
        ax1.plot(df['date'][validation_period1[0]: validation_period1[1]+1], df['close'][validation_period1[0]: validation_period1[1]+1], color = 'black')
        ax1.axvspan(df['date'][validation_period1[0]], df['date'][validation_period1[1]], color='#348ABD', alpha = 0.5)
        ax.axvspan(df['date'][validation_period1[0]], df['date'][validation_period1[1]], color='#348ABD', alpha = 0.5)

    # validation 2
    if validation_start_index2 != None:
        ax2.plot(df['date'][validation_period2[0]: validation_period2[1]+1], df['close'][validation_period2[0]: validation_period2[1]+1], color = 'black')
        ax2.axvspan(df['date'][validation_period2[0]], df['date'][validation_period2[1]], color='#348ABD', alpha = 0.5)
        ax.axvspan(df['date'][validation_period2[0]], df['date'][validation_period2[1]], color='#348ABD', alpha = 0.5)

    # validation 3
    if validation_start_index3 != None:
        ax3.plot(df['date'][validation_period3[0]: validation_period3[1]+1], df['close'][validation_period3[0]: validation_period3[1]+1], color = 'black')
        ax3.axvspan(df['date'][validation_period3[0]], df['date'][validation_period3[1]], color='#348ABD', alpha = 0.5)
        ax.axvspan(df['date'][validation_period3[0]], df['date'][validation_period3[1]], color='#348ABD', alpha = 0.5)
        
    # validation 4
    ax4.plot(df['date'][validation_period4[0]: validation_period4[1]+1], df['close'][validation_period4[0]: validation_period4[1]+1], color = 'black')
    ax4.axvspan(df['date'][validation_period4[0]], df['date'][validation_period4[1]], color='#348ABD', alpha = 0.5)
    ax.axvspan(df['date'][validation_period4[0]], df['date'][validation_period4[1]], color='#348ABD', alpha = 0.5)

    # trading
    ax5.plot(df['date'][trading_period[0]: trading_period[1]+1], df['close'][trading_period[0]: trading_period[1]+1], color = 'black')
    ax5.axvspan(df['date'][trading_period[0]], df['date'][trading_period[1]], color='#8EBA42', alpha = 0.5)
    ax.axvspan(df['date'][trading_period[0]], df['date'][trading_period[1]], color='#8EBA42', alpha = 0.5)

    # training
    if (validation_start_index1 != None) and (validation_start_index2 != None) and (validation_start_index3 != None):

        training_period1 = (total_training_period[0], validation_start_index1-1)
        print(f"training period 1 = {training_period1}, total {training_period1[1]-training_period1[0]+1} days")
        ax.axvspan(df['date'][training_period1[0]], df['date'][training_period1[1]], color='#E24A33', alpha = 0.5)

        training_period2 = (validation_period1[1]+1, validation_start_index2-1)
        print(f"training period 2 = {training_period2}, total {training_period2[1]-training_period2[0]+1} days")
        ax.axvspan(df['date'][training_period2[0]], df['date'][training_period2[1]], color='#E24A33', alpha = 0.5)

        training_period3 = (validation_period2[1]+1, validation_start_index3-1)
        print(f"training period 3 = {training_period3}, total {training_period3[1]-training_period3[0]+1} days")
        ax.axvspan(df['date'][training_period3[0]], df['date'][training_period3[1]], color='#E24A33', alpha = 0.5)

        training_period4 = (validation_period3[1]+1, validation_period4[0]-1)
        print(f"training period 4 = {training_period4}, total {training_period4[1]-training_period4[0]+1} days")
        ax.axvspan(df['date'][training_period4[0]], df['date'][training_period4[1]], color='#E24A33', alpha = 0.5)


    fig.suptitle(ticker)
    fig.savefig(figdir + '/' + ticker + '_train_val_test.jpeg',bbox_inches='tight')
    fig.show()



def plot_train_val(df,
                        total_training_period,
                        ntrain,
                        validation_start_index1,
                        validation_start_index2,
                        validation_start_index3,
                        validation_period1,
                        validation_period2,
                        validation_period3,
                        validation_period4,
                        figdir,
                        ):
    ticker = df.tic.unique()[0]
    fig = px.line(x=np.arange(total_training_period[0], validation_period4[1]), y=df[total_training_period[0]:validation_period4[1]]['close'])
    fig.add_trace(go.Scatter(x=np.arange(total_training_period[0], validation_period4[1]), y=df[total_training_period[0]:validation_period4[1]]['close'],
                    mode='markers', name = "closing price", marker=dict(color='red', size=10)))

    if validation_start_index1 != None:
        fig.add_vrect(x0=validation_period1[0], x1=validation_period1[1], fillcolor="blue", opacity=0.25, line_width=0)
    if validation_start_index2 != None:
        fig.add_vrect(x0=validation_period2[0], x1=validation_period2[1], fillcolor="blue", opacity=0.25, line_width=0)
    if validation_start_index3 != None:
        fig.add_vrect(x0=validation_period3[0], x1=validation_period3[1], fillcolor="blue", opacity=0.25, line_width=0)

    fig.add_vrect(x0=validation_period4[0], x1=validation_period4[1], fillcolor="blue", opacity=0.25, line_width=0)


    d=round(ntrain/4)
    fig.add_vline(x=total_training_period[0]+d, line_width=2, line_dash="dash", line_color="black")
    fig.add_vline(x=total_training_period[0]+2*d, line_width=2, line_dash="dash", line_color="black")
    fig.add_vline(x=total_training_period[0]+3*d, line_width=2, line_dash="dash", line_color="black")
    fig.add_vline(x=total_training_period[0]+4*d, line_width=2, line_dash="dash", line_color="black")


    fig.write_image(figdir + '/' + ticker + '_train_val.jpeg')
    fig.show()

def plot_features(df, features,training_period1,window,trading_period):
    plt.style.use('ggplot')
    for ftr in features:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,5))
        # plt.figure(figsize=(12, 5))
        ax.plot(df['date'][training_period1[0]-window:trading_period[1]+1], df[ftr][training_period1[0]-window:trading_period[1]+1])
        ax.set_ylabel(ftr)
        # fig.gcf().autofmt_xdate()
        fig.show()

def plot_feature_corr_mat(df,features,training_period1,window,training_period4):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7,7))
    cor = df[features][training_period1[0]-window:training_period4[1]+1].corr()
    sns.heatmap(cor, cmap='rocket', annot=True, fmt=".2f", cbar=True,ax=ax, annot_kws={"fontsize":8})
    fig.show()
# d = {'zero': pd.Series(['a', 'b', 'c', 'd', 'e']),
#     'one': pd.Series([10.0, 20.0, 30.0, 40.0, 50.0]),
#      'two': pd.Series([10.0, -10.0, -30.0, 25.0, 30.0]),
#     'three': pd.Series([20.0, 10.0, 30.0, 40.0, 10.0])}
 
# # creates Dataframe.
# pdf = pd.DataFrame(d)

# fet = ['one', 'two', 'three']

# from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()

# scaler.fit(pdf[0:2][fet])

# display(pdf)
# pdf[fet] = pd.DataFrame(scaler.transform(pdf[fet]))
# pdf

def plot_returns(df_returns, tickers_list = [], filename = 'results/Strategy', period = 'daily', name_stock_world = None):
    
    plt.figure(figsize=(21,10), dpi=120)
    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,1.5]
    color_val = ['royalblue','red','darkorange','green','purple']
    plt.figure(figsize=(21,10), dpi=120)
    for idx in np.arange(len(df_returns.columns.to_list())):
        plt.plot(100*((df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()-1),color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx])
       
    plt.gcf().autofmt_xdate()
    # plt.xlabel("Date",fontsize=20)
    plt.legend(df_returns.columns.to_list(),fontsize=20)
    plt.ylabel("Cumulative Return (%)",fontsize=20)
    plt.xticks(fontsize=16, rotation=45)
    plt.yticks(fontsize=16)
    plt.grid(linestyle='dotted', linewidth=1)

    if len(tickers_list) == 0:
        suptitle_text = "Stock world: " + name_stock_world +'\n'
    else:
        suptitle_text = ""

    column_list = df_returns.columns.to_list()
    for i in range(len( column_list )):
        suptitle_text = suptitle_text + column_list[i] + "    CAGR: %.2f" % (100*ep.cagr(df_returns[df_returns.columns.to_list()[i]],period=period)) + ' ~ ' +\
                        "Sharpe Ratio: %.2f" % ep.sharpe_ratio(df_returns[df_returns.columns.to_list()[i]],period=period) + ' ~ ' +\
                        "Max Drawdown: %.2f" % (-100*ep.max_drawdown(df_returns[df_returns.columns.to_list()[i]]))+ "\n"
    if len(tickers_list) != 0:
        suptitle_text = suptitle_text + str(tickers_list)
    plt.suptitle(suptitle_text, fontsize=20)
    plt.tight_layout()
    plt.savefig(filename + '.jpeg')
    plt.show()
    plt.close()


def plot_returns_drawdown(df_returns, tickers_list = [], filename = 'results/Strategy', period = 'daily', name_stock_world = None):
    df_returns['date'] = mdates.date2num(df_returns.index)
    df_returns = df_returns.rename(columns = {"^GSPC":"S&P 500", "^NDX":"NASDAQ 100"})

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(21, 12), sharex=True,gridspec_kw={'height_ratios': [2.5, 1]})
    
    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,1.5]
    color_val = ['royalblue','red','darkorange','green','purple']
    for idx in np.arange(len(df_returns.columns.to_list())-1):
        ax1.plot(df_returns['date'].values,100*((df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()-1).values,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],label=f'{df_returns.columns.to_list()[idx]} Returns')
    ax1.legend(df_returns.columns.to_list(),fontsize=16)
    ax1.set_ylabel("Cumulative Return (%)",fontsize=16)
    ax1.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax1.grid(linestyle='dotted', linewidth=1)

    linestyle_val = ['-','-','-','-','-']
    linewidth_val = [1,1,1,1,1]
    color_val = ['royalblue', 'tomato', 'limegreen', 'mediumorchid', 'darkslategray']
    for idx in np.arange(len(df_returns.columns.to_list())-1):
        cum_return = (df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()
        drawdown = -(1 - cum_return / cum_return.cummax())*100
        ax2.fill_between(df_returns['date'], drawdown,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],alpha=0.3, label=f'{df_returns.columns.to_list()[idx]} Drawdown')
    ax2.set_xlabel('Date',fontsize=16)
    ax2.set_ylabel('Drawdown (%)',fontsize=16)
    ax2.legend(loc = "lower left")
    ax2.legend(df_returns.columns.to_list(),fontsize=16,loc = "lower left")
    ax2.xaxis_date()
    ax2.tick_params(axis='x', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax2.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax2.grid(linestyle='dotted', linewidth=1)

    if len(tickers_list) == 0:
        suptitle_text = "Stock world: " + name_stock_world +'\n'
    else:
        suptitle_text = ""

    column_list = df_returns.columns.to_list()
    for i in range(len(column_list)-1):
        suptitle_text = suptitle_text + column_list[i] + "    Cum Return: %.2f" % (100*ep.cum_returns_final(df_returns[df_returns.columns.to_list()[i]])) + "    CAGR: %.2f" % (100*ep.cagr(df_returns[df_returns.columns.to_list()[i]],period=period)) + ' ~ ' +\
                        "Sharpe Ratio: %.2f" % ep.sharpe_ratio(df_returns[df_returns.columns.to_list()[i]],period=period) + ' ~ ' +\
                        "Max Drawdown: %.2f" % (-100*ep.max_drawdown(df_returns[df_returns.columns.to_list()[i]]))+ "\n"
    if len(tickers_list) != 0:
        suptitle_text = suptitle_text + str(tickers_list)
    plt.suptitle(suptitle_text, fontsize=16)
    plt.tight_layout()
    fig.savefig(filename + '.jpeg')
    # plt.show()
    plt.close()

def plot_returns_cash_drawdown(df_returns, tickers_list = [], filename = 'results/Strategy', period = 'daily', name_stock_world = None):
    df_returns['date'] = mdates.date2num(df_returns.index)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(21, 16), sharex=True,gridspec_kw={'height_ratios': [2.5, 1, 1]})
    
    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,1.5]
    color_val = ['royalblue','red','darkorange','green','purple']
    for idx in np.arange(len(df_returns.columns.to_list())-3):
        ax1.plot(df_returns['date'].values,100*((df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()-1).values,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],label=f'{df_returns.columns.to_list()[idx]} Returns')
    ax1.legend(df_returns.columns.to_list(),fontsize=16)
    ax1.set_ylabel("Cumulative Return (%)",fontsize=16)
    ax1.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax1.grid(linestyle='dotted', linewidth=1)

    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,2]
    color_val = ['royalblue','red','darkorange','green','purple']

    ax2.plot(df_returns['date'],df_returns['Cash'],color = color_val[4],linestyle = linestyle_val[0],linewidth=linewidth_val[4],label='Cash Amount')
    ax2.plot(df_returns['date'],df_returns['Invested'],color = color_val[3],linestyle = linestyle_val[1],linewidth=linewidth_val[1],label='Invested Amount')
    ax2.fill_between(df_returns['date'], 0, df_returns['Cash'], where=(df_returns['Cash'] < 0), color='red', alpha=0.5, interpolate=True, label='Leverage')
    
    ax2.legend(fontsize=16,loc = "lower left")
    ax2.set_ylabel("Cash and Invested",fontsize=16)
    ax2.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax2.grid(linestyle='dotted', linewidth=1)

    linestyle_val = ['-','-','-','-','-']
    linewidth_val = [1,1,1,1,1]
    color_val = ['royalblue', 'tomato', 'limegreen', 'mediumorchid', 'darkslategray']
    for idx in np.arange(len(df_returns.columns.to_list())-3):
        cum_return = (df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()
        drawdown = -(1 - cum_return / cum_return.cummax())*100
        ax3.fill_between(df_returns['date'], drawdown,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],alpha=0.3, label=f'{df_returns.columns.to_list()[idx]} Drawdown')
    ax3.set_xlabel('Date',fontsize=16)
    ax3.set_ylabel('Drawdown (%)',fontsize=16)
    ax3.legend(loc = "lower left")
    ax3.legend(['DRL_Drawdown','Volatility_Target_Drawdown'],fontsize=16,loc = "lower left")
    ax3.xaxis_date()
    ax3.tick_params(axis='x', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax3.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax3.grid(linestyle='dotted', linewidth=1)

    if len(tickers_list) == 0:
        suptitle_text = "Stock world: " + name_stock_world +'\n'
    else:
        suptitle_text = ""

    column_list = df_returns.columns.to_list()
    for i in range(len(column_list)-3):
        suptitle_text = suptitle_text + column_list[i] + "    Cum Return: %.2f" % (100*ep.cum_returns_final(df_returns[df_returns.columns.to_list()[i]])) + "    CAGR: %.2f" % (100*ep.cagr(df_returns[df_returns.columns.to_list()[i]],period=period)) + ' ~ ' +\
                        "Sharpe Ratio: %.2f" % ep.sharpe_ratio(df_returns[df_returns.columns.to_list()[i]],period=period) + ' ~ ' +\
                        "Max Drawdown: %.2f" % (-100*ep.max_drawdown(df_returns[df_returns.columns.to_list()[i]]))+ "\n"
    if len(tickers_list) != 0:
        suptitle_text = suptitle_text + str(tickers_list)
    plt.suptitle(suptitle_text, fontsize=16)
    plt.tight_layout()
    fig.savefig(filename + '.jpeg')
    plt.show()
    plt.close()

def plot_backtest(df_returns, tickers_list = [], filename = 'results/Strategy', period = 'daily', name_stock_world = None):
    df_returns['date'] = mdates.date2num(df_returns.index)
    df_returns = df_returns.rename(columns = {"^GSPC":"S&P 500", "^NDX":"NASDAQ 100"})
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(21, 16), sharex=True,gridspec_kw={'height_ratios': [2.5, 1, 1]})
    
    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,1.5]
    color_val = ['royalblue','red','darkorange','green','purple']
    for idx in np.arange(len(df_returns.columns.to_list())-3):
        ax1.plot(df_returns['date'].values,100*((df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()-1).values,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],label=f'{df_returns.columns.to_list()[idx]} Returns')
    ax1.legend(df_returns.columns.to_list(),fontsize=16)
    ax1.set_ylabel("Cumulative Return (%)",fontsize=16)
    ax1.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax1.grid(linestyle='dotted', linewidth=1)

    linestyle_val = ['-','-.','-.','-.','-.']
    linewidth_val = [3,1.5,1.5,1.5,2]
    color_val = ['royalblue','red','darkorange','green','purple']

    ax2.plot(df_returns['date'].values,df_returns['Cash'].values,color = color_val[4],linestyle = linestyle_val[0],linewidth=linewidth_val[4],label='Cash Amount')
    ax2.plot(df_returns['date'].values,df_returns['Invested'].values,color = color_val[3],linestyle = linestyle_val[1],linewidth=linewidth_val[1],label='Invested Amount')
    # ax2.fill_between(df_returns['date'], 0, df_returns['Cash'], where=(df_returns['Cash'] < 0), color='red', alpha=0.5, interpolate=True, label='Leverage')
    
    ax2.legend(fontsize=16,loc = "lower left")
    ax2.set_ylabel("Cash and Invested",fontsize=16)
    ax2.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax2.grid(linestyle='dotted', linewidth=1)

    linestyle_val = ['-','-','-','-','-']
    linewidth_val = [1,1,1,1,1]
    color_val = ['royalblue', 'tomato', 'limegreen', 'mediumorchid', 'darkslategray']
    for idx in np.arange(len(df_returns.columns.to_list())-3):
        cum_return = (df_returns[df_returns.columns.to_list()[idx]]+1).cumprod()
        drawdown = -(1 - cum_return / cum_return.cummax())*100
        ax3.fill_between(df_returns['date'], drawdown,color = color_val[idx],linestyle = linestyle_val[idx],linewidth=linewidth_val[idx],alpha=0.3, label=f'{df_returns.columns.to_list()[idx]} Drawdown')
    ax3.set_xlabel('Date',fontsize=16)
    ax3.set_ylabel('Drawdown (%)',fontsize=16)
    ax3.legend(loc = "lower left")
    ax3.legend(['DRL_Drawdown','Volatility_Target_Drawdown'],fontsize=16,loc = "lower left")
    ax3.xaxis_date()
    ax3.tick_params(axis='x', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax3.tick_params(axis='y', labelsize=16)  # Set font size to 12 (adjust as needed)
    ax3.grid(linestyle='dotted', linewidth=1)

    if len(tickers_list) == 0:
        suptitle_text = "Stock world: " + name_stock_world +'\n'
    else:
        suptitle_text = ""

    column_list = df_returns.columns.to_list()
    for i in range(len(column_list)-3):
        suptitle_text = suptitle_text + column_list[i] + "    CAGR: %.2f" % (100*ep.cagr(df_returns[df_returns.columns.to_list()[i]],period=period)) + ' ~ ' +\
                        "Sharpe Ratio: %.2f" % ep.sharpe_ratio(df_returns[df_returns.columns.to_list()[i]],period=period) + ' ~ ' +\
                        "Max Drawdown: %.2f" % (-100*ep.max_drawdown(df_returns[df_returns.columns.to_list()[i]]))+ "\n"
    if len(tickers_list) != 0:
        suptitle_text = suptitle_text + str(tickers_list)
    plt.suptitle(suptitle_text, fontsize=16)
    plt.tight_layout()
    fig.savefig(filename + '.jpeg')
    # plt.show()
    plt.close()