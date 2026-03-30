# funksiyalar.py

from telebot import types
import json
import random
import tugmalar
import time
import defs
from language import get_lang

def funksiyalar(bot, admin):
    
    user_state = {}
    TIMEOUT = 1000
    
    #CLEANER
    def timeout(user_id):
    	
    	if user_id in user_state:
    		
    		if time.time() - user_state[user_id]["time"] > TIMEOUT:
    			
    			del user_state[user_id]
    			return False
    			
    		return True
    		
    #OS TANLASH DEF
    def os_choicer(id):
    	
    	msg = bot.send_message(id, get_lang(id, 'platform_choice'), reply_markup=tugmalar.and_ios, parse_mode="HTML")
    	
    #KAT TANLASH
    def kat_choicer(id):
    	
    	bot.send_message(id, get_lang(id, "kat_choice"), reply_markup=tugmalar.kat_btns, parse_mode="HTML")
    
    #LINK YUBORISH
    def send_link(id):
        
        os = user_state[id]["os"]
        kat = user_state[id]["kat"]
        
        with open("data.json", "r", encoding="utf-8") as f:
        	data = json.load(f)
        
        if os is None:
        	os_choicer(id)
        	return
        	
        elif kat is None:
        	kat_choicer(id)
        	return
        	
        link = random.choice(data[os][kat])
        panel = tugmalar.user_panel(link)
        	
        bot.send_message(id, f"<b>{kat}\n{get_lang(id, 'theme_kat')}</b>", reply_markup=panel, parse_mode="HTML")
    
    
    #REPLY COMMANDS
    @bot.message_handler(func=lambda message: True)
    
    def tanlash_tugmalari(message):
        
        #USER STATE
        user_id = message.chat.id
        
        if not timeout(user_id):
        	
        	user_state[user_id] = {
        		"os": None,
        		"kat": None,
        		"time": time.time()
        	}
        
        if user_id not in user_state:
        	user_state[user_id] = {
        		"os": None,
        		"kat": None,
        		"time": time.time()
        	}
        
        #TIME YANGILANISHI
        user_state[user_id]["time"] = time.time()
        
        #IF NOT USERNAME
        username = f"@{message.from_user.username}" if message.from_user.username else "username yoʻq"
        
        #TEMALAR
        if message.text == "🎨 THEMES":
        	
        	bot.send_message(admin, f"Botda aktivlik temalar\n\n•link: {username}\n•Nomi: {message.from_user.first_name}")
        	
        	os_choicer(message.chat.id)
        
        #MAHFIY BÓLIM
        elif message.text == "🔐 PRIVATE":
        	
        	bot.send_message(message.chat.id, get_lang(message.chat.id, "sekret"), parse_mode="HTML")
        
        #BOSHQA NARSA YOZILSA
        else:
            bot.send_message(message.chat.id, "⚡ Salom! Bot yangilanishi mavjud.\n\n Iltimos, davom etish uchun <b>/start</b> tugmasini bosing ✅\n\n\n⚡ Салом! Навсозии бот дастрас аст. Лутфан барои идом додан тугмаи <b>/start</b> ро пахш кунед ✅\n\n\n⚡ Привет! Доступно обновление бота. Пожалуйста, нажмите кнопку <b>start</b> для продолжения ✅\n\n\n⚡ Hello! A bot update is available. Please press the <b>start</b> button to continue ✅",parse_mode="HTML")
    
    #CALBACK FUNKSIYALAR
    @bot.callback_query_handler(func=lambda call: True)
    def temalar_chiqarish(call):
        
        #USR STATE
        user_id = call.from_user.id
        
        #ESKI BOʻLSA OʻCHADI
        if not timeout(user_id):
        	user_state[user_id] = {
        		"os": None,
        		"kat": None,
        		"time": time.time()
        	}
        
        #YANGI USER QOʻSHILISHI
        if user_id not in user_state:
        	user_state[user_id] = {
        		"os": None,
        		"kat": None,
        		"time": time.time()
        	}
        	
        #TIMENI YANGILASH
        user_state[user_id]["time"] = time.time()
        
        #ANDROID OR IOS
        if call.data == "android" or call.data == "ios":
        	user_state[user_id]["os"] = call.data
        	kat_choicer(user_id)
        
        	
        elif call.data in tugmalar.kategoriyalar:
        	user_state[user_id]["kat"] = call.data
        	send_link(user_id)
        
        #NEXT BTN
        elif call.data == "next":
        	send_link(user_id)
        
        #USERS HISOBLASH
        elif call.data == "all_users":
        	users = 0
        	
        	for i in user_state:
        		users += 1
        	
        	bot.send_message(admin, f"1000 SEKUND ICHIDA {users} foydalanuvchi")
        
        #AKTIVLARGA REKLAMA
        elif call.data == "reklama":
        	defs.reklama(bot)
        		
        elif call.data in tugmalar.langs:
        	defs.lang_update(bot, user_id, call.data)
        
        elif call.data == "back":
        	kat_choicer(user_id)