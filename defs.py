#defs.py
import sqlite3
import tugmalar
from language import get_lang	

#TILNK TANLASH FUNKSIYASI
def lang_choicer_start(bot, user_id):
	
	bot.send_message(user_id, "<b>🇺🇿 Salom! Xush kelibsiz 👋\n👇 Bo‘limni tanlang\n\n🇷🇺 Привет! Добро пожаловать 👋\n👇 Выберите раздел\n\n🇬🇧 Hello! Welcome 👋\n👇 Choose a section\n\n🇹🇯 Салом! Хуш омадед 👋\n👇 Интихоб кунед</b>",  reply_markup=tugmalar.langs_btn, parse_mode="HTML")

#TILNI YANGILASH
def lang_update(bot, user_id, new_lang):
	#DATANI OCHAMIZ
	db = sqlite3.connect("data.db", check_same_thread=False)
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
	refe_bonus
	)
	""")
	cursor.execute("UPDATE users SET lang = ? WHERE user_id = ?", (new_lang, user_id))
	db.commit()
	db.close()
	
	bot.send_message(user_id, get_lang(user_id, "lang_update"), parse_mode="HTML")

def reklama(bot):
	cursor.execute("SELECT * FROM users")
	
	users = cursor.fetchall()
	
	for user in users:
		try:
			print(user[1])
			bot.send_message(user[1], get_lang(user[1], "rek"), reply_markup=tugmalar.reklama_creator(user[1]), parse_mode="HTML")
		except Exception as e:
			print(f"Xatolik {user[1]} ga yuborishda:", e)