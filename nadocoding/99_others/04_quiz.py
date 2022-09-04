# 신조어 퀴즈 클래스

# Word 클래스 작성
# __init__(...) : 신조어, 보기1, 보기2, 정답을 받아서 멤버 변수 설정
# show_question(...) : 질문 내용 표시
# check_answer(...) : 입력값이 정답인지 확인하여 '정답', '오답' 출력

class Word:
    def __init__(self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer
    
    def show_question(self):
        print(f'"{self.word}"의 뜻은?')
        print(f'1. {self.ex1}')
        print(f'2. {self.ex2}')
    
    def check_answer(self, user_input):
        if user_input == self.answer:
            print('정답')
        else:
            print('오답')

word = Word('얼죽아', '얼어 죽어도 아메리카노', '얼굴만은 죽어도 아기피부', 1)
word.show_question()
word.check_answer(int(input('=> ')))