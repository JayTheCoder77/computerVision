package main

import (
	"fmt"
	"sync"
	"time"
)

type User struct {
	Name string
	Age  int
}

func average(nums []int) float64 {
	sum := 0
	for i := 0; i <= len(nums); i++ { // BUG 1: index out of range
		sum += nums[i]
	}

	// BUG 2: integer division
	return float64(sum / len(nums))
}

func updateUser(u User) {
	// BUG 3: passed by value
	u.Age++
}

func printNumbers(wg sync.WaitGroup) { // BUG 4: WaitGroup copied
	defer wg.Done()

	for i := 0; i < 5; i++ {
		go func() {
			// BUG 5: loop variable captured
			fmt.Println(i)
		}()
	}
}

func readMap(m map[string]int, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i < 1000; i++ {
		fmt.Println(m["count"])
	}
}

func writeMap(m map[string]int, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i < 1000; i++ {
		// BUG 6: concurrent map writes/reads
		m["count"]++
	}
}

func main() {
	nums := []int{10, 20, 30}

	fmt.Println("Average:", average(nums))

	user := User{
		Name: "Alice",
		Age:  25,
	}

	updateUser(user)
	fmt.Println("Updated age:", user.Age) // BUG 7: remains unchanged

	var wg sync.WaitGroup

	wg.Add(1)
	go printNumbers(wg)

	counter := map[string]int{
		"count": 0,
	}

	wg.Add(2)
	go readMap(counter, &wg)
	go writeMap(counter, &wg)

	// BUG 8: nil pointer dereference
	var ptr *int
	fmt.Println(*ptr)

	time.Sleep(time.Second)

	wg.Wait()

	// BUG 9: division by zero
	empty := []int{}
	fmt.Println("Average:", average(empty))

	// BUG 10: dead code due to panic above
	fmt.Println("Finished")
}