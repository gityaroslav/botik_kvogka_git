import telebot
import random
bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')

g='Женя'
d='Даша'
l='Лиза'
r='Рося'
vz_pnut_m='пнул '
vz_pnut_g='пнула'
vz_posl_m='послал'
vz_posl_g='послала'
vz_obn_m='обнял'
vz_obn_g='обняла'
vz_poc_m='поцеловал'
vz_poc_g='поцеловала'
idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@r4419'
spisok_good_slovechek=['Делай так почаще!', 'Вот, ну можешь же быть молодцом!', 'Всегда бы так!']
spisok_bad_slovechek=['Не шути так больше!', 'Человеку модет быть обидно!', 'Зачем ты это сделало, недостойное создание?']
spisok_ludei=['анонимуса', 'абобуса', 'глобуса']

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Заскучали?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms_l=message.text.lower()
    new_sms=message.text
    id_user=message.from_user.id
    if new_sms_l[0:2] == 'оп':
        if new_sms_l[2] == 'л':
            bot.send_message(message.chat.id, nikl)
        elif new_sms_l[2] == 'д':
            bot.send_message(message.chat.id, nikd)
        elif new_sms_l[2] == 'ж':
            bot.send_message(message.chat.id, nikg)
        elif new_sms_l[2] == 'р':
            bot.send_message(message.chat.id, nikr)
        elif new_sms_l[2:5] == 'все':
            bot.send_message(message.chat.id, f'{nikr} {nikd} {nikl} {nikg}')
    elif new_sms_l == 'квожка':
        bot.send_message(message.chat.id, 'Квожка здесь, чё пристали?')
    elif new_sms == "*+":
        bot.send_message(message.chat.id, 'Квожка работает!') 
    elif new_sms_l[0:7]=='отпвчат':
        bot.send_message(-1001139329557, new_sms[8:])
        bot.send_message(message.chat.id, 'Отправил!')
    elif new_sms_l=='пнуть':
        random_chtoto1=random.randint(0, 2)
        random_chtoto2=random.randint(0, 2)
        if id_user==idr:
            bot.send_message(message.chat.id, f'{r} {vz_pnut_m} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idd:
            bot.send_message(message.chat.id, f'{d} {vz_pnut_g} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idg:
            bot.send_message(message.chat.id, f'{g} {vz_pnut_m} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idl:
            bot.send_message(message.chat.id, f'{l} {vz_pnut_g} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
    elif new_sms_l=='послать':
        random_chtoto1=random.randint(0, 2)
        random_chtoto2=random.randint(0, 2)
        if id_user==idr:
            bot.send_message(message.chat.id, f'{r} {vz_posl_m} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idd:
            bot.send_message(message.chat.id, f'{d} {vz_posl_g} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idg:
            bot.send_message(message.chat.id, f'{g} {vz_posl_m} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idl:
            bot.send_message(message.chat.id, f'{l} {vz_posl_g} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
    elif new_sms_l=='обнять':
        random_chtoto1=random.randint(0, 2)
        random_chtoto2=random.randint(0, 2)
        if id_user==idr:
            bot.send_message(message.chat.id, f'{r} {vz_posl_m} {spisok_ludei[random_chtoto1]}. {spisok_bad_slovechek[random_chtoto2]}')
        elif id_user==idd:
            bot.send_message(message.chat.id, f'{d} {vz_obn_g} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
        elif id_user==idg:
            bot.send_message(message.chat.id, f'{g} {vz_obn_m} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
        elif id_user==idl:
            bot.send_message(message.chat.id, f'{l} {vz_obn_g} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
    elif new_sms_l=='поцеловать':
        random_chtoto1=random.randint(0, 2)
        random_chtoto2=random.randint(0, 2)
        if id_user==idr:
            bot.send_message(message.chat.id, f'{r} {vz_poc_m} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
        elif id_user==idd:
            bot.send_message(message.chat.id, f'{d} {vz_poc_g} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
        elif id_user==idg:
            bot.send_message(message.chat.id, f'{g} {vz_poc_m} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
        elif id_user==idl:
            bot.send_message(message.chat.id, f'{l} {vz_poc_g} {spisok_ludei[random_chtoto1]}. {spisok_good_slovechek[random_chtoto2]}')
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()