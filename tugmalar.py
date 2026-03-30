#Tugmalar 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import urllib.parse
from language import get_lang

reply_kategories = [
	"🎨 THEMES",
	"🔐 PRIVATE"
]

kategoriyalar = [
	"🖤 DARK",
	"🎌 ANIME",
	"🐾 ANIMALS",
	"🌸 SOFT",
	"🔥 MORE"
]

langs = [
	"🇷🇺 РУССКИЙ 🇷🇺",
	"🇲🇾 ENGLISH 🇲🇾",
	"🇺🇿 UZBEK 🇺🇿",
	"🇹🇯 ТОҶИКӢ 🇹🇯"
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
	
	next_btn = InlineKeyboardButton("⏭️", callback_data="next")
	news_btn = InlineKeyboardButton("KATEGORIES", callback_data="back")
	inst_btn = InlineKeyboardButton("📲", url=f"{link}")
	
	kb.add(inst_btn)
	kb.row(news_btn, next_btn)
	
	return kb
	
#USER  TELFONI
and_ios = InlineKeyboardMarkup()

and_btn = InlineKeyboardButton("🤖ANDROID", callback_data="android")
ios_btn = InlineKeyboardButton("🍏IOS", callback_data="ios")

and_ios.row(ios_btn, and_btn)

#LANG BUTTONS
langs_btn = InlineKeyboardMarkup(row_width=2)

btns = []

for i in langs:
	btn = InlineKeyboardButton(i, callback_data=i)
	btns.append(btn)

langs_btn.add(*btns)

#SEND LINK
def reklama_creator(user_id):
	send_link = InlineKeyboardMarkup()
	
	bot_username = "temelar_bot"
	text = get_lang(user_id, "rek")
	encoded_text = urllib.parse.quote(text)

	url = f"https://t.me/share/url?url=https://t.me/{bot_username}&text={encoded_text}"

	link_btn = InlineKeyboardButton("🚀 SHARE", url=url)

	send_link.add(link_btn)
	
	return send_link