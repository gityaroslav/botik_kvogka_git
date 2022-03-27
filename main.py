############################ все модули и импорты1
import telebot
import random
import time
import os
import psycopg2 #
from datetime import datetime
######################################## все подсоединения + мой айди
idr = 841463984
is_kvogka_rabotaet=""
bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')
DATABASE_URL = os.environ['DATABASE_URL']
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    bot.send_message(idr, "Подключился/Обновился")
    cur.execute("select key from names_keys where name = 'is_kvogka_rabotaet'")
    is_kvogka_rabotaet = cur.fetchone()
except Exception as e:
    bot.send_message(idr, f'Ошибка:\n{e}')
######################################### все переменные
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
niki_ludishek=[idg, idd, idl, idr, 1039315228, 1230762892]
nashi_ludishki=["Ника", "Рося", "Женя", "Поля", "Лиза", "Даша"]
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
КВОЖКА - проверка, тут ли бот
ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ПИНГ - измерить скорость ответа бота
——————————————
Для игры "Валютка":
БАЛАНС(или БАЛ) - узнать свой баланс
ПЕРЕВОД[СУММА](или СВОП[СУММА])- перевести другому пользователю (ответом на сообщение)
КАЗ[СУММА] - поставить в казино ставку размером с сумму
КУБ[ПРОГНОЗ][СУММА] - поставить в кубик ставку размером с сумму с прогнозом(цифрой от 1 до 6)
КУРС - посмотреть курс продажи/скупки валюты
"""
commands_ludishki="""
Р - рося
Ж - женя
Д - даша
Л - лиза
ВСЕ - все вместе
——————————————
ОП - отметить пользователя
КВОЖКА - проверка, тут ли бот
ОТПВЧАТ - отправить текст (написанный боту в личном сообщении) после этого слова
ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ШПИОН СТАРТ///ШПИОН СТОП - начать/закончить игру Шпион
ПИНГ - измерить скорость ответа бота
——————————————
Для игры "Валютка":
БАЛАНС(или БАЛ) - узнать свой баланс
ПЕРЕВОД[СУММА](или СВОП[СУММА])- перевести другому пользователю (ответом на сообщение)
КАЗ[СУММА] - поставить в казино ставку размером с сумму
КУБ[ПРОГНОЗ][СУММА] - поставить в кубик ставку размером с сумму с прогнозом(цифрой от 1 до 6)
ВСЕБАЛЫ - посмотреть балансы наших
КУРС - посмотреть курс продажи/скупки валюты
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
ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ШПИОН СТАРТ///ШПИОН СТОП - начать/закончить игру Шпион
ПИНГ - измерить скорость ответа бота
——————————————
*+ - проверка, работает ли бот
(НОЧЬ///УТРО) КВОЖКА - пожелать спокойной ночи/доброго утра
СПАМ - (и имя через пробел) отметит человека 3 раза
КВОЖКА СКАЖИ АЙДИ - скажет айди пользователя(ответом на сообщение)
КВОЖКА Я ВКЛЮЧАЮ/ВЫКЛЮЧАЮ ТЕБЯ - включить/выключить бота
——————————————
Для игры "Валютка":
БАЛАНС(или БАЛ) - узнать свой баланс
ПЕРЕВОД[СУММА](или СВОП[СУММА])- перевести другому пользователю (ответом на сообщение)
КАЗ[СУММА] - поставить в казино ставку размером с сумму
КУБ[ПРОГНОЗ][СУММА] - поставить в кубик ставку размером с сумму с прогнозом(цифрой от 1 до 6)
ВСЕБАЛЫ - посмотреть балансы наших
КУРС - посмотреть курс продажи/скупки валюты
БАНК[ДЕЙСТВИЕ] - выполнить любое действие с балансом (ответом на сообщение)
ВЕСЬ БАНК[ДЕЙСТВИЕ] - выполнить любое действие со всеми балансами
"""
emoji='✋😴💰😔😲🎲🎰'# {emoji[2]}
########################################### все функции для хендлеров
'''
def kakoy_balans(id_chelika):
    command_kakoy_balans = f"select balance from kvg_db where id = {id_chelika}"
    cur.execute(command_kakoy_balans)
    balans_kakoy_balans = cur.fetchone()
    balans_kakoy_balans = balans_kakoy_balans[0]
    return balans_kakoy_balans
def kkakoy_balans(id_chelika):
    command_kkakoy_balans = f"select balance from kvg_db where id = {id_chelika}"
    cur.execute(command_kkakoy_balans)
    balans_kkakoy_balans = cur.fetchone()
    balans_kkakoy_balans = balans_kkakoy_balans[0]
    kiber_balance='{0:,}'.format(balans_kkakoy_balans).replace(',', ' ')
    return kiber_balance
'''
def kakoy_balans(id_chelika, type_vivod):
    command_kakoy_balans = f"select balance from kvg_db where id = {id_chelika}"
    cur.execute(command_kakoy_balans)
    balans_kakoy_balans = cur.fetchone()
    balans_kakoy_balans = balans_kakoy_balans[0]
    if type_vivod==1:
        return '{0:,}'.format(balans_kakoy_balans).replace(',', ' ')
    if type_vivod==0:
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
    bot.send_message(m.chat.id, f'Привет! {emoji[0]} Я Квожка, вы наверно уже заскучали? {emoji[1]}')

@bot.message_handler(commands=["commands"])
def commands(m, res=False):
    if m.chat.id == idr:
        bot.send_message(m.chat.id, commands_rosya)
    elif m.from_user.id in niki_ludishek:
        bot.send_message(m.chat.id, commands_ludishki)
    else:
        bot.send_message(m.chat.id, commands_all)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms=message.text
    new_sms_l=message.text.lower()
    id_chel=message.from_user.id
    id_chat=message.chat.id
### основная часть хендлера
    global is_kvogka_rabotaet
    if is_kvogka_rabotaet=="YES":
        if new_sms_l[0:2] == 'оп' and id_chel in niki_ludishek:
            if new_sms_l[2] == 'л':
                bot.send_message(id_chat, nikl)
            elif new_sms_l[2] == 'д':
                bot.send_message(id_chat, nikd)
            elif new_sms_l[2] == 'ж':
                bot.send_message(id_chat, nikg)
            elif new_sms_l[2] == 'р':
                bot.send_message(id_chat, nikr)
            elif new_sms_l[2:5] == 'все':
                bot.send_message(id_chat, f'{nikr} {nikd} {nikl} {nikg}')
        elif new_sms_l == 'квожка':
            bot.send_message(id_chat, 'Квожка здесь, чё пристали?')
        elif new_sms_l[0:7]=='отпвчат' and id_chel in niki_ludishek:
            bot.send_message(ourchatid, new_sms[8:])
            bot.send_message(message.chat.id, 'Отправил ваше сообщение!')
        elif new_sms_l == 'полюбить':
            name_poluch=message.reply_to_message.from_user.first_name
            name_otprav=message.from_user.first_name
            bot.send_message(id_chat, f"{name_otprav} полюбил(а) {name_poluch}")
        elif new_sms_l == 'послать':
            name_poluch=message.reply_to_message.from_user.first_name
            name_otprav=message.from_user.first_name
            bot.send_message(id_chat, f"{name_otprav} послал(а) {name_poluch}")
        elif new_sms_l == 'похвалить':
            name_poluch=message.reply_to_message.from_user.first_name
            name_otprav=message.from_user.first_name
            bot.send_message(id_chat, f"{name_otprav} похвалил(а) {name_poluch}")
        elif new_sms_l == 'обидеться':
            name_poluch=message.reply_to_message.from_user.first_name
            name_otprav=message.from_user.first_name
            bot.send_message(id_chat, f"{name_otprav} обиделся(ась) на {name_poluch}")
        elif new_sms_l == 'пинг':
            start_time = datetime.now()
            bot.send_message(id_chat, "Беру ракетку!")
            end_time = datetime.now()
            finish_time = end_time - start_time
            bot.send_message(id_chat, f'Понг (за {finish_time.total_seconds()} секунд)')
            bot.send_message(id_otchet_chat, f'{message.from_user.first_name} ({message.from_user.username}) команда - "пинг"')
    ### скрытые команды хендлера
        elif new_sms == "*+" and id_chel==idr:
            bot.send_message(id_chat, 'Квожка работает!')
        elif new_sms_l[0:11]=='ночь квожка' and id_chel==idr:
            bot.delete_message(id_chat, message.message_id)
            bot.send_message(id_chat, f'{nikr} {nikd} {nikl} {nikg}\nВсем спокойной ночи!')
        elif new_sms_l[0:11]=='утро квожка' and id_chel==idr:
            bot.delete_message(id_chat, message.message_id)
            bot.send_message(id_chat, f'{nikr} {nikd} {nikl} {nikg}\nВсем доброе утро!')
        elif new_sms_l[0:4]=="спам" and id_chel==idr:
            bot.delete_message(message.chat.id, message.message_id)
            if new_sms_l[5:9]=='лиза':
                bot.send_message(id_chat, nikl)
                time.sleep(1)
                bot.send_message(id_chat, nikl)
                time.sleep(1)
                bot.send_message(id_chat, nikl)
                time.sleep(1)
            if new_sms_l[5:9]=='женя':
                bot.send_message(id_chat, nikg)
                time.sleep(1)
                bot.send_message(id_chat, nikg)
                time.sleep(1)
                bot.send_message(id_chat, nikg)
                time.sleep(1)
            if new_sms_l[5:9]=='даша':
                bot.send_message(id_chat, nikd)
                time.sleep(1)
                bot.send_message(id_chat, nikd)
                time.sleep(1)
                bot.send_message(id_chat, nikd)
                time.sleep(1)
            if new_sms_l[5:8]=='все':
                bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                time.sleep(1)
                bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                time.sleep(1)
                bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                time.sleep(1)
    ### все для игры в шпиона
        elif new_sms_l == "шпион старт" and id_chel in niki_ludishek:
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
            bot.send_message(id_chat, 'Игра Шпион начинается. Зайдите в лс бота узнать вашу роль/локацию!')
        elif new_sms_l == "шпион стоп" and id_chel in niki_ludishek:
            bot.send_message(id_chat, f'Игра Шпион окончена.\nПредателем был(а) {chel_shpion}.\nЛокация называлась {location_shp}')
    ### все для валютной игры
        elif new_sms_l=='баланс' or new_sms_l=='бал':
            bot.send_message(id_chat, f"Ваш баланс: {kakoy_balans(id_chel, 1)}{emoji[2]}")
        elif new_sms_l[0:7]=='перевод':
            id_poluch=message.reply_to_message.from_user.id 
            id_otprav=message.from_user.id
            try:
                perevod_summa = int(new_sms[7:])
                balans_perevodimogo = kakoy_balans(id_otprav, 0)
                if balans_perevodimogo>=perevod_summa:
                    minus_balans(id_otprav, perevod_summa)
                    plus_balans(id_poluch, perevod_summa)
                    bot.send_message(id_chat, f"Перевод выполнен успешно!\nБаланс получателя: {kakoy_balans(id_poluch, 1)}{emoji[2]}\nВаш баланс: {kakoy_balans(id_otprav, 1)}{emoji[2]}")
                else:
                    bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l[0:4]=='своп':
            id_poluch=message.reply_to_message.from_user.id 
            id_otprav=message.from_user.id
            try:
                perevod_summa = int(new_sms[4:])
                balans_perevodimogo = kakoy_balans(id_otprav, 0)
                if balans_perevodimogo>=perevod_summa:
                    minus_balans(id_otprav, perevod_summa)
                    plus_balans(id_poluch, perevod_summa)
                    bot.send_message(id_chat, f"Перевод выполнен успешно!\nБаланс получателя: {kakoy_balans(id_poluch, 1)}{emoji[2]}\nВаш баланс: {kakoy_balans(id_otprav, 1)}{emoji[2]}")
                else:
                    bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l[0:4]=="банк" and id_chel==idr:
            id_poluch=message.reply_to_message.from_user.id 
            try:
                perevod_summa = new_sms[4:]            
                command = f"update kvg_db set balance = balance {perevod_summa} where id = {id_poluch}"
                cur.execute(command)
                conn.commit()
                bot.send_message(id_chat, f"Операция выполнена успешно!\nБаланс клиента: {kakoy_balans(id_poluch, 1)}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l[0:3]=="каз":
            random_kef=random.choice(random_kefiki)
            try:
                igr_kazik_summa = int(new_sms[3:])
                balans_igr_vkazik = kakoy_balans(id_chel, 0)
                if balans_igr_vkazik>=igr_kazik_summa:
                    minus_balans(id_chel, igr_kazik_summa)
                    new_igr_kazik_summa=igr_kazik_summa*(float(random_kef))
                    plus_balans(id_chel, new_igr_kazik_summa)
                    bot.send_message(id_chat, f"Казино: {emoji[6]} {random_kef} {emoji[6]}\nВаш баланс: {emoji[2]}{kakoy_balans(id_chel, 1)}{emoji[2]}")
                else:
                    bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l[0:3]=="куб":
            random_cifra = random.randint(1,6)
            try:
                igr_kubick_cifra = int(new_sms[3])
                igr_kubick_summa = int(new_sms[4:])
                balans_igr_vkubick = kakoy_balans(id_chel, 0)
                if balans_igr_vkubick>=igr_kubick_summa:
                    minus_balans(id_chel, igr_kubick_summa)
                    new_igr_kubick_summa=igr_kubick_summa*5
                    if igr_kubick_cifra==random_cifra:
                        plus_balans(id_chel, new_igr_kubick_summa)
                    bot.send_message(id_chat, f"Кубик: {emoji[5]} {random_cifra} {emoji[5]}\nВаш баланс: {emoji[2]}{kakoy_balans(id_chel, 1)}{emoji[2]}")
                else:
                    bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l=="всебалы" and id_chel in niki_ludishek:
            cur.execute("select name, balance from kvg_db")
            namebalance = cur.fetchall()
            itogoviy_vivod="Балансы наших:\n"
            try:
                for el in namebalance:
                    if str(el[0]) in nashi_ludishki:
                        itogoviy_vivod+=str(str(el[0])+f"{emoji[2]}"+str('{0:,}'.format(el[1]).replace(',', ' '))+"\n")
                bot.send_message(id_chat, itogoviy_vivod)
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l=="курс":
            try:
                cur.execute("select balance from kvg_db")
                namebalance = cur.fetchall()
                summ_balans=0
                count_balans=0
                for el in namebalance:
                    count_balans+=1
                    summ_balans+=int(el[0])
                kursik=summ_balans//(count_balans**3)
                kursik4=kursik*4
                kursik='{0:,}'.format(kursik).replace(',', ' ')
                kursik4='{0:,}'.format(kursik4).replace(',', ' ')
                bot.send_message(id_chat, f"Курс:\nСкупка: 1 рубль = {kursik4}{emoji[2]} (от 10Р)\nПродажа: 1 рубль = {kursik}{emoji[2]} (от 1Р)\nПо всем вопросам: {nikr}")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l=="квожка скажи айди" and id_chel==idr:
            bot.send_message(id_chat, message.reply_to_message.from_user.id)
        elif new_sms_l[0:8]=='весьбанк' and id_chel==idr:
            try:
                cur.execute("select id from kvg_db")
                idshki = cur.fetchall()
                summa_vseh = new_sms[8:]
                for el in idshki:
                    command = f"update kvg_db set balance = balance {summa_vseh} where id = {int(el[0])}"
                    cur.execute(command)
                conn.commit()
                bot.send_message(id_chat, f"Операция {summa_vseh} для всех выполнена успешно!")
            except:
                bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
        elif new_sms_l=="квожка я выключаю тебя" and id_chel==idr:
            is_kvogka_rabotaet="NO"
            cur.execute("update names_keys set key = 'NO' where name = 'is_kvogka_rabotaet'")
            conn.commit()
    else:
        if new_sms_l=="квожка я включаю тебя" and id_chel==idr:
            is_kvogka_rabotaet="YES"
            cur.execute("update names_keys set key = 'YES' where name = 'is_kvogka_rabotaet'")
            conn.commit()
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()