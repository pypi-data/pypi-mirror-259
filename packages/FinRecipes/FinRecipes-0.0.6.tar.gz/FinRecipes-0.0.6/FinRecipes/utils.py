import os
import pandas as pd
import empyrical as ep


# Function to calculate volatility
def compute_rolling_volatility(df_return, lookback_period):
    df_return['volatility'] = df_return['returns'].rolling(window=lookback_period).std()*np.sqrt(252)
    return df_return

# Function to calculate momentum
def compute_rolling_momentum(price_data, lookback_period):
    price_data['returns'] = price_data['close'].pct_change().fillna(0)
    price_data['momentum'] = price_data['returns'].rolling(window=lookback_period).mean()
    return price_data

def list_files_starting_with(directory_path, prefix):
    files = [file for file in os.listdir(directory_path) if file.startswith(prefix)]
    files.sort()
    files = [os.path.join(directory_path, f) for f in files]
    return files

def list_files_paths_starting_with(directory_path, prefix):
    files = [file for file in os.listdir(directory_path) if file.startswith(prefix)]
    files.sort()
    files_path = [os.path.join(directory_path, f) for f in files]
    return files, files_path

def list_files_paths_end_with(directory_path, extension = '.zip'):
    files = [f for f in os.listdir(directory_path) if f.endswith(extension)]
    files.sort()
    files_paths = [os.path.join(directory_path, f) for f in files]
    return files, files_paths

def list_files_end_with(directory_path, extension = '.zip'):
    files = [f for f in os.listdir(directory_path) if f.endswith(extension)]
    files.sort()
    files_paths = [os.path.join(directory_path, f) for f in files]
    return files

def check_directory_exists(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):

        print(f"The directory '{directory_path}' exists.")
        return True
    else:
        print(f"The directory '{directory_path}' does not exist.")

def add_tickers_file(filepath = 'datasets/tickers_list.txt'):
    # ============== Add a tickers list from a text file =========================
    TICKERS_LIST = []
    with open(filepath, 'r') as file:
        for line in file:
            # Remove newline characters from the line
            line = line.strip()
            TICKERS_LIST.append(line)
    # print(TICKERS_LIST) 
    return TICKERS_LIST

def create_folders(config):
    if not os.path.exists("./" + config.DATA_SAVE_DIR):
        os.makedirs("./" + config.DATA_SAVE_DIR)
    if not os.path.exists("./" + config.TRAINED_MODEL_DIR):
        os.makedirs("./" + config.TRAINED_MODEL_DIR)
    if not os.path.exists("./" + config.TENSORBOARD_LOG_DIR):
        os.makedirs("./" + config.TENSORBOARD_LOG_DIR)
    if not os.path.exists("./" + config.RESULTS_DIR):
        os.makedirs("./" + config.RESULTS_DIR)

def data_split(df, start, end, target_date_col="date"):
    """
    split the dataset into training or testing using date
    :param data: (df) pandas dataframe, start, end
    :return: (df) pandas dataframe
    """
    # df[target_date_col] = pd.to_datetime(df[target_date_col])
    # start = pd.to_datetime(start, utc = True)
    # end = pd.to_datetime(end, utc = True)
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    data = df[(df[target_date_col] >= start) & (df[target_date_col] <= end)]
    data = data.sort_values([target_date_col, "tic"], ignore_index=True)
    data.index = data[target_date_col].factorize()[0]
    return data

def check_and_make_directories(directories: list):
    for directory in directories:
        if not os.path.exists("./" + directory):
            os.makedirs("./" + directory)

def gen_first_day_month(start_date, end_date):
    date = start_date.replace(day=1)  # Set the day to 1st of the start month

    while date <= end_date:
        yield date
        date += pd.DateOffset(months=1)  # Move to the 1st day of the next month

def gen_third_fridays_dates(start_date, end_date):
    date = start_date

    while date <= end_date:
        if date.weekday() == 4 and 15 <= date.day <= 21:
            yield date
        date += pd.Timedelta(days=1)

def gen_friday_dates(start_date, end_date):
    date = start_date
    while date <= end_date:
        if date.weekday() == 4:  # Check if the current date is a Friday (0=Monday, 1=Tuesday, ..., 6=Sunday)
            yield date
        date += pd.DateOffset(days=1)  # Move to the next day

def is_friday(date):
    if date.weekday() == 4:  # Check if the current date is a Friday (0=Monday, 1=Tuesday, ..., 6=Sunday)
        return True
    else:
        return False

def first_day_month_list(start_date, end_date):
    date = start_date.replace(day=1)  # Set the day to 1st of the start month
    date_list = []
    while date <= end_date:
        # yield date
        date_list.append(date.date())
        date += pd.DateOffset(months=1)  # Move to the 1st day of the next month

    return date_list

def third_fridays_dates_list(start_date, end_date):
    date = start_date
    
    date_list = []
    while date <= end_date:
        if date.weekday() == 4 and 15 <= date.day <= 21:
            # yield date
            date_list.append(date.date())
        date += pd.Timedelta(days=1)

    return date_list

def first_monday_dates_list(start_date, end_date):
    date = start_date
    
    date_list = []
    while date <= end_date:
        if date.weekday() == 0 and 1 <= date.day <= 7:
            # yield date
            date_list.append(date.date())
        date += pd.Timedelta(days=1)

    return date_list


def trans_cost_ibkr(position, price, quantity, instrument = "stocks"):
    # https://www.interactivebrokers.com/en/pricing/commissions-stocks.php?re=amer
    # effective_trans_cost = effective_trans_cost + Regulatory Fees
    if instrument == "stocks":
        ## compute transaction cost
        n_stocks = quantity
        stock_price = price
        trans_type = position

        monthly_volume = 200

        if monthly_volume <= 300000:
            trans_cost = 0.005 * n_stocks
            trade_value = stock_price * n_stocks

            max_per_order = 0.01 * trade_value
            min_per_order = 1

            if max_per_order < min_per_order:
                effective_trans_cost = trade_value * 0.01
            elif trans_cost <= 1:
                effective_trans_cost = 1
            else:
                effective_trans_cost = min(trans_cost, max_per_order)

            if trans_type == "SELL":
                effective_trans_cost = effective_trans_cost + 0.000008*trade_value + 0.000145 * n_stocks





        print(f"Minimum per order = $ {min_per_order}")
        print(f"Maximum per order = $ {max_per_order}")
        print(f"Trans_cost = $ {trans_cost}")
        print(f"Trade value = $ {trade_value}")
        print(f"Final Transaction cost = $ {effective_trans_cost}")
    else:
        print("Options transaction cost is to be updated")

def weekday_dates_list(start_date, end_date, weekday = 4):
    date = start_date

    date_list = []
    while date <= end_date:
        if date.weekday() == weekday:  # Check if the current date is a Friday (0=Monday, 1=Tuesday, ..., 6=Sunday)
            # yield date
            date_list.append(date.date())
        date += pd.DateOffset(days=1)  # Move to the next day

    return date_list

def plot_returns(bnh_returns, with_indices = False, RESULTS_DIR = 'results'):
    bnh_returns = bnh_returns.rename(columns = {'Buy_Hold_returns':'Buy-Hold','^GSPC': 'S&P 500', '^NDX': 'NASDAQ 100','^RUT':'RUSSELL 2000'})

    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')
    # %matplotlib inline
    plt.figure(figsize=(21,10), dpi=120)
    plt.plot(100*((bnh_returns+1).cumprod()-1),linewidth=2)
    plt.gcf().autofmt_xdate()
    # plt.xlabel("Date",fontsize=20)
    plt.legend(bnh_returns.columns.to_list(),fontsize=20)
    plt.ylabel("Cumulative Return (%)",fontsize=20)
    plt.xticks(fontsize=16, rotation=45)
    plt.yticks(fontsize=16)

    suptitle_text = "Buy-Hold"+"    CAGR: %.2f" % (100*ep.cagr(bnh_returns[bnh_returns.columns.to_list()[0]])) + ' ~ ' +\
            "Sharpe Ratio: %.2f" % ep.sharpe_ratio(bnh_returns[bnh_returns.columns.to_list()[0]]) + ' ~ ' +\
            "Max Drawdown: %.2f" % (-100*ep.max_drawdown(bnh_returns[bnh_returns.columns.to_list()[0]])) + "\n"

    indices_list = bnh_returns.columns.to_list()[1:]
    if with_indices:
        for i in range(len(indices_list)):
            suptitle_text = suptitle_text + indices_list[i] +"    CAGR: %.2f" % (100*ep.cagr(bnh_returns[bnh_returns.columns.to_list()[i+1]])) + ' ~ ' +\
            "Sharpe Ratio: %.2f" % ep.sharpe_ratio(bnh_returns[bnh_returns.columns.to_list()[i+1]]) + ' ~ ' +\
            "Max Drawdown: %.2f" % (-100*ep.max_drawdown(bnh_returns[bnh_returns.columns.to_list()[i+1]]))+ "\n"
        
    # suptitle_text = suptitle_text
    plt.suptitle(suptitle_text, fontsize=20)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR + '/Buy_n_Hold_Cum_Return.jpeg')
    plt.show()
    # plt.close()