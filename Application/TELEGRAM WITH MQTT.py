"""Bibliotecas necessarias:
    import numpy as np, import telebot
    e import paho.mqtt.client as 
    paho tem que instalar"""

import numpy as np
import paho.mqtt.client as paho
import telebot
import ast
import time
from telebot import types
import json

global cid, msgPrice, ret, matrix, CPF, id_chat, cont
cont = 0
matrix = np.empty([0,2])

"""Conexões do broker e telegram:"""
broker = "SEU TOKEN broker"
port=1883
bot = telebot.TeleBot("SEU TOKEN")


def on_publish(client,userdata,result):
    
    pass

client1 = paho.Client("control1")  
client1.username_pw_set("user", "key")                       
client1.on_publish = on_publish                         
client1.connect(broker,port) 
    
@bot.message_handler(commands=['start'])
def handle_text(message):
    cid = message.chat.id
    msgPrice = bot.send_message(cid, 'Digite o seu CPF:')
    bot.register_next_step_handler(msgPrice , init_command)

def init_command(message):
    global matrix, cont, CPF

    CPF = message.text
    id_chat = message.chat.id
    if (CPF.isnumeric()):
        if cont == 0:
            matrix = np.append(matrix, [[id_chat, CPF]], 0)
            cont = cont + 1
        else:
            search = np.where(matrix[cont-1][0] == id_chat, 0, 1)
            if search == 1 and matrix[cont-1][1] != CPF:
                matrix = np.append(matrix, [[id_chat, CPF]], 0)
 
        bot.send_message(id_chat,f"Você confirma {CPF} como seu CPF, se sim escolha /comando ou se não /start")
       
    else:
        bot.send_message(chat_id=id_chat, text=f"Você digitou alguma letra, por isso aperte /start para enviar o ID corretamente")

@bot.message_handler(commands=['comando'])
def menu(message):
    cid = message.chat.id

    menuKeyboard = types.InlineKeyboardMarkup() 
    
    menuKeyboard.add(types.InlineKeyboardButton('Ligar saida1', callback_data='sd1=1'), 
                    types.InlineKeyboardButton('Desligar saida1', callback_data='sd1=0')) 
                    
    menuKeyboard.add(types.InlineKeyboardButton('Ligar saida2', callback_data='sd2=1'), 
                    types.InlineKeyboardButton('Desligar saida2', callback_data='sd2=0')) 
                    
    menuKeyboard.add(types.InlineKeyboardButton('Ligar saida3', callback_data='sd3=1'), 
                    types.InlineKeyboardButton('Desligar saida3', callback_data='sd3=0')) 
                    
    menuKeyboard.add(types.InlineKeyboardButton('Ligar saida4', callback_data='sd4=1'), 
                    types.InlineKeyboardButton('Desligar saida4', callback_data='sd4=0')) 
                    
    bot.send_message(cid, "OPÇÕES", reply_markup=menuKeyboard)
@bot.callback_query_handler(func=lambda callback_data: True)
def handle_query(callback_data):
    global CPF
    escolha = callback_data.data
    client1.publish(f'{CPF}/controls/sd', escolha)
    bot.answer_callback_query(callback_query_id=callback_data.id,
                        show_alert=False,
                        text=f"Você escolheu {escolha}. Se deseja mandar outro comando no mesmo ID digite /comando OU /start para id diferente")
            

bot.polling()
