
import time
from cryptopia_api import Api
print('''
#################################################################################
#                                                                               #
#                                                                               #
#____   ____.__      .__                                                        #
#\   \ /   /|__|__  _|__|____    ____                                           #
# \   Y   / |  \  \/ /  \__  \  /    \                                          #
#  \     /  |  |\   /|  |/ __ \|   |  \                                         #
#   \___/   |__| \_/ |__(____  /___|  /                                         #
#                            \/     \/                                          #
#                                       v0.3.2                                  #
# C.T.S:                                                                        #
# Public Cryptopia Trading System                                              #
# Unlicenced, Public Domain                                                     # 
#                                                                               #         
#USE AT OWN RISK!                                                               #
#################################################################################
|[Vivian]| >>: Welcome To Vivians Central Server Monitoring System.''')
print('|[VIVIAN]|>>: Welcome To Cryptopia ETN/BTC Trader! Written By Skrypt Please Feel Free To Donate In BTC!')
print('|[VIVIAN]|>>: Skrypt [BTC] Donation Address: [1KwnTGnuhBQHFkxTnaYiPt7RyJYJGzDcWn]')

####### OBJECT GUTS BELOW ######
def set_trade_amount():
 global ETN
 global Etn_Set
 balance_etn = client.get_balance('ETN')
 balance_btc = client.get_balance('BTC')
 tick = client.get_market('ETN_BTC')
 Sell = tick['AskPrice']
 print('|[CRYPTOPIA]|>>: Current ETN Balance: [{}].'.format(balance_etn['Available']))
 print('|[CRYPTOPIA]|>>: Current BTC Balance: [{}].'.format(balance_btc['Available']))
 print('|[VIVIAN]|>>: You May Trade Current BTC: [{}] For [{}] ETN At [{}] Satoshi Per ETN'.format(balance_btc['Available'],(balance_btc['Available']-balance_btc['Available']*0.00201)//Sell,Sell*1e8))
 print('|[VIVIAN]|>>: How Much ETN Are You Trading? [FLOAT/#.#]')
 ETN = input('|[INPUT]|>>: ')
 try:
  squishy = '0.1'
  Test = float(ETN) + float(squishy)
  print('|[VIVIAN]|>>: ETN To Be Traded: [{}].'.format(ETN))
  Etn_Set = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_trade_amount()
  
def set_call_timer():
 global TIMER
 global Timer_Set
 print('|[VIVIAN]|>>: How Much Time (In Seconds) Between Calls? [FLOAT/#.#]')
 TIMER = input('|[INPUT]|>>: ')
 try:
  Test = float(TIMER) + 0.1
  print('|[VIVIAN]|>>: Time In Seconds Before Each Call: [{}].'.format(TIMER))
  Timer_Set = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_call_timer()

def set_buy_max():
 global BUY_MAX
 global Buy_Max_Set
 tick = client.get_market('ETN_BTC')
 Sell = tick['AskPrice'] * 1e8
 print('|[VIVIAN]|>>: Last ETN Sale Price Satoshi Per ETN [{}].'.format(Sell))
 print('|[VIVIAN]|>>: How Much Max Do You Want To Spend Per ETN In Satoshi? [FLOAT/#.#]')
 BUY_MAX = input('|[INPUT]|>>: ')
 try:
  Test = float(BUY_MAX) + 0.1
  print('|[VIVIAN]|>>: Spending: [{}] Max Satoshi Per ETN.'.format(BUY_MAX))
  Buy_Max_Set = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_buy_max()

def set_sell_min():
 global SELL_MIN
 global Sell_Min_Set
 tick = client.get_market('ETN_BTC')
 Buy = tick['BidPrice'] * 1e8
 print('|[VIVIAN]|>>: Last ETN Buy Price Satoshi Per ETN [{}].'.format(Buy))
 print('|[VIVIAN]|>>: How Much Min Do You Want To Sell Per ETN In Satoshi? [FLOAT/#.#]')
 SELL_MIN = input('|[INPUT]|>>: ')
 try:
  Test = float(SELL_MIN) + 0.1
  print('|[VIVIAN]|>>: Selling Each ETN For [{}] Min Satoshi Per ETN.'.format(SELL_MIN))
  Sell_Min_Set = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_sell_min()

def set_api_key():
 global API_KEY
 global Api_Key_Set
 print('|[VIVIAN]|>>: Please Enter Cryptopia API Key [KEY]')
 API_KEY = input('|[INPUT]|>>: ')
 try:
  print('|[VIVIAN]|>>: Current API Key: [{}].'.format(API_KEY))
  Api_Key_Set = True
 except Exception as Api_Key_Error:
  print('|[VIVIAN]|>>: You Must Enter A Cryptopia API Key.')
  set_api_key()

def set_api_secret():
 global API_SECRET
 global Api_Secret_Set
 print('|[VIVIAN]|>>: Please Enter Cryptopia API Secret [SECRET]')
 API_SECRET = input('|[INPUT]|>>: ')
 try:
  print('|[VIVIAN]|>>: Current API Secret: [{}].'.format(API_SECRET))
  Api_Secret_Set = True
 except Exception as Api_Secret_Error:
  print('|[VIVIAN]|>>: You Must Enter A Cryptopia API Secret.')
  set_api_secret()

def calc_sell():
 tick = client.get_market('ETN_BTC')
 if float(tick['AskPrice']) * 1e8 >= float(SELL_MIN):
  return [True, tick['AskPrice'] * 1e8]
 else:
  return [False, tick['AskPrice'] * 1e8]

def calc_buy():
 tick = client.get_market('ETN_BTC')
 orders = client.get_openorders('ETN_BTC')
 if float(tick['BidPrice']) * 1e8 <= float(BUY_MAX):
  return [True, tick['BidPrice'] * 1e8]
 else:
  return [False, tick['BidPrice'] * 1e8]

def get_etn_balance():
 balance = client.get_balance('ETN')
 if balance['Available'] > 0.0:
  return 'Sell'
 elif balance['Available'] <= 0.0:
  return 'Buy'

def sell_etn():
 tick = client.get_market('ETN_BTC')
 balance = client.get_balance('ETN')
 if float(balance['Available']) >= float(ETN):
  print('Selling {} ETN For {} Satoshi Each'.format(ETN,tick['BidPrice']*1e8))
  sold = client.submit_trade('ETN/BTC', 'Sell', tick['BidPrice'], ETN)
  print(sold)
 elif float(balance['Available']) < float(ETN) and float(balance['Available']) > 0:
  print('|[VIVIAN]|>>: Selling {} ETN For {} Satoshi Each'.format(balance['Available'],tick['BidPrice']*1e8))
  sold = client.submit_trade('ETN/BTC', tick['BidPrice'], balance['Available'])
  print(sold)
 else:
  print('|[VIVIAN]|>>: Not Enough Balance For Trading Routine.')

def buy_etn():
 tick = client.get_market('ETN_BTC')
 balance = client.get_balance('BTC')
 balance_etn = client.get_balance('ETN')
 if float(tick['AskPrice'])*float(ETN) <= float(balance['Available']):
  print('|[VIVIAN]|>>: Buying {} ETN For {} Satoshi Each'.format(ETN,tick['AskPrice']*1e8))
  bought = client.submit_trade('ETN/BTC', tick['AskPrice'], float(tick['AskPrice'])*float(ETN))
  print(bought)
 elif float(tick['AskPrice'])*(float(ETN)-float(balance_etn['Available'])) <= balance['Available']:
  print('|[VIVIAN]|>>: Buying {} ETN For {} Satoshi Each'.format((float(ETN)-float(balance_etn['Available'])),tick['AskPrice']*1e8))
  bought = client.submit_trade('ETN/BTC', tick['AskPrice'], float(tick['AskPrice'])*(float(ETN)-float(balance_etn['Available'])))
  print(bought)
 else:
  print('|[VIVIAN]|>>: Not Enough Balance BTC For Trading Routine.')

def Activate_Client():
 global client
 try:
  client = Api(API_KEY, API_SECRET)
  print('|[VIVIAN]|>>: Cryptopia Client Activated With API Key [{}].'.format(API_KEY))
 except Exception as Client_Error:
  print('|[VIVIAN]|>>: There Was A Client Activation Error Trying Again.')
  Activate_Client()

def set_globals():
 global Timer_Set
 global Api_Key_Set
 global Api_Secret_Set
 global Buy_Max_Set
 global Sell_Min_Set
 global Etn_Set
 Timer_Set = None
 Api_Key_Set = None
 Api_Secret_Set = None
 Buy_Max_Set = None
 Sell_Min_Set = None
 Etn_Set = None
 print('|[VIVIAN]|>>: All Global Controls Reset To [NONE]')

print('|[VIVIAN]|>>: Setting Global Controls Now.')
set_globals()
while True:
 if Timer_Set == None or Timer_Set == False:
  set_call_timer()
 if Api_Key_Set == None or Api_Key_Set == False:
  set_api_key()
 if Api_Secret_Set == None or Api_Key_Set == False:
  set_api_secret()
  Activate_Client()
 if Etn_Set == None or Etn_Set == False:
  set_trade_amount()
 if Buy_Max_Set == None or Buy_Max_Set == False:
  set_buy_max()
 if Sell_Min_Set == None or Sell_Min_Set == False:
  set_sell_min()
 else:
  try:
   trade = get_etn_balance()
   if trade == 'Sell':
    should_sell = calc_sell()
    if should_sell[0] == True:
     print('|[SELL]|>>: Selling ETN At {} Satoshi'.format(should_sell[1]))
     transaction = sell_etn()
     time.sleep(float(TIMER))
    else:
     print('|[SELL]|>>: Waiting For Price Flux')
     time.sleep(float(TIMER))
   elif trade == 'Buy':
    should_buy = calc_buy()
    if should_buy[0] == True:
     print('|[BUY]|>>: Buying ETN At {} Satoshi'.format(should_buy[1]))
     transaction = buy_etn()
     time.sleep(float(TIMER))
    else:
     print('|[BUY]|>>: Waiting For Price Flux')
     time.sleep(float(TIMER))
   else:
    print('|[VIVIAN]|>>: Something Has Fucked Up, Waiting Timer Then Trying Again')
    time.sleep(float(TIMER))
  except Exception as Run_Time_Error:
   print('|[VIVIAN]|>>: We Have Had The Following Run Time Error: [{}]'.format(Run_Time_Error))
   print('|[VIVIAN]|>>: Going To Instruct Program To Exit Contact Skrypt With Plenty Of Information Including [{}].'.format(Run_Time_Error))

