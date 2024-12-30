import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24777493")

API_HASH = os.environ.get("API_HASH", "bf5a6381d07f045af4faeb46d7de36e5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7975449308:AAG9Zc3jnt9CtkBG4M7HILexUYdACwQgPQ8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002139139355") 

DB_NAME = os.environ.get("DB_NAME","clustero")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://leecher-x:#DiViN143#@cluster0.e9vvmrg.mongodb.net/?retrywrites=true&w majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5116530698').split()]

PORT = os.environ.get("PORT", "8080")
