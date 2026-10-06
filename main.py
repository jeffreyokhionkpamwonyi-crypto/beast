import os
from flask import Flask
import telebot, threading, time

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "BEAST V2 LIVE"

@bot.message_handler(commands=['start'])
def handle(m):
    bot.reply_to(m, "BEAST V2 LIVE 24/7")

def run_bot():
    while True:
        try:
            bot.infinity_polling()
        except:
            time.sleep(5)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))




