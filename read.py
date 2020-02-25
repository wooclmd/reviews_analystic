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

