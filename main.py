import telebot

# Telegram bot tokeningizni shu yerga kiriting
TOKEN = '7097233011:AAFmLdHBJtidaLJ2hW4V5ibb1oF-nZj4VKk'

# Bot ob'ektini yaratish
bot = telebot.TeleBot(TOKEN)

# /start komandasini ko'rsatuvchi funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Salom! Men echo botman. Siz nima yozsangiz, men shuni qaytaraman.')

# Matnli xabarlarni qabul qilish va qaytarish uchun funksiya
@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

# Video xabarlarni qabul qilish va qaytarish uchun funksiya
@bot.message_handler(content_types=['video'])
def echo_video(message):
    bot.send_video(message.chat.id, message.video.file_id)

# Ovozli xabarlarni qabul qilish va qaytarish uchun funksiya
@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    bot.send_voice(message.chat.id, message.voice.file_id)

# Botni ishga tushirish
bot.polling()
