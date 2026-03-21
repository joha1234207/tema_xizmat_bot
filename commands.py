# commands.py

from telebot import types
from admin__panel import admin_panel_
import tugmalar


def start_command(bot, admin):
    
    #ADMIN COMMAND
    @bot.message_handler(commands=["admin"])
    
    def admin_go(message):
    	 
    	 if message.chat.id == admin:
    	 	admin_panel_(bot, admin)
    	 else:
    	 	bot.send_message(message.chat.id, f"Siz admin emassiz😅\n\n🆔: {message.chat.id}")
    	 	
    #START COMMAND
    @bot.message_handler(commands=["start"])
    def salomlash(message):
       
       
     
       bot.send_message(admin, f"🥳Yangi foydalanuvchi kirdi:\n\n————————————\n👤username: @{message.from_user.username}\n\n🆔: <code>{message.chat.id}</code>\n\n🟡Name: {message.from_user.first_name}", parse_mode="HTML")
       bot.reply_to(message,
            f"""<b>👋 Xush kelibsiz! <code>{message.from_user.first_name}</code>\n
🎨Bu bot orqali turli xil chiroyli Telegram temalarini topishingiz mumkin.\n
 📥 Temani tanlang va oʻrnatib oling.\n
⚡ Yangi temalar doimiy qo‘shib boriladi.\n
👇 Boshlash uchun quyidagi tugmalardan foydalaning.</b>""",
            reply_markup=tugmalar.reply_panel, parse_mode="HTML")
    
    @bot.message_handler(commands=["help"])
    def help_command(message):
        refe_btn = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("BOT YANGILIKLARI📻", url="https://t.me/jahongi_studi010")
        btn2 = types.InlineKeyboardButton("OBOILAR🥰", url="https://t.me/oboilar_temalar")
        refe_btn.add(btn1)
        refe_btn.add(btn2)
        
        bot.send_message(message.chat.id, """<b>🤖 Bot haqida

🎨 Ushbu bot Telegram uchun eng chiroyli va sifatli temalarni jamlagan maxsus botdir.

📂 Bot ichida siz turli xil kategoriyadagi temalarni topishingiz mumkin:

🖤 Dark — zamonaviy va qorong‘i uslubdagi temalar

💖 Anime — anime uslubidagi chiroyli dizaynlar

🐯 Hayvonchalar — hayvon rasmlari bilan bezatilgan temalar

🤍 Soft — ko‘zga yoqimli va yumshoq rangli temalar

💔 Boshqa — noodatiy va kreativ temalar

📜 Bundan tashqari bot ichida:
🔤 Turli xil chiroyli tillar
😂 Qiziqarli stiker paketlari ham mavjud

⚡ Botga doimiy ravishda yangi temalar qo‘shib boriladi.

📢 Eng yangi temalar va bot yangiliklarini birinchi bo‘lib olish uchun kanalimizga obuna bo‘ling!</b>
""",
    reply_markup=refe_btn,
    parse_mode="HTML"
)