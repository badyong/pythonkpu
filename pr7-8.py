phone_book = {}
phone_book["홍길동"] = "01012345678"
phone_book["이순신"] = "12345678901"
phone_book["강감찬"] = "12121212122"
print(phone_book)
print(phone_book.values())
print(phone_book.items())
for name,phone_num in phone_book.items():
    print(name,':',phone_num)
