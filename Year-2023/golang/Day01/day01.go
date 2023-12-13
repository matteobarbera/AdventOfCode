package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	inputFile := "day01_input.txt"

	fmt.Println("-------- Day01 ---------")
	fmt.Printf("Part 1: %d\n", day01_part1(inputFile))
	fmt.Printf("Part 2: %d\n", day01_part2(inputFile))
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

func day01_part1(inputFile string) int {
	sum := 0
	re := regexp.MustCompile(`[1-9]`)
	lines, _ := readFile(inputFile)
	for _, line := range lines {
		matches := re.FindAllStringSubmatch(line, -1)
		num, _ := strconv.Atoi(matches[0][0] + matches[len(matches)-1][0])
		sum += num
	}
	return sum
}

func day01_part2(inputFile string) int {
	sum := 0
	re := regexp.MustCompile(`(one|two|three|four|five|six|seven|eight|nine|[1-9]).*(one|two|three|four|five|six|seven|eight|nine|[1-9])`)
	reSingle := regexp.MustCompile(`one|two|three|four|five|six|seven|eight|nine|[1-9]`)
	lines, _ := readFile(inputFile)
	for _, line := range lines {
		matches := re.FindAllStringSubmatch(line, -1)
		var num int
		if len(matches) > 0 {
			num, _ = strconv.Atoi(wordToInt(matches[0][1]) + wordToInt(matches[0][2]))
		} else {
			matches = reSingle.FindAllStringSubmatch(line, -1)
			num, _ = strconv.Atoi(wordToInt(matches[0][0]) + wordToInt(matches[0][0]))
		}
		sum += num
	}
	return sum
}

func wordToInt(s string) string {
	switch s {
	case "one":
		return "1"
	case "two":
		return "2"
	case "three":
		return "3"
	case "four":
		return "4"
	case "five":
		return "5"
	case "six":
		return "6"
	case "seven":
		return "7"
	case "eight":
		return "8"
	case "nine":
		return "9"
	default:
		return s
	}
}
