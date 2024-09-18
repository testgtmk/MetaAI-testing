from meta_ai_api import MetaAI
import telebot
from dotenv import load_dotenv
import os
import time

ai = MetaAI()
promptIntro = ""
ques =  "Enumerate the National Water Policy of India. Taking river Ganges as an example, discuss the strategies which may be adopted for river water pollution control and management. What are the legal provisions of management and handling of hazardous wastes in India?"
msg = "This question was asked in CSE Mains. Give me approach, keywords and answer of this question. Use data, reports, supreme court judgements to make it more enriching. \n "
msg += ques
ans = ""

while True:
    try:
        response = ai.prompt(message=msg)
        print(response["message"])
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

