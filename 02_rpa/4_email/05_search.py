from imap_tools import MailBox
from account import *

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    # 전체 메일
    for msg in mailbox.fetch(limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 읽지 않은 메일
    for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 보낸 사람
    for msg in mailbox.fetch('(FROM hello@itdaa.net)', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 글자 포함 메일
    for msg in mailbox.fetch('(TEXT "slack")', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 제목만 포함 메일
    for msg in mailbox.fetch('(SUBJECT "slack")', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 특정 날짜(ON 날짜)
    for msg in mailbox.fetch('(SENTSINCE 07-Feb-2022)', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 여러 조건
    for msg in mailbox.fetch('(SENTSINCE 07-Jan-2022 SUBJECT "slack")', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)
    
    # 여러 조건
    for msg in mailbox.fetch('(OR SENTSINCE 07-Jan-2022 SUBJECT "slack")', limit=5, reverse=True):
        print(f'{msg.from_} {msg.subject}')
    print('=' * 50)