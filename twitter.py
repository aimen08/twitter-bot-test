import os
import telebot
from dotenv import load_dotenv
from loguru import logger
from twitterScraper import *
import uuid


load_dotenv()

API_KEY= os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY,threaded=True,num_threads=10)
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60

@bot.message_handler(commands=['mysnap','start'],)
def send_mysnap(message):
	bot.send_message(message.chat.id, "تابعنا على حسابنا في سناب شات: rashed \n"
            "https://www.snapchat.com/add/rashed") 


    

@bot.message_handler(commands=['twitter'])
def send_mysnap(message):
	bot.send_message(message.chat.id, "ضع رابط فيديوالتويتر") 
    


           
@bot.message_handler()
def snap(message):
    request = message.text.split()
    chatId = message.chat.id
    if len(request) > 1 :
        bot.send_message(chatId, "الرجاء التأكد من صحة الرابط")
        return 
    random =  uuid.uuid1()
    bot.send_message(message.chat.id, "جاري التحميل يرجى إنتظار")    
    logger.info("[+] video with id {} started ".format( random ))

    link = getVideo(message.text)
    bot.send_chat_action(chatId, 'upload_video')
    bot.send_video(chatId,link)
    bot.send_message(chatId, "تم تحميل")   


    logger.info("[✔] {} video downloaded".format(random))

      

# bot.polling(non_stop=True)
bot.infinity_polling(allowed_updates=telebot.util.update_types)



