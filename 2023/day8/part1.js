function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().split("\n")
    if (data[data.length-1].length == 0) {
        data.pop()
    }

    data = data.map((e) => e.split(" = "))
    return data; //convert data to string and split by EOL
}

const inputData = getInput()

function solution(input) {
    let instructions = input[0][0]
    let locations = input.slice(2).map((e) => e[0])
    let destinations = input.slice(2).map((e) => e[1].replace(/[\(\)]/g, '').split(", "))

    //console.log(instructions)

    let curr = locations.findIndex(x => x == 'AAA'); //starting location
    let steps = 0
    let instruction = 0

    

    while (locations[curr] != "ZZZ") {
        if (instructions[instruction++] == 'L') {
            curr = locations.findIndex(x => x == destinations[curr][0])
        }
        else {
            curr = locations.findIndex(x => x == destinations[curr][1])
        }
        if (instruction == instructions.length) instruction = 0

        steps++
    }


    return steps
}

console.log("Part 1")
console.log(solution(inputData))