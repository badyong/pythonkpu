t = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20(LG U+ Mystick Pink 30%, SKT Mystic Blue discloesd) '
t = t.lower()
company = ['kt','skt','samsung','lg']
for word in company:
    t = t.replace(word,'*')
print(t)