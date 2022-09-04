import os

# 파일 기본
print(os.getcwd()) # 현 작업 공간
os.chdir('..')
print(os.getcwd())
os.chdir('../..')
print(os.getcwd())
os.chdir('C:/avatarProject/venv/trader/rpa_basic/2_desktop')
print(os.getcwd())

# 파일 경로
file_path = os.path.join(os.getcwd(), 'my_file.txt')
print(file_path)

# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r'C:\avatarProject\venv\trader\rpa_basic'))

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성 날짜
ctime = os.path.getctime('11_file_system.py')
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S'))

# 파일의 수정 날짜
mtime = os.path.getmtime('11_file_system.py')
print(datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S'))

# 파일의 마지막 접근 날짜
atime = os.path.getatime('11_file_system.py')
print(datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S'))

# 파일 크기(바이트 단위)
size = os.path.getsize('kiwoom_menu.png')
print(size)

# 파일 목록 가져오기
l = os.listdir('..')
print(l)

# 하위 폴더 모두 포함 가져오기
result = os.walk('..')
for root, dirs, files in result:
    print(root, dirs, files)

# 폴더에서 특정 파일 찾기
name = '11_file_system.py'
result = []
for root, dirs, files in os.walk('.'):
    if name in files:
        result.append(os.path.join(root, name))
print(result)

# 특정 형태(확장자)의 파일 찾기
import fnmatch
pattern = '*.py'
result = []
for root, dirs, files in os.walk('.'):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
print(result)

# 주어진 경로가 파일인지 경로인지 확인
tf = '11_file_system.py'
print(os.path.isdir(tf))
print(os.path.isfile(tf))

# 주어진 경로 존재 여부
if os.path.exists('rpa_basic'):
    print('t')
else:
    print('f')

# 파일 만들기
# open('new_file.txt', 'a').close() # 빈 파일 생성

# 파일명 변경하기
# os.rename('new_file.txt', 'new_file_rename.txt')
# 파일 삭제
# os.remove('new_file_rename.txt')

# 폴더 삭제
# os.rmdir('new_folder_rename')

# 폴더 만들기
# os.mkdir('new_folder')

# 하위 폴더 가지는 폴더 생성
# os.makedirs('new/a/b/c')

# 폴더명 변경
# os.rename('new_folder', 'new_folder_rename')

# 폴더 지우기 : 비어 있지 않은 폴더
import shutil
# shutil.rmtree('new_folder')

# 파일 복사
shutil.copy('box.png', 'new_folder')
shutil.copy('box.png', 'new_folder/test.png')

# shutil.copyfile('box.png', 'new_folder/test1.png')

shutil.copy2('box.png', 'new_folder/test3.png')

# copy, copyfile : 메타 정보 복사하지 않음
# copy2 : 메타정보 복사

# 폴더 복사
# shutil.copytree('new_folder', 'new_folder2')

# 폴더 이동
shutil.move('new_folder2', 'new_folder')