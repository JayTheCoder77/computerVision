package main

import "fmt"

func divide(a int, b int) int {
	return a / b
}

func findUser(users map[string]int, name string) int {
	return users[name]
}

func main() {
	users := map[string]int{
		"Jayant": 20,
		"Alex":   21,
	}

	fmt.Println(divide(10, 0))
	fmt.Println(findUser(users, "John"))
}