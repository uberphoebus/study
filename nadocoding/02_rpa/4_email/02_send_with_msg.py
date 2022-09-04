import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '테스트 메일'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'uberphoebus@naver.com' # 여러 사람 ,로 가능
msg.set_content('테스트 본문')
# msg['Cc'] = '참조인 메일'
# msg['Bcc'] = '비밀참조인 메일'
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)