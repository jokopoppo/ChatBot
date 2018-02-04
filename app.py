from flask import Flask, request
import json
import requests
import os
import redis

r = redis.from_url(os.environ.get("redis://h:peb8a946b775505a189710b878a91e63b56ad8512c2fb2b05e83b81c9720c8f4b@ec2-34-196-130-224.compute-1.amazonaws.com:51659","ec2-34-196-130-224.compute-1.amazonaws.com"))
# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป

global LINE_API_KEY
LINE_API_KEY = 'Bearer h+qeE1xA1qN6BdAqq411jgmkMh3e93g0+Vpe4139BlsEsFC2gKPecE79EGp426PeyzpNcITX2Cb1hdzw1GI0hOivGtpmNH+/j6CLr6vjLd5to1PSqV00zZTauNPB7ien1uVju+dX2+ew0fhGhHm7OAdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyStack = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    umsgText =  msg_in_json["events"][0]['message']['text']
    userID = msg_in_json["events"][0]['source']['userId']
    r.lpush("kkk","eiei")
    umsgText=msgcon(umsgText,userID);

    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไป-มา (แบบ json)
    replyStack.append(umsgText)
    reply(replyToken, replyStack[:5])

    return 'OK',200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ

    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type": "text",
            "text": text

        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

def msgcon(umsgText,userID):
    if umsgText=="room":
        umsgText="1-12"
    if userID=="U0818e020c39a3d0945f679469801e2bf":
        umsgText+="\r\nhi winner"



    return umsgText

if __name__ == '__main__':
    app.run()
