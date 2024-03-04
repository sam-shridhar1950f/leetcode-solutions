import (
    "fmt"
    "strconv"
)

func evalRPN(tokens []string) int {
    var stack []int

    for _, token := range tokens {
        switch token {
        case "+", "-", "*", "/":
           
            num2, num1 := stack[len(stack)-1], stack[len(stack)-2]
            stack = stack[:len(stack)-2] // Remove the elements

           
            result := performOp(num1, num2, token)
            stack = append(stack, result)
        default:
            num, _ := strconv.Atoi(token)
            stack = append(stack, num)
        }
    }

    return stack[0]
}

func performOp(a, b int, op string) int {
    switch op {
    case "+":
        return a + b
    case "-":
        return a - b
    case "*":
        return a * b
    case "/":
        return a / b
    default:
        return 0
    }
}