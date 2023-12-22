package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	inputFile := "day03_input.txt"

	fmt.Println("-------- Day03 ---------")
	day03(inputFile)
}

func readFile(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func day03(filename string) {
	lines, _ := readFile(filename)
	lenX := len(lines[0])
	lenY := len(lines)

	symbols := make([][2]int, 0)
	gears := make([][2]int, 0)
	nums := make(map[int]int)

	numsIdx := make([][]int, lenY)
	for i := range numsIdx {
		numsIdx[i] = make([]int, lenX)
	}

	numCtr := 0
	for i, line := range lines {
		numFound := false
		currentNum := ""
		for j, char := range line {
			if char >= 48 && char <= 57 {
				if !numFound {
					numFound = true
					numCtr++
				}
				currentNum += string(char)
				numsIdx[i][j] = numCtr
			} else {
				if numFound {
					nums[numCtr], _ = strconv.Atoi(currentNum)
					currentNum = ""
					numFound = false
				}
				if char != 46 {
					symbols = append(symbols, [2]int{i, j})
					if char == 42 {
						gears = append(gears, [2]int{i, j})
					}
				}
			}
		}
		if numFound {
			nums[numCtr], _ = strconv.Atoi(currentNum)
		}
	}

	numSet := make(map[int]bool)
	for _, idx := range symbols {
		yMin := max(0, idx[0]-1)
		yMax := min(lenY, idx[0]+1)
		xMin := max(0, idx[1]-1)
		xMax := min(lenX, idx[1]+1)
		for y := yMin; y <= yMax; y++ {
			for x := xMin; x <= xMax; x++ {
				if numIdx := numsIdx[y][x]; numIdx != 0 {
					numSet[numIdx] = true
				}
			}
		}
	}

	sum := 0
	for idx := range numSet {
		sum += nums[idx]
	}
	fmt.Printf("Part 1: %d\n", sum)

	sum = 0
	for _, gear := range gears {
		numSet := make(map[int]bool)
		yMin := max(0, gear[0]-1)
		yMax := min(lenY, gear[0]+1)
		xMin := max(0, gear[1]-1)
		xMax := min(lenX, gear[1]+1)
		for y := yMin; y <= yMax; y++ {
			for x := xMin; x <= xMax; x++ {
				if numIdx := numsIdx[y][x]; numIdx != 0 {
					numSet[numIdx] = true
				}
			}
		}
		if len(numSet) == 2 {
			prod := 1
			for idx := range numSet {
				prod *= nums[idx]
			}
			sum += prod
		}
	}
	fmt.Printf("Part 2: %d\n", sum)
}
