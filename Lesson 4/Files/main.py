# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')  # здесь указываем режим в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()