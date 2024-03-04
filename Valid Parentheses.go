func isValid(s string) bool {
    var stack []rune

    p := map[rune]rune{
        ')': '(',
        ']': '[',
        '}': '{',
    }


    for _, c := range s {
  
        if _, exists := p[c]; !exists { // check to see if c is a key in p (closed bracket), if not then exists := false and thus if -> !exists -> true (bracket is open)
            stack = append(stack, c)
        } else {
          
            if len(stack) == 0 || stack[len(stack)-1] != p[c] { // if the stack is empty return false or if the last element doesnt match with the closed bracket
                return false
            }
          
            stack = stack[:len(stack)-1] // pop 
        }
    }

   
    return len(stack) == 0 
}