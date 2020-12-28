# enumerate() Function
for i, char in enumerate('Hellllooo'):
    print(i, char)

for j, chars in enumerate(list(range(100))):
    if chars == 50:
        print(f'index of 50 is: {chars}')
