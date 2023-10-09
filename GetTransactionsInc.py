import requests
import json
import os
import pandas as pd
from datetime import datetime, timedelta

refresh = 1
sandbox = 0
which_key = 'alt'

# set start date to the first of any month. 
start_date = '2023-10-01'

if sandbox == 1:
    file = 'sandbox_config.json'
else:
    file = 'config.json'

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
config_dir = os.path.join(parent_dir, 'Config')
output_dir = os.path.join(parent_dir, 'Output')
acc_dir = os.path.join(output_dir, 'Accounts')
trx_dir = os.path.join(output_dir, 'Transactions')
trx_csv_dir = os.path.join(output_dir, 'TransactionsCSV')

all_transactions_csv = os.path.join(trx_csv_dir, 'all.csv')

config_file = os.path.join(config_dir, file)

if which_key == 'main' and sandbox == 0:
    key_string = 'main_api_key'
elif which_key == 'alt' and sandbox == 0:
    key_string = 'alt_api_key'
else:
    key_string = 'api_key'

with open(config_file) as cf:
    config = json.load(cf)
    host = config["host"]
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    acc_id = config["acc_id"]
    api_key = config[key_string]
    auth = config["auth_base64"]

def InitialAuth():
    endpoint = '/identity/v2/oauth2/token'
    url = host + endpoint
    payload = 'grant_type=client_credentials'
    headers = {
      'x-api-key': api_key,
      'Accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': f'Basic {auth}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print('API Key Authentication Successful')
        pass
    else:
        print('API Key Authentication Failed')
        print('Status Code:', response.status_code)
    btj = response.json()
    bt = btj['access_token']
    return bt

def GetTransactions(start,end):
    endpoint = f'/za/pb/v1/accounts/{acc_id}/transactions?fromDate={start}&toDate={end}'
    url = host + endpoint
    payload = 'grant_type=client_credentials'
    bt = InitialAuth()
    headers_bearer_token = {
      'x-api-key': api_key,
      'Accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': f'Bearer {bt}'
    }

    transactions_file = os.path.join(trx_dir, f'transactions_{start}_to_{end}.json')

    response = requests.request("GET", url, headers=headers_bearer_token, data=payload)

    if response.status_code == 200:
        print('Bearer Token Authentication Successful')
        #print('Response:', response.json())
        transactions_details = json.dumps(response.json(), indent=4)
        with open(transactions_file, 'w+') as af:
            af.write(transactions_details)
        pass
    else:
        print('Bearer Token Authentication Failed')
        print('Status Code:', response.status_code)

def ConvertTransactionsToCSV():
    transaction_list = []
    for trfile in os.scandir(trx_dir):
        with open(trfile) as tf:
            json_data = json.load(tf)
            transactions = json_data["data"]["transactions"]
            df = pd.DataFrame(transactions)
            df["amount"] = df["amount"].astype(float)
            df["runningBalance"] = df["runningBalance"].astype(float)
        transaction_list.append(df)
    combined_df = pd.concat(transaction_list, ignore_index=True)
    combined_df = combined_df.sort_values(by='postedOrder')
    combined_df.to_csv(all_transactions_csv, index=False)

start_date = datetime.strptime(start_date, '%Y-%m-%d')
today = datetime.today()

while start_date <= today:
    start_date = start_date.replace(day=1)
    start_date_ini = start_date
    
    if start_date.month == 12:
        start_date = start_date.replace(year=start_date.year + 1, month=1)
    else:
        start_date = start_date.replace(month=start_date.month + 1)

    end_date = start_date.replace(day=1) - timedelta(days=1)

    start_date_string = str(start_date_ini.strftime('%Y-%m-%d'))
    end_date_string = str(end_date.strftime('%Y-%m-%d'))

    if refresh == 1:
        GetTransactions(start_date_string, end_date_string)
        pass
    else:
        pass

ConvertTransactionsToCSV()