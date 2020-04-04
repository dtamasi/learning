# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip
import re

phoneRegex = re.compile(
    r'''((\d{3}|\(\d{3}\))?         #area code(3digits or:| (3 digits)escaped paranthesis ex: 415 or (415)
    (\s|-|\.)?                      # separator can be \s space or| - hyphen or| .period ex: 415-320.600
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension spaces\s for ext or x or ext. and space for 2 to 5 {d}
    )''', re.VERBOSE)


emailRegex = re.compile(
    r'''([a-zA-Z0-9._%+-]+  # username: listlower&UpperCase,digits,
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name gmail,yahoo,fairmont
    (\.[a-zA-Z]{2,4})   # dot-something [.period,list of lowerupper adn 2 to 4 digits
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)

for groups in emailRegex.findall(text):
  matches.append(groups[0])

if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipboard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')
