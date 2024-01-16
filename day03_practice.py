# # 6.1 for문으로 리스트 [3,2,1,0] 출력
#
# num=[]
# for i in range(3,-1,-1):
#     num.append(i)
# print(num)

# 6.2 guess_me, number를 비교하는 while 문 작성
# guess_me=7
# number=1
#
# while True:
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it')
#         break
#     elif number > guess_me:
#         print('oops')
#         break
#
#     number+=1

# 6.3 guess_me, number를 비교하는 for 문 작성
guess_me=5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break