import telebot;
bot = telebot.TeleBot('6043847875:AAEF5ahSJIcDacZRQapGwrXMTSto6Yloy5o')
from telebot import types 
TO_CHAT_ID = 299077924


@bot.message_handler(commands=['start','command1'])

def welcome(message):

     photo = open('D:\\bot\\NITS_small.jpg', 'rb')
     bot.send_photo(message.chat.id, photo)
     markup = types.InlineKeyboardMarkup(row_width=1)
     item = types.InlineKeyboardButton('Подать документы', callback_data='qvestion1')
     markup.add(item)


     bot.send_message(message.chat.id, 'Привет! Я бот для вопросов о магистерской программе "Предприниматель в биомедицине" Сеченовского университета! Задай мне любой вопрос, в течение 24 часов ты получишь ответ\n'





'Поторопись!\n'
'Дедлайн подачи документов - 30 июля\n'
'информация', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)            
def callback_worker(call):
        
     if call.message:
            
          if call.data == 'qvestion1':
               
               markup2 = types.InlineKeyboardMarkup(row_width=1)
               item2 = types.InlineKeyboardButton('оплатить', callback_data='qvestion2')
               markup2.add(item2)
               bot.send_message(call.message.chat.id, 'подай документы:\n'
'узнай о программе', reply_markup=markup2)

            
          elif call.data == 'qvestion2':
                 
               bot.send_message(call.message.chat.id, 'Перейти на сайт\n')
@bot.message_handler(content_types=['text','photo'])
def all_messages(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


                




bot.polling()


