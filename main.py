import telebot
import random
import time

bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')

ourchatid=-1001139329557
idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@r4419'
game_shp_locations=['Футбольное поле', 'Школа', 'Рынок', 'Магазин', 'Площадка', 'Квартира', 'Ферма', 'Лес', 'Парк', 'Озеро', 'Сад', 'Пляж', 'Заброшка', 'Стройка', 'Поляна', 'Аквапарк', 'Лагерь', 'Зоопарк', 'Цум', 'Отель']
ludi=['Даша', 'Лиза', 'Женя', 'Рося']
chel_shpion=0
location_shp=0
my_zastavka="""
============================================================================
============================================================================
"""

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я Квожка, вы наверно уже заскучали?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms_l=message.text.lower()
    new_sms=message.text
    id_chel=message.from_user.id
    id_peresl_chel=message.forward_from.user
######################################################
    if new_sms_l[0:2] == 'оп':
        if new_sms_l[2] == 'л':
            bot.send_message(ourchatid, nikl)
        elif new_sms_l[2] == 'д':
            bot.send_message(ourchatid, nikd)
        elif new_sms_l[2] == 'ж':
            bot.send_message(ourchatid, nikg)
        elif new_sms_l[2] == 'р':
            bot.send_message(ourchatid, nikr)
        elif new_sms_l[2:5] == 'все':
            bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}')
    elif new_sms_l == 'квожка':
        bot.send_message(message.chat.id, 'Квожка здесь, чё пристали?')
    elif new_sms_l[0:7]=='отпвчат':
        bot.send_message(ourchatid, new_sms[8:])
        bot.send_message(message.chat.id, 'Отправил ваше сообщение!')
    elif message.text == 'уебать':
        name_poluch=message.reply_to_message.from_user.first_name
        name_otprav=message.from_user.first_name
        bot.send_message(ourchatid, f"{name_otprav} уебал(а) {name_poluch}")
######################################################
    elif new_sms == "*+":
        bot.send_message(message.chat.id, 'Квожка работает!')
    elif new_sms_l[0:11]=='ночь квожка':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем спокойной ночи!')
        bot.send_message(idr, 'Пожелал спокойной ночи!')
    elif new_sms_l[0:11]=='утро квожка':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем доброе утро!')
        bot.send_message(idr, 'Пожелал доброго утра!')
    elif new_sms_l[0:4]=="спам":
        bot.delete_message(message.chat.id, message.message_id)
        if new_sms_l[5:9]=='лиза':
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
            bot.send_message(ourchatid, nikl)
            time.sleep(1)
        if new_sms_l[5:9]=='женя':
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
            bot.send_message(ourchatid, nikg)
            time.sleep(1)
        if new_sms_l[5:9]=='даша':
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
            bot.send_message(ourchatid, nikd)
            time.sleep(1)
#########################################################
    elif new_sms_l == "шпион старт":
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
        bot.send_message(ourchatid, f'Игра Шпион окончена.\nПредателем был(а) {chel_shpion}.\nЛокация называлась {location_shp}')

if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()
