# Импортируем необходимые библиотеки
import time
import telebot
from telebot import TeleBot
from telebot import types
import docx
import uuid
from datetime import datetime
from docx2pdf import convert
import pythoncom
import random

doc = docx.Document('documents\gramota.docx')
paragraphs = list(doc.paragraphs)


class Data(object):
    def __init__(self):
        self.sayed = int
        self.count = int

        self.robot_do = int
        self.robot_fail = int
        self.robot_correct = int

        self.aero_do = int
        self.aero_fail = int
        self.aero_correct = int

        self.bio_do = int
        self.bio_fail = int
        self.bio_correct = int

        self.vrar_do = int
        self.vrar_fail = int
        self.vrar_correct = int

        self.promdiz_do = int
        self.promdiz_fail = int
        self.promdiz_correct = int

        self.place = int


Date = Data()
Date.sayed = 0
Date.count = 0

Date.robot_do = 0
Date.robot_fail = 0
Date.robot_correct = 0

Date.aero_do = 0
Date.aero_fail = 0
Date.aero_correct = 0

Date.bio_do = 0
Date.bio_fail = 0
Date.bio_correct = 0

Date.vrar_do = 0
Date.vrar_fail = 0
Date.vrar_correct = 0

Date.promdiz_do = 0
Date.promdiz_fail = 0
Date.promdiz_correct = 0

Date.place = 0

bot: TeleBot = telebot.TeleBot('6282382646:AAGrbRtD9lSJcJsW3X-hyquOQM0v_1SV_h8')
avtor = types.ReplyKeyboardMarkup(resize_keyboard=True)
avtor.add('Автор🕶')

startkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
startkeyboard.add('Начать▶️️')

starting7 = types.InlineKeyboardMarkup()
da1 = types.InlineKeyboardButton(text='Конечно!', callback_data='start!')
starting7.add(da1)

contin = types.InlineKeyboardMarkup()
continye = types.InlineKeyboardButton(text='Продолжаем!', callback_data='start!')
contin.add(continye)

# Клавиатура - направления - все
napravleniya5 = types.ReplyKeyboardMarkup()
napravleniya5.add('Робоквантум🤖')
napravleniya5.add('Аэроквантум🚁')
napravleniya5.add('Биоквантум🔬')
napravleniya5.add('VR/AR-квантум🥽')
napravleniya5.add('Промдизайнквантум🎨🖌')

# Клавиатура - направления - не все (регулируются с прохождением)
napravleniya4 = types.ReplyKeyboardMarkup()
napravleniya3 = types.ReplyKeyboardMarkup()
napravleniya2 = types.ReplyKeyboardMarkup()
napravleniya1 = types.ReplyKeyboardMarkup()
napravleniya0 = types.ReplyKeyboardMarkup()
napravleniya01 = types.ReplyKeyboardMarkup()

# Клавиатура - робоквантум #
robokvantkeyboard = types.InlineKeyboardMarkup()
robkv_door = types.InlineKeyboardButton(text='Открыть дверь', callback_data='robkvdoor')
robokvantkeyboard.add(robkv_door)
# Робоквантум - вопрос 1 #
robokvantquestkeyboard1_2 = types.InlineKeyboardMarkup()
robokv_quest1_1 = types.InlineKeyboardButton(text='Lego',
                                             callback_data='Uncorrect_robokv1_2')
robokv_quest1_2 = types.InlineKeyboardButton(text='Сложная робототехника',
                                             callback_data='robokv_quest1_2_correct')
robokvantquestkeyboard1_2.add(robokv_quest1_1)
robokvantquestkeyboard1_2.add(robokv_quest1_2)

# Робоквантум - вопрос 2 #
robokvantquestkeyboard2_2 = types.InlineKeyboardMarkup()
robokv_quest2_1 = types.InlineKeyboardButton(text='Смириться и собирать роботов',
                                             callback_data='Uncorrect_robokv2_2')
robokv_quest2_2 = types.InlineKeyboardButton(text='Создавать код для роботов',
                                             callback_data='robokv_quest2_2_correct')
robokvantquestkeyboard2_2.add(robokv_quest2_1)
robokvantquestkeyboard2_2.add(robokv_quest2_2)

# Робоквантум - вопрос 3 #
robokvantquestkeyboard3_2 = types.InlineKeyboardMarkup()
robokv_quest3_1 = types.InlineKeyboardButton(text='16',
                                             callback_data='Uncorrect_robokv3_2')
robokv_quest3_2 = types.InlineKeyboardButton(text='12',
                                             callback_data='robokv_quest3_2_correct')
robokvantquestkeyboard3_2.add(robokv_quest3_1, robokv_quest3_2)

# Робоквантум - вопрос 4 #
robokvantquestkeyboard4_2 = types.InlineKeyboardMarkup()
robokv_quest4_1 = types.InlineKeyboardButton(text='С квантового компьютера',
                                             callback_data='Uncorrect_robokv4_2')
robokv_quest4_2 = types.InlineKeyboardButton(text='С не очень сложных машинок',
                                             callback_data='robokv_quest4_2_correct')
robokvantquestkeyboard4_2.add(robokv_quest4_1)
robokvantquestkeyboard4_2.add(robokv_quest4_2)

# Клавиатура - аэроквантум
aerokvantkeyboard = types.InlineKeyboardMarkup()
aerokv_door = types.InlineKeyboardButton(text='Открыть дверь', callback_data='aerokvdoor')
aerokvantkeyboard.add(aerokv_door)
# Аэроквантум - вопрос 1 #
aerokvantquestkeyboard1_2 = types.InlineKeyboardMarkup()
aerokv_quest1_1 = types.InlineKeyboardButton(text='Курс, посвящённый авиапромышленности',
                                             callback_data='aerokv_quest1_2_correct')
aerokv_quest1_2 = types.InlineKeyboardButton(text='Квадрокоптеры, машины, самолёт и вертолёты',
                                             callback_data='Uncorrect_aerokv1_2')
aerokvantquestkeyboard1_2.add(aerokv_quest1_1)
aerokvantquestkeyboard1_2.add(aerokv_quest1_2)

# Аэроквантум - вопрос 2 #
aerokvantquestkeyboard2_2 = types.InlineKeyboardMarkup()
aerokv_quest2_1 = types.InlineKeyboardButton(text='72',
                                             callback_data='aerokv_quest2_2_correct')
aerokv_quest2_2 = types.InlineKeyboardButton(text='100',
                                             callback_data='Uncorrect_aerokv2_2')
aerokvantquestkeyboard2_2.add(aerokv_quest2_1)
aerokvantquestkeyboard2_2.add(aerokv_quest2_2)

# Аэроквантум - вопрос 3 #
aerokvantquestkeyboard3_2 = types.InlineKeyboardMarkup()
aerokv_quest3_1 = types.InlineKeyboardButton(text='Нет',
                                             callback_data='Uncorrect_aerokv3_2')
aerokv_quest3_2 = types.InlineKeyboardButton(text='Да',
                                             callback_data='aerokv_quest3_2_correct')
aerokvantquestkeyboard3_2.add(aerokv_quest3_1)
aerokvantquestkeyboard3_2.add(aerokv_quest3_2)

# Аэроквантум - вопрос 4 #
aerokvantquestkeyboard4_2 = types.InlineKeyboardMarkup()
aerokv_quest4_1 = types.InlineKeyboardButton(text='Все этапы жизненного цикла кванториума',
                                             callback_data='Uncorrect_aerokv4_2')
aerokv_quest4_2 = types.InlineKeyboardButton(text='Все этапы жизненного цикла выпуска летательного аппарата',
                                             callback_data='aerokv_quest4_2_correct')
aerokvantquestkeyboard4_2.add(aerokv_quest4_1)
aerokvantquestkeyboard4_2.add(aerokv_quest4_2)

# Клавиатура - биоквантум
biokvantkeyboard = types.InlineKeyboardMarkup()
biokv_door = types.InlineKeyboardButton(text='Открыть дверь', callback_data='biokvdoor')
biokvantkeyboard.add(biokv_door)

# Биоквантум - вопрос 1 #
biokvantquestkeyboard1_2 = types.InlineKeyboardMarkup()
biokv_quest1_1 = types.InlineKeyboardButton(text='Крутой урок биологии',
                                            callback_data='biokv_quest1_2_correct')
biokv_quest1_2 = types.InlineKeyboardButton(text='Школьный урок биологии',
                                            callback_data='Uncorrect_biokv1_2')
biokvantquestkeyboard1_2.add(biokv_quest1_1)
biokvantquestkeyboard1_2.add(biokv_quest1_2)

# Биоквантум - вопрос 2 #
biokvantquestkeyboard2_2 = types.InlineKeyboardMarkup()
biokv_quest2_1 = types.InlineKeyboardButton(text='учёбе',
                                            callback_data='Uncorrect_biokv2_2')
biokv_quest2_2 = types.InlineKeyboardButton(text='новейшим достижениям',
                                            callback_data='biokv_quest2_2_correct')
biokvantquestkeyboard2_2.add(biokv_quest2_1)
biokvantquestkeyboard2_2.add(biokv_quest2_2)

# Биоквантум - вопрос 3 #
biokvantquestkeyboard3_2 = types.InlineKeyboardMarkup()
biokv_quest3_1 = types.InlineKeyboardButton(text='Математики, химии, русского языка',
                                            callback_data='Uncorrect_biokv3_2')
biokv_quest3_2 = types.InlineKeyboardButton(text='Генной инженерии и микробиологии растений',
                                            callback_data='biokv_quest3_2_correct')
biokvantquestkeyboard3_2.add(biokv_quest3_1)
biokvantquestkeyboard3_2.add(biokv_quest3_2)

# Биоквантум - вопрос 4 #
biokvantquestkeyboard4_2 = types.InlineKeyboardMarkup()
biokv_quest4_1 = types.InlineKeyboardButton(text='15+',
                                            callback_data='biokv_quest4_2_correct')
biokv_quest4_2 = types.InlineKeyboardButton(text='10+',
                                            callback_data='Uncorrect_biokv4_2')
biokvantquestkeyboard4_2.add(biokv_quest4_1)
biokvantquestkeyboard4_2.add(biokv_quest4_2)

# Клавиатура - VR/AR-квантум
vrarkvantkeyboard = types.InlineKeyboardMarkup()
vrar_door = types.InlineKeyboardButton(text='Открыть дверь', callback_data='vrardoor')
vrarkvantkeyboard.add(vrar_door)

# VR/AR-квантум - вопрос 1 #
vrarkvantquestkeyboard1_2 = types.InlineKeyboardMarkup()
vrar_quest1_1 = types.InlineKeyboardButton(text='VR/AR технологиям',
                                           callback_data='vrarkv_quest1_2_correct')
vrar_quest1_2 = types.InlineKeyboardButton(text='компьютерам и телефонам',
                                           callback_data='Uncorrect_vrar1_2')
vrarkvantquestkeyboard1_2.add(vrar_quest1_1)
vrarkvantquestkeyboard1_2.add(vrar_quest1_2)

# VR/AR-квантум - вопрос 2 #
vrarkvantquestkeyboard2_2 = types.InlineKeyboardMarkup()
vrar_quest2_1 = types.InlineKeyboardButton(text='телефоны',
                                           callback_data='Uncorrect_vrar2_2')
vrar_quest2_2 = types.InlineKeyboardButton(text='здания',
                                           callback_data='vrarkv_quest2_2_correct')
vrarkvantquestkeyboard2_2.add(vrar_quest2_1)
vrarkvantquestkeyboard2_2.add(vrar_quest2_2)

# VR/AR-квантум - вопрос 3 #
vrarkvantquestkeyboard3_2 = types.InlineKeyboardMarkup()
vrar_quest3_1 = types.InlineKeyboardButton(text='Улучшению графики',
                                           callback_data='Uncorrect_vrar3_2')
vrar_quest3_2 = types.InlineKeyboardButton(text='Командной работе и проектной деятельности',
                                           callback_data='vrarkv_quest3_2_correct')
vrarkvantquestkeyboard3_2.add(vrar_quest3_1)
vrarkvantquestkeyboard3_2.add(vrar_quest3_2)

# VR/AR-квантум - вопрос 4 #
vrarkvantquestkeyboard4_2 = types.InlineKeyboardMarkup()
vrar_quest4_1 = types.InlineKeyboardButton(text='12+',
                                           callback_data='vrarkv_quest4_2_correct')
vrar_quest4_2 = types.InlineKeyboardButton(text='15+',
                                           callback_data='Uncorrect_vrar4_2')
vrarkvantquestkeyboard4_2.add(vrar_quest4_1)
vrarkvantquestkeyboard4_2.add(vrar_quest4_2)

# Клавиатура - Промдизайнквантум
promdizkvantkeyboard = types.InlineKeyboardMarkup()
promdiz_door = types.InlineKeyboardButton(text='Открыть дверь', callback_data='promdizdoor')
promdizkvantkeyboard.add(promdiz_door)
# Промдизайнквантум - вопрос 1 #
promdizkvantquestkeyboard1_2 = types.InlineKeyboardMarkup()
promdiz_quest1_1 = types.InlineKeyboardButton(text='Урок ИЗО высокого уровня',
                                              callback_data='promdizkv_quest1_2_correct')
promdiz_quest1_2 = types.InlineKeyboardButton(text='Самый простой урок ИЗО',
                                              callback_data='Uncorrect_promdiz1_2')
promdizkvantquestkeyboard1_2.add(promdiz_quest1_1)
promdizkvantquestkeyboard1_2.add(promdiz_quest1_2)

# Промдизайнквантум - вопрос 2 #
promdizkvantquestkeyboard2_2 = types.InlineKeyboardMarkup()
promdiz_quest2_1 = types.InlineKeyboardButton(text='телефона, компьютера',
                                              callback_data='Uncorrect_promdiz2_2')
promdiz_quest2_2 = types.InlineKeyboardButton(text='дизайнерского скетчинга',
                                              callback_data='promdizkv_quest2_2_correct')
promdizkvantquestkeyboard2_2.add(promdiz_quest2_1)
promdizkvantquestkeyboard2_2.add(promdiz_quest2_2)

promdizkvantquestkeyboard2 = types.InlineKeyboardMarkup()
promdizkvantquestkeyboard2.add(promdiz_quest2_2)
# Промдизайнквантум - вопрос 3 #
promdizkvantquestkeyboard3_2 = types.InlineKeyboardMarkup()
promdiz_quest3_1 = types.InlineKeyboardButton(text='предлагать функциональные и красивые решения',
                                              callback_data='promdizkv_quest3_2_correct')
promdiz_quest3_2 = types.InlineKeyboardButton(text='предлагать решить задачу другому',
                                              callback_data='Uncorrect_promdiz3_2')
promdizkvantquestkeyboard3_2.add(promdiz_quest3_1)
promdizkvantquestkeyboard3_2.add(promdiz_quest3_2)

# Промдизайнквантум - вопрос 4 #
promdizkvantquestkeyboard4_2 = types.InlineKeyboardMarkup()
promdiz_quest4_1 = types.InlineKeyboardButton(text='10+',
                                              callback_data='Uncorrect_promdiz4_2')
promdiz_quest4_2 = types.InlineKeyboardButton(text='12+',
                                              callback_data='promdizkv_quest4_2_correct')
promdizkvantquestkeyboard4_2.add(promdiz_quest4_1)
promdizkvantquestkeyboard4_2.add(promdiz_quest4_2)

# Клавиатура - конец
finalkeyboard = types.ReplyKeyboardMarkup()
finalkeyboard.add('Конец🏁')


# Ответ на /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.delete_message(message.chat.id, message.message_id)
    start_pic = open(r'img\kv33.png', 'rb')
    bot.send_photo(message.chat.id, start_pic, 'Приветствую вас!', reply_markup=avtor)
    start_pic.close()


# "Берём в обхват" callback (ответ назад) функцию, чтобы отвечать на нажатие InlineKeyboardButtons
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_cb_data(callback):
    # Начало начал
    if callback.data == 'start!':
        if Date.sayed == 0:
            # Переменная "Date.Sayed" отвечает за кол-во раз сказанного текста, чтобы текст всё время не повторялся
            Date.sayed += 1
            # Дальше идёт текст сюжета:
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                  text='_Ну тогда чего же мы ждём?_\n*Начинаем!*', parse_mode='MarkDown')
            time.sleep(5)
            bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
            b1 = bot.send_message(callback.message.chat.id,
                                  '_Однажды Вася Иванов решил сходить на профориентацию\nв Кванториум-33, ему не хотелось отставать от прогресса, и он хотел узнать_ *что-нибудь новое*!',
                                  parse_mode='MarkDown')
            time.sleep(15)
            bot.delete_message(chat_id=callback.message.chat.id, message_id=b1.id)
            b2 = bot.send_message(callback.message.chat.id,
                                  '_Когда Вася пришёл в кванториум, его встретил преподаватель,\nкоторый как раз проводил профориентацию._',
                                  parse_mode='MarkDown')
            time.sleep(10)
            bot.delete_message(chat_id=callback.message.chat.id, message_id=b2.id)
            kv_photo = open(r'img\kv33T.png', 'rb')
            kv = bot.send_photo(callback.message.chat.id, kv_photo,
                                '`Кванториум — это место на территории технопарка, оснащённое высокотехнологичным оборудованием.\n'
                                'Благодаря кванториуму дети развиваются,\n'
                                'узнают что-либо новое, а главное – получают ценный опыт.\n'
                                'В общем и целом, это классное место!\n'
                                'В кванториуме много направлений!\n'
                                'Но мы рассмотрим и узнаем лишь некоторые из них.`',
                                parse_mode='MarkDown').message_id
            kv_photo.close()
            bot.pin_chat_message(callback.message.chat.id, kv)
            time.sleep(25)
            bot.send_message(callback.message.chat.id,
                             '_Всех приветствую!\nСегодня мы должны посетить в общем 5 направлений!_\n(P.S: кнопки можно двигать вверх-вниз)\n(снизу ещё промдизайквантум                )',
                             parse_mode='MarkDown', reply_markup=napravleniya5)
            # reply_markup=napravleniya5 - перекидываем пользователя на выбор 1 из 5 направлений
        elif Date.sayed == 1:
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
            if Date.robot_do > 0 and Date.aero_do > 0 and Date.bio_do > 0 and Date.vrar_do > 0 and Date.promdiz_do > 0:
                bot.send_message(callback.message.chat.id, '__*Вот и подошёл наш день профориентации концу\!*__',
                                 parse_mode='MarkDownV2')
                time.sleep(5)
                bot.send_message(callback.message.chat.id, '_Спасибо за прохождение игры!_\n*Ещё увидимся!*',
                                 parse_mode='MarkDown', reply_markup=finalkeyboard)
            else:
                if Date.count == 0:
                    # проверяем, что прошёл пользователь
                    # если прошёл - больше не добавляем
                    if Date.robot_do == 0:
                        napravleniya4.add('Робоквантум🤖')
                    if Date.aero_do == 0:
                        napravleniya4.add('Аэроквантум🚁')
                    if Date.bio_do == 0:
                        napravleniya4.add('Биоквантум🔬')
                    if Date.vrar_do == 0:
                        napravleniya4.add('VR/AR-квантум🥽')
                    if Date.promdiz_do == 0:
                        napravleniya4.add('Промдизайнквантум🎨🖌')
                    # reply_markup=napravleniya4 - перекидываем пользователя на выбор 1 из 4 направлений
                    bot.send_message(callback.message.chat.id, 'Куда дальше?', reply_markup=napravleniya4)
                elif Date.count == 1:
                    # так же как и в предыдущем
                    if Date.robot_do == 0:
                        napravleniya3.add('Робоквантум🤖')
                    if Date.aero_do == 0:
                        napravleniya3.add('Аэроквантум🚁')
                    if Date.bio_do == 0:
                        napravleniya3.add('Биоквантум🔬')
                    if Date.vrar_do == 0:
                        napravleniya3.add('VR/AR-квантум🥽')
                    if Date.promdiz_do == 0:
                        napravleniya3.add('Промдизайнквантум🎨🖌')
                    bot.send_message(callback.message.chat.id, '1/5, хорошее начало, продолжаем!',
                                     reply_markup=napravleniya3)
                    # reply_markup=napravleniya3 - перекидываем пользователя на выбор 1 из 3 направлений
                elif Date.count == 2:
                    # то же самое
                    if Date.robot_do == 0:
                        napravleniya2.add('Робоквантум🤖')
                    if Date.aero_do == 0:
                        napravleniya2.add('Аэроквантум🚁')
                    if Date.bio_do == 0:
                        napravleniya2.add('Биоквантум🔬')
                    if Date.vrar_do == 0:
                        napravleniya2.add('VR/AR-квантум🥽')
                    if Date.promdiz_do == 0:
                        napravleniya2.add('Промдизайнквантум🎨🖌')
                    bot.send_message(callback.message.chat.id, '2/5 GOOD!', reply_markup=napravleniya2)
                # reply_markup=napravleniya2 - перекидываем пользователя на выбор 1 из 2 направлений
                elif Date.count == 3:
                    if Date.robot_do == 0:
                        napravleniya1.add('Робоквантум🤖')
                    if Date.aero_do == 0:
                        napravleniya1.add('Аэроквантум🚁')
                    if Date.bio_do == 0:
                        napravleniya1.add('Биоквантум🔬')
                    if Date.vrar_do == 0:
                        napravleniya1.add('VR/AR-квантум🥽')
                    if Date.promdiz_do == 0:
                        napravleniya1.add('Промдизайнквантум🎨🖌')
                    bot.send_message(callback.message.chat.id, '3/5 Ты близок к концу!', reply_markup=napravleniya1)
                elif Date.count == 4:
                    if Date.robot_do == 0:
                        napravleniya0.add('Робоквантум🤖')
                    if Date.aero_do == 0:
                        napravleniya0.add('Аэроквантум🚁')
                    if Date.bio_do == 0:
                        napravleniya0.add('Биоквантум🔬')
                    if Date.vrar_do == 0:
                        napravleniya0.add('VR/AR-квантум🥽')
                    if Date.promdiz_do == 0:
                        napravleniya0.add('Промдизайнквантум🎨🖌')
                    bot.send_message(callback.message.chat.id, '4/5 75% выполнено! Остался последний!',
                                     reply_markup=napravleniya0)


    # РОБОКВАНТУМ - НАЧАЛО
    elif callback.data == 'robkvdoor':
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Дверь открыта! *звуки открытия двери*')
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
        rb1 = bot.send_message(callback.message.chat.id, '`Здесь вам не LEGO, а более сложная робототехника!\n'
                                                         'Всё начинается с не очень сложных машинок, каких-либо устройств, которые можно программировать, для выполнения задач.\n'
                                                         'Проще говоря робоквантум – это углублённое изучение роботостроения, программирования.\n'
                                                         'Но всё же, иногда, если желания что-либо собирать нет, а есть желание только программировать, то you are WELCOME!\n'
                                                         'Программируй сколько хочешь!\n'
                                                         'У нас уже есть готовые роботы, нуждающиеся в программном коде для их работы.\n'
                                                         'Это тоже очень интересно и увлекательно!`\n'
                                                         '*Учебных часа в программе: 72\n'
                                                         'Возрастная категория: 12+\n'
                                                         'Количество обучающихся в группе: 12*', parse_mode='MarkDown')
        time.sleep(55)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb1.id)
        rb2 = bot.send_message(callback.message.chat.id, '_И так, давайте же пройдём_ *тест!*', parse_mode='MarkDown')
        time.sleep(5)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb2.id)
        bot.send_message(callback.message.chat.id, '*№1* _Робоквантум это..._', parse_mode='MarkDown',
                         reply_markup=robokvantquestkeyboard1_2)
    # РОБОКВАНТУМ - ВОПРОС 1
    elif callback.data == 'robokv_quest1_2_correct':
        rb3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb3.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _А если я не хочу собирать роботов, а только программировать, то что мне делать?_',
                         parse_mode='MarkDown', reply_markup=robokvantquestkeyboard2_2)
        Date.robot_correct += 1
    # РОБОКВАНТУМ - ВОПРОС 2
    elif callback.data == 'robokv_quest2_2_correct':
        rb3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb3.id)
        bot.send_message(callback.message.chat.id, '*№3* _Какое количество обучающихся может быть в группе?_',
                         parse_mode='MarkDown', reply_markup=robokvantquestkeyboard3_2)
        Date.robot_correct += 1
    # РОБОКВАНТУМ - ВОПРОС 3
    elif callback.data == 'robokv_quest3_2_correct':
        rb3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb3.id)
        bot.send_message(callback.message.chat.id, '*№4* _С чего всё начинается?_', parse_mode='MarkDown',
                         reply_markup=robokvantquestkeyboard4_2)
        Date.robot_correct += 1
    # РОБОКВАНТУМ - ВОПРОС 4
    elif callback.data == 'robokv_quest4_2_correct':
        rb3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        Date.robot_do += 1
        Date.count += 1
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=rb3.id)
        bot.send_message(callback.message.chat.id, '*Поздравляю!*\n_Весь тест по отделу "Робоквантум🤖" пройдён!_',
                         parse_mode='MarkDown', reply_markup=contin)
        Date.robot_correct += 1

    # АЭРОКВАНТУМ - НАЧАЛО
    elif callback.data == 'aerokvdoor':
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Дверь открыта! *звуки открытия двери*')
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
        aer1 = bot.send_message(callback.message.chat.id,
                                '`Аэроквантум – это не просто квадрокоптеры, самолёты и вертолёты, а целый курс, посвящённый авиапромышленности!\n'
                                'Сегодня летающие роботы помогают человеку в различных сферах начиная от доставки и заканчивая спасением людей.\n'
                                'Здесь ребята знакомятся с основными частями беспилотника, осваивают принципы работы и управления мультикоптера,\n'
                                'получают навыки проектирования собственных аппаратов.\n'
                                'В Аэроквантуме обучающиеся пройдут все этапы жизненного цикла выпуска летательного аппарата, узнают, что такое квадрокоптер,\n'
                                'самолёт и вертолет, научатся выбирать оптимальные варианты для доставки грузов, организовывать воздушное движение,\n'
                                'проводить автономные полеты и внедрять инновационные технологии в авиапромышленность.\n'
                                'Если ты хочешь научиться делать таких роботов, делать их полезными и применять их не только в аэрофотосъемке, то это направление тебе подойдёт точно!\n`'
                                '*Учебных часа в программе: 72\n'
                                'Возрастная категория: 12+\n'
                                'Количество обучающихся в группе: 12-14*', parse_mode='MarkDown')
        time.sleep(65)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer1.id)
        aer2 = bot.send_message(callback.message.chat.id, '_И так, давайте же пройдём_ *тест!*', parse_mode='MarkDown')
        time.sleep(5)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer2.id)
        bot.send_message(callback.message.chat.id, '*№1* _Аэроквантум это..._', parse_mode='MarkDown',
                         reply_markup=aerokvantquestkeyboard1_2)
    # АЭРОКВАНТУМ - ВОПРОС 1
    elif callback.data == 'aerokv_quest1_2_correct':
        aer3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer3.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _Сколько всего учебных часов в программе?_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard2_2)
        Date.aero_correct += 1
    # АЭРОКВАНТУМ - ВОПРОС 2
    elif callback.data == 'aerokv_quest2_2_correct':
        aer3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer3.id)
        bot.send_message(callback.message.chat.id,
                         '*№3* _Умеют ли летающие роботы помогать человеку??_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard3_2)
        Date.aero_correct += 1
    # АЭРОКВАНТУМ - ВОПРОС 3
    elif callback.data == 'aerokv_quest3_2_correct':
        aer3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer3.id)
        bot.send_message(callback.message.chat.id,
                         '*№4* _Этапы какого жизненного цикла пройдут обучающиеся?_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard4_2)
        Date.aero_correct += 1
    # АЭРОКВАНТУМ - ВОПРОС 4
    elif callback.data == 'aerokv_quest4_2_correct':
        aer3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        Date.aero_do += 1
        Date.count += 1
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=aer3.id)
        bot.send_message(callback.message.chat.id, '*Поздравляю!*\n_Весь тест по отделу "Аэроквантум🚁" пройдён!_',
                         parse_mode='MarkDown', reply_markup=contin)
        Date.aero_correct += 1

    # БИОКВАНТУМ - НАЧАЛО
    elif callback.data == 'biokvdoor':
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Дверь открыта! *звуки открытия двери*')
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
        bio1 = bot.send_message(callback.message.chat.id,
                                '`Биоквантум – это как урок биологии, только круче!\n'
                                'Здесь много новых технологий для исследований.\n'
                                'Обучающиеся смогут приобщаться к новейшим достижениям в области биологии и биотехнологии, почувствовать себя биологами-инженерами,\n'
                                'работающими в современной лаборатории.\n'
                                'Освоят основы генной инженерии, микробиологии и микроклонального размножения растений,\n'
                                'научаться работать с микроскопами, лабораторной посудой, реактивами.\n'
                                'Будут изучать биотехнологию в экологии и агропромышленности.\n'
                                'Разработают проекты в сфере биологии и экологии.`\n'
                                '*Учебных часа в программе: 72\n'
                                'Возрастная категория: 15+\n'
                                'Количество обучающихся в группе: 15*',
                                parse_mode='MarkDown')
        time.sleep(55)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio1.id)
        bio2 = bot.send_message(callback.message.chat.id, '_И так, давайте же пройдём_ *тест!*', parse_mode='MarkDown')
        time.sleep(5)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio2.id)
        bot.send_message(callback.message.chat.id, '*№1* _Биоквантум это..._', parse_mode='MarkDown',
                         reply_markup=biokvantquestkeyboard1_2)
    # БИОКВАНТУМ - ВОПРОС 1
    elif callback.data == 'biokv_quest1_2_correct':
        bio3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio3.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _Обучающие смогут приобщаться к ... в области биологии_',
                         parse_mode='MarkDown', reply_markup=biokvantquestkeyboard2_2)
        Date.bio_correct += 1
    # БИОКВАНТУМ - ВОПРОС 2
    elif callback.data == 'biokv_quest2_2_correct':
        bio3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio3.id)
        bot.send_message(callback.message.chat.id,
                         '*№3* _Основы чего смогут освоить учащиеся?_',
                         parse_mode='MarkDown', reply_markup=biokvantquestkeyboard3_2)
        Date.bio_correct += 1
    # БИОКВАНТУМ - ВОПРОС 3
    elif callback.data == 'biokv_quest3_2_correct':
        bio3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio3.id)
        bot.send_message(callback.message.chat.id,
                         '*№4* _Какова возрастная категория обучающихся?_',
                         parse_mode='MarkDown', reply_markup=biokvantquestkeyboard4_2)
        Date.bio_correct += 1
    # БИОКВАНТУМ - ВОПРОС 4
    elif callback.data == 'biokv_quest4_2_correct':
        bio3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        Date.bio_do += 1
        Date.count += 1
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=bio3.id)
        bot.send_message(callback.message.chat.id, '*Поздравляю!*\n_Весь тест по отделу "Биоквантум🔬" пройдён!_',
                         parse_mode='MarkDown', reply_markup=contin)
        Date.bio_correct += 1

    # VR/AR-КВАНТУМ - НАЧАЛО
    elif callback.data == 'vrardoor':
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Дверь открыта! *звуки открытия двери*')
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
        vrar1 = bot.send_message(callback.message.chat.id,
                                 '`На занятиях, преподаватели с ребятами создают различные приложения в\n'
                                 'формате виртуальной или дополненной реальности,\n'
                                 'учатся конструировать здания и сооружения в программных 3-D комплексах,\n'
                                 'а ещё создают свои собственные виртуальные игры!\n'
                                 'Особое внимание уделяется командной работе и проектной деятельности учащихся,\n'
                                 'а также развитию личностного потенциала и эмоционального интеллекта.`\n'
                                 '*Учебных часа в программе: 72\n'
                                 'Возрастная категория: 12+\n'
                                 'Количество обучающихся в группе: 10-15*',
                                 parse_mode='MarkDown')
        time.sleep(40)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar1.id)
        vrar2 = bot.send_message(callback.message.chat.id, '_И так, давайте же пройдём_ *тест!*', parse_mode='MarkDown')
        time.sleep(5)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar2.id)
        bot.send_message(callback.message.chat.id, '*№1* _VR/AR-квантум посвящён..._', parse_mode='MarkDown',
                         reply_markup=vrarkvantquestkeyboard1_2)
    # VR/AR-КВАНТУМ - ВОПРОС 1
    elif callback.data == 'vrarkv_quest1_2_correct':
        vrar3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar3.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _На занятиях, преподаватели с ребятами учатся конструировать ... и сооружения._',
                         parse_mode='MarkDown', reply_markup=vrarkvantquestkeyboard2_2)

        Date.vrar_correct += 1
    # VR/AR-КВАНТУМ - ВОПРОС 2
    elif callback.data == 'vrarkv_quest2_2_correct':
        vrar3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar3.id)
        bot.send_message(callback.message.chat.id,
                         '*№3* _Чему уделяется особое внимание?_',
                         parse_mode='MarkDown', reply_markup=vrarkvantquestkeyboard3_2)
        Date.vrar_correct += 1
    # VR/AR-КВАНТУМ - ВОПРОС 3
    elif callback.data == 'vrarkv_quest3_2_correct':
        vrar3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar3.id)
        bot.send_message(callback.message.chat.id,
                         '*№4* _Какова возрастная категория обучающихся?_',
                         parse_mode='MarkDown', reply_markup=vrarkvantquestkeyboard4_2)
        Date.vrar_correct += 1
    # VR/AR-КВАНТУМ - ВОПРОС 4
    elif callback.data == 'vrarkv_quest4_2_correct':
        vrar3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Верно!')
        Date.vrar_do += 1
        Date.count += 1
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=vrar3.id)
        bot.send_message(callback.message.chat.id, '*Поздравляю!*\n_Тест по отделу "VR/AR-квантум🥽" пройден!_',
                         parse_mode='MarkDown', reply_markup=contin)
        Date.vrar_correct += 1

    # ПРОМДИЗАЙНКВАНТУМ - НАЧАЛО
    elif callback.data == 'promdizdoor':
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Дверь открыта! *звуки открытия двери*')
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
        promdiz1 = bot.send_message(callback.message.chat.id,
                                    '`Промдизайнквантум – это почти как урок ИЗО, но не простой и более высокого уровня.\n'
                                    'Сама расшифровка названия уже всё говорит: промышленный дизайн - профессиональная разработка изделий,\n'
                                    'устройств и услуг с особым вниманием к внешнему виду и функциональности.\n'
                                    'Во время обучения учащиеся овладеют навыками дизайнерского скетчинга (или создания эскизов),\n'
                                    'макетирования (из бумаги, картона, скульптурного пластилина, подручных средств), создания действующих прототипов.\n'
                                    'Научатся решать сложные проблемы и предлагать функциональные и красивые их решения.\n'
                                    'Занятия по промышленному дизайну!\n'
                                    'Здесь ты научишься работать в различных графических программах для 3-D и 2-D моделирования,\n'
                                    'а свои оригинальные идеи сможешь смоделировать и воплотить в реальность!\n'
                                    'Так что приходи, будет интересно!`\n'
                                    '*Учебных часа в программе: 72\n'
                                    'Возрастная категория: 12+\n'
                                    'Количество обучающихся в группе: 15*',
                                    parse_mode='MarkDown')
        time.sleep(65)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz1.id)
        promdiz2 = bot.send_message(callback.message.chat.id, '_И так, давайте же приступать к_ *тесту!*',
                                    parse_mode='MarkDown')
        time.sleep(5)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz2.id)
        bot.send_message(callback.message.chat.id, '*№1* _Промдизайнквантум это..._', parse_mode='MarkDown',
                         reply_markup=promdizkvantquestkeyboard1_2)
    # ПРОМДИЗАЙНКВАНТУМ - ВОПРОС 1
    elif callback.data == 'promdizkv_quest1_2_correct':
        promdiz3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                         text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz3.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _Во время обучения учащиеся овладеют навыками..._',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard2_2)
        Date.promdiz_correct += 1
    # ПРОМДИЗАЙНКВАНТУМ - ВОПРОС 2
    elif callback.data == 'promdizkv_quest2_2_correct':
        promdiz3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                         text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz3.id)
        bot.send_message(callback.message.chat.id,
                         '*№3* _Научатся решать сложные проблемы и..._',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard3_2)
        Date.promdiz_correct += 1
    # ПРОМДИЗАЙНКВАНТУМ - ВОПРОС 3
    elif callback.data == 'promdizkv_quest3_2_correct':
        promdiz3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                         text='Верно!')
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz3.id)
        bot.send_message(callback.message.chat.id,
                         '*№4* _Какова возрастная категория обучающихся?_',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard4_2)
        Date.promdiz_correct += 1
    # ПРОМДИЗАЙНКВАНТУМ - ВОПРОС 4
    elif callback.data == 'promdizkv_quest4_2_correct':
        promdiz3 = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,
                                         text='Верно!')
        Date.promdiz_do += 1
        Date.count += 1
        time.sleep(3)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=promdiz3.id)
        bot.send_message(callback.message.chat.id, '*Поздравляю!*\n_Тест  по отделу "Промдизайнквантум🎨🖌" пройден!_',
                         parse_mode='MarkDown', reply_markup=contin)
        Date.promdiz_correct += 1

    # НЕПРАВИЛЬНЫЕ ОТВЕТЫ
    elif callback.data == 'Uncorrect_robokv1_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.robot_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неправильно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _А если я не хочу собирать роботов, а только программировать, то что мне делать?_',
                         parse_mode='MarkDown', reply_markup=robokvantquestkeyboard2_2)
    elif callback.data == 'Uncorrect_robokv2_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.robot_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№3* _Какое количество обучающихся может быть в группе?_',
                         parse_mode='MarkDown', reply_markup=robokvantquestkeyboard3_2)
    elif callback.data == 'Uncorrect_robokv3_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.robot_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№4* _С чего всё начинается?_', parse_mode='MarkDown',
                         reply_markup=robokvantquestkeyboard4_2)
    elif callback.data == 'Uncorrect_robokv4_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.robot_fail += 1
        notcorrect(callback)
        Date.robot_do += 1
        Date.count += 1
        bot.send_message(callback.message.chat.id, 'Ответ не верный!', reply_markup=contin)

    elif callback.data == 'Uncorrect_aerokv1_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.aero_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Стоит подумать!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№2* _Сколько всего учебных часов в программе?_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard2_2)
    elif callback.data == 'Uncorrect_aerokv2_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.aero_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№3* _Умеют ли летающие роботы помогать человеку?_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard3_2)
    elif callback.data == 'Uncorrect_aerokv3_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.aero_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неправильно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№4* _Этапы какого жизненного цикла пройдут обучающиеся?_',
                         parse_mode='MarkDown', reply_markup=aerokvantquestkeyboard4_2)
    elif callback.data == 'Uncorrect_aerokv4_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.aero_fail += 1
        notcorrect(callback)
        Date.aero_do += 1
        Date.count += 1
        bot.send_message(callback.message.chat.id, 'Неверно!', reply_markup=contin)

    elif callback.data == 'Uncorrect_biokv1_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неправильно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№2* _Обучающие смогут приобщаться к ... в области биологии._',
                         parse_mode='MarkDown', reply_markup=biokvantquestkeyboard2_2)
    elif callback.data == 'Uncorrect_biokv2_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№3* _Основы чего смогут освоить учащиеся?_', parse_mode='MarkDown',
                         reply_markup=biokvantquestkeyboard3_2)
    elif callback.data == 'Uncorrect_biokv3_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Ответ не правильный!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№4* _Какова возрастная категория обучающихся_',
                         parse_mode='MarkDown', reply_markup=biokvantquestkeyboard4_2)
    elif callback.data == 'Uncorrect_biokv4_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        Date.bio_do += 1
        Date.count += 1
        bot.send_message(callback.message.chat.id, 'Неверно!', reply_markup=contin)

    elif callback.data == 'Uncorrect_vrar1_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id,
                         '*№2* _На занятиях, преподаватели с ребятами учатся конструировать ... и сооружения._',
                         parse_mode='MarkDown', reply_markup=vrarkvantquestkeyboard2_2)
    elif callback.data == 'Uncorrect_vrar2_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Не верно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№3* _Чему уделяется особое внимание?_', parse_mode='MarkDown',
                         reply_markup=vrarkvantquestkeyboard3_2)
    elif callback.data == 'Uncorrect_vrar3_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Никак нет!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№4* _Какова возрастная категория обучающихся?_',
                         parse_mode='MarkDown', reply_markup=vrarkvantquestkeyboard4_2)
    elif callback.data == 'Uncorrect_vrar4_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.bio_fail += 1
        notcorrect(callback)
        Date.vrar_do += 1
        Date.count += 1
        bot.send_message(callback.message.chat.id, 'Неверно!', reply_markup=contin)

    elif callback.data == 'Uncorrect_promdiz1_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.promdiz_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Стоит подумать!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№2* _Во время обучения учащиеся овладеют навыками..._',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard2_2)
    elif callback.data == 'Uncorrect_promdiz2_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.promdiz_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Неверно!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№3* _Научатся решать сложные проблемы и..._',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard3_2)
    elif callback.data == 'Uncorrect_promdiz3_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.promdiz_fail += 1
        notcorrect(callback)
        dele = bot.send_message(callback.message.chat.id, 'Что?!')
        time.sleep(5)
        bot.delete_message(callback.message.chat.id, dele.id)
        bot.send_message(callback.message.chat.id, '*№4* _Какова возрастная категория обучающихся?_',
                         parse_mode='MarkDown', reply_markup=promdizkvantquestkeyboard4_2)
    elif callback.data == 'Uncorrect_promdiz4_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        Date.promdiz_fail += 1
        notcorrect(callback)
        Date.promdiz_do += 1
        Date.count += 1
        bot.send_message(callback.message.chat.id, 'Неверно!', reply_markup=contin)


# обрабатываем текст
@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == 'Автор🕶':
        develop = open(r'img\dev.jpg', 'rb')
        dev = bot.send_photo(message.chat.id, develop, '_Telegram Bot was created and configured by_ __*@Pasha33Pro*__',
                             parse_mode='MarkDownV2', reply_markup=startkeyboard).message_id
        develop.close()
        bot.pin_chat_message(message.chat.id, dev)
    elif message.text == 'Начать▶️️':
        bot.delete_message(message.chat.id, message.message_id)
        txt0 = bot.send_message(message.chat.id,
                                'Добро пожаловать в игру\!\n'
                                '`Это квест-игра "Кванториум"\!`\n'
                                '__Игра была написана на базе Telegram Bot на Python\!__',
                                parse_mode='MarkDownV2', reply_markup=types.ReplyKeyboardRemove())
        # reply_markup=types.ReplyKeyboardRemove() - убираем клавиатуру, чтобы предотвратить возможные БАГИ
        time.sleep(15)
        bot.delete_message(message.chat.id, txt0.id)
        txt1 = bot.send_message(message.chat.id,
                                '*Читай всё очень внимательно*\!\n_Ведь текст может пропасть прямо на глазах_\!',
                                parse_mode='MarkDownV2')
        time.sleep(8)
        bot.delete_message(message.chat.id, txt1.id)
        txt2 = bot.send_message(message.chat.id, '*Или может замениться ~другим~\!*', parse_mode='MarkDownV2')
        time.sleep(5)
        bot.delete_message(message.chat.id, txt2.id)
        txt3 = bot.send_message(message.chat.id, f'||А может даже стать невидимым\!||', parse_mode='MarkDownV2')
        time.sleep(6)
        bot.delete_message(message.chat.id, txt3.id)
        txt4 = bot.send_message(message.chat.id,
                                '_Так что ~настоятельно~_ __рекомендую__ *читать всё* ||предельно|| *внимательно*\!',
                                parse_mode='MarkDownV2')
        time.sleep(8)
        bot.delete_message(message.chat.id, txt4.id)
        what = bot.send_message(message.chat.id, '*__Небольшое пояснение:__*\n'
                                                 '*Тактика боя \- * _реализована в формате_ *||тестов с баллами||*\!\n'
                                                 '*Взаимодействие с объектами \- * _в виде_ *||"открытия" дверей||*\.',
                                parse_mode='MarkDownV2').message_id
        bot.pin_chat_message(message.chat.id, what)
        time.sleep(14)
        bot.send_message(message.chat.id, 'Ну что, начинаем?', reply_markup=starting7)
    elif message.text == 'Робоквантум🤖':
        bot.delete_message(message.chat.id, message.message_id)
        robokv = open(r'img\Kvant-robo.png', 'rb')
        robokvant = bot.send_photo(message.chat.id, robokv, '*Робоквантум🤖*\n'
                                                            '_В Робоквантуме обучающиеся погрузятся в такие научные и инженерные дисциплины как механика, электроника, электротехника, физика, информатика, математическое моделирование и др.\n'
                                                            'Проектная деятельность, направленная на создание интеллектуальных систем для различных сфер человеческой деятельности, в частности производства,\n'
                                                            'позволяет формировать системное мышление как в инженерном, так и в мировоззренческом смысле._',
                                   parse_mode='MarkDown', reply_markup=types.ReplyKeyboardRemove()).message_id
        robokv.close()
        bot.pin_chat_message(message.chat.id, robokvant)
        time.sleep(30)
        bot.send_message(message.chat.id,
                         '_И так, мы подошли к отделу под название_ *«Робоквантум»*_!\n'
                         'Сейчас вам все расскажут и покажут, а под конец вам потребуется пройти тест для дальнейшего прохождения._',
                         parse_mode='MarkDown', reply_markup=robokvantkeyboard)
    elif message.text == 'Аэроквантум🚁':
        bot.delete_message(message.chat.id, message.message_id)
        aerokv = open('img\Kvant-aero.png', 'rb')
        aerokvant = bot.send_photo(message.chat.id, aerokv, '*Аэроквантум🚁*\n'
                                                            '_В Аэроквантуме обучающиеся пройдут все этапы жизненного цикла выпуска летательного аппарата, узнают, что такое квадрокоптер, самолет и вертолет,\n'
                                                            'научатся выбирать оптимальные варианты для доставки грузов, организовывать воздушное движение,\n'
                                                            'проводить автономные полеты и внедрять инновационные технологии в авиапромышленность._',
                                   parse_mode='MarkDown', reply_markup=types.ReplyKeyboardRemove()).message_id
        aerokv.close()
        bot.pin_chat_message(message.chat.id, aerokvant)
        time.sleep(25)
        bot.send_message(message.chat.id,
                         '_И так, мы подошли к отделу под название_ *«Аэроквантум»*_!\n'
                         'Сейчас вам все расскажут и покажут, а под конец вам потребуется пройти тест для дальнейшего прохождения._',
                         parse_mode='MarkDown', reply_markup=aerokvantkeyboard)
    elif message.text == 'Биоквантум🔬':
        bot.delete_message(message.chat.id, message.message_id)
        biokv = open('img\Kvant-bio.png', 'rb')
        biokvant = bot.send_photo(message.chat.id, biokv, '*Биоквантум🔬*\n'
                                                          '_В Биоквантуме учащиеся осваивают современные методы изучения биологических объектов,\n'
                                                          'учатся работать на современном оборудовании в условиях\n'
                                                          'биологических лабораторий и живой природы._',
                                  parse_mode='MarkDown', reply_markup=types.ReplyKeyboardRemove()).message_id
        biokv.close()
        bot.pin_chat_message(message.chat.id, biokvant)
        time.sleep(30)
        bot.send_message(message.chat.id,
                         '_И так, мы подошли к отделу под название_ *«Биоквантум»*_!\n'
                         'Сейчас вам все расскажут и покажут, а под конец вам потребуется пройти тест для дальнейшего прохождения._',
                         parse_mode='MarkDown', reply_markup=biokvantkeyboard)
    elif message.text == 'VR/AR-квантум🥽':
        bot.delete_message(message.chat.id, message.message_id)
        vrar = open(r'img\Kvant-vr.ar.png', 'rb')
        vrarkvant = bot.send_photo(message.chat.id, vrar, '*VR/AR-квантум🥽:*\n'
                                                          '_В VR/AR-квантуме обучающиеся осваивают объемную визуализацию, работают с виртуальной (VR), дополненной (AR) и смешанной (MR) реальностью.\n'
                                                          'Учащиеся разрабатывают образовательные приложения, проектируют симуляторы для будущих инженеров,\n'
                                                          'проводят виртуальные туры по культурным и историческим достопримечательностям и др._',
                                   parse_mode='MarkDown', reply_markup=types.ReplyKeyboardRemove()).message_id
        vrar.close()
        bot.pin_chat_message(message.chat.id, vrarkvant)
        time.sleep(30)
        bot.send_message(message.chat.id,
                         '_И так, мы подошли к отделу под название_ *«VR/AR-квантум»*_!\n'
                         'Сейчас вам все расскажут и покажут, а под конец вам потребуется пройти тест для дальнейшего прохождения._',
                         parse_mode='MarkDown', reply_markup=vrarkvantkeyboard)
    elif message.text == 'Промдизайнквантум🎨🖌':
        bot.delete_message(message.chat.id, message.message_id)
        promdiz = open(r'img\Kvant-dizain.png', 'rb')
        promdizkvant = bot.send_photo(message.chat.id, promdiz, '*Промдизайнквантум🎨🖌*\n'
                                                                '_В Промдизайнквантуме обучающиеся учатся проектировать окружающий предметный мир и взаимодействие с ним, работать на стыке инженерии и искусства,\n'
                                                                'решать прикладные задачи и формировать новое восприятие, соединять технологичность и эстетичность в одном изделии._',
                                      parse_mode='MarkDown', reply_markup=types.ReplyKeyboardRemove()).message_id
        promdiz.close()
        bot.pin_chat_message(message.chat.id, promdizkvant)
        time.sleep(25)
        bot.send_message(message.chat.id,
                         '_И так, мы подошли к отделу под название_ *«Промдизайнквантум»*_!\n'
                         'Сейчас вам все расскажут и покажут, а под конец вам потребуется пройти тест для дальнейшего прохождения._',
                         parse_mode='MarkDown', reply_markup=promdizkvantkeyboard)
    # Концовка
    elif message.text == 'Конец🏁':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '_Мы надеемся, что, занимаясь в кванториуме,\n'
                                          'вы найдёте много новых друзей,\n'
                                          'придумаете интересные проекты,\n'
                                          'поучаствуете в различных мероприятиях,\n'
                                          'получите возможность посетить действующие предприятия,\n'
                                          'пообщаетесь с экспертами, учёными,\n'
                                          'различными выдающимися людьми нашей области и страны\._\n'
                                          '__*Желаем вам удачи и успехов*__\!',
                         parse_mode='MarkDownV2', reply_markup=types.ReplyKeyboardRemove())
        time.sleep(25)
        robot = Date.robot_correct - Date.robot_fail
        aero = Date.aero_correct - Date.aero_fail
        bio = Date.bio_correct - Date.bio_fail
        vrar = Date.vrar_correct - Date.vrar_fail
        promdiz = Date.promdiz_correct - Date.promdiz_fail
        Date.place = robot + aero + bio + vrar + promdiz
        # Смотрим сколько раз правильно ответил
        if Date.place == 1:
            bot.send_message(message.chat.id, f'📋По итогу игры, вы ответили правильно: {Date.place} раз.❌')
            bot.send_message(message.chat.id, f'Но вы всё равно получаете грамоту!🏆\n'
                                              'За участие! Благодарю вас!💥')
        if 1 < Date.place < 5:
            bot.send_message(message.chat.id, f'📋По итогу игры, вы ответили правильно: {Date.place} раза.❌')
            bot.send_message(message.chat.id, f'Но вы всё равно получаете грамоту!🏆\n'
                                              'За участие! Благодарю вас!💥')
        if Date.place > 4:
            if Date.place == 20:
                bot.send_message(message.chat.id, f'📋По итогу игры, вы ответили правильно: {Date.place} раз!✅')
                bot.send_message(message.chat.id, 'ЭТО УСПЕХ!')
                bot.send_message(message.chat.id, 'Вы занимаете 1 место!')
                bot.send_message(message.chat.id, 'Вы получаете грамоту!🏆\n'
                                                  'За участие! Благодарю вас!💥')
            else:
                bot.send_message(message.chat.id, f'📋По итогу игры, вы ответили правильно: {Date.place} раз.❌')
                bot.send_message(message.chat.id, f'Но вы всё равно получаете грамоту!🏆\n'
                                                  'За участие! Благодарю вас!💥')
        # Проверяем и выводим место, которое занял
        if Date.place == 0 or Date.place == 1 or Date.place == 2:
            position = 10
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🎗 место из 10 возможных\!*_\n'
                                              f'__Но это тоже результат\!\n'
                                              'Не расстраивайтесь\!__ :\)', parse_mode='MarkDownV2')
        elif Date.place == 3 or Date.place == 4:
            position = 9
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🎗 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 5 or Date.place == 6:
            position = 8
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🏅 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 7 or Date.place == 8:
            position = 7
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🏅 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 9 or Date.place == 10:
            position = 6
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🏅 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 11 or Date.place == 12:
            position = 5
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🏅 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 13 or Date.place == 14:
            position = 4
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🏅 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 15 or Date.place == 16:
            position = 3
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🥉 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 17 or Date.place == 18:
            position = 2
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🥈 место из 10 возможных\!*_\n'
                                              'Хороший результат\!', parse_mode='MarkDownV2')
        elif Date.place == 19 or Date.place == 20:
            position = 1
            bot.send_message(message.chat.id, f'_*Вы заняли {position}🥇 место из 10 возможных\!*_\n'
                                              '__~*Великолепный результат*~__\!', parse_mode='MarkDownV2')
        ending(message)

    @bot.message_handler(content_types=['text'])
    def cmds():
        pass


def docx_find_replace_text(search_text, replace_text, paragraphs):
    for p in paragraphs:
        if search_text in p.text:
            inline = p.runs
            started = False
            search_index = 0
            # found_runs - список
            found_runs = list()
            found_all = False
            replace_done = False
            for i in range(len(inline)):
                # попытка 1 обнаружен при одиночном запуске, затем замена
                if search_text in inline[i].text and not started:
                    found_runs.append((i, inline[i].text.find(search_text), len(search_text)))
                    text = inline[i].text.replace(search_text, str(replace_text))
                    inline[i].text = text
                    replace_done = True
                    found_all = True
                    break
                if search_text[search_index] not in inline[i].text and not started:
                    # продолжаем поиск
                    continue
                # попытка 2 поиск частичного текста
                if search_text[search_index] in inline[i].text and inline[i].text[-1] in search_text and not started:
                    # check sequence
                    start_index = inline[i].text.find(search_text[search_index])
                    check_length = len(inline[i].text)
                    for text_index in range(start_index, check_length):
                        if inline[i].text[text_index] != search_text[search_index]:
                            # нет совпадения
                            break
                    if search_index == 0:
                        started = True
                    chars_found = check_length - start_index
                    search_index += chars_found
                    found_runs.append((i, start_index, chars_found))
                    if search_index != len(search_text):
                        continue
                    else:
                        # найдены все символы в search_text
                        found_all = True
                        break
                # попытка 2.2 поиск частичного текста
                if search_text[search_index] in inline[i].text and started and not found_all:
                    # последовательность проверки
                    chars_found = 0
                    check_length = len(inline[i].text)
                    for text_index in range(0, check_length):
                        if inline[i].text[text_index] == search_text[search_index]:
                            search_index += 1
                            chars_found += 1
                        else:
                            break
                    # ничего не найдено - конец
                    found_runs.append((i, 0, chars_found))
                    if search_index == len(search_text):
                        found_all = True
                        break
            if found_all and not replace_done:
                for i, item in enumerate(found_runs):
                    index, start, length = [t for t in item]
                    if i == 0:
                        text = inline[index].text.replace(inline[index].text[start:start + length], str(replace_text))
                        inline[index].text = text
                    else:
                        text = inline[index].text.replace(inline[index].text[start:start + length], '')
                        inline[index].text = text


# Рандомный (1 из 3) ответ на неправильный ответ
def notcorrect(callback):
    rand = random.randint(1, 3)
    if rand == 1:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Неверно! Подумай ещё раз!')
    elif rand == 2:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Некорректно! Вспомни что говорили!')
    elif rand == 3:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=True,
                                  text='Ну, а если подумать ещё раз?')


def ending(message):
    bot.send_message(message.chat.id, 'Для получения грамоты, введите свою фамилию и имя!')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Пожалуйста, введите свою фамилию и имя:')
    bot.register_next_step_handler(message, get_end)


def get_end(message):
    pythoncom.CoInitialize()
    name = message.text
    try:
        file_name = str(uuid.uuid4())
        date_today = str(datetime.today().date())
        docx_find_replace_text('ФИ', name, paragraphs)
        docx_find_replace_text('Дата', date_today, paragraphs)
        doc.save(fr'documents\{file_name}.docx')
    finally:
        convert(fr'documents\{file_name}.docx', fr'documents\{file_name}.pdf')
        bot.send_document(chat_id=message.chat.id, document=open(fr'documents\{file_name}.pdf', 'rb'))
        time.sleep(5)
        exit(0)


try:
    bot.polling(none_stop=True, interval=0)
    print('Bot(ok)')
except Exception as e:
    print(f'Bot(error)\n{e}')
