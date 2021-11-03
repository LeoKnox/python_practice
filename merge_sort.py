def merge_sort(sort_arr):
	mid = len(sort_arr)//2;
	print(mid)

	left = sort_arr[:mid]
	right = sort_arr[mid:]

	print(left)
	print(right)

	x = y = z = 0

	while (x < len(left) and y < len(right)):
		if left[x] < right[y]:
			sort_arr[z] = left[x]
			x += 1
		else:
			sort_arr[z] = right[x]
			y += 1
		z += 1

	while (x < len(left)):
		sort_arr[z] = left[x]
		x += 1
		z += 1

	while (y < len(right)):
		sort_arr[z] = right[y]
		y += 1
		z += 1

start_arr = [5,9,2,8,4,3,1]
merge_sort(start_arr)

print(start_arr)
