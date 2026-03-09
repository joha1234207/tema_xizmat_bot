#IMPORTLAR
import os
import telebot
from telebot import types
import json
import random
from flask import Flask, request

#TOKEN VA BOTNI QURISH
TOKEN = "8302804985:AAGyvvWoO7w9IFgE61SWbiIxNaSyO5__0tc"
app = Flask(__name__)

bot = telebot.TeleBot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok"

#START COMMAND
@bot.message_handler(commands=["start"])
def salomlash(message):
	user_panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
	
	
	temalar = types.KeyboardButton("Temalar🎆")
	shrift = types.KeyboardButton("Ilova tili😅")
	stikerlar = types.KeyboardButton("Emodzi❤")
	
	user_panel.add(temalar)
	user_panel.row(shrift, stikerlar)
	
	bot.reply_to(message, "👋 Xush kelibsiz!\n\n🎨Bu bot orqali turli xil chiroyli Telegram temalarini topishingiz mumkin.\n\n📥 Temani tanlang va oʻrnatib oling.\n\n⚡ Yangi temalar doimiy qo‘shib boriladi.\n\n👇 Boshlash uchun quyidagi tugmalardan foydalaning.", reply_markup=user_panel)

#HELP COMMAND
@bot.message_handler(commands=["help"])
def help(message):
	
	refe_btn = types.InlineKeyboardMarkup()

	btn1 = types.InlineKeyboardButton("Bot yangiliklari📻", url="https://t.me/jahongi_studi010")
	btn2 = types.InlineKeyboardButton("Ooboilar🥰", url="https://t.me/oboilar_temalar")
	
	refe_btn.add(btn1)
	refe_btn.add(btn2)
	
	bot.send_message(message.chat.id, "🤖 Bot haqida\n\n🎨 Ushbu bot siz uchun eng chiroyli Telegram temalarni jamlagan maxsus bot hisoblanadi.\n\n📂 Bu yerda siz turli xil kategoriya temalarni topishingiz mumkin:\n\n🖤 Dark — qorong‘i uslubdagi zamonaviy temalar \n\n💖 Anime — anime uslubidagi chiroyli temalar  \n\n🐯 Hayvonchalar — hayvon rasmlari bilan bezatilgan temalar  \n\n🤍 Soft — yumshoq va ko‘zga yoqimli rangli temalar  \n\n💔 Boshqa — turli xil noodatiy temalar\n\n📜 Bundan tashqari bot ichida turli xil shriftlar ham mavjud.  \n\n❤ Qiziqarli stiker paketlarini ham topishingiz mumkin.\n\n⚡ Botga doimiy ravishda yangi temalar qo‘shib boriladi, shuning uchun botni tez-tez tekshirib turing.\n\n📢 Ko‘proq temalar va bot yangiliklari uchun kanalimizga obuna bo‘ling.\n\n👥 Agar bot sizga yoqqan bo‘lsa, do‘stlaringizga ham ulashishni unutmang.\n\n🚀 Sizga yoqadigan eng yaxshi Telegram temalar aynan shu yerda!", reply_markup=refe_btn)

#REPLY TUGMALAR	
@bot.message_handler(func=lambda message: True)
def tanlash_tugmalari(message):
	inline_key = types.InlineKeyboardMarkup(row_width=2)
	
	if message.text == "Temalar🎆":
		inline_key.add(
			types.InlineKeyboardButton(
				"Dark🖤",
				 callback_data="dark"),
			types.InlineKeyboardButton(
				"Anime💖",
				callback_data="anime"),
			types.InlineKeyboardButton(
				"Hayvonchalar🐯", 
				callback_data="animals"),
			types.InlineKeyboardButton(
				"Soft🤍",
				callback_data="soft"),
			types.InlineKeyboardButton(
				"Boshqa💔",
				callback_data="boshqa")
		)
		bot.send_message(message.chat.id, "Qaysi turdagi temalar kerak", reply_markup=inline_key)
	elif message.text == "Ilova tili😅":
		with open("langs.json", "r") as f:
			langs = json.load(f)
		lang = random.choice(langs)
		
		inline_key.add(
			types.InlineKeyboardButton("Oʻrnatish📲",url=lang["link"])
		)
		inline_key.add(
			types.InlineKeyboardButton("Keyingisi⏭️", callback_data="next_lang")
		)
		bot.send_message(message.chat.id, f"{lang['name']} — Tili👅", reply_markup=inline_key)
	elif message.text == "Emodzi❤":
		with open("emodzi.json", "r") as f:
			emodzi = json.load(f)
			emo = random.choice(emodzi)
		inline_key.add(
			types.InlineKeyboardButton("Qoʻshib qoʻyish 📲", url=emo['link'])
		)
		inline_key.add(
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="next_emo")
		)
		bot.send_message(message.chat.id, f"Paket nomi {emo['name']}", reply_markup=inline_key)
	else:
		bot.send_message(message.chat.id, "ERROR☹️\n\nHatolikni yechish yoʻllari☺\n\n1⃣ - /start bilan botni yangilang\nn2⃣ - Pastdagi tugmalarni ishlating")

#CALLBACK FUNKSIYASI
@bot.callback_query_handler(func=lambda call: True)
def temalar_chiqarish(call):
	
	#FAYLLARNI OLISH
	with open("android.json", "r") as a_f:
		android = json.load(a_f)
	with open("ios.json", "r") as i_f:
		ios = json.load(i_f)
		
	#UMUMIY TUGMALARNI YARATISH
	theme_btn = types.InlineKeyboardMarkup(row_width=2)
	kanal_btn = types.InlineKeyboardButton("Koʻproq", url="https://t.me/jahongi_studi010")
	
	#DARK IOS AND ANDROID
	if call.data == "dark":
		theme_btn.add(
			types.InlineKeyboardButton("IOS🍏", callback_data="iosdark"),
			types.InlineKeyboardButton("Android🤖", callback_data="andark")
		)
		bot.send_message(call.message.chat.id, "Dark tema zoʻr👍\n\nPaltformani tanlang", reply_markup=theme_btn)
		
	#ANDROID DARK TEMALAR
	elif call.data == "andark":
		kategory = android["dark"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="andark")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#IOS DARK TEMALAR
	elif call.data == "iosdark":
		kategory = ios["dark"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="iosdark")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#ANIME ANDROID AND IOS
	elif call.data == "anime":
		theme_btn.add(
			types.InlineKeyboardButton("IOS🍏", callback_data="iosanim"),
			types.InlineKeyboardButton("Android🤖", callback_data="andanim")
		)
		bot.send_message(call.message.chat.id, "Anime temalar💖\n\nPlatformani tanlang😊", reply_markup=theme_btn)
		
	#ANDROID ANIME TEMA YUBORISH
	elif call.data == "andanim":
		kategory = android["anime"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="andanim")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#IOS ANIME TEMA
	elif call.data == "iosanim":
		kategory = ios["anime"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="iosanim")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#ANIDORID YOKI IOS ANIMALS
	elif call.data == "animals":
		theme_btn.add(
			types.InlineKeyboardButton("IOS🍏", callback_data="iosanimals"),
			types.InlineKeyboardButton("Android🤖", callback_data="andanimals")
		)
		bot.send_message(call.message.chat.id, "Anime temalar💖\n\nPlatformani tanlang😊", reply_markup=theme_btn)
	
	#ANDROID ANIMALS TEMA YUBORISH
	elif call.data == "andanimals":
		kategory = android["animals"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="andanimals")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#IOS ANIME TEMA
	elif call.data == "iosanimals":
		kategory = ios["animals"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="iosanimals")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
	
	#ANIDORID YOKI IOS ANIMALS
	elif call.data == "soft":
		theme_btn.add(
			types.InlineKeyboardButton("IOS🍏", callback_data="iossoft"),
			types.InlineKeyboardButton("Android🤖", callback_data="andsoft")
		)
		bot.send_message(call.message.chat.id, "Anime temalar💖\n\nPlatformani tanlang😊", reply_markup=theme_btn)
	
	#ANDROID ANIMALS TEMA YUBORISH
	elif call.data == "andsoft":
		kategory = android["soft"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="andb")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#IOS ANIME TEMA
	elif call.data == "iossoft":
		kategory = ios["soft"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="iossoft")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#ANIDORID YOKI IOS ANIMALS
	elif call.data == "boshqa":
		theme_btn.add(
			types.InlineKeyboardButton("IOS🍏", callback_data="iosb"),
			types.InlineKeyboardButton("Android🤖", callback_data="andb")
		)
		bot.send_message(call.message.chat.id, "Anime temalar💖\n\nPlatformani tanlang😊", reply_markup=theme_btn)
		
	#ANDROID ANIMALS TEMA YUBORISH
	elif call.data == "andb":
		kategory = android["boshqa"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="andb")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	#IOS ANIMALS TEMA
	elif call.data == "iosb":
		kategory = ios["boshqa"]
		theme = random.choice(kategory)
		theme_btn.add(
			types.InlineKeyboardButton(f"🌌 Tema: {theme['theme']}", url=theme["link"])
		)
		theme_btn.add(
			kanal_btn,
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="iosb")
		)
		
		bot.send_message(call.message.chat.id, "Temani koʻrish uchun pastdagi tugmani ishlating💕", reply_markup=theme_btn)
		
	elif call.data == "next_lang":
		with open("langs.json", "r") as f:
			langs = json.load(f)
		lang = random.choice(langs)
		
		theme_btn.add(
			types.InlineKeyboardButton("Oʻrnatish📲",url=lang["link"])
		)
		theme_btn.add(
			types.InlineKeyboardButton("Keyingisi⏭️", callback_data="next_lang")
		)
		bot.send_message(call.message.chat.id, f"{lang['name']} — Tili👅", reply_markup=theme_btn)
		
	elif call.data == "next_emo":
		with open("emodzi.json", "r") as f:
			emodzi = json.load(f)
			emo = random.choice(emodzi)
		theme_btn.add(
			types.InlineKeyboardButton("Qoʻshib qoʻyish 📲", url=emo['link'])
		)
		theme_btn.add(
			types.InlineKeyboardButton("Keyingisi⏩", callback_data="next_emo")
		)
		bot.send_message(call.message.chat.id, f"Paket nomi {emo['name']}", reply_markup=theme_btn)

bot.infinity_polling()
