import smtplib
import pandas as pd
import csv
from email.message import EmailMessage
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import requests


# csv파일 읽는 부분
with open('ex.csv', newline='', encoding="UTF8") as f:
    reader = csv.reader(f)
    next(f)
    data = list(reader)

for i,v in enumerate(data) :
    print('-------------')
    print(i+1,'번째 시작')


    if not v[0]:
        print(i+1,'번째에 회사 이름이 없어요')
    elif not v[1]:
        print(i+1,'번째에 브랜드 이름이 없어요')
    elif not v[2]:
        print(i+1,'번째에 링크가 없어요')
    elif not v[3]:
        print(i+1,'번째에 메일 주소가 없어요')
    else:
        # 보내는 사람 / 받는 사람 / 제목 입력
        msg = MIMEMultipart('alternative')
        msg["From"] = 'Relay <info@the-relay.kr>'
        msg["To"] = v[3]
        msg["Subject"] = v[0]+"만의 리세일 마켓을 열고, 자사몰을 활성화 시키세요!"

        contents = """
            컨텐츠 => html

        """
        part2 = MIMEText(contents, 'html')
        msg.attach(part2)


        part = MIMEBase('application', "octet-stream")
        with open("RELAY.pdf", 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment", filename="RELAY.pdf")
        msg.attach(part)

        with SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login('info@the-relay.kr', '비밀번호')
            smtp.send_message(msg)
            print(i+1,'번째 메일 전송')
        print(i+1,'번째 끝')

