import telebot
from telebot import types

token = 'bot token'
bot = telebot.TeleBot(token)

trackingList = []
switcher = -1
ParsTocen = []
counter = -1

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btton_1 = types.KeyboardButton("Add token tracking")
    btton_2 = types.KeyboardButton("Remove token tracking")
    btton_3 = types.KeyboardButton("What tokens are tracked")
    markup.add(btton_3).row(btton_1, btton_2)
    bot.send_message(message.chat.id, text = 'Start of parsing...', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def button_message(message):
    global trackingList, switcher, ParsTocen, counter
    if (message.text == "Add token tracking") and switcher != 1 and switcher != 0:
        switcher = 1
        bot.send_message(message.chat.id, text = 'Enter the name of the token to add')
                         
    elif (message.text == "Remove token tracking") and switcher != 1 and switcher != 0:
        switcher = 0
        bot.send_message(message.chat.id, text = 'Enter the name of the token to delete')

    elif (message.text == "What tokens are tracked"):
        bot.send_message(message.chat.id, text = f'List of tracked tokens: {trackingList}')

    if switcher == 1 and message.text != "Add token tracking" and message.text != "What tokens are tracked" and message.text != "Remove token tracking" and len(message.text) < 60:
        if not message.text.lower() in trackingList:
            trackingList.append(message.text.lower())
            bot.send_message(message.chat.id, text = 'The token was successfully added to the tracking list')
        elif message.text.lower() in trackingList:
            bot.send_message(message.chat.id, text = 'This token is already tracked')
        else :
            bot.send_message(message.chat.id, text = 'Try again from the beginning')
        switcher = -1

    elif switcher == 0 and message.text != "Remove token tracking" and message.text != "What tokens are tracked" and message.text != "Add token tracking" and len(message.text) < 60:
        if message.text.lower() in trackingList:
            trackingList.remove((message.text).lower())
            bot.send_message(message.chat.id, text = 'The token has been successfully removed from the tracking list')
        elif not message.text.lower() in trackingList:
            bot.send_message(message.chat.id, text = 'This token is either not tracked or has been deleted')
        else :
            bot.send_message(message.chat.id, text = 'Try again from the beginning')
        switcher = -1

    if message.text[0] == 'N' and message.text[1] == 'e' and message.text[2] == 'w' and message.text[3] == ' ' and message.text[4] == 'B' and message.text[23] == 'n' and message.text[24] == 't': # substitute your values in the example, processing the OttoBASEDeployments channel
        for i in message.text:
            if i == '(' and counter == -1:
                counter = 0

            elif i == ')' and counter == 0:
                counter = -1
                ParsTocen = ''.join(ParsTocen)
                print(ParsTocen)
                if ParsTocen in trackingList:
                    bot.forward_message('ID of the channel to which notifications will be sent', message.chat.id, message.message_id)
                ParsTocen = []

            elif counter == 0:
                ParsTocen.append(i.lower()) 


bot.polling(none_stop=True)