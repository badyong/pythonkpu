import string
t = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"
src_str = string.ascii_uppercase
t2 = list(t)
count = 0
for ch in t2:
    if ch in src_str:
        count += 1
print("느낌표의 개수:",t.count('!'))
print("대문자의 개수:",count)