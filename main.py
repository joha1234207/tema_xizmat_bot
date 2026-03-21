# main.py

import telebot
from config import TOKEN, admin
import commands
import funksiyalar
import admin__panel
from flask import Flask, request


app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

# UPTIME ROBOT UCHUN GET
@app.route("/", methods=['GET'])
def home():
    return "Bot ishlayapti"

#WEBHOOK
@app.route('/webhook', methods=['POST'])
def webhook():
    
    json_str = request.get_data().decode('UTF-8')
    
    update = telebot.types.Update.de_json(json_str)
    
    bot.process_new_updates([update])
    
    return "ok"

# START & HELP
commands.start_command(bot, admin)

# REPLY TUGMALAR & CALLBACK
funksiyalar.funksiyalar(bot, admin)


# LOCAL TEST UCHUN (telefon yoki Pydroid)
#if __name__ == "__main__":
    # Agar local test qilmoqchi bo'lsang polling ishlaydi
#    bot.remove_webhook()
#    bot.infinity_polling()
    
# FLASKNI
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://tema-xizmat-bot.onrender.com/webhook")
    app.run(host="0.0.0.0", port=8080)
