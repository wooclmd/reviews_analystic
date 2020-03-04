data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 100000 == 0:
			print(len(data))

print(len(data))

wc = {}  #每個字(key)配對一個數字(value)
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進wc字典,第一次遇到

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
	word = input('你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('沒有出現過的字')






# for d in data:
# 	sum_len = sum_len + len(d)

# print('平均是', sum_len / len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言小於100')


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])
