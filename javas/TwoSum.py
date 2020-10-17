def twoNumberSum(arr, target):
	
	for num in arr:
		potMatch = target - num
		if potMatch in arr and potMatch != num:
			return [num, potMatch]
		else:
			continue
			
	return []
