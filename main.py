############################ все модули и импорты
import telebot
import random
import time
import os
import psycopg2
from datetime import datetime
######################################## все подсоединения + мой айди
idr = 841463984
bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')
DATABASE_URL = os.environ['DATABASE_URL']
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    bot.send_message(841463984, "Подключился/Обновился")
except Exception as e:
    bot.send_message(idr, f'Ошибка:\n{e}')
######################################### все переменные
ourchatid1=-1001139329557
ourchatid=-1001681687517
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
random_kefiki=["0", "0", "0", "0", "0", "0", "0", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.5", "0.5", "0.5", "0.5", "0.5", "0.5", "0.5",  "1", "1", "1", "1", "1", "1", "1", "1.25", "1.25", "1.25", "1.25", "1.25", "1.5", "1.5", "1.5", "1.5", "1.5", "2", "2", "2", "2", "5", "5", "5", "10", "10", "100"]
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
——————————————
Для игры (тут типо название будет как придумаем):
БАЛАНС - узнать свой баланс
ПЕРЕВОД[СУММА] - перевести другому пользователю (ответом на сообщение)
КАЗ[СУММА] - поставить в казино ставку размером с сумму
КУБ[ПРОГНОЗ][СУММА] - поставить в кубик ставку размером с сумму с прогнозом(цифрой от 1 до 6)
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
——————————————
Для игры (тут типо название будет как придумаем):
БАЛАНС - узнать свой баланс
ПЕРЕВОД[СУММА] - перевести другому пользователю (ответом на сообщение)
КАЗ[СУММА] - поставить в казино ставку размером с сумму
КУБ[ПРОГНОЗ][СУММА] - поставить в кубик ставку размером с сумму с прогнозом(цифрой от 1 до 6)
"""
########################################### все функции для хендлеров
def kakoy_balans(id_chelika):
    command_kakoy_balans = f"select balance from kvg_db where id = {id_chelika}"
    cur.execute(command_kakoy_balans)
    balans_kakoy_balans = cur.fetchone()
    balans_kakoy_balans = balans_kakoy_balans[0]
    return balans_kakoy_balans
def plus_balans(id_plus_balansa, summa_plus_balansa):
    command_plus_balansa = f"update kvg_db set balance = balance + {summa_plus_balansa} where id = {id_plus_balansa}"
    cur.execute(command_plus_balansa)
    conn.commit()
def minus_balans(id_minus_balansa, summa_minus_balansa):
    command_minus_balansa = f"update kvg_db set balance = balance - {summa_minus_balansa} where id = {id_minus_balansa}"
    cur.execute(command_minus_balansa)
    conn.commit()
############################################# все хендлеры
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
    new_sms=message.text
    new_sms_l=message.text.lower()
    id_chel=message.from_user.id
    id_chat=message.chat.id
### основная часть хендлера
    if new_sms_l[0:2] == 'оп':
        if new_sms_l[2] == 'л':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опл"')
            bot.send_message(id_chat, nikl)
        elif new_sms_l[2] == 'д':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опд"')
            bot.send_message(id_chat, nikd)
        elif new_sms_l[2] == 'ж':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опж"')
            bot.send_message(id_chat, nikg)
        elif new_sms_l[2] == 'р':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опр"')
            bot.send_message(id_chat, nikr)
        elif new_sms_l[2:5] == 'все':
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "опвсе"')
            bot.send_message(id_chat, f'{nikr} {nikd} {nikl} {nikg}')
    elif new_sms_l == 'квожка':
        bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "квожка"')
        bot.send_message(id_chat, 'Квожка здесь, чё пристали?')
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
### скрытые команды хендлера
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
### все для игры в шпиона
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
### все для валютной игры
    elif new_sms_l=='баланс':
        balance = kakoy_balans(id_chel)
        bot.send_message(ourchatid, f"Ваш баланс: {balance}$")
    elif new_sms_l[0:7]=='перевод':
        id_poluch=message.reply_to_message.from_user.id 
        id_otprav=message.from_user.id
        try:
            perevod_summa = int(new_sms[7:])
            balans_perevodimogo = kakoy_balans(id_otprav)
            if balans_perevodimogo>=perevod_summa:
                minus_balans(id_otprav, perevod_summa)
                plus_balans(id_poluch, perevod_summa)
                balans_poluchaemogo = kakoy_balans(id_poluch)
                balans_perevodimogo = kakoy_balans(id_otprav)
                bot.send_message(ourchatid, f"Перевод выполнен успешно!\nБаланс получателя: {balans_poluchaemogo}$\nВаш баланс: {balans_perevodimogo}$")
            else:
                bot.send_message(ourchatid, "На вашем балансе недостаточно средств!")
        except:
            bot.send_message(id_chat, "Что-то пошло не так. Попробуйте заново")
    elif new_sms_l[0:4]=="банк" and id_chel==idr:
        id_poluch=message.reply_to_message.from_user.id 
        try:
            perevod_summa = new_sms[4:]            
            command = f"update kvg_db set balance = balance {perevod_summa} where id = {id_poluch}"
            cur.execute(command)
            conn.commit()
            bot.send_message(id_chat, "Операция выполнена успешно!")
        except:
            bot.send_message(id_chat, "Что-то пошло не так. Попробуйте заново")
    elif new_sms_l[0:3]=="каз":
        random_kef=random.choice(random_kefiki)
        try:
            igr_kazik_summa = int(new_sms[3:])
            balans_igr_vkazik = kakoy_balans(id_chel)
            if balans_igr_vkazik>=igr_kazik_summa:
                minus_balans(id_chel, igr_kazik_summa)
                new_igr_kazik_summa=igr_kazik_summa*(float(random_kef))
                plus_balans(id_chel, new_igr_kazik_summa)
                balans_igr_vkazik = kakoy_balans(id_chel)
                bot.send_message(id_chat, f"Казино: {random_kef}\nВаш баланс: {balans_igr_vkazik}$")
            else:
                bot.send_message(id_chat, "На вашем балансе недостаточно средств!")
        except:
            bot.send_message(id_chat, "Что-то пошло не так. Попробуйте заново")
    elif new_sms_l[0:3]=="куб":
        random_cifra = random.randint(1,6)
        try:
            igr_kubick_cifra = int(new_sms[3])
            igr_kubick_summa = int(new_sms[4:])
            balans_igr_vkubick = kakoy_balans(id_chel)
            if balans_igr_vkubick>=igr_kubick_summa:
                minus_balans(id_chel, igr_kubick_summa)
                new_igr_kubick_summa=igr_kubick_summa*6
                if igr_kubick_cifra==random_cifra:
                    plus_balans(id_chel, new_igr_kubick_summa)
                balans_igr_vkubick = kakoy_balans(id_chel)
                bot.send_message(id_chat, f"Кубик: {random_cifra}\nВаш баланс: {balans_igr_vkubick}$")
            else:
                bot.send_message(id_chat, "На вашем балансе недостаточно средств!")
        except:
            bot.send_message(id_chat, "Что-то пошло не так. Попробуйте заново")
    elif new_sms_l=="всебалы":
        command1= f"select name, balance from kvg_db"
        cur.execute(command1)
        namebalance = cur.fetchall()
        for el in namebalance:
            bot.send_message(id_chat, el[0])
        
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()