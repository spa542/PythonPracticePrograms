# Advanced Patterns

import re

pattern = re.compile(r"(^[a-zA-Z0-0_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'b@b.com'


a = pattern.search(string)
print(a)

# Password Checker Challenge
# At least 8 char long
# Contains any sort letters, number $%#@
# has to end with a number

pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

password = 'asjdfkasjd4253e52$$5'

check = pattern2.fullmatch(password)
print(check)
