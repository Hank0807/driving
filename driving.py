country = input('請輸入國家 = ')
age = input('請輸入年紀 = ')
age = int(age)

if country == '台灣':
    if age > 18:
        print('可以考駕照了！')
    else:
        print('年紀太小哦。')