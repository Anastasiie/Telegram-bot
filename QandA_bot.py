import webbrowser
import telebot

bot = telebot.TeleBot('toki_doki_botti_here')
GROUP_CHAT_ID = -1002228900181
user_messages = {}

@bot.message_handler(commands=['site', 'website', 'сайт', 'вебсайт'])
def site(message):
    bot.send_message(message.chat.id, 'Перейдіть за посиланням університету: https://vstup.udu.edu.ua/')

@bot.message_handler(commands=['start', 'привіт'])
def start(message):
    bot.send_message(message.chat.id, f'Вітаю, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
<b>Інструкція для користування ботом:</b>

/start - Привітання від бота.
/help - Відображення цієї інструкції.
/site - Відкрити вебсайт університету.

Коли ви надсилаєте текстові повідомлення, фото або документи у приватному чаті з ботом, вони будуть автоматично пересилатися до групи. \nВідповіді на ці повідомлення у групі також будуть пересилатися назад до вас.
"""
    bot.send_message(message.chat.id, help_text, parse_mode='html')

@bot.message_handler(commands=['chatID'])
def chatID(message):
    bot.send_message(message.chat.id, f'ID chat: {message.chat.id}')

@bot.message_handler(content_types=['text'], func=lambda message: message.chat.type == 'private')
def forward_text_to_group(message):
    user_messages[message.message_id] = message.chat.id
    print(f"Зберігаємо повідомлення: {message.message_id} від {message.chat.id}")
    forwarded_message = bot.send_message(
        GROUP_CHAT_ID,
        f"<em>Повідомлення</em> від <b>{message.from_user.first_name}</b>:\n{message.text}",
        parse_mode='HTML'
    )
    user_messages[forwarded_message.message_id] = message.chat.id

@bot.message_handler(content_types=['photo'], func=lambda message: message.chat.type == 'private')
def forward_photo_to_group(message):
    user_messages[message.message_id] = message.chat.id
    print(f"Зберігаємо фото: {message.message_id} від {message.chat.id}")
    file_id = message.photo[-1].file_id
    forwarded_message = bot.send_photo(
        GROUP_CHAT_ID,
        file_id,
        caption=f"<em>Фото</em> від <b>{message.from_user.first_name}</b>\n{message.caption or ''}",
        parse_mode='HTML'
    )
    user_messages[forwarded_message.message_id] = message.chat.id

@bot.message_handler(content_types=['document'], func=lambda message: message.chat.type == 'private')
def forward_document_to_group(message):
    user_messages[message.message_id] = message.chat.id
    print(f"Зберігаємо документ: {message.message_id} від {message.chat.id}")
    file_id = message.document.file_id
    forwarded_message = bot.send_document(
        GROUP_CHAT_ID,
        file_id,
        caption=f"<em>Файл</em> від <b>{message.from_user.first_name}</b>\n{message.caption or ''}",
        parse_mode='HTML'
    )
    user_messages[forwarded_message.message_id] = message.chat.id

@bot.message_handler(content_types=['text', 'photo', 'document'], func=lambda message: message.reply_to_message is not None and message.chat.id == GROUP_CHAT_ID)
def reply_to_user(message):
    print(f"Отримано відповідь у групі на повідомлення ID: {message.reply_to_message.message_id}")
    original_message_id = message.reply_to_message.message_id
    if original_message_id in user_messages:
        user_chat_id = user_messages[original_message_id]
        print(f"Знайдено оригінальне повідомлення. Відправка відповіді користувачеві: {user_chat_id}")
        try:
            if message.content_type == 'text':
                bot.send_message(user_chat_id, f"<b><em>Відповідь з групи:</em></b>\n{message.text}", parse_mode='HTML')
            elif message.content_type == 'photo':
                file_id = message.photo[-1].file_id
                bot.send_photo(user_chat_id, file_id, caption=f"<b><em>Відповідь з групи:</em></b>\n{message.caption or ''}", parse_mode='HTML')
            elif message.content_type == 'document':
                file_id = message.document.file_id
                bot.send_document(user_chat_id, file_id, caption=f"<b><em>Відповідь з групи:</em></b>\n{message.caption or ''}", parse_mode='HTML')
        except Exception as e:
            print(f"Помилка при відправці повідомлення: {e}")
    else:
        print("Не вдалося знайти оригінальне повідомлення користувача.")
        bot.send_message(GROUP_CHAT_ID, "Не вдалося знайти оригінальне повідомлення користувача.")

bot.polling(non_stop=True)
