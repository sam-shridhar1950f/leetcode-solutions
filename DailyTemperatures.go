func dailyTemperatures(temperatures []int) []int {
   
    answer := make([]int, len(temperatures))
  
    var stack []int

    for i, t := range temperatures {

        for len(stack) > 0 && t > temperatures[stack[len(stack)-1]] {

            topIndex := stack[len(stack)-1]
            stack = stack[:len(stack)-1]

            answer[topIndex] = i - topIndex
        }

        stack = append(stack, i)
    }

    return answer
}

