string_in = input('\nEnter a phrase to be acronyzed...\n\n')
parts = string_in.split(' ')
result = ''
for i in range(len(parts)):
    result += parts[i][0].upper()
print('Result: {}'.format(result))
