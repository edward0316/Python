'''
file = open('test.txt')
text = file.readlines()
print(text)
for i in range(len(text)):
    text[i] = text[i].split(' ')
    text[i][3] = text[i][3].replace('\n','')
print(text)
'''
d = {'a':['1','2'],'d':['3','4']}

for i in d.keys():
    f = open('test.txt', 'a')
    text = '%s %s %s\n' % (i, d[i][0], d[i][1])
    f.writelines(text)
    f.close()

"""
users = []
passwords = []
tags = []
counts = []
file = open('test.txt')
text = file.readlines()
file.close()
for i in range(len(text)):
    user, password,tag, count = text[i].split(' ')
    users.append(user)
    passwords.append(password)
    tags.append(tag.strip())
    counts.append(count.strip())

counts[users.index('kathy')] = '2'

file = open('test.txt','w')
file.close()

for i in range(len(text)):
    text_final = users[i] + ' ' + passwords[i] + ' '+tags[i] + ' '+counts[i] + '\n'
    file = open('test.txt','a')
    file.writelines(text_final)
    file.close()

print(len(text))
print(text_final)
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
"""
'''
user, password, tag = text.split(' ')
tag = '1'
text = user+ ' ' + password + ' ' + tag
print(text)
print(user)
print(password)
print(tag)
'''
