'''
입력 : 0001100
출력 : 1
'''

data=input()

count0 = 0
count1 = 0

for i in range(len(data)-1):
  if data[i] != data[i+1]:
    if data[i] == '1':
      count0 += 1
    else :
      count1 += 1

if i == '1':
  count0 +=1
else :
  count1 +=1 
  
print(min(count0,count1))
