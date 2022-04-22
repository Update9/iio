import requests
import telebot
import random
from telebot import types
token = "5127906351:AAGddP00jeVghp6G97o_WsvmCajc_iY7XZQ"
bot = telebot.TeleBot(token)
call  = types.InlineKeyboardButton(text = "- START", callback_data = 'stri')
dev  = types.InlineKeyboardButton(text = "- Dev 🧑‍💻", url = 'https://t.me/PIII9')
@bot.message_handler(commands=['start'])
def start(message):
    rye = types.InlineKeyboardMarkup()
    rye.row_width = 1
    rye.add(call,dev)
    bot.send_message(message.chat.id, text=f"- Start",parse_mode="markdown",reply_markup=rye)
@bot.callback_query_handler(func=lambda call: True)
def ButOn(call):
    if call.data =="stri":
        button(call.message)
    if call.data =="instaupbot":
         idup(call.message)


inco  = types.InlineKeyboardButton(text = "بدء الفحص", callback_data= 'instaupbot')
def button(message):
    ms = types.InlineKeyboardMarkup(row_width=1)
    ms.add(inco)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="* --*",parse_mode='markdown',reply_markup=ms)        


def idup(message):
        false_ = 0
        true_ = 0
        Num = '0123456789'  
        listStart = ("4", "5")
        NuIds = ("11", "10")
        while True:
            RNuIds = int(random.choice(NuIds))
            StId = random.choice(listStart)
            idran = StId + str(''.join((random.choice(Num) for i in range(RNuIds))))
            userid = idran
            url = f'https://dev-instaupapi.pantheonsite.io/NewFolder/coin-checker.php?oid={userid}&submit=submit'
            try:
                chido = str(requests.get(url).text)
                if 'coins":"' in chido:
                    coin=str(chido.split('coins":"')[1])
                    coins=str(chido.split('"')[0])
                    bot.send_message(message.chat.id, text=f"New ID ✅\nID : {userid} 🆔\nCoins : {coins} 🪙",parse_mode="markdown")
                    true_ += 1
                else:
	                  false_ += 1
            except:
                pass
            mees = types.InlineKeyboardMarkup(row_width=1)
            buut = types.InlineKeyboardButton(f"🆔 | ID : {idran} ",callback_data='idu')
            buut5 = types.InlineKeyboardButton(f"⚠️ | Bad : {false_}",callback_data='badid')
            buut1 = types.InlineKeyboardButton(f"✅ | Hits : {true_}",callback_data='hitid')            
            mees.add(buut,buut5,buut1)
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Cheaker InstaUp*",parse_mode='markdown',reply_markup=mees)        

bot.polling()
