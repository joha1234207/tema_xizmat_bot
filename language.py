#language.py

import sqlite3
import json

def get_lang(user_id, savol):
    from main import bot
    import defs
    
    with sqlite3.connect("data.db", check_same_thread=False) as db:
        cursor = db.cursor()
        
        # TABLE
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
        
        # SELECT LANGUAGE
        cursor.execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
        user_lang = cursor.fetchone()
        
        if not user_lang or user_lang[0] == "none":
            print("Tilni tanlamagan")
            return defs.lang_choicer_start(bot, user_id)
        
        # TILNI OLISH VA QAYTARISH
        langs = {
            "🇷🇺 РУССКИЙ 🇷🇺": "ru",
            "🇲🇾 ENGLISH 🇲🇾": "en",
            "🇺🇿 UZBEK 🇺🇿": "uz",
            "🇹🇯 ТОҶИКӢ 🇹🇯": "tj"
        }
        lang = langs.get(user_lang[0], "uz")  # default uz
        with open(f"{lang}.json", "r", encoding="utf-8") as f:
            lugat = json.load(f)
            return lugat.get(savol, savol)  # default savol agar topilmasa