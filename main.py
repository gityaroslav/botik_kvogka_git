import telebot
import random

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
game_shp=False
game_shp_locations=['Футбольное поле', 'Школа']
ludi=['даша', 'лиза', 'женя', 'рося']

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я Квожка, вы наверно уже заскучали?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms_l=message.text.lower()
    new_sms=message.text
    id_chel=message.from_user.id
    game_shp_chel=random.choice(ludi)
    game_shp_locat=random.choice(game_shp_locations)
######################################################
    if new_sms_l[0:2] == 'оп' and game_shp==False:
        if new_sms_l[2] == 'л' and game_shp==False:
            bot.send_message(message.chat.id, nikl)
        elif new_sms_l[2] == 'д' and game_shp==False:
            bot.send_message(message.chat.id, nikd)
        elif new_sms_l[2] == 'ж' and game_shp==False:
            bot.send_message(message.chat.id, nikg)
        elif new_sms_l[2] == 'р' and game_shp==False:
            bot.send_message(message.chat.id, nikr)
        elif new_sms_l[2:5] == 'все' and game_shp==False:
            bot.send_message(message.chat.id, f'{nikr} {nikd} {nikl} {nikg}')
    elif new_sms_l == 'квожка' and game_shp==False:
        bot.send_message(message.chat.id, 'Квожка здесь, чё пристали?')
    elif new_sms_l[0:7]=='отпвчат' and game_shp==False:
        bot.send_message(ourchatid, new_sms[8:])
        bot.send_message(message.chat.id, 'Отправил!')
######################################################
    elif new_sms == "*+":
        bot.send_message(message.chat.id, 'Квожка работает!')
    elif new_sms_l[0:11]=='ночь квожка':
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем спокойной ночи!')
        bot.send_message(message.chat.id, 'Отправил!')
    elif new_sms_l[0:11]=='утро квожка':
        bot.send_message(ourchatid, f'{nikr} {nikd} {nikl} {nikg}\nВсем доброе утро!')
        bot.send_message(message.chat.id, 'Отправил!')
#########################################################
    if new_sms_l == "шпион старт":
        game_shp = True
        if game_shp_chel=='даша':
            bot.send_message(idd, 'Вы шпион!')
            bot.send_message(idr, game_shp_locat)
            bot.send_message(idl, game_shp_locat)
            bot.send_message(idg, game_shp_locat)
        if game_shp_chel=='лиза':
            bot.send_message(idl, 'Вы шпион!')
            bot.send_message(idr, game_shp_locat)
            bot.send_message(idd, game_shp_locat)
            bot.send_message(idg, game_shp_locat)
        if game_shp_chel=='рося':
            bot.send_message(idr, 'Вы шпион!')
            bot.send_message(idd, game_shp_locat)
            bot.send_message(idl, game_shp_locat)
            bot.send_message(idg, game_shp_locat)
        if game_shp_chel=='женя':
            bot.send_message(idg, 'Вы шпион!')
            bot.send_message(idr, game_shp_locat)
            bot.send_message(idl, game_shp_locat)
            bot.send_message(idd, game_shp_locat)
        bot.send_message(message.chat.id, 'Игра Шпион начинается. Зайдите в лс бота узнать вашу роль/локацию!')
    elif new_sms_l == "шпион стоп":
        game_shp = False
        bot.send_message(message.chat.id, f'Игра Шпион окончена.\nПредателем был(а) {game_shp_chel}.\nЛокация называлась {game_shp_locat}')
    
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()
