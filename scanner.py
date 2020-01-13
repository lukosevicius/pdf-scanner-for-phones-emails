#! python3

import re
text="something 444-555-0000 something, also , 555-0000, (415) 555-0000, 555-0000 ext 12345, 555-0000 ext. 123, 555-0000 x12345 (2-5 ext digits) "


#Regex for phones (US numbers only)

phoneRegex = re.compile(r'''
# Possible variations: 
# 444-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, 555-0000 ext. 123, 555-0000 x12345 (2-5 ext digits) 
(
(\d\d\d|\(\d\d\d\))?   # area code (optional)
(\s|-)                      # separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
((\s ext(\.)? \s)|\s x)      # extension's word part (optional)
 (\d{2,5}))?                   # extension's 2-5 digits (optional)
)''', re.VERBOSE)


mo = phoneRegex.findall(text)

def firstOnly(mo):
    newList = []
    for el in mo:
        newList.append(el[0])
    return newList

phonesList = firstOnly(mo)
print(phonesList)