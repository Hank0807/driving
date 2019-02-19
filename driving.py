country = input('請輸入國家 = ')
age = input('請輸入年紀 = ')
age = int(age)

if country == '台灣':
    if age > 18:
        print('可以考駕照了！')
    else:
        print('年紀太小哦。')

if country == '美國':
    if age > 20:
        print('可以考駕照了！')
    else:
        print('年紀太小哦。')
else:
    print('一定要選台灣或美國唷。')