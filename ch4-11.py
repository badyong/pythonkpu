id = "ilovepython"
pw = "mypass1234"
s = input("아이디를 입력하시오:")
sp = input("비밀번호를 입력하시오:")
if s == id and pw == sp:
    print("환영합니다")
elif s == id and pw != sp:
    print("비밀번호가 틀렸습니다")
else:
    print("아이디를 찾을 수 없습니다")