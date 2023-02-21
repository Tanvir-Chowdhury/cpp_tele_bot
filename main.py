#import logging
#from os import environ as env
from dotenv import load_dotenv

import telebot
import openai

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

#chatidlist = [1056094976]

BOT_PERSONALITY = "Please pretend that you don't know anything other than c++ programming. now reply for the following texts if you find it related to c++ in a friendly tone: "

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)

load_dotenv()
bot = telebot.TeleBot('5911304747:AAE9qUSJo7ODtu3xezGjYixIJ20J5IQvW1s')
openai.api_key = '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'
keep_alive()

@bot.message_handler(func=lambda message: message.chat.type == "private")
def get_codex2(message):
    #user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.chat.id == 1056094976:
        prompt1 = '"""\n{}{}\n"""'.format(BOT_PERSONALITY,message.text)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt1,
            temperature=0.2,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['"""'])


        bot.send_message(message.chat.id,f'\n{user_name},\n{response["choices"][0]["text"].strip()}\n')


@bot.message_handler(func=lambda message: message.chat.type == "supergroup")
def get_codex(message):
    #user_id = message.from_user.id
    user_name = message.from_user.first_name
    if '/cpp' in message.text:
        prompt1 = '"""\n{}{}\n"""'.format(BOT_PERSONALITY,message.text.replace("/cpp", ""))
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt1,
            temperature=0.2,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['"""'])


        bot.send_message(message.chat.id,f'\n{user_name},\n{response["choices"][0]["text"].strip()}\n')

@bot.message_handler(func=lambda message: message.chat.type == "group")
def get_codex3(message):
    #user_id = message.from_user.id
    user_name = message.from_user.first_name
    if '/cpp' in message.text:
        prompt1 = '"""\n{}{}\n"""'.format(BOT_PERSONALITY,message.text.replace("/cpp", ""))
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt1,
            temperature=0.2,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['"""'])


        bot.send_message(message.chat.id,f'\n{user_name},\n{response["choices"][0]["text"].strip()}\n')


bot.infinity_polling()
