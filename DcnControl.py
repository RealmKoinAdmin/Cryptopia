
import time
from cryptopia_api import Api

User = dict()
Cryptopia = dict()

####### OBJECT GUTS BELOW ######
def vivian_banner():
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
 #USE AT OWN RISK!          ~Dentacoin (DCN) CONTROLLER~                         #
 #################################################################################
|[VIVIAN]| >>: Welcome To My Central Cryptopia Monitoring System.''')
 print('|[VIVIAN]|>>: Written By Skrypt Please Feel Free To Donate In To The RealmKoin Project!')
 print('|[VIVIAN]|>>: (RK) [ETH/Tokens] Donation Address: [0xdb436485f38d0f9c78acfb20ededc97419eb2ea5]')

### Sets Amount Of DCN To Be Traded ###
def set_trade_amount():
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 print('|[CRYPTOPIA]|>>: Current DCN Balance: [{}].'.format(User['Wallets']['DCN']['Balance']))
 print('|[CRYPTOPIA]|>>: Current BTC Balance: [{}].'.format(User['Wallets']['Bitcoin']['Balance']))
 print('|[VIVIAN]|>>: You May Trade Current BTC: [{}] For [{}] DCN At [{}] Satoshi Per DCN Volume Available: [{}]'.format(User['Wallets']['Bitcoin']['Balance'],(User['Wallets']['Bitcoin']['Balance']-User['Wallets']['Bitcoin']['Balance']*0.00201)//Cryptopia['DCN Current Ask'][0],
                                                                                                     Cryptopia['DCN Current Ask'][0]*1e8,Cryptopia['DCN Current Ask'][1]))
 print('|[VIVIAN]|>>: You May Trade Current DCN: [{}] For [{}] BTC At [{}] Satoshi Per DCN Volume Available: [{}]'.format(User['Wallets']['DCN']['Balance'],(User['Wallets']['DCN']['Balance']-User['Wallets']['DCN']['Balance']*0.00201)*Cryptopia['DCN Current Bid'][0],
                                                                                                     Cryptopia['DCN Current Bid'][0]*1e8,Cryptopia['DCN Current Bid'][1]))
 print('|[VIVIAN]|>>: How Much DCN Are You Trading? [FLOAT/#.#]')
 DCN = input('|[INPUT]|>>: ')
 try:
  squishy = '0.1'
  Test = float(DCN) + float(squishy)
  print('|[VIVIAN]|>>: DCN To Be Traded: [{}].'.format(DCN))
  User['DCN Set'] = True
  User['DCN Trade Amount'] = float(DCN)
  if User['Wallets']['DCN']['Balance'] < float(DCN):
   print('|[VIVIAN]|>>: Adjusting To Buy State. {} Needed Before Sell Conversion.'.format(float(DCN) - User['Wallets']['DCN']['Balance']))
   User['State'] = 1
   User['DCN Left To Buy'] = float(DCN) - User['Wallets']['DCN']['Balance']
   User['DCN Left To Sell'] = 0.0
  elif User['Wallets']['DCN']['Balance'] >= float(DCN):
   print('|[VIVIAN]|>>: Adjusting To Sell State. {} Original DCN Balance Before Sell Conversion.'.format(User['Wallets']['DCN']['Balance']))
   User['State'] = 2
   User['DCN Left To Sell'] = float(DCN)
   User['DCN Left To Buy'] = 0.0
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_trade_amount()


### Sets Timing Between Calls To Cryptopia ###
def set_call_timer():
 global Cryptopia
 global User
 print('|[VIVIAN]|>>: How Much Time (In Seconds) Between Calls? [FLOAT/#.#]')
 TIMER = input('|[INPUT]|>>: ')
 try:
  Test = float(TIMER) + 0.1
  print('|[VIVIAN]|>>: Time In Seconds Before Each Call: [{}].'.format(TIMER))
  User['Timer Set'] = True
  Cryptopia['Time Between Calls'] = float(TIMER)
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_call_timer()


### Sets Maximum Buy Price In Satoshi Per DCN ###
def set_buy_max():
 global User
 global Cryptopia
 update_cryptopia()
 update_user()
 print('|[VIVIAN]|>>: Last DCN Asking Price Satoshi Per DCN [{}] Volume At Value: [{}].'.format(Cryptopia['DCN Current Ask'][0]*1e8,
                                                                                                  Cryptopia['DCN Current Ask'][1]))
 print('|[VIVIAN]|>>: How Much Max Do You Want To Spend Per DCN In Satoshi? [FLOAT/#.#]')
 BUY_MAX = input('|[INPUT]|>>: ')
 try:
  Test = float(BUY_MAX) + 0.1
  print('|[VIVIAN]|>>: Spending: [{}] Max Satoshi Per DCN.'.format(BUY_MAX))
  User['DCN']['Buy Maximum'] = float(BUY_MAX)
  User['Buy Max Set'] = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_buy_max()


### Sets Minimum Sell Price In Satoshi Per DCN ###
def set_sell_min():
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 print('|[VIVIAN]|>>: Last DCN Bid Price Satoshi Per DCN [{}] Volume At Value [{}].'.format(Cryptopia['DCN Current Bid'][0]*1e8,
                                                                                             Cryptopia['DCN Current Bid'][1]))
 print('|[VIVIAN]|>>: How Much Min Do You Want To Sell Per DCN In Satoshi? [FLOAT/#.#]')
 SELL_MIN = input('|[INPUT]|>>: ')
 try:
  Test = float(SELL_MIN) + 0.1
  print('|[VIVIAN]|>>: Selling Each DCN For [{}] Min Satoshi Per DCN.'.format(SELL_MIN))
  User['DCN']['Sell Minimum'] = float(SELL_MIN)
  User['Sell Min Set'] = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_sell_min()

  
### Sets Cryptopia User API Key ###
def set_api_key():
 global User
 global Cryptopia
 print('|[VIVIAN]|>>: Please Enter Cryptopia API Key [KEY]')
 API_KEY = input('|[INPUT]|>>: ')
 try:
  print('|[VIVIAN]|>>: Current API Key: [{}].'.format(API_KEY))
  Cryptopia['Api Key'] = API_KEY
  User['Api Key Set'] = True
 except Exception as Api_Key_Error:
  print('|[VIVIAN]|>>: You Must Enter A Cryptopia API Key.')
  set_api_key()

  
### Sets Cryptopia User API Secret ###
def set_api_secret():
 global Cryptopia
 global User
 print('|[VIVIAN]|>>: Please Enter Cryptopia API Secret [SECRET]')
 API_SECRET = input('|[INPUT]|>>: ')
 try:
  print('|[VIVIAN]|>>: Current API Secret: [{}].'.format(API_SECRET))
  Cryptopia['Api Secret'] = API_SECRET
  User['Api Secret Set'] = True
 except Exception as Api_Secret_Error:
  print('|[VIVIAN]|>>: You Must Enter A Cryptopia API Secret.')
  set_api_secret()

### Submit Trade Call (SELL) Requires Amount Arg. ###
def sell_DCN(Amount):
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 try:
  if Amount <= User['DCN Left To Sell']:
   print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: Selling {} DCN For {} Satoshi Each'.format(Amount,Cryptopia['DCN Current Bid'][0]*1e8))
   sold = Cryptopia['Client'].submit_trade('DCN/BTC', 'Sell', Cryptopia['DCN Current Bid'][0], Amount)
   if Amount == User['DCN Left To Sell']:
    User['DCN Left To Sell'] = 0
    User['DCN Left To Buy'] = User['DCN']['Trade Amount']
    User['State'] = 1
    print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: [DCN][LEFT TO SELL]: [{}] Swapping To Fresh Buy State.'.format(User['DCN Left To Sell']))
   elif Amount < User['DCN Left To Sell']:
    User['DCN Left To Sell'] -= Amount
    print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: [DCN][LEFT TO SELL]: [{}] Left Before Fresh Buy State.'.format(User['DCN Left To Sell']))
   User['Trades Completed'] += 1
   Cryptopia['DCN Order Book'].append({'Sell': [Cryptopia['DCN Current Bid'][0], Amount]})
   print(sold)
  elif Amount > User['DCN Left To Sell']:
   print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: Selling {} DCN For {} Satoshi Each'.format(User['DCN Left To Sell'],Cryptopia['DCN Current Bid'][0]*1e8))
   sold = Cryptopia['Client'].submit_trade('DCN/BTC', 'Sell', Cryptopia['DCN Current Bid'], User['DCN Left To Sell'])
   User['DCN Left To Sell'] = 0
   User['DCN Left To Buy'] = User['DCN']['Trade Amount']
   User['Trades Completed'] += 1
   User['State'] = 1
   print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: [DCN][LEFT TO SELL]: [{}] Swapping To Fresh Buy State.'.format(User['DCN Left To Sell']))
   print(sold)
  elif Amount <= User['DCN Left To Sell'] and Amount > User['Wallets']['DCN']['Balance'] or User['DCN Left To Sell'] > User['Wallets']['DCN']['Balance']:
   print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: There Is Not Enough DCNCoin Balance To Complete The Trade Routine Instructing Program To Exit() Please Inform Skrypt Of Loss Profit Actions')
   exit()
  else:
   print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: Something Unexpected Has Happened Instructing Program To Exit.')
   exit()
 except Exception as Sell_DCN_Error:
  print('|[VIVIAN]|[SELL DCN FUNCTION]|>>: There Has Been A Exception [{}] Within Our sell_DCN() Function Instructing Program To Exit Please Inform Skrypt.'.format(Sell_DCN_Error))
  exit()

### Submit Trade Call (BUY) Requires Amount Arg. ###
def buy_DCN(Amount):
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 try:
  if Amount <= User['DCN Left To Buy'] and Cryptopia['DCN Current Ask'][0]*Amount <= User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: Buying {} DCN For {} Satoshi Each'.format(Amount,Cryptopia['DCN Current Ask'][0]*1e8))
   bought = Cryptopia['Client'].submit_trade('DCN/BTC', 'Buy', Cryptopia['DCN Current Ask'][0], Amount)
   if Amount == User['DCN Left To Buy']:
    User['DCN Left To Buy'] = 0
    User['DCN Left To Sell'] = User['DCN']['Trade Amount']
    User['State'] = 2
    print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: [DCN][LEFT TO BUY]: [{}] Swapping To Fresh Sell State.'.format(User['DCN Left To Buy']))
   elif Amount < User['DCN Left To Buy']:
    User['DCN Left To Buy'] -= Amount
    print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: [DCN][LEFT TO BUY]: [{}] Left Before Fresh Sell State.'.format(User['DCN Left To Buy']))
   User['Trades Completed'] += 1
   Cryptopia['DCN Order Book'].append({'Buy': [Cryptopia['DCN Current Ask'][0], Amount]})
   print(bought)
  elif Amount > User['DCN Left To Buy'] and Cryptopia['DCN Current Ask'][0]*User['DCN Left To Buy'] <= User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: Buying {} DCN For {} Satoshi Each'.format(User['DCN Left To Buy'],Cryptopia['DCN Current Ask'][0]*1e8))
   bought = Cryptopia['Client'].submit_trade('DCN/BTC', 'Buy', Cryptopia['DCN Current Ask'], User['DCN Left To Buy'])
   User['DCN Left To Buy'] = 0
   User['DCN Left To Sell'] = User['DCN']['Trade Amount']
   User['Trades Completed'] += 1
   User['State'] = 2
   print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: [DCN][LEFT TO BUY]: [{}] Swapping To Fresh Sell State.'.format(User['DCN Left To Buy']))
   print(bought)
  elif Amount <= User['DCN Left To Buy'] and Cryptopia['DCN Current Ask'][0]*Amount > User['Wallets']['Bitcoin']['Balance'] or Amount > User['DCN Left To Buy'] and Cryptopia['DCN Current Ask'][0]*User['DCN Left To Buy'] > User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: There Is Not Enough Bitcoin Balance To Complete The Trade Routine Instructing Program To Exit() Please Inform Skrypt Of Loss Profit Actions')
   exit()
  else:
   print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: Something Unexpected Has Happened Instructing Program To Exit.')
   exit()
 except Exception as Buy_DCN_Error:
  print('|[VIVIAN]|[BUY DCN FUNCTION]|>>: There Has Been A Exception [{}] Within Our buy_DCN() Function Instructing Program To Exit Please Inform Skrypt.'.format(Buy_DCN_Error))
  exit()

### Activates Cryptopia['Client'] With User API Key/Secret ###
def Activate_Client():
 global Cryptopia
 try:
  Cryptopia['Client'] = Api(Cryptopia['Api Key'], Cryptopia['Api Secret'])
  print('|[VIVIAN]|>>: Cryptopia Client Activated With API Key [{}].'.format(Cryptopia['Api Key']))
 except Exception as Client_Error:
  print('|[VIVIAN]|>>: There Was A Client Activation Error Trying Again.')
  Activate_Client()

  
### Updates User Information Via Cryptopia API ###
def update_user():
 global User
 global Cryptopia
 balance,error = Cryptopia['Client'].get_balance('DCN')
 if error == None:
  User['Wallets']['DCN']['Balance'] = float(balance['Available'])
 elif error != None:
  print('We Have Had An Update_User().balance Error, Please Contact Skrypt With: [{}].'.format(error))
 balance,error = Cryptopia['Client'].get_balance('BTC')
 if error == None:
  User['Wallets']['Bitcoin']['Balance'] = float(balance['Available'])
 elif error != None:
  print('We Have Had An Update_User().balance Error, Please Contact Skrypt With: [{}].'.format(error))
 open_DCN_orders,error = Cryptopia['Client'].get_openorders('DCN_BTC')
 if open_DCN_orders == [] and error == None:
  User['Wallets']['DCN']['Open Orders'] = [None]
 elif open_DCN_orders != [] and error == None:
  User['Wallets']['DCN']['Open Orders'] = []
  User['Wallets']['DCN']['Open Orders'].append(open_DCN_orders)
 elif error != None:
  print('We Have Had An Update_User().open_DCN_orders Error, Please Contact Skrypt With: [{}].'.format(error))
 else:
  print('Something Unexpected Has Happened Within Update_User() Function, Please Contact Skrypt. Instructing Program To Execute Exit().')
  exit()
 print('User Updated')

  
### Sets Up User Database Object To Store Returned Data ###
def set_user():
 global User
 User = dict()
 User['Trades Completed'] = 0
 User['DCN'] = dict()
 User['DCN']['Buy Maximum'] = 0.0
 User['DCN']['Sell Minimum'] = 0.0
 User['DCN']['Trade Amount'] = 0.0
 User['Wallets'] = dict()
 User['Wallets']['DCN'] = dict()
 User['Wallets']['DCN']['Balance'] = 0.0
 User['Wallets']['DCN']['Open Orders'] = list()
 User['Wallets']['DCN']['Completed Orders List'] = list()
 User['Wallets']['Bitcoin'] = dict()
 User['Wallets']['Bitcoin']['Balance'] = 0.0
 User['Wallets']['Bitcoin']['Open Orders'] = list()
 User['Wallets']['Bitcoin']['Completed Orders List'] = list()
 User['DCN Left To Sell'] = 0.0
 User['DCN Left To Buy'] = 0.0
 User['State'] = 0
 User['Timer Set'] = None
 User['Api Key Set'] = None
 User['Api Secret Set'] = None
 User['Buy Max Set'] = None
 User['Sell Min Set'] = None
 User['DCN Set'] = None
 print('|[VIVIAN]|>>: User Created')

 
### Sets Up Cryptopia Database Object To Store Returned Data ###
def set_cryptopia():
 global Cryptopia
 Cryptopia = dict()
 Cryptopia['Time Between Calls'] = 0.0
 Cryptopia['Total Calls'] = 0
 Cryptopia['Api Key'] = ''
 Cryptopia['Api Secret'] = ''
 Cryptopia['Client'] = None
 Cryptopia['DCN Current Bid'] = [0.0, 0.0]
 Cryptopia['DCN Current Ask'] = [0.0, 0.0]
 Cryptopia['DCN Order Book'] = list()

 
### Updates Cryptopia Database Object Via Cryptopia API ###
def update_cryptopia():
 global Cryptopia
 orders,error = Cryptopia['Client'].get_orders('DCN_BTC')
 Cryptopia['DCN Current Bid'][0] = orders['Buy'][0]['Price']
 Cryptopia['DCN Current Ask'][0] = orders['Sell'][0]['Price']
 Cryptopia['DCN Current Bid'][1] = orders['Buy'][0]['Volume']
 Cryptopia['DCN Current Ask'][1] = orders['Sell'][0]['Volume']
 Cryptopia['Total Calls'] += 1
 print('Cryptopia Updated')


##### Quik Control Switches #####
Vivian = False
set_user()
set_cryptopia()
if Vivian == False:
 vivian_banner()
 Vivian = True


### Trading Routine ###
print('|[VIVIAN]|>>: Please Answer A Few Short Questions To Set User Controls.')
while True:
 if User['Timer Set'] == None or User['Timer Set'] == False:
  set_call_timer()
 if User['Api Key Set'] == None or User['Api Key Set'] == False:
  set_api_key()
 if User['Api Secret Set'] == None or User['Api Secret Set'] == False:
  set_api_secret()
  Activate_Client()
 if User['DCN Set'] == None or User['DCN Set'] == False:
  set_trade_amount()
 if User['Buy Max Set'] == None or User['Buy Max Set'] == False:
  set_buy_max()
 if User['Sell Min Set'] == None or User['Sell Min Set'] == False:
  set_sell_min()
 else:
  try:
   update_user()
   update_cryptopia()
   if User['State'] == 1:
    if Cryptopia['DCN Current Ask'][0]*1e8 <= User['DCN']['Buy Maximum']:
     if Cryptopia['DCN Current Ask'][1] >= User['DCN Left To Buy']:
      buy_DCN(User['DCN Left To Buy'])
     elif Cryptopia['DCN Current Ask'][1] < User['DCN Left To Buy']:
      buy_DCN(Cryptopia['DCN Current Ask'][1])
     else:
      print('|[VIVIAN]|>>: [DCN] Market Might Be Closed? Doesn\'t Seem To Be Any Options To Buy Please Inform Skrypt. Instructing Program To Exit().')
      exit()
    elif Cryptopia['DCN Current Ask'][0]*1e8 > User['DCN']['Buy Maximum']:
     print('|[VIVIAN]|>>: Waiting For DCN Price To Drop From [{}] To [{}] Satoshi Or Below. Current Order Volume [{}]'.format(Cryptopia['DCN Current Ask'][0]*1e8,User['DCN']['Buy Maximum'],Cryptopia['DCN Current Ask'][1]))
     time.sleep(Cryptopia['Time Between Calls'])
   elif User['State'] == 2:
    if Cryptopia['DCN Current Bid'][0]*1e8 >= User['DCN']['Sell Minimum']:
     if Cryptopia['DCN Current Bid'][1] >= User['DCN Left To Sell']:
      sell_DCN(User['DCN Left To Sell'])
     elif Cryptopia['DCN Current Bid'][1] < User['DCN Left To Sell']:
      sell_DCN(Cryptopia['DCN Current Bid'][1])
     else:
      print('|[VIVIAN]|>>: [DCN] Market Might Be Closed? Doesn\'t Seem To Be Any Options To Buy Please Inform Skrypt. Instructing Program To Exit().')
      exit()
    elif Cryptopia['DCN Current Bid'][0]*1e8 < User['DCN']['Sell Minimum']:
     print('|[VIVIAN]|>>: Waiting For DCN Price To Raise From [{}] To [{}] Satoshi Or Higher. Current Order Volume [{}]'.format(Cryptopia['DCN Current Bid'][0]*1e8,User['DCN']['Sell Minimum'],Cryptopia['DCN Current Bid'][1]))
     time.sleep(Cryptopia['Time Between Calls'])
   else:
    print('|[VIVIAN]|>>: Something Has Fucked Up With User[\'State\'], Waiting Timer Then Trying Again')
    time.sleep(float(Cryptopia['Time Between Calls']))
  except Exception as Run_Time_Error:
   if 'Connection Aborted' in Run_Time_Error:
    print('Resetting Client Due To Connection Failure')
    Activate_Client()
   else:
    print('|[VIVIAN]|>>: We Have Had The Following Run Time Error: [{}]'.format(Run_Time_Error))
    print('|[VIVIAN]|>>: Going To Instruct Program To Exit Contact Skrypt With Plenty Of Information Including [{}].'.format(Run_Time_Error))
    exit()
