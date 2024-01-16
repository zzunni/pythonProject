# 6.2 guess_me, number를 비교하는 while 문 작성
guess_me=7
number=1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it')
        break
    elif number > guess_me:
        print('oops')
        break

    number+=1

# 6.3 guess_me, number를 비교하는 for 문 작성
