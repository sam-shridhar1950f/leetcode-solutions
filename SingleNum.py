package main


import "fmt"

func main() {

	type person struct {}

	joe := person{
		name: "Doe, John",
		age:  32,
	  }

	var m map[string]int

	fmt.Println(joe)



}