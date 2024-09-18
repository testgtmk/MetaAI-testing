from meta_ai_api import MetaAI
import telebot
from dotenv import load_dotenv
import os
import time

promptIntro = ""
ques =  "Account for the change in the spatial pattern of the Iron and Steel industry in the world. "
msg = "This question was asked in CSE Mains. Give me approach, keywords and answer of this question. Use data, reports, supreme court judgements to make it more enriching. \n "
msg += ques
ans = ""

tc = 1
while tc < 5:
    tc += 1
    print(tc)
    try:
        ai = MetaAI()
        response = ai.prompt(message=msg)
        #print(response["message"])
        ans = response["message"]
        break
    except:
        print("Connection issue")
        time.sleep(1)


ans = ans.replace(":", "\n")
ans = ques + "\n\n\n" + ans

def send_message(answer):
    while True:
        try:
            bot = telebot.TeleBot(TELEGRAM_TOKEN)
            bot.send_message(CHAT_ID, answer)
            break
        except:
            print("Some issue is happening from server. Lets wait and watch")
            time.sleep(1)

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
send_message(ans)

