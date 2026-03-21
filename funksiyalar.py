# funksiyalar.py

from telebot import types
import json
import random
import tugmalar
import time

def funksiyalar(bot, admin):
    
    user_state = {}
    TIMEOUT = 10
    
    #CLEANER
    def timeout(user_id):
    	
    	if user_id in user_state:
    		
    		if time.time() - user_state[user_id]["time"] > TIMEOUT:
    			
    			del user_state[user_id]
    			return False
    			
    		return True
    		
    #OS TANLASH DEF
    def os_choicer(id):
    	
    	bot.send_message(id, "<b>❗ PLATFORMANI TANLANG</b>", reply_markup=tugmalar.and_ios, parse_mode="HTML")
    	
    #KAT TANLASH
    def kat_choicer(id):
    	
    	bot.send_message(id, "<b>🔠 KATEGORIYANI TANLANG</b>", reply_markup=tugmalar.kat_btns, parse_mode="HTML")
    
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
        	
        bot.send_message(id, f"<b>{kat}\nSTYLEDAGI TEMA\n\nOʻRNATISH📲\nTUGMASI ORQALI OʻRNATIB OLING</b>", reply_markup=panel, parse_mode="HTML")
    
    
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
        if message.text == "📂 Temalar":
        	
        	bot.send_message(admin, f"Botda aktivlik temalar\n\n•link: {username}\n•Nomi: {message.from_user.first_name}")
        	
        	os_choicer(message.chat.id)
        
        #MAHFIY BÓLIM
        elif message.text == "🔐 Maxfiy bo‘lim":
        	
        	bot.send_message(message.chat.id, """<b>🔥 BOT VERSION 4.0 – YAQINDA 🔥
        	
🚀 KUTILAYOTGAN YANGI FUNKSIYA: 1 TA RASMDAN THEME YARATISH
        	
📸 VERSION 4.0 DA SIZ FAQAT BITTA RASM YUBORASIZ…
⚡ BOT ESA UNI AVTOMATIK TARZDA CHIROYLI THEME GA AYLANTIRADI

🎨 RASM RANGLARI ANALIZ QILINADI
🧠 ENG MOS DIZAYN TANLANADI
✨ VA NATIJADA TAYYOR, PROFESSIONAL THEME YARATILADI

💡 HAMMASI SODDA VA QULAY
⏱ BARCHASI BIR NECHA SONIYADA ISHLAYDI

YARATISH IMKONIYATI
🚀 VERSION 4.0 BILAN YANGI DARAJAGA CHIQING
        	</b>""", parse_mode="HTML")
        
        #BOSHQA NARSA YOZILSA
        else:
            bot.send_message(message.chat.id, "<b>👾 ERROR 👾\n\n1⃣ ILTIMOS PASTDAGI TUGMALARDAN FOYDALANING\n\n2⃣ /start BILAN BOTNI YANGILANG</b>", parse_mode="HTML")
    
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
        	for id in user_state:
        		bot.send_message(id, """<b>
🚀 BOTNI YANADA ZO‘R QILISHGA YORDAM BERING!

😎 DO‘STLARINGIZNI TAKLIF 
QILING
🔥 VA BIRGA FOYDALANING
📸 YAQINDA: 1 TA RASMDAN THEME YARATISH FUNKSIYASI!

👇 HOZIRDO‘Q DO‘STLARINGIZGA YUBORING
<a href="https://t.me/temelar_bot">CLICK</a>
        	</b>""", parse_mode="HTML")