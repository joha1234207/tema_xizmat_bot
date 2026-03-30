# commands.py

from telebot import types
from admin__panel import admin_panel_
import tugmalar
import sqlite3
import defs
from language import get_lang

def start_command(bot, admin):
    
    #ADMIN COMMAND
    @bot.message_handler(commands=["admin"])
    
    def admin_go(message):
    	 if message.chat.id == admin:
    	 	admin_panel_(bot, admin)
    	 else:
    	 	bot.send_message(message.chat.id, f"<b>{get_lang(message.chat.id, 'not_admmin')}</b>\n\n🆔: <code>{message.chat.id}</code>", parse_mode="HTML")
    	 	
    #START COMMAND
    @bot.message_handler(commands=["start"])
    def salomlash(message):
        
        #USER MALUMOT
        username = f"@{message.from_user.username}" if message.from_user.username else "username yoʻq"
        
        user_id = message.chat.id
        
        name = message.from_user.first_name
        
        #DATABASE ULASH
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
       
        #TABLE
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        	id INTEGER PRIMARY KEY AUTOINCREMENT,
        	user_id INTEGER,
        	username TEXT,
        	name TEXT,
        	lang TEXT,
        	token INTEGER,
        	refe_bonus INTEGER
       )
       """)
       
       
        #USER YOʻQ BOʻLSA QOʻSHAMIZ
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id, ))
        user = cursor.fetchone()
       
        if user:
        	
        	bot.reply_to(message, get_lang(user_id, 'yana_qaytdi'), parse_mode="HTML", reply_markup=tugmalar.reply_panel)
        	
        else:
         	
         	#DATBASEGA QOʻSHISH
         	cursor.execute("INSERT INTO users (user_id, username, name, lang, token, refe_bonus) VALUES (?, ?, ?, ?, ?, ?)", (user_id, username, name, "none", 0, 0))
         	
         	db.commit()
         	db.close()
         	
         	defs.lang_choicer_start(bot, user_id)
         	#ADMINGA XABAR
         	bot.send_message(admin, f"🥳BOTGA YANGI FOYDALANUVCHI KIRDI\n••••••••••••••••••••••••••••••••••••\nusername: 👤{username}\n\n🟠Name: {name}\n\n🆔: <code>{user_id}</code>", parse_mode="HTML")
    
    @bot.message_handler(commands=["help"])
    
    def help_command(message):
        
        user_id = message.chat.id
        
        refe_btn = types.InlineKeyboardMarkup()
        
        btn1 = types.InlineKeyboardButton(get_lang(user_id, "bot_news"), url="https://t.me/jahongi_studi010")
        btn2 = types.InlineKeyboardButton(get_lang(user_id, "oboi"), url="https://t.me/oboilar_temalar")
        refe_btn.add(btn1)
        refe_btn.add(btn2)
        
        bot.send_message(message.chat.id, get_lang(user_id, "help"),
    reply_markup=refe_btn,
    parse_mode="HTML"
)

    @bot.message_handler(commands=["lang"])
    def lang(message):
    	defs.lang_choicer_start(bot, message.chat.id)