import csv
import os
import datetime
from dotenv import load_dotenv
from solana.rpc.api import Client
from solders.pubkey import Pubkey

load_dotenv()

wallet = Pubkey.from_string(os.getenv('PUB_KEY_1'))
wallet2 = Pubkey.from_string(os.getenv('PUB_KEY_2'))
solana_client = Client(os.getenv('RPC_ENDPOINT'))
file_csv = os.getenv('FILE_CSV')

#Current date & time 
now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
hour = '{:02d}'.format(now.hour)
time_output = '{}/{}/{}'.format(month, day,year)

#append CSV with only one wallet
def csvwriter(wallet,file_csv):
    balance = solana_client.get_balance(wallet).value
    ui_balance = round(balance*10**(-9), 9)
    print(time_output)
    print(ui_balance)
    with open(file_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time_output, hour, ui_balance])

#append CSV with 2 wallets
def csvwriter2(wallet,wallet2,file_csv):
    balance1 = solana_client.get_balance(wallet).value
    balance2 = solana_client.get_balance(wallet2).value
    ui_balance1 = round(balance1*10**(-9), 9)
    ui_balance2 = round(balance2*10**(-9), 9)
    print(time_output,'\n', ui_balance1, '\n',ui_balance2)
    with open(file_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time_output, hour, ui_balance1,ui_balance2])
        

csvwriter2(wallet,wallet2, file_csv)