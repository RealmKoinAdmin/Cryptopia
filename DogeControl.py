
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
# Public Cryptopia Trading System                                               #
# Unlicenced, Public Domain                                                     # 
#                                                                               #         
#USE AT OWN RISK!                                                               #
#################################################################################
|[VIVIAN]| >>: Welcome To Vivians Central Cryptopia Monitoring System.''')
print('|[VIVIAN]|>>: Welcome To Cryptopia DOGE/BTC Trader! Written By Skrypt Please Feel Free To Donate In BTC!')
print('|[VIVIAN]|>>: Skrypt [BTC] Donation Address: [1KwnTGnuhBQHFkxTnaYiPt7RyJYJGzDcWn]')

####### OBJECT GUTS BELOW ######
def set_trade_amount():
 global DOGE
 global Doge_Set
 balance_doge,error = client.get_balance('DOGE')
 balance_btc,error = client.get_balance('BTC')
 tick = client.get_market('DOGE_BTC')
 Sell = tick[0]['AskPrice']
 print('|[CRYPTOPIA]|>>: Current DOGE Balance: [{}].'.format(balance_doge['Available']))
 print('|[CRYPTOPIA]|>>: Current BTC Balance: [{}].'.format(balance_btc['Available']))
 print('|[VIVIAN]|>>: You May Trade Current BTC: [{}] For [{}] DOGE At [{}] Satoshi Per DOGE'.format(balance_btc['Available'],(balance_btc['Available']-balance_btc['Available']*0.00201)//Sell,Sell*1e8))
 print('|[VIVIAN]|>>: You May Trade Current DOGE: [{}] For [{}] BTC At [{}] Satoshi Per DOGE'.format(balance_doge['Available'],(balance_doge['Available']-balance_doge['Available']*0.00201)*Sell,Sell*1e8))
 print('|[VIVIAN]|>>: How Much DOGE Are You Trading? [FLOAT/#.#]')
 DOGE = input('|[INPUT]|>>: ')
 try:
  squishy = '0.1'
  Test = float(DOGE) + float(squishy)
  print('|[VIVIAN]|>>: DOGE To Be Traded: [{}].'.format(DOGE))
  Doge_Set = True
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
 tick = client.get_market('DOGE_BTC')
 Sell = tick[0]['AskPrice'] * 1e8
 print('|[VIVIAN]|>>: Last DOGE Sale Price Satoshi Per DOGE [{}].'.format(Sell))
 print('|[VIVIAN]|>>: How Much Max Do You Want To Spend Per DOGE In Satoshi? [FLOAT/#.#]')
 BUY_MAX = input('|[INPUT]|>>: ')
 try:
  Test = float(BUY_MAX) + 0.1
  print('|[VIVIAN]|>>: Spending: [{}] Max Satoshi Per DOGE.'.format(BUY_MAX))
  Buy_Max_Set = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_buy_max()

def set_sell_min():
 global SELL_MIN
 global Sell_Min_Set
 tick = client.get_market('DOGE_BTC')
 Buy = tick[0]['BidPrice'] * 1e8
 print('|[VIVIAN]|>>: Last DOGE Buy Price Satoshi Per DOGE [{}].'.format(Buy))
 print('|[VIVIAN]|>>: How Much Min Do You Want To Sell Per DOGE In Satoshi? [FLOAT/#.#]')
 SELL_MIN = input('|[INPUT]|>>: ')
 try:
  Test = float(SELL_MIN) + 0.1
  print('|[VIVIAN]|>>: Selling Each DOGE For [{}] Min Satoshi Per DOGE.'.format(SELL_MIN))
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
 tick = client.get_market('DOGE_BTC')
 if float(tick[0]['AskPrice']) * 1e8 >= float(SELL_MIN):
  return [True, tick[0]['AskPrice'] * 1e8]
 else:
  return [False, tick[0]['AskPrice'] * 1e8]

def calc_buy():
 tick = client.get_market('DOGE_BTC')
 orders = client.get_openorders('DOGE_BTC')
 if float(tick[0]['BidPrice']) * 1e8 <= float(BUY_MAX):
  return [True, tick[0]['BidPrice'] * 1e8]
 else:
  return [False, tick[0]['BidPrice'] * 1e8]

def get_doge_balance():
 balance,error = client.get_balance('DOGE')
 if balance['Available'] > 0.0:
  return 'Sell'
 elif balance['Available'] <= 0.0:
  return 'Buy'

def sell_doge():
 tick = client.get_market('DOGE_BTC')
 balance,error = client.get_balance('DOGE')
 if float(balance['Available']) >= float(DOGE):
  print('Selling {} DOGE For {} Satoshi Each'.format(DOGE,tick[0]['BidPrice']*1e8))
  sold = client.submit_trade('DOGE/BTC', 'Sell', tick[0]['BidPrice'], DOGE)
  print(sold)
 elif float(balance['Available']) < float(ETN) and float(balance['Available']) > 0:
  print('|[VIVIAN]|>>: Selling {} DOGE For {} Satoshi Each'.format(balance['Available'],tick[0]['BidPrice']*1e8))
  sold = client.submit_trade('DOGE/BTC', tick[0]['BidPrice'], balance['Available'])
  print(sold)
 else:
  print('|[VIVIAN]|>>: Not Enough Balance For Trading Routine.')

def buy_doge():
 tick = client.get_market('DOGE_BTC')
 balance,error = client.get_balance('BTC')
 balance_doge,error = client.get_balance('DOGE')
 if float(tick[0]['AskPrice'])*float(DOGE) <= float(balance['Available']):
  print('|[VIVIAN]|>>: Buying {} DOGE For {} Satoshi Each'.format(DOGE,tick[0]['AskPrice']*1e8))
  bought = client.submit_trade('DOGE/BTC', tick[0]['AskPrice'], float(tick[0]['AskPrice'])*float(DOGE))
  print(bought)
 elif float(tick[0]['AskPrice'])*(float(DOGE)-float(balance_doge['Available'])) <= balance['Available']:
  print('|[VIVIAN]|>>: Buying {} DOGE For {} Satoshi Each'.format((float(DOGE)-float(balance_doge['Available'])),tick[0]['AskPrice']*1e8))
  bought = client.submit_trade('DOGE/BTC', tick[0]['AskPrice'], float(tick['AskPrice'])*(float(DOGE)-float(balance_doge['Available'])))
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
 global Doge_Set
 Timer_Set = None
 Api_Key_Set = None
 Api_Secret_Set = None
 Buy_Max_Set = None
 Sell_Min_Set = None
 Doge_Set = None
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
 if Doge_Set == None or Doge_Set == False:
  set_trade_amount()
 if Buy_Max_Set == None or Buy_Max_Set == False:
  set_buy_max()
 if Sell_Min_Set == None or Sell_Min_Set == False:
  set_sell_min()
 else:
  try:
   trade = get_doge_balance()
   if trade == 'Sell':
    should_sell = calc_sell()
    if should_sell[0] == True:
     print('|[SELL]|>>: Selling DOGE At {} Satoshi'.format(should_sell[1]))
     transaction = sell_doge()
     time.sleep(float(TIMER))
    else:
     print('|[SELL]|>>: Waiting For Price Flux')
     time.sleep(float(TIMER))
   elif trade == 'Buy':
    should_buy = calc_buy()
    if should_buy[0] == True:
     print('|[BUY]|>>: Buying DOGE At {} Satoshi'.format(should_buy[1]))
     transaction = buy_doge()
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

