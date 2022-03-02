import telebot
import random
import time
import os
import psycopg2
from datetime import datetime

bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')

DATABASE_URL = os.environ['DATABASE_URL']
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    bot.send_message(841463984, "Подключился/Обновился")
except Exception as e:
    bot.send_message(841463984, f'Ошибка:\n{e}')

ourchatid=-1001139329557
id_otchet_chat=-1001750309280
idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@gikhok'
game_shp_locations=['Футбольное поле', 'Школа', 'Рынок', 'Магазин', 'Площадка', 'Квартира', 'Ферма', 'Лес', 'Парк', 'Озеро', 'Сад', 'Пляж', 'Заброшка', 'Стройка', 'Поляна', 'Аквапарк', 'Лагерь', 'Зоопарк', 'Цум', 'Отель']
ludi=['Даша', 'Лиза', 'Женя', 'Рося']
chel_shpion=0
location_shp=0
my_zastavka="""
============================================================================
============================================================================
"""
commands_all="""
Р - рося
Ж - женя
Д - даша
Л - лиза
ВСЕ - все вместе
——————————————
ОП - отметить пользователя
КВОЖКА - проверка, тут ли бот
ОТПВЧАТ - отправить текст (написанный боту в личном сообщении) после этого слова
УЕБАТЬ, ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ШПИОН СТАРТ///ШПИОН СТОП - начать/закончить игру Шпион
"""
commands_rosya="""
Р - рося
Ж - женя
Д - даша
Л - лиза
ВСЕ - все вместе
——————————————
ОП - отметить пользователя
КВОЖКА - проверка, тут ли бот
ОТПВЧАТ - отправить текст (написанный боту в личном сообщении) после этого слова
УЕБАТЬ, ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ШПИОН СТАРТ///ШПИОН СТОП - начать/закончить игру Шпион
——————————————
*+ - проверка, работает ли бот
(НОЧЬ///УТРО) КВОЖКА - пожелать спокойной ночи/доброго утра
МАПС - (и имя через пробел) отметит человека 3 раза
"""
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я Квожка, вы наверно уже заскучали?')

@bot.message_handler(commands=["commands"])
def commands(m, res=False):
    if m.chat.id == idr:
        bot.send_message(m.chat.id, commands_rosya)
    else:
        bot.send_message(m.chat.id, commands_all)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms_l=message.text.lower()
    new_sms=message.text
    id_chel=message.from_user.id
######################################################
    if new_sms_l[0:2] == 'оп':
        if new_sms_l[2] == 'л':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опл"')
            bot.send_message(ourchatid, nikl)
        elif new_sms_l[2] == 'д':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опд"')
            bot.send_message(ourchatid, nikd)
        elif new_sms_l[2] == 'ж':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опж"')
            bot.send_message(ourchatid, nikg)
        elif new_sms_l[2] == 'р':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опр"')
            bot.send_message(ourchatid, nikr)
        elif new_sms_l[2:5] == 'все':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опвсе"')
            bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}')
    elif new_sms_l == 'квожка':
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "квожка"')
        bot.send_message(message.chat.id, 'Квожка здесь, чё пристали?')
    elif new_sms_l[0:7]=='отпвчат':
        bot.send_message(ourchatid, new_sms[8:])
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "отпвчат"')
        bot.send_message(message.chat.id, 'Отправил ваше сообщение!')
    elif message.text == 'уебать':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "уебать"')
        bot.send_message(ourchatid, f"{name_otprav} уебал(а) {name_poluch}")
    elif message.text == 'полюбить':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "полюбить"')
        bot.send_message(ourchatid, f"{name_otprav} полюбил(а) {name_poluch}")
    elif message.text == 'послать':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "послать"')
        bot.send_message(ourchatid, f"{name_otprav} послал(а) {name_poluch}")
    elif message.text == 'похвалить':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "похвалить"')
        bot.send_message(ourchatid, f"{name_otprav} похвалил(а) {name_poluch}")
    elif message.text == 'обидеться':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "обидеться"')
        bot.send_message(ourchatid, f"{name_otprav} обиделся(ась) на {name_poluch}")
    elif message.text == 'пинг':
        start_time = datetime.now()
        bot.send_message(ourchatid, "Беру ракетку!")
        end_time = datetime.now()
        finish_time = end_time - start_time
        bot.send_message(ourchatid, f'Понг (за {finish_time.total_seconds()} секунд)')
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "пинг"')
######################################################
    elif new_sms == "*+":
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "*+"')
        bot.send_message(message.chat.id, 'Квожка работает!')
    elif new_sms_l[0:11]=='ночь квожка':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "ночь квожка"')
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем спокойной ночи!')
        bot.send_message(idr, 'Пожелал спокойной ночи!')
    elif new_sms_l[0:11]=='утро квожка':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "утро квожка"')
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем доброе утро!')
        bot.send_message(idr, 'Пожелал доброго утра!')
    elif new_sms_l[0:4]=="мапс":
        bot.delete_message(message.chat.id, message.message_id)
        if new_sms_l[5:9]=='лиза':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "мапс лиза"')
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
        if new_sms_l[5:9]=='женя':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "мапс женя"')
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
        if new_sms_l[5:9]=='даша':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "мапс даша"')
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
        if new_sms_l[5:8]=='все':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "мапс все"')
            bot.send_message(ourchatid, f'{nikd} {nikl} {nikg}')
            time.sleep(1)
            bot.send_message(ourchatid, f'{nikd} {nikl} {nikg}')
            time.sleep(1)
            bot.send_message(ourchatid, f'{nikd} {nikl} {nikg}')
            time.sleep(1)
#########################################################
    elif new_sms_l == "шпион старт":
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "шпион старт"')
        game_shp_chel=random.choice(ludi)
        game_shp_locat=random.choice(game_shp_locations)
        global chel_shpion
        chel_shpion=game_shp_chel
        global location_shp
        location_shp=game_shp_locat
        if game_shp_chel=='Даша':
            bot.send_message(idd, 'Вы шпион!')
            bot.send_message(idr, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idl, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idg, f'Локация на игру: {game_shp_locat}')
        if game_shp_chel=='Лиза':
            bot.send_message(idl, 'Вы шпион!')
            bot.send_message(idr, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idd, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idg, f'Локация на игру: {game_shp_locat}')
        if game_shp_chel=='Рося':
            bot.send_message(idr, f'Вы шпион!, {my_zastavka}=={game_shp_locat}')
            bot.send_message(idd, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idl, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idg, f'Локация на игру: {game_shp_locat}')
        if game_shp_chel=='Женя':
            bot.send_message(idg, 'Вы шпион!')
            bot.send_message(idr, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idl, f'Локация на игру: {game_shp_locat}')
            bot.send_message(idd, f'Локация на игру: {game_shp_locat}')
        bot.send_message(ourchatid, 'Игра Шпион начинается. Зайдите в лс бота узнать вашу роль/локацию!')
    elif new_sms_l == "шпион стоп":
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "шпион стоп"')
        bot.send_message(ourchatid, f'Игра Шпион окончена.\nПредателем был(а) {chel_shpion}.\nЛокация называлась {location_shp}')
#########################################################
    elif new_sms_l=='баланс':
        command = f"select balance from kvg_db where id = {id_chel}"
        cur.execute(command)
        balance = cur.fetchone()
        bot.send_message(ourchatid, f"Ваш баланс: {balance}💲")

if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()
