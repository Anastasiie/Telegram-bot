import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import time

API_TOKEN = 'here_token'

bot = telebot.TeleBot(API_TOKEN)

# Список передбачень з подвійним підтекстом та гіфками
predictions = [
    {"text": "Усе, що тобі потрібно, вже поруч.", "gif": "https://media1.tenor.com/m/0CPce9dVFjcAAAAd/arata-amagi-destroyermen.gif"},
    {"text": "Все складеться якнайкраще.", "gif": "https://media1.tenor.com/m/Vl80J1kJK70AAAAC/anime-thumbs-up.gif"},
    {"text": "Сонце світить сьогодні для тебе.", "gif": "https://media1.tenor.com/m/sCRXnog7vqQAAAAC/hidamari-sketch-yuno.gif"},
    {"text": "Твоя усмішка сьогодні зведе з розуму не одну людину.", "gif": "https://media1.tenor.com/m/xYodkEBiw38AAAAC/anime-yes.gif"},
    {"text": "Дивись уважніше: сьогодні всесвіт підкине тобі приємний сюрприз.", "gif": "https://media1.tenor.com/m/6eNDo9FO0iwAAAAC/your-lie-in-april-anime.gif"},
    {"text": "Твоя усмішка приверне удачу.", "gif": "https://media1.tenor.com/m/m2l3d9u-ZuAAAAAC/bad-luck-unfortunate-events.gif"},
    {"text": "Не дивуйся, якщо хтось сьогодні не зможе відвести від тебе очей.", "gif": "https://media1.tenor.com/m/sBCLip9eDcQAAAAC/hyouka.gif"},
    {"text": "Ти на шляху до великого успіху.", "gif": "https://media1.tenor.com/m/m4v-ItJTwroAAAAC/noragami-yato.gif"},
    {"text": "Всі дороги ведуть до тебе, тож будь готовий(а) до приємних несподіванок.", "gif": "https://media1.tenor.com/m/-29xIzuquiwAAAAC/ngnl-no-game-life.gif"},
    {"text": "Гармонія тебе супроводжує.", "gif": "https://media1.tenor.com/m/41EKpijy7dEAAAAC/anime-nature.gif"},
    {"text": "Настав твій день для здійснення мрій.", "gif": "https://media1.tenor.com/m/rXtnbcDGdjwAAAAC/sleep-tired.gif"},
    {"text": "Сьогодні доля на твоєму боці.", "gif": "https://media1.tenor.com/m/oH1iW9NwrngAAAAd/anime-fate-zero.gif"},
    {"text": "Усі твої бажання сьогодні здійсняться.", "gif": "https://media1.tenor.com/m/M6bV3aiheJUAAAAC/wish-rain-weathering-with-you.gif"},
    {"text": "Твоя енергія притягує можливості.", "gif": "https://media1.tenor.com/m/EZX5igQvsxMAAAAC/kanna-beam.gif"},
    {"text": "Цей день принесе нові починання.", "gif": "https://media1.tenor.com/m/_XPtDdeouXQAAAAC/otoboku-the-maidens-are-falling-in-love-with-me.gif"},
    {"text": "На тебе чекають приємні новини.", "gif": "https://media1.tenor.com/m/i4TpjuY05P8AAAAC/yes-sir-yes.gif"},
    {"text": "Ти на порозі чогось неймовірного.", "gif": "https://media1.tenor.com/m/RRFpJRR1PUkAAAAC/anime-girl.gif"},
    {"text": "Сьогодні доля подарує тобі усмішку.", "gif": "https://media1.tenor.com/m/J80oh0-yYr0AAAAd/cartenon-temple-sung-jin-woo.gif"},
    {"text": "Все, що ти запланував(ла), вдасться.", "gif": "https://media1.tenor.com/m/iZGszrwZ0eEAAAAC/watashi-nouryoku-mile.gif"},
    {"text": "На тебе чекає день, повний позитиву.", "gif": "https://media1.tenor.com/m/MOvQz17mWcwAAAAC/soul-eater-positive-energy.gif"},
    {"text": "Твої зусилля сьогодні принесуть плоди.", "gif": "https://media1.tenor.com/m/zN6TnICSW8oAAAAd/tohru-honda-anime.gif"},
]

# Список жартів з гіфками
jokes = [
    {"text": "Чому комп’ютери не їдять морозиво? Тому що вони бояться зависнути!", "gif": "https://media.tenor.com/9ehe_JkMWZ8AAAAM/ninchijoufigurinha.gif"},
    {"text": "Що робить програміст, коли хоче чогось новенького? Відкриває нову вкладку!", "gif": "https://media1.tenor.com/m/3t0YdQjzX4EAAAAd/spray-girl-self-spray.gif"},
    {"text": "Чому програма не встигла на роботу? Вона застрягла в циклі!", "gif": "https://media1.tenor.com/m/iRnmQUtXnIAAAAAC/bocchi-bocchi-the-rock.gif"},
    {"text": "Що зробив програміст після роботи? Вийшов на прогулянку у реальному світі!", "gif": "https://media1.tenor.com/m/FM9cWPb5HbAAAAAC/nou-come-anime.gif"},
    {"text": "Якщо б інтернет був країною, Google був би її президентом.", "gif": "https://media1.tenor.com/m/M7-Ftr7tsz8AAAAC/dance.gif"},
    {"text": "Чому комп'ютерні мишки не люблять сир? Вони краще працюють з файлами!", "gif": "https://media1.tenor.com/m/TMgBAFTGYhgAAAAC/lol-mdr.gif"},
    {"text": "Чому клавіші не ходять на вечірки? Бо вони завжди натиснуті!", "gif": "https://media1.tenor.com/m/GHDnI4nlbCAAAAAC/bocchi-bocchi-the-rock.gif"},
    {"text": "Чому програмісти не люблять понеділки? Бо вони ще не завершили минулий тиждень!", "gif": "https://media1.tenor.com/m/TMgBAFTGYhgAAAAC/lol-mdr.gif"},
    {"text": "Чому бази даних не ходять на вечірки? Вони зберігають усі спогади!", "gif": "https://media1.tenor.com/m/zl4C7DCsoIwAAAAd/nichijou-hit.gif"},
    {"text": "Чому курка перейшла дорогу? Щоб подивитись на тебе!", "gif": "https://media1.tenor.com/m/oP46PcmQeQ4AAAAC/gintoki-jirocho.gif"},
]

# Список компліментів з подвійним підтекстом та гіфками
compliments = [
    {"text": "Твоя енергія настільки сильна, що її можна відчути навіть через екран.", "gif": "https://media1.tenor.com/m/BK_gLvx26fsAAAAC/blond-girl-glasses-frames.gif"},
    {"text": "Твої очі - справжня магія, вони полонять серця.", "gif": "https://media1.tenor.com/m/4SIYshZ6hmcAAAAC/golden-time-ily.gif"},
    {"text": "Твоя усмішка - це те, заради чого хочеться прокидатися щоранку.", "gif": "https://media1.tenor.com/m/Uz5iy1iEKAoAAAAd/shikimoris-not-just-cute-shikimori.gif"},
    {"text": "Якщо б погляди могли вбивати, то ти був(ла) би найнебезпечнішою людиною.", "gif": "https://media1.tenor.com/m/DMy-l-ZMG_kAAAAC/gasai-yuno-mad.gif"},
    {"text": "Ти справжній(ня) маг(иня), бо твої чари діють безвідмовно.", "gif": "https://media1.tenor.com/m/UWTrDBa1IccAAAAC/love-magical.gif"},
    {"text": "Коли ти заходиш до кімнати, світло стає яскравішим.", "gif": "https://media1.tenor.com/m/PPgJHUPnwAMAAAAd/touhou-zarkith.gif"},
    {"text": "Твої слова здатні підкорити будь-яке серце.", "gif": "https://media1.tenor.com/m/P3lV-BPaikAAAAAd/anime-money.gif"},
    {"text": "Ти сьогодні настільки привабливий(а), що навіть удача не змогла втриматися.", "gif": "https://media1.tenor.com/m/gcBDVr-ZNgUAAAAC/lucky-anime.gif"},
    {"text": "Коли ти проходиш поруч, зірки починають блимати частіше.", "gif": "https://media1.tenor.com/m/3wz1Y_c8VlIAAAAC/anime-cute.gif"},
    {"text": "Сьогодні ти настільки чарівний(а), що навіть квіти повертаються в твою сторону.", "gif": "https://media1.tenor.com/m/qWf4Fum5gEAAAAAC/tamaki-sassy.gif"},
    {"text": "Твої кроки сьогодні такі впевнені, що навіть сніг під тобою тане.", "gif": "https://media1.tenor.com/m/kU_EwdsrkLkAAAAC/frieren-dies-cold.gif"},
    {"text": "Ти як сонце після дощу - завжди радуєш око.", "gif": "https://media1.tenor.com/m/yUZllcN0l6gAAAAC/girl-animegirl.gif"},
    {"text": "Твоя природна чарівність неперевершена.", "gif": "https://media.tenor.com/qJnjTod_34oAAAAi/anime-grabby.gif"},
    {"text": "Ти гарний(а) таким(ою), яким(ою) є.", "gif": "https://media1.tenor.com/m/8SoReGELlnAAAAAC/anime-girl-slap.gif"},
    {"text": "Ти гармонійно поєднуєш у собі все найкраще.", "gif": "https://media1.tenor.com/m/EEQaFrEe3kEAAAAC/gintama-anime.gif"},
    {"text": "Твоя індивідуальність - це твоє багатство.", "gif": "https://media1.tenor.com/m/SqW6kmYUeGYAAAAC/money-anime.gif"},
    {"text": "Твоя простота і є справжньою красою.", "gif": "https://media1.tenor.com/m/-LWX47CPrfwAAAAC/anime-anime-girl.gif"},
]

# Лічильники для відстеження натискань
user_clicks = {}

def send_message_with_gif(message, text, gif_url, category):
    user_id = message.from_user.id
    thread_id = message.message_thread_id  # Визначаємо гілку чату
    if user_clicks.get(user_id, {}).get(category, 0) >= 3:
        if category == 'prediction':
            bot.send_message(message.chat.id, "Ти настільки не віриш в власні сили, що стільки натискаєш? 🤔", message_thread_id=thread_id,reply_to_message_id=message.message_id)
            bot.send_animation(message.chat.id, "https://media1.tenor.com/m/UrxDAmsiBPcAAAAC/disgusted-no.gif", message_thread_id=thread_id)
        elif category == 'joke':
            bot.send_message(message.chat.id, "Я тобі що, схожа на клоуна🤡? Хоча, ... \nз тебе життя і так вже пожартувало.", message_thread_id=thread_id,reply_to_message_id=message.message_id)
            bot.send_animation(message.chat.id, "https://media1.tenor.com/m/q8D1MG9lThMAAAAC/oh-no-disappointed.gif", message_thread_id=thread_id)
        elif category == 'compliment':
            bot.send_message(message.chat.id, "Тільки те і робиш, що випрошуєш компліменти.\nМоже зробиш щось для того щоб їх заслужити?🙄.", message_thread_id=thread_id,reply_to_message_id=message.message_id)
            bot.send_animation(message.chat.id, "https://media1.tenor.com/m/ljy1LMHGMF8AAAAC/anime-awkward.gif", message_thread_id=thread_id)

        user_clicks[user_id][category] = 0  # Скидання лічильника
    else:
        bot.send_message(message.chat.id, text, message_thread_id=thread_id,reply_to_message_id=message.message_id)
        bot.send_animation(message.chat.id, gif_url, message_thread_id=thread_id)
        user_clicks[user_id] = user_clicks.get(user_id, {})
        user_clicks[user_id][category] = user_clicks[user_id].get(category, 0) + 1

# Назва гілки, в якій бот працює
allowed_thread_id = 13202

#Кнопочки 
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('🎲 Отримати передбачення'), KeyboardButton('😂 Жарт'), KeyboardButton('😊 Комплімент'))

#Закоментчиний код для вимкнення кнопочок
#markup=telebot.types.ReplyKeyboardRemove()

# Обробник команди /start
@bot.message_handler(commands=['start', 'amen'])
def start_message(message):
    # Перевірка, чи знаходиться користувач у правильній гілці
    if message.chat.type == "supergroup" and message.message_thread_id:
        if message.message_thread_id == allowed_thread_id:
            bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}! Натисни на одну з кнопок, щоб отримати свій позитив на сьогодні!"
                             ,message_thread_id=message.message_thread_id, reply_markup=markup)
    elif message.chat.type == "private":
            bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}! Натисни на одну з кнопок, щоб отримати свій позитив на сьогодні!"
                             ,message_thread_id=message.message_thread_id, reply_markup=markup)
    else:
         bot.send_message(message.chat.id, f"Ніт"
                             ,message_thread_id=message.message_thread_id, reply_markup=telebot.types.ReplyKeyboardRemove())

# Обробник натискання на кнопки
@bot.message_handler(func=lambda message: message.text in ['🎲 Отримати передбачення', '😂 Жарт', '😊 Комплімент'])
def handle_buttons(message):
    # Перевірка, чи знаходиться користувач у правильній гілці
    if message.chat.type == "supergroup" and message.message_thread_id:
        if message.message_thread_id == allowed_thread_id:
            if message.text == '🎲 Отримати передбачення':
                send_prediction(message)
            elif message.text == '😂 Жарт':
                send_joke(message)
            elif message.text == '😊 Комплімент':
                send_compliment(message)

            # Після відправки прибираємо клавіатуру
            bot.send_message(message.chat.id, "Натисни /start або /amen, щоб знову побачити кнопки."
                             ,message_thread_id=message.message_thread_id, reply_markup=markup)
    elif message.chat.type == "private":
            bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}! Натисни на одну з кнопок, щоб отримати свій позитив на сьогодні!"
                             ,message_thread_id=message.message_thread_id, reply_markup=markup)
    else:pass

    
# Функція для відправки передбачення з гіфкою
def send_prediction(message):
    prediction = random.choice(predictions)
    send_message_with_gif(message, prediction["text"], prediction["gif"], 'prediction')

# Функція для відправки жарту з гіфкою
def send_joke(message):
    joke = random.choice(jokes)
    send_message_with_gif(message, joke["text"], joke["gif"], 'joke')

# Функція для відправки компліменту з гіфкою
def send_compliment(message):
    compliment = random.choice(compliments)
    send_message_with_gif(message, compliment["text"], compliment["gif"], 'compliment')

# Запуск бота
bot.polling(none_stop=True)
