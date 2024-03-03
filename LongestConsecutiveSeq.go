func longestConsecutive(nums []int) int {

    var trackslice []int
    var m []int

    
    numberSet := make(map[int]bool)
    for _, number := range nums {
        numberSet[number] = true
    }
    
    uniqueNumbers := make([]int, 0, len(numberSet))
    for number := range numberSet {
        uniqueNumbers = append(uniqueNumbers, number)
    }

    nums = uniqueNumbers
    sort.Ints(nums)

    for i, num := range nums {
        
        if i + 1 == len(nums) {
            trackslice = append(trackslice, num)
            m = append(m, len(trackslice))
            break
        }

        if num + 1 != nums[i + 1] {
            // check if next digit is consecutive to current digit; if so, add non-empty tracking slice to map with length mapped
                trackslice = append(trackslice, num)
                m = append(m, len(trackslice))
                trackslice = nil // reset tracking slice
            
        } else {
                trackslice = append(trackslice, num) 
            }
    }

    sort.Ints(m)
    
   
   if len(m) > 0 {
        return m[len(m) - 1]
   } else {
       return 0
   }
    
}