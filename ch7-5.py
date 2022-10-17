import random
Question = []
Question.append("100+200")
Question.append("200+200")
Question.append("300+200")
Question.append("400+200")
Question.append("500+200")
Question.append("600+200")
Question.append("700+200")
Question.append("800+200")
Question.append("900+200")
Question.append("1000+200")

q = random.choice(Question)
print(eval(q))