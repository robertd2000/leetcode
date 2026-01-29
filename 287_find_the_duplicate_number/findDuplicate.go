package main

func findDuplicate(nums []int) int {
	n := len(nums)

	if n < 1 {
		return -1
	}

	slow, fast := nums[0], nums[nums[0]]

	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}

	fast = 0

	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}

	return slow
}
