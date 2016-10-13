#!python3
# creates a place to save passwords for different account and can
# easily fetch a particular password by just passing the account name
import sys,pyperclip
passwords = {'email':'flajslkasjdlkasdjk',
              'blog':'blog',
              'facebook':'dfldflkakjfla'}
if len(sys.argv)<2:
    print('command line arguments cannot be less than 2 values')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print("password for "+account+" copied to clipboard")
else:
    print("No account named "+account)
    

    
