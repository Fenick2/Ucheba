def check_password(pwd):
    chk = list(pwd)
    simbols = '!@#$%*'
    digits = 0
    title = 0
    simb = 0
    for i in chk:
        if i in simbols:
            simb += 1
            continue
        elif i.isdigit():
            digits += 1
            continue
        elif i.isupper():
            title += 1
            continue

    if len(pwd) > 9 and digits > 2 and title and simb:
        return 'Perfect password'
    return 'Easy peasy'



pwd = input()
print(check_password(pwd))