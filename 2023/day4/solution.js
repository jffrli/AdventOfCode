function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().split("\n")
    if (data[data.length-1].length == 0) {
        data.pop()
    }
    return data; //convert data to string and split by EOL
}

var inputData = getInput()

//The first match makes the card worth one point and each match after the first doubles the point value of that card.
// powers of 2
//Math.pow(2,n-1) if n <=1

function solution(input) {
    let points = 0;

    let copies = Array(input.length).fill(1)

    for (let i = 0; i < input.length; i++) {
        let line = input[i]
        let nums = line.split(":")[1].trim() //trim gets rid of whitespace on the ends
        let card = nums.split("|")
        let winningNums = card[0].split(/\s+/).filter((e) => e.length > 0)
        let cardNums = card[1].split(/\s+/).filter((e) => e.length > 0)

        let winnums = 0
        for (let j = 0; j < cardNums.length; j++) {
            if (winningNums.includes(cardNums[j])) {
                winnums += 1
            }
        }

        if (winnums > 0) {
            points += Math.pow(2,winnums - 1)
        }
        for (let j = 0; j < winnums; j++) {
            copies[i+j+1] += copies[i]
        }
        
    }

    //count total copies
    let total = 0
    for (let i = 0; i < copies.length; i++) {
        total += copies[i]
    }

    return [points,total]

}


console.log("Part 1")
answers = solution(inputData)
console.log(answers[0])

console.log("Part 2")
console.log(answers[1])