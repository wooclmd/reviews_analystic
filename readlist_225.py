data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 100000 == 0:
			print(len(data))
print('總共有', len(data), '筆留言')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均每筆留言有', sum_len / len(data), '個字')

new = []
for d in data:  #每筆留言(data)中的字(d) 一筆一筆叫出來
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料小於100')
print(new[5]) 

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言中有提到good')
print(good[0])