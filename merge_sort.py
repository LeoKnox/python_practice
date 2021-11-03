def merge_sort(sort_arr):
	mid = len(sort_arr)//2;
	print(mid)

	left = sort_arr[:mid]
	right = sort_arr[mid:]

start_arr = {5,9,2,8,4,3,1}
merge_sort(start_arr)

print(start_arr)
