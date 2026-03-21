#Tugmalar 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

reply_kategories = [
	"📂 Temalar",
	"🔐 Maxfiy bo‘lim"
]

kategoriyalar = [
	"DARK🖤",
	"ANIME💖",
	"HAYVONCHALAR🐶",
	"SOFT🤍",
	"BOSHQA❤"
]

#ADMIN TUGMALARI
admin_tugma = InlineKeyboardMarkup()
	
all_users = InlineKeyboardButton("👥USERS", callback_data="all_users")
post = InlineKeyboardButton("📢ELON", callback_data="reklama")

admin_tugma.add(all_users, post)

#REPLY TUGMALAR
reply_panel = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

for i in range(0, len(reply_kategories), 2):
	row = reply_kategories[i:i+2]
	reply_panel.add(*[KeyboardButton(btn)for btn in row])

#KATEGORIYALAR
kat_btns = InlineKeyboardMarkup(row_width=2)

buttons = []
for kat in kategoriyalar:
	buttons.append(InlineKeyboardButton(kat, callback_data=kat))

kat_btns.add(*buttons)

#PANEL
def user_panel(link):
	
	kb = InlineKeyboardMarkup()
	
	next_btn = InlineKeyboardButton("⏭️ KEYINGISI", callback_data="next")
	news_btn = InlineKeyboardButton("📻 BOT NEWS", url="https://t.me/jahongi_studi010")
	inst_btn = InlineKeyboardButton("OʻRNATISH📲", url=f"{link}")
	
	kb.add(inst_btn)
	kb.row(news_btn, next_btn)
	
	return kb
	
#USER  TELFONI
and_ios = InlineKeyboardMarkup()

and_btn = InlineKeyboardButton("🤖ANDROID", callback_data="android")
ios_btn = InlineKeyboardButton("🍏IOS", callback_data="ios")

and_ios.row(ios_btn, and_btn)