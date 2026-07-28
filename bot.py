import os
import telebot

# توکنی که از BotFather گرفتید را اینجا وارد کنید
TOKEN = os.getenv("BOT_TOKEN", "8040157594:AAFkG6P0AvVw9sVW3acU71bJA3Xb2as8gSg")
bot = telebot.TeleBot(TOKEN)

# تگ قدیمی که باید پاک شود و تگ جدید شما
OLD_TAG = "@Naya_Press"
NEW_TAG = "@Forvatanam"

@bot.message_handler(func=lambda message: True)
def replace_tag(message):
    if message.text:
        # جایگزینی تگ قدیمی با تگ جدید
        new_text = message.text.replace(OLD_TAG, NEW_TAG)
        
        # ارسال پیام ویرایش شده به خودتان یا کانال مقصد
        bot.send_message(message.chat.id, new_text)

print("Bot is running...")
bot.infinity_polling()
