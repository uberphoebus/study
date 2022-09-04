from audioop import reverse
from account import *
from imap_tools import MailBox

mailbox = MailBox('imap.gmail.com', 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX')

for msg in mailbox.fetch(limit=3, reverse=True): # 최근부터
    print(msg.subject)
    print(msg.from_)
    print(msg.to)
    # print(msg.cc)
    # print(msg.bcc)
    print(msg.date)
    print(msg.text)
    # print(msg.html)
    print('=' * 30)
    
    # 첨부파일 다운로드
    for att in msg.attachments:
        print(att.filename)
        print(att.content_type)
        print(att.size)
        
        with open('download_' + att.filename, 'wb') as f:
            f.write(att.payload)

mailbox.logout()