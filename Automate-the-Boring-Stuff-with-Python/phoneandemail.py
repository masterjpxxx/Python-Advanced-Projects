import re, pyperclip

#PHONE NUMBER FORMAT: 415-555-4242, (415)-555-4242, 415 555 4242, 415.555.4242
phoneregex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #Area Code
    (-|\s|\.)?                      #Separator
    (\d{3})                         #First 3 Digits
    (-|\s|\.)?                      #Separator
    (\d{4})                         #Last 4 Digits
    (\s*|(ext|x|ext.)\s*(\d{2,5}))? #Optional extensions
)''', re.VERBOSE)

#Sample email: a@b.com

emailregex = re.compile(r''' (
    [a-zA-Z0-9._%+-]+               #Username
    @                               #@ symbol
    [a-zA-Z0-9._%+-]+               #domain
    (\.[a-zA-Z]{2,4})               #dot-something
)''', re.VERBOSE)


text = str(pyperclip.paste())

matches = []

for groups in phoneregex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneregex += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in emailregex.findall(text):
    matches.append(groups[0])
    
    #print(matches)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to the Clipboard:")
    print('\n'.join(matches))
else:
    print("No Phone Numbers or Email addresses were found!")