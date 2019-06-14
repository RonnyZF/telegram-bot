#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import serial
import logging
import datetime
import arduinoCtrl
import graphLib

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, RegexHandler,
                          ConversationHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, ReplyKeyboardMarkup


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def start(bot, update):
  now = datetime.datetime.now()
  arduinoCtrl.lectura_sensores()
  update.message.reply_text(text=main_menu_message(now),
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  now = datetime.datetime.now()
  arduinoCtrl.lectura_sensores()
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(now),
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=first_menu_keyboard())

def second_menu(bot, update):
  query = update.callback_query
  arduinoCtrl.controlar_luces()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=second_menu_message(),
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=second_menu_keyboard())

def third_menu(bot, update):
  query = update.callback_query
  arduinoCtrl.controlar_cortinas()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=third_menu_message(),
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=third_menu_keyboard())

def four_menu(bot, update):
  query = update.callback_query
  arduinoCtrl.controlar_ventiladores()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=four_menu_message(),
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=four_menu_keyboard())

def submenu_1_1(bot, update):
  query = update.callback_query
  now = datetime.datetime.now()
  graphLib.graficar_temp()
  bot.send_photo(chat_id=query.message.chat_id, photo=open('graphT.png', 'rb'), caption='Fecha: '+now.strftime("%Y-%m-%d")+' Hora: '+now.strftime("%H:%M:%S"  )+'\n')
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Grafica de temperatura en las ultimas 24 horas*',
                        parse_mode=ParseMode.MARKDOWN)

  bot.send_message(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Presione para volver al menu principal*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())
  

def submenu_1_2(bot, update):
  query = update.callback_query
  now = datetime.datetime.now()
  graphLib.graficar_hum()
  bot.send_photo(chat_id=query.message.chat_id, photo=open('graphH.png', 'rb'), caption='Fecha: '+now.strftime("%Y-%m-%d")+' Hora: '+now.strftime("%H:%M:%S"  )+'\n')

  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Grafica de humedad en las ultimas 24 horas*',
                        parse_mode=ParseMode.MARKDOWN)

  bot.send_message(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Presione para volver al menu principal*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_1_3(bot, update):
  query = update.callback_query
  now = datetime.datetime.now()
  graphLib.graficar_nivel()
  bot.send_photo(chat_id=query.message.chat_id, photo=open('graphA.png', 'rb'), caption='Fecha: '+now.strftime("%Y-%m-%d")+' Hora: '+now.strftime("%H:%M:%S"  )+'\n')

  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Grafica de nivel de alimento en el mes actual*',
                        parse_mode=ParseMode.MARKDOWN)
  bot.send_message(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Presione para volver al menu principal*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_2_1(bot, update):
  query = update.callback_query
  arduinoCtrl.encender_luces()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Se han encedido las luces*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_2_2(bot, update):
  query = update.callback_query
  arduinoCtrl.apagar_luces()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Se han apagado las luces*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_1(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_100()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran 100% abiertas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_2(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_80()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran 80% abiertas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_3(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_60()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran 60% abiertas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_4(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_40()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran 40% abiertas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_5(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_20()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran 20% abiertas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_3_6(bot, update):
  query = update.callback_query
  arduinoCtrl.cortinas_cerradas()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Las cortinas ahora se encuentran cerradas*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_4_1(bot, update):
  query = update.callback_query
  arduinoCtrl.encender_ventiladores()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Se han encendido los ventiladores*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

def submenu_4_2(bot, update):
  query = update.callback_query
  arduinoCtrl.apagar_ventiladores()
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='*Se han apagado los ventiladores*',
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=back_to_main_keyboard())

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Historico de Sensores', callback_data='m1')],
              [InlineKeyboardButton('Controlar Luces', callback_data='m2')],
              [InlineKeyboardButton('Controlar Cortinas', callback_data='m3')],
              [InlineKeyboardButton('Controlar Ventiladores', callback_data='m4')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Temperatura', callback_data='a1')],
              [InlineKeyboardButton('Humedad', callback_data='a2')],
              [InlineKeyboardButton('Nivel de alimento', callback_data='a3')],
              [InlineKeyboardButton('Menu principal', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Encender luces', callback_data='b1')],
              [InlineKeyboardButton('Apagar luces', callback_data='b2')],
              [InlineKeyboardButton('Menu principal', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def third_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Abrir 100%', callback_data='c1'),
              InlineKeyboardButton('Abrir 80%', callback_data='c2')],
              [InlineKeyboardButton('Abrir 60%', callback_data='c3'),
              InlineKeyboardButton('Abrir 40%', callback_data='c4')],
              [InlineKeyboardButton('Abrir 20%', callback_data='c5'),
              InlineKeyboardButton('Cerrar', callback_data='c6')],
              [InlineKeyboardButton('Menu principal', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def four_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Encender Ventiladores', callback_data='d1')],
              [InlineKeyboardButton('Apagar Ventiladores', callback_data='d2')],
              [InlineKeyboardButton('Menu principal', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def back_to_main_keyboard():
  keyboard = [[InlineKeyboardButton('Menu principal', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message(now):
  temp,lvl_f,hum,luz,estadoL,estadoV,estadoC = arduinoCtrl.display_sensor_data()
  return ('*Bienvenido al centro de control y monitoreo.*\n'
          'A continuacion se presenta el estado actual:\n\n'
          'Fecha: '+now.strftime("%Y-%m-%d")+' Hora: '+now.strftime("%H:%M:%S"  )+'\n'
          'Temperatura actual: *'+ temp+' °C*\n'
          'Humedad actual: *'+ hum+'%*\n'
          'Nivel de luz: *'+ luz+'%*\n'
          'Nivel de alimento: *'+ lvl_f+'%*\n'
          'Estado de las luces: *'+ estadoL+'*\n'
          'Estado de los ventiladores: *'+ estadoV+'*\n'
          'Estado de las cortinas: *'+ estadoC+'*\n\n'
          'Seleccione una opcion del menu principal:\n')

def first_menu_message():
    return('*A continuacion puede obtener una grafica del cambio en el tiempo para cada sensor.*\n\n'
           'Seleccione el sensor que desea consultar:\n')

def second_menu_message():
  return ('*El estado actual de las luces es:*\n\n'
          'Seleccione una opcion en el menu:')

def third_menu_message():
  return ('*El nivel actual de las cortinas es:*\n\n'
          'Seleccione una opcion en el menu:')

def four_menu_message():
  return ('*El estado actual de los ventiladores es:*\n\n'
          'Seleccione una opcion en el menu:')

def x_message():
  return ('*Volver al menu principal*\n\n')

def help(bot, update):
    """Send a message when the command /help is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Help!')


def echo(bot, update):
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("818687469:AAGJvxRleb3T1cY1yIgT3AQFBAT15rQao9g")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    ############################# Handlers #########################################
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(third_menu, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(four_menu, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(submenu_1_1, pattern='a1'))
    dp.add_handler(CallbackQueryHandler(submenu_1_2, pattern='a2'))
    dp.add_handler(CallbackQueryHandler(submenu_1_3, pattern='a3'))
    dp.add_handler(CallbackQueryHandler(submenu_2_1, pattern='b1'))
    dp.add_handler(CallbackQueryHandler(submenu_2_2, pattern='b2'))
    dp.add_handler(CallbackQueryHandler(submenu_3_1, pattern='c1'))
    dp.add_handler(CallbackQueryHandler(submenu_3_2, pattern='c2'))
    dp.add_handler(CallbackQueryHandler(submenu_3_3, pattern='c3'))
    dp.add_handler(CallbackQueryHandler(submenu_3_4, pattern='c4'))
    dp.add_handler(CallbackQueryHandler(submenu_3_5, pattern='c5'))
    dp.add_handler(CallbackQueryHandler(submenu_3_6, pattern='c6'))
    dp.add_handler(CallbackQueryHandler(submenu_4_1, pattern='d1'))
    dp.add_handler(CallbackQueryHandler(submenu_4_2, pattern='d2'))

    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
