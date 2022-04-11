############################ все модули и импорты1
import telebot
import random
import time
import os
import psycopg2
from datetime import datetime
######################################## все переменные
ourchatid=-1001139329557
idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@gikhok'
id_error_chat=-606727227
niki_ludishek=[idg, idd, idl, idr, 1039315228, 1230762892, 981661206]
imena_nashih_ludishek=["Ника", "Рося", "Женя", "Поля", "Лиза", "Даша", "Егор"]
game_shp_locations=['Футбольное поле', 'Школа', 'Рынок', 'Магазин', 'Площадка', 'Квартира', 'Ферма', 'Лес', 'Парк', 'Озеро', 'Сад', 'Пляж', 'Заброшка', 'Стройка', 'Поляна', 'Аквапарк', 'Лагерь', 'Зоопарк', 'Цум', 'Отель']
ludi=['Даша', 'Лиза', 'Женя', 'Рося']
random_kefiki=["0","0","0","0","0","0","0","0","0","0.25","0.25","0.25","0.25","0.25","0.25","0.25","0.25","0.25","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","1","1","1","1","1","1","1","1","1","1.25","1.25","1.25","1.25","1.25","1.25","1.25","1.5","1.5","1.5","1.5","1.5","1.5","1.5","2","2","2","2","2","5","10","50","100"]
nachalo_kefikov=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","3","3","3","3","3","3","4","5","6","7","8","9","10","11","12","13","14","15","100"]
okonchaniya_kefikov=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]
chel_shpion=0
location_shp=0
my_zastavka="""
============================================================================
============================================================================
"""
commands_all="""
КВОЖКА - узнать параметры о работе бота
ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ПИНГ - измерить скорость ответа бота
![ВАШ ТЕКСТ] - отправить ваш текст написанный от имени бота
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
КВОЖКА - узнать параметры о работе бота
![ВАШ ТЕКСТ] - отправить ваш текст написанный от имени бота
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
КВОЖКА - узнать параметры о работе бота
![ВАШ ТЕКСТ] - отправить ваш текст написанный от имени бота
ПОЛЮБИТЬ, ПОСЛАТЬ, ПОХВАЛИТЬ, ОБИДЕТЬСЯ - команды взаимодействия (ответом на сообщение)
ШПИОН СТАРТ///ШПИОН СТОП - начать/закончить игру Шпион
ПИНГ - измерить скорость ответа бота
——————————————
*+ - проверка, работает ли бот
(НОЧЬ///УТРО) КВОЖКА - пожелать спокойной ночи/доброго утра
СПАМ - (и имя через пробел) отметит человека 3 раза
КВОЖКА СКАЖИ АЙДИ - скажет айди пользователя(ответом на сообщение)
КВОЖКА РЕЖИМ ВКЛ/ВЫКЛ - включить/выключить бота
КВОЖКА СКАЖИ СООБЩЕНИЕ - скажет сообщение(message, все его данные)
КВОЖКА ВЫДАЙ ЗА БАГ - выдаст валютку за находку бага
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
try:
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
        bot.send_message(idr, f'Ошибка в подключении:\n{e}')
    emoji='✋😴💰😔😲🎲🎰📈🔒'# {emoji[7]}
    ########################################### все функции для хендлеров
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
        command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
        cur.execute(command123456)
        conn.commit()
    
    @bot.message_handler(commands=["commands"])
    def commands(m, res=False):
        if m.chat.id == idr:
            bot.send_message(m.chat.id, commands_rosya)
        elif m.from_user.id in niki_ludishek:
            bot.send_message(m.chat.id, commands_ludishki)
        else:
            bot.send_message(m.chat.id, commands_all)
        command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
        cur.execute(command123456)
        conn.commit()
    
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        new_sms=message.text
        new_sms_l=message.text.lower()
        id_chel=message.from_user.id
        id_chat=message.chat.id
    ### основная часть хендлера
        global is_kvogka_rabotaet
        cur.execute("select key from names_keys where name = 'is_kvogka_rabotaet'")
        is_kvogka_rabotaet = cur.fetchone()
        cur.execute("select key from names_keys where name = 'sms_count'")
        sms_count=cur.fetchone()
        sms_count=int(sms_count[0])+1
        if is_kvogka_rabotaet[0]=="YES":
            if new_sms_l[0:2] == 'оп' and id_chel in niki_ludishek:
                if new_sms_l[2] == 'л':
                    bot.send_message(id_chat, nikl)
                    command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                    cur.execute(command123456)
                elif new_sms_l[2] == 'д':
                    bot.send_message(id_chat, nikd)
                    command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                    cur.execute(command123456)
                elif new_sms_l[2] == 'ж':
                    bot.send_message(id_chat, nikg)
                    command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                    cur.execute(command123456)
                elif new_sms_l[2] == 'р':
                    bot.send_message(id_chat, nikr)
                    command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                    cur.execute(command123456)
                elif new_sms_l[2:5] == 'все':
                    bot.send_message(id_chat, f'{nikr} {nikd} {nikl} {nikg}')
            elif new_sms_l[0]=='!':
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(id_chat, new_sms[1:])
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == 'полюбить':
                name_poluch=message.reply_to_message.from_user.first_name
                name_otprav=message.from_user.first_name
                bot.send_message(id_chat, f"{name_otprav} полюбил(а) {name_poluch}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == 'послать':
                name_poluch=message.reply_to_message.from_user.first_name
                name_otprav=message.from_user.first_name
                bot.send_message(id_chat, f"{name_otprav} послал(а) {name_poluch}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == 'похвалить':
                name_poluch=message.reply_to_message.from_user.first_name
                name_otprav=message.from_user.first_name
                bot.send_message(id_chat, f"{name_otprav} похвалил(а) {name_poluch}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == 'обидеться':
                name_poluch=message.reply_to_message.from_user.first_name
                name_otprav=message.from_user.first_name
                bot.send_message(id_chat, f"{name_otprav} обиделся(ась) на {name_poluch}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == 'пинг':
                start_time = datetime.now()
                bot.send_message(id_chat, "Беру ракетку!")
                end_time = datetime.now()
                finish_time = end_time - start_time
                bot.send_message(id_chat, f'Понг (за {finish_time.total_seconds()} секунд)')
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif "dashina_pesnya"=="dashina_pesnya" and (id_chel==idd or id_chel==idr) and new_sms_l[0:3]=="кв ":
                if new_sms_l[3:]=="пой трям":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Раз ромашка")
                elif new_sms_l[3:]=="раз ромашка":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Два ромашка")
                elif new_sms_l[3:]=="два ромашка":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Три ромашка")
                elif new_sms_l[3:]=="три ромашка":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "А я четвёртую сорву")
                elif new_sms_l[3:]=="а я четвёртую сорву" or new_sms_l[3:]=="а я четвертую сорву":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Пять ромашка")
                elif new_sms_l[3:]=="пять ромашка":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Шесть ромашка")
                elif new_sms_l[3:]=="шесть ромашка":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "Семь")
                elif new_sms_l[3:]=="семь":
                    time.sleep(0.5)
                    bot.send_message(id_chat, "А она это, того самое, закончилась, песенка то :(")
        ### скрытые команды хендлера
            elif new_sms_l=="квожка скажи сообщение" and id_chel==idr:
                bot.send_message(idr, message)
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:28]=="квожка работа с базой данных" and id_chel==idr:
                try:
                    sql_zaprosik=new_sms_l[29:]
                    if sql_zaprosik[0:6]=="select":
                        cur.execute(sql_zaprosik)
                        dlya_vivoda_sql_zaprosika=cur.fetchall()
                        vivod_sql_zaprosika=''
                        for el in dlya_vivoda_sql_zaprosika:
                            vivod_sql_zaprosika+=f"{el}\n"
                        bot.send_message(id_chat, vivod_sql_zaprosika)
                    else:
                        cur.execute(sql_zaprosik)
                        conn.commit()
                    itog_sql_zaprosika=f"SQL запрос:\n―――――\nУспешно!"
                    bot.send_message(id_chat, itog_sql_zaprosika)
                except Exception as e:
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                    bot.send_message(idr, e)
            elif new_sms == "*+" and id_chel==idr:
                bot.send_message(id_chat, 'Квожка работает!')
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:11]=='ночь квожка' and id_chel==idr:
                bot.delete_message(id_chat, message.message_id)
                bot.send_message(id_chat, f'{nikd} {nikl} {nikg}\nВсем спокойной ночи!')
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:11]=='утро квожка' and id_chel==idr:
                bot.delete_message(id_chat, message.message_id)
                bot.send_message(id_chat, f'{nikd} {nikl} {nikg}\nВсем доброе утро!')
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:4]=="спам" and id_chel==idr:
                bot.delete_message(message.chat.id, message.message_id)
                if new_sms_l[5:9]=='лиза':
                    bot.send_message(id_chat, nikl)
                    time.sleep(1)
                    bot.send_message(id_chat, nikl)
                    time.sleep(1)
                    bot.send_message(id_chat, nikl)
                    time.sleep(1)
                    command123456 = f"update names_keys set key = {sms_count+2} where name = 'sms_count'"
                    cur.execute(command123456)
                if new_sms_l[5:9]=='женя':
                    bot.send_message(id_chat, nikg)
                    time.sleep(1)
                    bot.send_message(id_chat, nikg)
                    time.sleep(1)
                    bot.send_message(id_chat, nikg)
                    time.sleep(1)
                    command123456 = f"update names_keys set key = {sms_count+2} where name = 'sms_count'"
                    cur.execute(command123456)
                if new_sms_l[5:9]=='даша':
                    bot.send_message(id_chat, nikd)
                    time.sleep(1)
                    bot.send_message(id_chat, nikd)
                    time.sleep(1)
                    bot.send_message(id_chat, nikd)
                    time.sleep(1)
                    command123456 = f"update names_keys set key = {sms_count+2} where name = 'sms_count'"
                    cur.execute(command123456)
                if new_sms_l[5:8]=='все':
                    bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                    time.sleep(1)
                    bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                    time.sleep(1)
                    bot.send_message(id_chat, f'{nikd} {nikl} {nikg}')
                    time.sleep(1)
                    command123456 = f"update names_keys set key = {sms_count+2} where name = 'sms_count'"
                    cur.execute(command123456)
            elif new_sms_l=="квожка режим выкл" and id_chel==idr:
                cur.execute("update names_keys set key = 'NO' where name = 'is_kvogka_rabotaet'")
                bot.send_message(idr, "Режим квожки изменён на 'NO'")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
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
                command123456 = f"update names_keys set key = {sms_count+4} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l == "шпион стоп" and id_chel in niki_ludishek:
                bot.send_message(id_chat, f'Игра Шпион окончена.\nПредателем был(а) {chel_shpion}.\nЛокация называлась {location_shp}')
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
        ### все для валютной игры
            elif new_sms_l=='баланс' or new_sms_l=='бал':
                bot.send_message(id_chat, f"Ваш баланс: {kakoy_balans(id_chel, 1)}{emoji[2]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:7]=='перевод': #перевод
                id_poluch=message.reply_to_message.from_user.id 
                id_otprav=message.from_user.id
                try:
                    kolichestvo_k=new_sms_l.count("к")
                    if kolichestvo_k>0:
                        index_kolichestva_k=new_sms_l.find("к")
                        perevod_summa = int(new_sms[7:index_kolichestva_k])*(1000**(kolichestvo_k))
                    else:
                        perevod_summa = int(new_sms[7:])
                    balans_perevodimogo = kakoy_balans(id_otprav, 0)
                    if balans_perevodimogo>=perevod_summa:
                        minus_balans(id_otprav, perevod_summa)
                        plus_balans(id_poluch, perevod_summa)
                        bot.send_message(id_chat, f"Перевод выполнен успешно!\nБаланс получателя: {kakoy_balans(id_poluch, 1)}{emoji[2]}\nВаш баланс: {kakoy_balans(id_otprav, 1)}{emoji[2]}")
                    else:
                        bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:4]=='своп': #своп
                id_poluch=message.reply_to_message.from_user.id 
                id_otprav=message.from_user.id
                try:
                    kolichestvo_k=new_sms_l.count("к")
                    if kolichestvo_k>0:
                        index_kolichestva_k=new_sms_l.find("к")
                        perevod_summa = int(new_sms[4:index_kolichestva_k])*(1000**(kolichestvo_k))
                    else:
                        perevod_summa = int(new_sms[4:])
                    balans_perevodimogo = kakoy_balans(id_otprav, 0)
                    if balans_perevodimogo>=perevod_summa:
                        minus_balans(id_otprav, perevod_summa)
                        plus_balans(id_poluch, perevod_summa)
                        bot.send_message(id_chat, f"Перевод выполнен успешно!\nБаланс получателя: {kakoy_balans(id_poluch, 1)}{emoji[2]}\nВаш баланс: {kakoy_balans(id_otprav, 1)}{emoji[2]}")
                    else:
                        bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:4]=="банк" and id_chel==idr:#банк
                id_poluch=message.reply_to_message.from_user.id 
                try:
                    znak_banka=new_sms[4]
                    kolichestvo_k=new_sms_l[4:].count("к")
                    if kolichestvo_k>0:
                        index_kolichestva_k=(new_sms_l[4:].find("к"))+4
                        perevod_summa = int(new_sms_l[5:index_kolichestva_k])*(1000**(kolichestvo_k))
                    else:
                        perevod_summa = int(new_sms_l[5:])         
                    command = f"update kvg_db set balance = balance {znak_banka}{perevod_summa} where id = {id_poluch}"
                    cur.execute(command)
                    conn.commit()
                    bot.send_message(id_chat, f"Операция выполнена успешно!\nБаланс клиента: {kakoy_balans(id_poluch, 1)}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:3]=="каз": #каз
                random_kef=random.choice(random_kefiki)
                try:
                    kolichestvo_k=new_sms_l[1:].count("к")
                    if kolichestvo_k>0:
                        index_kolichestva_k=(new_sms_l[1:].find("к"))+1
                        igr_kazik_summa = int(new_sms[3:index_kolichestva_k])*(1000**(kolichestvo_k))
                    else:
                        igr_kazik_summa = int(new_sms[3:])
                    balans_igr_vkazik = kakoy_balans(id_chel, 0)
                    if balans_igr_vkazik>=igr_kazik_summa:
                        minus_balans(id_chel, igr_kazik_summa)
                        new_igr_kazik_summa=igr_kazik_summa*(float(random_kef))
                        plus_balans(id_chel, new_igr_kazik_summa)
                        bot.send_message(id_chat, f"Казино: {emoji[6]} {random_kef} {emoji[6]}\nВаш баланс: {emoji[2]}{kakoy_balans(id_chel, 1)}{emoji[2]}")
                    else:
                        bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
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
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l=="всебалы" and id_chel in niki_ludishek: #всебалы
                cur.execute("select name, balance from kvg_db")
                namebalance = cur.fetchall()
                itogoviy_vivod="Балансы наших:\n"
                try:
                    for el in namebalance:
                        if str(el[0]) in imena_nashih_ludishek:
                            itogoviy_vivod+=str(str(el[0])+f"{emoji[2]}"+str('{0:,}'.format(el[1]).replace(',', ' '))+"\n")
                    bot.send_message(id_chat, itogoviy_vivod)
                except:
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l=="инфо" and id_chel==idr:
                id_togo_chela=message.reply_to_message.from_user.id
                try:
                    bot.send_message(id_chat, f"Айди|{id_togo_chela}\nБаланс|{kakoy_balans(id_togo_chela, 1)}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Айди|{id_togo_chela}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:4]=="краш":#краш
                try:
                    kolichestvo_k=new_sms_l[1:].count("к")
                    gde_tochka=new_sms_l.find(".")
                    if kolichestvo_k>0:
                        index_kolichestva_k=(new_sms_l[1:].find("к"))+1
                        igr_krashik_summa = int(new_sms[gde_tochka+3:index_kolichestva_k])*(1000**(kolichestvo_k))
                    else:
                        igr_krashik_summa = int(new_sms[gde_tochka+3:])
                    prognoz_igrayushego=str(new_sms_l[4:gde_tochka]+new_sms_l[gde_tochka+1:gde_tochka+3])
                    nach_kefika_krasha=random.choice(nachalo_kefikov)
                    okon_kefika_krasha=random.choice(okonchaniya_kefikov)
                    kefik_krasha=str(nach_kefika_krasha+okon_kefika_krasha)
                    balans_igr_vkrashik = kakoy_balans(id_chel, 0)
                    if int(prognoz_igrayushego)>100:
                        if balans_igr_vkrashik>=igr_krashik_summa:
                            if int(prognoz_igrayushego)<=int(kefik_krasha):
                                new_igr_krashik_summa=igr_krashik_summa*(float(f"{new_sms_l[4:gde_tochka]}.{new_sms_l[gde_tochka+3:gde_tochka+5]}"))
                                minus_balans(id_chel, igr_krashik_summa)
                                plus_balans(id_chel, new_igr_krashik_summa)
                            bot.send_message(id_chat, f"Краш: {emoji[7]} {nach_kefika_krasha}.{okon_kefika_krasha} {emoji[7]}\nВаш прогноз: {emoji[8]} {new_sms_l[4:gde_tochka]}.{new_sms_l[gde_tochka+1:gde_tochka+3]} {emoji[8]}\nВаш баланс: {emoji[2]}{kakoy_balans(id_chel, 1)}{emoji[2]}")
                        else:#
                            bot.send_message(id_chat, f"На вашем балансе недостаточно средств! {emoji[3]}")
                    else:
                        bot.send_message(id_chat, "Сделайте ставку в краше побольше :)")
                except Exception as e:
                    bot.send_message(id_error_chat, e)
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l=="курс":#курс
                try:
                    cur.execute("select balance from kvg_db")
                    namebalance = cur.fetchall()
                    summ_balans=0
                    count_balans=0
                    for el in namebalance:
                        count_balans+=1
                        summ_balans+=int(el[0])
                    kursik=summ_balans//(count_balans**3)
                    kursik20=kursik*15
                    kursik='{0:,}'.format(kursik).replace(',', ' ')
                    kursik20='{0:,}'.format(kursik20).replace(',', ' ')
                    bot.send_message(id_chat, f"Курс:\nПродажа: 1 рубль = {kursik}{emoji[2]}\nПродавать другим игрокам ниже курса запрещается!\nСумма ордена: {kursik20}{emoji[2]}")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l=="квожка выдай орден":#квожка выдай орден
                try:
                    cur.execute("select balance from kvg_db")
                    namebalance = cur.fetchall()
                    summ_balans=0
                    count_balans=0
                    for el in namebalance:
                        count_balans+=1
                        summ_balans+=int(el[0])
                    kursik15=(summ_balans//(count_balans**3))*15
                    plus_balans(message.reply_to_message.from_user.id, kursik15)
                    bot.send_message(id_chat, "Успешно выдал награду за находку бага!")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[0:8]=='весьбанк' and id_chel==idr:#весьбанк
                try:
                    cur.execute("select id from kvg_db")
                    idshki = cur.fetchall()
                    summa_vseh = new_sms[8:]
                    for el in idshki:
                        command = f"update kvg_db set balance = balance {summa_vseh} where id = {int(el[0])}"
                        cur.execute(command)
                    conn.commit()
                    bot.send_message(id_chat, f"Операция {summa_vseh} для всех выполнена успешно!")
                except Exception as e:
                    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
                    bot.send_message(id_chat, f"Что-то пошло не так. Попробуйте заново! {emoji[4]}")
                command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
                cur.execute(command123456)
            elif new_sms_l[:18]=="квожка отправь смс" and id_chel==idr:
                index1=new_sms_l.find("(")
                index2=new_sms_l.find(")")
                index3=new_sms_l.find("[")
                index4=new_sms_l.find("]")
                bot.send_message(int(new_sms_l[index3+1:index4]), str(new_sms_l[index1+1:index2]))
            elif new_sms_l[:21]=="квожка скажи все айди" and id_chel==idr:
                bot.send_message(id_chat, f"Айди Роси: {idr}\nАйди Даши: {idd}\nАйди Жени: {idg}\nАйди Лизы: {idl}\nАйди Егора: 981661206\nАйди Вари: 1450023923\nАйди Ники: 1039315228\nАйди Полины: 1230762892\n―――――\nАйди основного чата: {ourchatid}\nАйди Валютки: -1001779256622\nАйди чата с ошибками: {id_error_chat}")
            elif new_sms_l[:15]=="квожка рассылка" and id_chel==idr:
                text_rassilka=new_sms[16:]
                cur.execute("select id from kvg_db")
                idshki = cur.fetchall()
                all_id=repr(idshki)
                all_id=all_id.replace("(", "")
                all_id=all_id.replace(")", "")
                all_id=all_id.replace(",", "")
                all_id=all_id.replace("'", "")
                all_id=all_id[1:-1]
                all_id=list(map(int, all_id.split()))
                for ids in all_id:
                    try:
                        bot.send_message(ids, text_rassilka)
                    except:
                        pass
                bot.send_message(idr, "Рассылка готова!")
            conn.commit()
        if new_sms_l=="квожка режим вкл" and id_chel==idr:
            cur.execute("update names_keys set key = 'YES' where name = 'is_kvogka_rabotaet'")
            bot.send_message(idr, "Режим квожки изменён на 'YES'")
            command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
            cur.execute(command123456)
            conn.commit()
        if new_sms_l == 'квожка':
            command123456 = f"update names_keys set key = {sms_count} where name = 'sms_count'"
            cur.execute(command123456)
            conn.commit()
            cur.execute("select key from names_keys where name = 'is_kvogka_rabotaet'")
            kolvo_is_kvogka_rabotaet = cur.fetchone()
            cur.execute("select key from names_keys where name = 'sms_count'")
            kolvo_sms_count=cur.fetchone()
            bot.send_message(id_chat, f'КВОЖКА\n―――――\nСтатус работы: {kolvo_is_kvogka_rabotaet[0]}\nКоличество сообщений: {kolvo_sms_count[0]}')
        #if new_sms_l=="qwerfd":
            #bot.send_message(message.chat.id, f"[{message.from_user.first_name}](@{message.from_user.username})", parse_mode='MarkdownV2')
except Exception as e:
    bot.send_message(id_error_chat, f"Ошибка в коде: {e}")
    
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()