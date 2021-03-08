while True:
    s = input('Enter something(Enter quit to exit):')
    # 换行替换
    s = s.replace('\r', '')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
