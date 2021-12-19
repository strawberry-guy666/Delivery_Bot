import telebot;
bot = telebot.TeleBot('5056942756:AAHdJTmVGD6Ltj3nUMCEVBONf3qKQiUvk5Q')
from telebot import types 
TO_CHAT_ID = 282901555


@bot.message_handler(commands=['start','command1'])

def welcome(message):

     photo = open('Картинка.png', 'rb')
     bot.send_photo(message.chat.id, photo)
     markup = types.InlineKeyboardMarkup(row_width=1)
     item = types.InlineKeyboardButton('Купить билет', callback_data='qvestion1')
     markup.add(item)


     bot.send_message(message.chat.id, 'Beton FTP\nВрываемся в f.t.p. формате вечеринки хип-хоп + техно и электро.Точка сбора бар "Слезы". Начнем с мемфиса и хип-хопа от Naked и Cheykeys, который подкрепится еврорэпом в лайв исполнении Polo3xo. Вторую часть банкета открывает Арина Петрова с подборкой электроники в смеси басс-этно мотивов стран СНГ. Следом Dawn Razor, который отмечен на более 30 релизах и выступлениях по всей России, отыграет техно канонических форм с ломаными ритмами breakbeat, electro-breaks и bass. Zr Dfkt презентует неизданный кислотный эйсид материал из самых недр подземных владений. При поддержке участников команды выстрел из жуткой смеси электроники и рэпа Strawberry guy 666 и Helg.\n'

'22:00->00:30\n'
'Naked\n'
'Cheykeys\n'
'Pölo 3xo (live)\n'

'00:30->6:00\n'
'Arina Petrova\n'
'Dawn Razor (R & S, ARTS, Illegal Alien)\n'
'Zr Dfkt (Darksidekilla rec)\n'
'Strawberry guy 666\n'
'Helg\n'

'Предпродажа в данном боте (100 билетов по 400 рублей)\n'
'Цена на входе: 600 ( 500 с репостом афиши)\n'

'24 декабря 22:00\n'
'@slozy_bar\n'
'Москва, Костомаровский пер., 3 стр 12', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)            
def callback_worker(call):
        
     if call.message:
            
          if call.data == 'qvestion1':
               
               markup2 = types.InlineKeyboardMarkup(row_width=1)
               item2 = types.InlineKeyboardButton('оплатить', callback_data='qvestion2')
               markup2.add(item2)
               bot.send_message(call.message.chat.id, 'Для того чтобы купить билет нужно оплатить 400 рублей на карту:\n'
                                '5484 3800 1964 5753\n'
                               '💡Ты можешь оплатить одним платежом за несколько человек.\n'
'(Из расчета 400 рублей = 1 человек)''После успешной оплаты нажми кнопку ниже👇', reply_markup=markup2)

            
          elif call.data == 'qvestion2':
                 
               bot.send_message(call.message.chat.id, 'Пришли сюда скрин транзакции, имя и фамилию и мы внесем тебя в список.\n'
               'Мы детально проверяем все платежи и вносим в список тех людей, которые выполнили все вышесказанные требования.\n'
                'Если у тебя возникли какие-то проблемы с платежом и тд. — смело пиши @beton_delivery_ftp')
@bot.message_handler(content_types=['text','photo'])
def all_messages(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


                




bot.polling()


