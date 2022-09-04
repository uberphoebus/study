import smtplib
from account import *

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    
    subject = 'test mail'
    body = 'mail body'
    
    msg = f'Subject: {subject}\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'uberphoebus@naver.com', msg)
    # 발신자, 수신자, 메시지