import telebot 
print ("start ok")
TOKEN = "7865573862:AAFTwhJn2HpLTL7VHy3hbEN4ZMEFyb86WBQ" 
bot = telebot.TeleBot(TOKEN) 
@bot.message_handler(commands=['ban']) 
def ban_user(message): 
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    # Проверяем, является ли пользователь администратором чата 
    if is_user_admin(chat_id, user_id): 
        try: 
            user_to_ban = message.reply_to_message.from_user.id 
            bot.kick_chat_member(chat_id, user_to_ban) 
            bot.reply_to(message, "Пользователь забанен.") 
            print("banned")
        except Exception as e: 
            bot.reply_to(message, "Не удалось забанить пользователя.") 
            print("banned error")
    else: 
        bot.reply_to(message, "У вас нет прав для этой команды. Или запуск в чате!") 
        print("banned error")
        
@bot.message_handler(commands=['info']) 
def ban_user(message): 
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    # Проверяем, является ли пользователь администратором чата 
    if is_user_admin(chat_id, user_id): 
        try:
            bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
            print("Info started")
        except Exception as e: 
            bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
            print("Info started")
    else: 
        bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
        print("info started")

@bot.message_handler(commands=['admin']) 
def ban_user(message): 
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    # Проверяем, является ли пользователь администратором чата 
    if is_user_admin(chat_id, user_id): 
        try:
            bot.reply_to(message, "Я не дурак") 
            print("admin started")
        except Exception as e: 
            bot.reply_to(message, "Я не дурак") 
            print("admin started")
    else: 
        bot.reply_to(message, "Я не дурак") 
        print("admin started")        

@bot.message_handler(commands=['start']) 
def ban_user(message): 
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    # Проверяем, является ли пользователь администратором чата 
    if is_user_admin(chat_id, user_id): 
        try:
            bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
            print("bot started")
        except Exception as e: 
            bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
            print("bot started")
    else: 
        bot.reply_to(message, "Привет! Я бан-Бот меня создал Гриша из ООО АО КГИ @xakerguymnasium11 ") 
        print("bot started")        


@bot.message_handler(commands=['unban']) 
def unban_user(message): 
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    # Проверяем, является ли пользователь администратором чата 
    if is_user_admin(chat_id, user_id): 
        try: 
            user_to_unban = message.reply_to_message.from_user.id 
            bot.unban_chat_member(chat_id, user_to_unban) 
            bot.reply_to(message, "Пользователь разбанен.") 
            print("unbanned")
        except Exception as e: 
            bot.reply_to(message, "Не удалось разбанить пользователя.") 
            print("unbanned error")
    else: 
        bot.reply_to(message, "У вас нет прав для этой команды.") 
        print("unbanned error")

def is_user_admin(chat_id, user_id): 
    chat_member = bot.get_chat_member(chat_id, user_id) 
    return chat_member.status == "administrator" or chat_member.status == "creator" 


if __name__ == '__main__': 
    bot.polling(none_stop=True)
