package solutions

func majorityElement(nums []int) int {
    length := len(nums)
	major := length / 2
	counter1 := make(map[int]int)

	for i, _ := range nums {
		if counter1[nums[i]] > 0 {
			// Add 1 to the counter
			counter1[nums[i]] += 1
		} else {
			// Otherwise, create a new counter for that new letter
			counter1[nums[i]] = 1
		}
	}

	for key, element := range counter1 {
		if element > major {
			return key
		} else {
			continue
		}
	}
	return 0
    
}
