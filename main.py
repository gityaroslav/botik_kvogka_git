import telebot

bot = telebot.TeleBot('5075753945:AAHLRPtgOoUTyps1AntGwpY3lsCEcIoQ-No')

idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@r4419'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Заскучали?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_sms_l=message.text.lower()
    new_sms=message.text
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
if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()