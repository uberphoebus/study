import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
txt = '다운로드'
msg['Subject'] = txt
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'uberphoebus@naver.com' # 여러 사람 ,로 가능
msg.set_content(txt)

with open(r'C:\workspace\avatarProject\basic_rpa\4_email\screenshot.png', 'rb') as f:
    # MIME type으로 메인/서브타입 확인
    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=f.name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)