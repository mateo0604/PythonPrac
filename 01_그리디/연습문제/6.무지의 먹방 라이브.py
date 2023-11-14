from heapq import heapify,heappush,heappop
food_items = [3,1,2]
heap = []
for i,v in enumerate(food_items):
    heappush(heap,(v,i+1))
# print(heap)

# heap.sort(key = lambda x : x[1])
s = heappop(heap)
print(s[1])
print(heap)