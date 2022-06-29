from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, _):
    keyboard = [
                [
                    InlineKeyboardButton(text='1', callback_data='1'),
                    InlineKeyboardButton(text='2', callback_data='2'),
                    InlineKeyboardButton(text='3', callback_data='3')
                ],
                [
                    InlineKeyboardButton(text='4', callback_data='4'),
                    InlineKeyboardButton(text='5', callback_data='5'),
                    InlineKeyboardButton(text='6', callback_data='6')
                ],
                [
                    InlineKeyboardButton(text='7', callback_data='7'),
                    InlineKeyboardButton(text='8', callback_data='8'),
                    InlineKeyboardButton(text='9', callback_data='9')
                ]
            ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если 
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы. 
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # редактируем сообщение, тем самым кнопки 
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"Выбранный вариант: {variant}")

def help_command(update, _):
    update.message.reply_text("Используйте `/start` для тестирования.")

if __name__ == '__main__':
    # Передайте токен вашего бота.
    updater = Updater("5513940923:AAEEOoRDz_tACeXlUWJcQvO8l_A3cDzzhGU")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Запуск бота
    updater.start_polling()
    updater.idle()