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

@bot.message_handler(content_types=["text"])
def handle_text(message):
        if message.text[0:2] == 'оп':
            if message.text[2] == 'л':
                bot.send_message(message.chat.id, nikl)
            elif message.text[2] == 'д':
                bot.send_message(message.chat.id, nikd)
            elif message.text[2] == 'ж':
                bot.send_message(message.chat.id, nikg)
            elif message.text[2] == 'р':
                bot.send_message(message.chat.id, nikr)
        elif (message.text).lower() == 'квожка':
            bot.send_message(message.chat.id, 'Квожка здесь, чё пристали?')
        elif message.text == "*+":
            bot.send_message(message.chat.id, 'Квожка работает!')
        elif message.text == "test":
            bot.send_message(message.chat.id, 'синхронизация работает')

if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()
    # bot.polling(none_stop=True, interval=0)