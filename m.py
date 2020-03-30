name = input('enter your name: ')
subscribe = False

if name:
    if not subscribe:
        print('your not yet subscribed')
    var = input('would you like to subscribed')
    if var == 'yes':
        print('welcome ' + name)
else:
    print('no name was given')
