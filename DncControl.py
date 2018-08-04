
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
 #USE AT OWN RISK!          ~Dentacoin CONTROLLER~                                #
 #################################################################################
|[VIVIAN]| >>: Welcome To My Central Cryptopia Monitoring System.''')
 print('|[VIVIAN]|>>: Written By Skrypt Please Feel Free To Donate In To The RealmKoin Project!')
 print('|[VIVIAN]|>>: (RK) [ETH/Tokens] Donation Address: [0xdb436485f38d0f9c78acfb20ededc97419eb2ea5]')

### Sets Amount Of DNC To Be Traded ###
def set_trade_amount():
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 print('|[CRYPTOPIA]|>>: Current DNC Balance: [{}].'.format(User['Wallets']['DNC']['Balance']))
 print('|[CRYPTOPIA]|>>: Current BTC Balance: [{}].'.format(User['Wallets']['Bitcoin']['Balance']))
 print('|[VIVIAN]|>>: You May Trade Current BTC: [{}] For [{}] DNC At [{}] Satoshi Per DNC Volume Available: [{}]'.format(User['Wallets']['Bitcoin']['Balance'],(User['Wallets']['Bitcoin']['Balance']-User['Wallets']['Bitcoin']['Balance']*0.00201)//Cryptopia['DNC Current Ask'][0],
                                                                                                     Cryptopia['DNC Current Ask'][0]*1e8,Cryptopia['DNC Current Ask'][1]))
 print('|[VIVIAN]|>>: You May Trade Current DNC: [{}] For [{}] BTC At [{}] Satoshi Per DNC Volume Available: [{}]'.format(User['Wallets']['DNC']['Balance'],(User['Wallets']['DNC']['Balance']-User['Wallets']['DNC']['Balance']*0.00201)*Cryptopia['DNC Current Bid'][0],
                                                                                                     Cryptopia['DNC Current Bid'][0]*1e8,Cryptopia['DNC Current Bid'][1]))
 print('|[VIVIAN]|>>: How Much DNC Are You Trading? [FLOAT/#.#]')
 DNC = input('|[INPUT]|>>: ')
 try:
  squishy = '0.1'
  Test = float(DNC) + float(squishy)
  print('|[VIVIAN]|>>: DNC To Be Traded: [{}].'.format(DNC))
  User['DNC Set'] = True
  User['DNC Trade Amount'] = float(DNC)
  if User['Wallets']['DNC']['Balance'] < float(DNC):
   print('|[VIVIAN]|>>: Adjusting To Buy State. {} Needed Before Sell Conversion.'.format(float(DNC) - User['Wallets']['DNC']['Balance']))
   User['State'] = 1
   User['DNC Left To Buy'] = float(DNC) - User['Wallets']['DNC']['Balance']
   User['DNC Left To Sell'] = 0.0
  elif User['Wallets']['DNC']['Balance'] >= float(DNC):
   print('|[VIVIAN]|>>: Adjusting To Sell State. {} Original DNC Balance Before Sell Conversion.'.format(User['Wallets']['DNC']['Balance']))
   User['State'] = 2
   User['DNC Left To Sell'] = float(DNC)
   User['DNC Left To Buy'] = 0.0
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


### Sets Maximum Buy Price In Satoshi Per DNC ###
def set_buy_max():
 global User
 global Cryptopia
 update_cryptopia()
 update_user()
 print('|[VIVIAN]|>>: Last DNC Asking Price Satoshi Per DNC [{}] Volume At Value: [{}].'.format(Cryptopia['DNC Current Ask'][0]*1e8,
                                                                                                  Cryptopia['DNC Current Ask'][1]))
 print('|[VIVIAN]|>>: How Much Max Do You Want To Spend Per DNC In Satoshi? [FLOAT/#.#]')
 BUY_MAX = input('|[INPUT]|>>: ')
 try:
  Test = float(BUY_MAX) + 0.1
  print('|[VIVIAN]|>>: Spending: [{}] Max Satoshi Per DNC.'.format(BUY_MAX))
  User['DNC']['Buy Maximum'] = float(BUY_MAX)
  User['Buy Max Set'] = True
 except Exception as Float_Error:
  print('|[VIVIAN]|>>: You Must Enter A Float Here.')
  set_buy_max()


### Sets Minimum Sell Price In Satoshi Per DNC ###
def set_sell_min():
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 print('|[VIVIAN]|>>: Last DNC Bid Price Satoshi Per DNC [{}] Volume At Value [{}].'.format(Cryptopia['DNC Current Bid'][0]*1e8,
                                                                                             Cryptopia['DNC Current Bid'][1]))
 print('|[VIVIAN]|>>: How Much Min Do You Want To Sell Per DNC In Satoshi? [FLOAT/#.#]')
 SELL_MIN = input('|[INPUT]|>>: ')
 try:
  Test = float(SELL_MIN) + 0.1
  print('|[VIVIAN]|>>: Selling Each DNC For [{}] Min Satoshi Per DNC.'.format(SELL_MIN))
  User['DNC']['Sell Minimum'] = float(SELL_MIN)
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
def sell_DNC(Amount):
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 try:
  if Amount <= User['DNC Left To Sell']:
   print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: Selling {} DNC For {} Satoshi Each'.format(Amount,Cryptopia['DNC Current Bid'][0]*1e8))
   sold = Cryptopia['Client'].submit_trade('DNC/BTC', 'Sell', Cryptopia['DNC Current Bid'][0], Amount)
   if Amount == User['DNC Left To Sell']:
    User['DNC Left To Sell'] = 0
    User['DNC Left To Buy'] = User['DNC']['Trade Amount']
    User['State'] = 1
    print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: [DNC][LEFT TO SELL]: [{}] Swapping To Fresh Buy State.'.format(User['DNC Left To Sell']))
   elif Amount < User['DNC Left To Sell']:
    User['DNC Left To Sell'] -= Amount
    print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: [DNC][LEFT TO SELL]: [{}] Left Before Fresh Buy State.'.format(User['DNC Left To Sell']))
   User['Trades Completed'] += 1
   Cryptopia['DNC Order Book'].append({'Sell': [Cryptopia['DNC Current Bid'][0], Amount]})
   print(sold)
  elif Amount > User['DNC Left To Sell']:
   print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: Selling {} DNC For {} Satoshi Each'.format(User['DNC Left To Sell'],Cryptopia['DNC Current Bid'][0]*1e8))
   sold = Cryptopia['Client'].submit_trade('DNC/BTC', 'Sell', Cryptopia['DNC Current Bid'], User['DNC Left To Sell'])
   User['DNC Left To Sell'] = 0
   User['DNC Left To Buy'] = User['DNC']['Trade Amount']
   User['Trades Completed'] += 1
   User['State'] = 1
   print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: [DNC][LEFT TO SELL]: [{}] Swapping To Fresh Buy State.'.format(User['DNC Left To Sell']))
   print(sold)
  elif Amount <= User['DNC Left To Sell'] and Amount > User['Wallets']['DNC']['Balance'] or User['DNC Left To Sell'] > User['Wallets']['DNC']['Balance']:
   print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: There Is Not Enough DNCCoin Balance To Complete The Trade Routine Instructing Program To Exit() Please Inform Skrypt Of Loss Profit Actions')
   exit()
  else:
   print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: Something Unexpected Has Happened Instructing Program To Exit.')
   exit()
 except Exception as Sell_DNC_Error:
  print('|[VIVIAN]|[SELL DNC FUNCTION]|>>: There Has Been A Exception [{}] Within Our sell_DNC() Function Instructing Program To Exit Please Inform Skrypt.'.format(Sell_DNC_Error))
  exit()

### Submit Trade Call (BUY) Requires Amount Arg. ###
def buy_DNC(Amount):
 global User
 global Cryptopia
 update_user()
 update_cryptopia()
 try:
  if Amount <= User['DNC Left To Buy'] and Cryptopia['DNC Current Ask'][0]*Amount <= User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: Buying {} DNC For {} Satoshi Each'.format(Amount,Cryptopia['DNC Current Ask'][0]*1e8))
   bought = Cryptopia['Client'].submit_trade('DNC/BTC', 'Buy', Cryptopia['DNC Current Ask'][0], Amount)
   if Amount == User['DNC Left To Buy']:
    User['DNC Left To Buy'] = 0
    User['DNC Left To Sell'] = User['DNC']['Trade Amount']
    User['State'] = 2
    print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: [DNC][LEFT TO BUY]: [{}] Swapping To Fresh Sell State.'.format(User['DNC Left To Buy']))
   elif Amount < User['DNC Left To Buy']:
    User['DNC Left To Buy'] -= Amount
    print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: [DNC][LEFT TO BUY]: [{}] Left Before Fresh Sell State.'.format(User['DNC Left To Buy']))
   User['Trades Completed'] += 1
   Cryptopia['DNC Order Book'].append({'Buy': [Cryptopia['DNC Current Ask'][0], Amount]})
   print(bought)
  elif Amount > User['DNC Left To Buy'] and Cryptopia['DNC Current Ask'][0]*User['DNC Left To Buy'] <= User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: Buying {} DNC For {} Satoshi Each'.format(User['DNC Left To Buy'],Cryptopia['DNC Current Ask'][0]*1e8))
   bought = Cryptopia['Client'].submit_trade('DNC/BTC', 'Buy', Cryptopia['DNC Current Ask'], User['DNC Left To Buy'])
   User['DNC Left To Buy'] = 0
   User['DNC Left To Sell'] = User['DNC']['Trade Amount']
   User['Trades Completed'] += 1
   User['State'] = 2
   print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: [DNC][LEFT TO BUY]: [{}] Swapping To Fresh Sell State.'.format(User['DNC Left To Buy']))
   print(bought)
  elif Amount <= User['DNC Left To Buy'] and Cryptopia['DNC Current Ask'][0]*Amount > User['Wallets']['Bitcoin']['Balance'] or Amount > User['DNC Left To Buy'] and Cryptopia['DNC Current Ask'][0]*User['DNC Left To Buy'] > User['Wallets']['Bitcoin']['Balance']:
   print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: There Is Not Enough Bitcoin Balance To Complete The Trade Routine Instructing Program To Exit() Please Inform Skrypt Of Loss Profit Actions')
   exit()
  else:
   print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: Something Unexpected Has Happened Instructing Program To Exit.')
   exit()
 except Exception as Buy_DNC_Error:
  print('|[VIVIAN]|[BUY DNC FUNCTION]|>>: There Has Been A Exception [{}] Within Our buy_DNC() Function Instructing Program To Exit Please Inform Skrypt.'.format(Buy_DNC_Error))
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
 balance,error = Cryptopia['Client'].get_balance('DNC')
 if error == None:
  User['Wallets']['DNC']['Balance'] = float(balance['Available'])
 elif error != None:
  print('We Have Had An Update_User().balance Error, Please Contact Skrypt With: [{}].'.format(error))
 balance,error = Cryptopia['Client'].get_balance('BTC')
 if error == None:
  User['Wallets']['Bitcoin']['Balance'] = float(balance['Available'])
 elif error != None:
  print('We Have Had An Update_User().balance Error, Please Contact Skrypt With: [{}].'.format(error))
 open_DNC_orders,error = Cryptopia['Client'].get_openorders('DNC_BTC')
 if open_DNC_orders == [] and error == None:
  User['Wallets']['DNC']['Open Orders'] = [None]
 elif open_DNC_orders != [] and error == None:
  User['Wallets']['DNC']['Open Orders'] = []
  User['Wallets']['DNC']['Open Orders'].append(open_DNC_orders)
 elif error != None:
  print('We Have Had An Update_User().open_DNC_orders Error, Please Contact Skrypt With: [{}].'.format(error))
 else:
  print('Something Unexpected Has Happened Within Update_User() Function, Please Contact Skrypt. Instructing Program To Execute Exit().')
  exit()
 print('User Updated')

  
### Sets Up User Database Object To Store Returned Data ###
def set_user():
 global User
 User = dict()
 User['Trades Completed'] = 0
 User['DNC'] = dict()
 User['DNC']['Buy Maximum'] = 0.0
 User['DNC']['Sell Minimum'] = 0.0
 User['DNC']['Trade Amount'] = 0.0
 User['Wallets'] = dict()
 User['Wallets']['DNC'] = dict()
 User['Wallets']['DNC']['Balance'] = 0.0
 User['Wallets']['DNC']['Open Orders'] = list()
 User['Wallets']['DNC']['Completed Orders List'] = list()
 User['Wallets']['Bitcoin'] = dict()
 User['Wallets']['Bitcoin']['Balance'] = 0.0
 User['Wallets']['Bitcoin']['Open Orders'] = list()
 User['Wallets']['Bitcoin']['Completed Orders List'] = list()
 User['DNC Left To Sell'] = 0.0
 User['DNC Left To Buy'] = 0.0
 User['State'] = 0
 User['Timer Set'] = None
 User['Api Key Set'] = None
 User['Api Secret Set'] = None
 User['Buy Max Set'] = None
 User['Sell Min Set'] = None
 User['DNC Set'] = None
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
 Cryptopia['DNC Current Bid'] = [0.0, 0.0]
 Cryptopia['DNC Current Ask'] = [0.0, 0.0]
 Cryptopia['DNC Order Book'] = list()

 
### Updates Cryptopia Database Object Via Cryptopia API ###
def update_cryptopia():
 global Cryptopia
 orders,error = Cryptopia['Client'].get_orders('DNC_BTC')
 Cryptopia['DNC Current Bid'][0] = orders['Buy'][0]['Price']
 Cryptopia['DNC Current Ask'][0] = orders['Sell'][0]['Price']
 Cryptopia['DNC Current Bid'][1] = orders['Buy'][0]['Volume']
 Cryptopia['DNC Current Ask'][1] = orders['Sell'][0]['Volume']
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
 if User['DNC Set'] == None or User['DNC Set'] == False:
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
    if Cryptopia['DNC Current Ask'][0]*1e8 <= User['DNC']['Buy Maximum']:
     if Cryptopia['DNC Current Ask'][1] >= User['DNC Left To Buy']:
      buy_DNC(User['DNC Left To Buy'])
     elif Cryptopia['DNC Current Ask'][1] < User['DNC Left To Buy']:
      buy_DNC(Cryptopia['DNC Current Ask'][1])
     else:
      print('|[VIVIAN]|>>: [DNC] Market Might Be Closed? Doesn\'t Seem To Be Any Options To Buy Please Inform Skrypt. Instructing Program To Exit().')
      exit()
    elif Cryptopia['DNC Current Ask'][0]*1e8 > User['DNC']['Buy Maximum']:
     print('|[VIVIAN]|>>: Waiting For DNC Price To Drop From [{}] To [{}] Satoshi Or Below. Current Order Volume [{}]'.format(Cryptopia['DNC Current Ask'][0]*1e8,User['DNC']['Buy Maximum'],Cryptopia['DNC Current Ask'][1]))
     time.sleep(Cryptopia['Time Between Calls'])
   elif User['State'] == 2:
    if Cryptopia['DNC Current Bid'][0]*1e8 >= User['DNC']['Sell Minimum']:
     if Cryptopia['DNC Current Bid'][1] >= User['DNC Left To Sell']:
      sell_DNC(User['DNC Left To Sell'])
     elif Cryptopia['DNC Current Bid'][1] < User['DNC Left To Sell']:
      sell_DNC(Cryptopia['DNC Current Bid'][1])
     else:
      print('|[VIVIAN]|>>: [DNC] Market Might Be Closed? Doesn\'t Seem To Be Any Options To Buy Please Inform Skrypt. Instructing Program To Exit().')
      exit()
    elif Cryptopia['DNC Current Bid'][0]*1e8 < User['DNC']['Sell Minimum']:
     print('|[VIVIAN]|>>: Waiting For DNC Price To Raise From [{}] To [{}] Satoshi Or Higher. Current Order Volume [{}]'.format(Cryptopia['DNC Current Bid'][0]*1e8,User['DNC']['Sell Minimum'],Cryptopia['DNC Current Bid'][1]))
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
