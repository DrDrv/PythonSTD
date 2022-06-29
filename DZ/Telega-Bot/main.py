from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler, PollAnswerHandler, PollHandler


from conf_ig import conf


updater = Updater(token=conf())
dispatcher = updater.dispatcher

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет! Я бот. Поговори со мной.")

# функция обработки текстовых сообщений
def echo(update, context):
    text = 'ECHO: ' + update.message.text 
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=text)    

def close_keyboard(update, context):
    update.message.reply_text('',reply_markup = ReplyKeyboardRemove())

# функция обработки команды '/game'
def game(update, context):

    def pole_game():
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Кнопка 1', callback_data='1'),
                    InlineKeyboardButton(text='Кнопка 2', callback_data='2'),
                    InlineKeyboardButton(text='Кнопка 3', callback_data='3')
                ],
                [
                    InlineKeyboardButton(text='Кнопка 4', callback_data='4'),
                    InlineKeyboardButton(text='Кнопка 5', callback_data='5'),
                    InlineKeyboardButton(text='Кнопка 6', callback_data='6')
                ],
                [
                    InlineKeyboardButton(text='Кнопка 7', callback_data='7'),
                    InlineKeyboardButton(text='Кнопка 8', callback_data='8'),
                    InlineKeyboardButton(text='Кнопка 9', callback_data='9')
                ]
            ])
            
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Игра 'Крестики - нолики'", reply_markup=reply_markup)


    pole = '*********'                                  # Поле - 9 ячеек, хотел списком, но мороки с проверкой много
    step = 1                                            # Ходы - разделяем игроков по чет/нечет
    sign = ''                                           # Символ X/O

    def check_win(pole_st,st):
        win_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    #Выигрышные комбинации
        return [l for l in win_comb if pole_st[l[0]] == st and pole_st[l[1]] == st and pole_st[l[2]] == st]

    def iis(pol):
        import random
        new_pole = []
        new_pole = [l for l in range(0,len(pol)) if pol[l]=='*']
        f = lambda x,k: pol[:k] + x + pol[k+1:]
        for i in new_pole:
            pol = f('O',i)
            if len(check_win(pol,'O')) != 0: 
                return(pol)
            pol = f('*',i)
        for i in new_pole:    
            pol = f('X',i)
            if len(check_win(pol,'X')) != 0:
                pol = f('O',i)
                return(pol)
            pol = f('*',i)
        rand_shag = random.randrange(0, len(new_pole))
        pol = pol[:new_pole[rand_shag]] + 'O' + pol[new_pole[rand_shag]+1:]
        return(pol)
 
    def button(update, context):
        global variant
        query = update.callback_query
        query.answer()
        variant = query.data
        msg = "Тра-та-та"

        query.edit_message_text(msg, reply_markup = )




    
    res = 0
    while res != -1:
        if step%2 == 0: 
            sign = 'O'
            context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Мой ход...')
            pole = iis(pole)
            if len(check_win(pole,sign)) != 0:
                txt = f'Победу одержали {sign} на {step} ходу \n Игра закончена!'
                context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=txt)
                break
            step += 1


        else: 
            sign = 'X'
            questions = 'Ваш Ход'
            # answer = ['1','2']
            a = 1
            
            #context.bot.send_poll(
                #update.effective_chat.id, questions, answer, 
                #is_anonymous=False, allows_multiple_answers=True,
                #)


        
            print(a)
            a = int(a)
            if a > 0 and a < 10:
                a -= 1
                if str(pole[a]) != '*': 
                    #print('Эта ячейка уже занята !')
                    step -= 1
                else: pole = pole[:a] + sign + pole[a+1:]
            
            if len(check_win(pole,sign)) != 0:
                txt = f'Победу одержали {sign} на {step} ходу \n Игра закончена!'
                context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
                #print(f'Игра закончена!')
                break
            step += 1
            if step == 10: 
                res = -1
                #print(f'Игра закончена! Ничья! ')
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Не понимаю, о чём вы.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('stop', start)
dispatcher.add_handler(start_handler)      

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик команды '/game'

game_handler = CommandHandler('game', game)
dispatcher.add_handler(game_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений

updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()