class ThailandPackage:
    def detail(self):
        print('[thai]')

if __name__ == '__main__':
    print('Thai 직접 실행')
    print('직접 실행할 때만 실행됨')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('외부에서 호출')