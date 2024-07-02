# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv


load_dotenv()
bot_name = "Pikashow-File2Link"
bisal_channel = "https://telegram.me/pikashow_Movies_Update"
bisal_grp = "https://t.me/+wD9gChGIfjo1MDQ9"

class Var(object):
    SHORT_API = environ.get("SHORT_API", "6ac07ac202019e09497a0daad5abe04e11a98ac2") # shortlink api
    SHORT_URL = environ.get("SHORT_URL", "publicearn.com") # shortlink domain without https://
    VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/how2dow/55") # how to open link 
    BOT_USERNAME = environ.get("BOT_USERNAME", "TGMoveisRobot") # bot username without @
    VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.    
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '904789'))
    API_HASH = str(getenv('API_HASH', '2262ef67ced426b9eea57867b11666a1'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6819565837:AAG_MLRvjhtdqPX__EwavORHGraJrcsmQiE'))
    name = str(getenv('name', 'biisal'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002047582643'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001931308157'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "622730585").split()]  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None 
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'SpShah878'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "http://3.27.120.76:8080/".format(FQDN)
    else:
        URL = "http://3.27.120.76:8080/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://file2link:Surajrathod.878@cluster0.qsj0pe0.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Rx_Bots')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))

 