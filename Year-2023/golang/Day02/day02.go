package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	inputFile := "day02_input.txt"

	fmt.Println("-------- Day02 ---------")
	fmt.Printf("Part 1: %d\n", day02_part1(inputFile))
	fmt.Printf("Part 2: %d\n", day02_part2(inputFile))
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

func processGameData(lines []string) map[int][][3]int {
	games := make(map[int][][3]int)
	for i, line := range lines {
		gameRecord := strings.Split(strings.Split(line, ":")[1], ";")
		games[i] = make([][3]int, len(gameRecord))
		for j, run := range gameRecord {
			cubes := strings.Split(run, ",")
			for _, cube := range cubes {
				cubeInfo := strings.Fields(cube)
				idx := getIndexFromColor(cubeInfo[1])
				games[i][j][idx], _ = strconv.Atoi(cubeInfo[0])
			}
		}
	}
	return games
}

func getIndexFromColor(c string) int {
	if c == "red" {
		return 0
	} else if c == "green" {
		return 1
	} else if c == "blue" {
		return 2
	} else {
		return -1
	}
}

func day02_part1(filename string) int {
	lines, _ := readFile(filename)
	games := processGameData(lines)
	sum := 0
	maxRed := 12
	maxGreen := 13
	maxBlue := 14
	for k, v := range games {
		isPossible := true
		for _, gameRun := range v {
			if gameRun[0] > maxRed {
				isPossible = false
				break
			}
			if gameRun[1] > maxGreen {
				isPossible = false
				break
			}
			if gameRun[2] > maxBlue {
				isPossible = false
				break
			}
		}
		if isPossible {
			sum += k + 1
		}
	}
	return sum
}

func day02_part2(filename string) int {
	lines, _ := readFile(filename)
	games := processGameData(lines)
	sum := 0
	for _, v := range games {
		maxRed := 0
		maxGreen := 0
		maxBlue := 0
		for _, gameRun := range v {
			if gameRun[0] > maxRed {
				maxRed = gameRun[0]
			}
			if gameRun[1] > maxGreen {
				maxGreen = gameRun[1]
			}
			if gameRun[2] > maxBlue {
				maxBlue = gameRun[2]
			}
		}
		sum += maxRed * maxBlue * maxGreen
	}
	return sum
}
