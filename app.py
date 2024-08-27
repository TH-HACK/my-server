from flask import Flask, request
import telebot

API_TOKEN = "7517544528:AAEwE_8hpzGDqaQyaNSBlRUHi0CZ-ptGn_o"  # ضع هنا توكن البوت الخاص بك
WEBHOOK_URL = "https://my-server-lilac.vercel.app/get-url"  # ضع هنا رابط الويبهوك الخاص بك

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Unsupported Media Type', 415

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome! Bot is now running via Webhook.")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=5000)
