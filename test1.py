# from collections import defaultdict

# from numpy import append
# g = defaultdict(list)
# g[1].append('asdfsa')
# g[1].append('DFHISDF')
# g[2].append('wer')
# # g[1][0].remove('a')
# for i in g:
#     for j in g[i]:
#         print(j)
#         print(j[0])
# print("".join(g[1])[:-1])
d=[1,2,3,4,5]
s=set(d)
tp=[]
# tp.append(6)
s.discard(8)
# tp.update(s)
for i in range(2):
    tp.extend(s)
# tp.extend(d)

print(tp)