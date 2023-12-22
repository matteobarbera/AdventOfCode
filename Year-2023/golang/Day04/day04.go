package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type mySet map[int]bool

func main() {
	// Needless parallelization to practice goroutines and channels

	inputFile := "day04_input.txt"

	fmt.Println("-------- Day04 ---------")
	day04(inputFile)
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

func parseScratchCards(lines []string, resChan chan [][]mySet) {
	cards := make([][]mySet, len(lines))
	for i, line := range lines {
		card := make([]mySet, 2)
		cardNums := make(mySet)
		winningNums := make(mySet)

		numbersString := strings.Split(strings.Split(line, ":")[1], "|")
		for _, numString := range strings.Fields(numbersString[0]) {
			num, _ := strconv.Atoi(numString)
			cardNums[num] = true
		}
		for _, numString := range strings.Fields(numbersString[1]) {
			num, _ := strconv.Atoi(numString)
			winningNums[num] = true
		}
		card[0] = cardNums
		card[1] = winningNums
		cards[i] = card
	}
	resChan <- cards
}

func getCardValue(card []mySet) int {
	value := 0
	for cardNum := range card[0] {
		if card[1][cardNum] {
			if value == 0 {
				value = 1
			} else {
				value *= 2
			}
		}
	}
	return value
}

func getMatchingNumbers(card []mySet) int {
	sum := 0
	for cardNum := range card[0] {
		if card[1][cardNum] {
			sum++
		}
	}
	return sum
}

func processScratchCards(cards [][]mySet, resChan chan int) {
	sum := 0
	for _, card := range cards {
		sum += getCardValue(card)
	}
	resChan <- sum
}

func processWonScratchCards(cards [][]mySet, indices []int, resChan chan int) {
	cardIndices := make([]int, indices[1]-indices[0])
	for i := 0; i < len(cardIndices); i++ {
		cardIndices[i] = indices[0] + i
	}
	ctr := 0
	for len(cardIndices) > 0 {
		idx := cardIndices[0]
		value := getMatchingNumbers(cards[idx])
		newIndices := make([]int, value)
		for j := 0; j < value; j++ {
			newIndices[j] = idx + j + 1
		}
		cardIndices = append(cardIndices[1:], newIndices...)
		ctr++
	}
	resChan <- ctr
}

func day04(filename string) {
	lines, _ := readFile(filename)
	nChans := 12

	if len(lines)%nChans != 0 {
		fmt.Println("ERROR! Change number of channels. len(lines) =", len(lines))
		return
	}
	step := len(lines) / nChans

	scratchCardsChan := make([]chan [][]mySet, nChans)
	for i := 0; i < nChans; i++ {
		scratchCardsChan[i] = make(chan [][]mySet)
		go parseScratchCards(lines[i*step:(i+1)*step], scratchCardsChan[i])
	}
	scratchCards := make([][]mySet, 0)
	for _, c := range scratchCardsChan {
		scratchCards = append(scratchCards, <-c...)
	}

	valueChan := make([]chan int, nChans)
	for i := 0; i < nChans; i++ {
		valueChan[i] = make(chan int)
		go processScratchCards(scratchCards[i*step:(i+1)*step], valueChan[i])
	}
	sum := 0
	for _, c := range valueChan {
		sum += <-c
	}
	fmt.Printf("Part 1: %d\n", sum)

	resChans := make([]chan int, nChans)
	for i := 0; i < nChans; i++ {
		resChans[i] = make(chan int)
		indices := []int{i * step, (i + 1) * step}
		go processWonScratchCards(scratchCards, indices, resChans[i])
	}
	ctr := 0
	for _, c := range resChans {
		ctr += <-c
	}
	fmt.Printf("Part 2: %d\n", ctr)
}
