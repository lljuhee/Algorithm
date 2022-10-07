'''
오름차순 정렬 -> 선택 정렬 사용
'''

n=int(input())
data=[]

for i in range(n):
  data.append(int(input()))

for i in range(n):
  min_index=i
  for j in range(i+1, n):
    if data[min_index] > data[j]:  
      min_index=j
  data[i], data[min_index]=data[min_index], data[i] 

for k in data:
  print(k)
