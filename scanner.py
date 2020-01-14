#! python3

import re
text = '''
something 444-555-0000 something, also , 555-0000, (415) 555-0000, 555-0000 ext 12345, 555-0000 ext. 123, 555-0000 x12345 (2-5 ext digits) 
example@example.com exa4545mple@e455xample.com vienas.du.test@mail.co.uk naujas-naujas+naujas_naujas@email.com
'''

def start():
    scanPhones()
    scanEmails()


print(text)
#Regex for emails

def firstOnly(mo):
    newList = []
    for el in mo:
        newList.append(el[0])
    return newList

def scanPhones():

    #Regex for phones (US numbers only)

    phoneRegex = re.compile(r'''
    # Possible variations: 
    # 444-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, 555-0000 ext. 123, 555-0000 x12345 (2-5 ext digits) 
    (
    (\d\d\d|\(\d\d\d\))?        # area code (optional)
    (\s|-)                      # separator
    \d\d\d                      # first 3 digits
    -                           # separator
    \d\d\d\d                    # last 4 digits
    (
    (\s ext(\.)? \s | \s x)    # extension's word part (optional)
    (\d{2,5})                  # extension's 2-5 digits (optional)
    )?               
    )''', re.VERBOSE)

    mo = phoneRegex.findall(text)
    phonesList = firstOnly(mo)
    print(phonesList)

def scanEmails():
    emailRegex = re.compile(r'''
    (
    ([a-zA-z0-9_+.-]*)?        # first part
    @                          # @ characted
    ([a-zA-z0-9_+.-]*)?        # domain
    )''', re.VERBOSE)

    mo = emailRegex.findall(text)
    emailsList = firstOnly(mo)
    print(emailsList)

start()
