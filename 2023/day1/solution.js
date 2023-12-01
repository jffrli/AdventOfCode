
// var == global scope
// let == block scope
// const = block scopes, can't be updated

const { get } = require('http');


function getInput() {
    const fs = require('fs') // fs is the File System module
    const os = require('os')

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    return data.toString().split("\n"); //convert data to string and split by EOL
}

function naiveDigitReplacement(line){
    line = line.replaceAll("one", "one1one")
    line = line.replaceAll("two", "two2two")
    line = line.replaceAll("three", "three3three")
    line = line.replaceAll("four", "four4four")
    line = line.replaceAll("five", "five5five")
    line = line.replaceAll("six", "six6six")
    line = line.replaceAll("seven", "seven7seven")
    line = line.replaceAll("eight", "eight8eight")
    line = line.replaceAll("nine", "nine9nine")
    return line;
}

function solution(input,spelledOut) {
    
    var sum = 0;

    //regex with global index for replaceAll
    const nonDigitsRegex = /\D+/gi;

    //input should be an array of strings
    input.forEach((line) => {//for each loop
        //debugging lines
        //console.log(line)
        //sum += 1;
        if (spelledOut) {
            line = naiveDigitReplacement(line);
        }
        let digits = line.replaceAll(nonDigitsRegex,'') //replace all nonDigits with nothing
        //console.log(digits)
        let last = digits.charAt(digits.length-1); //digits.pop() would be faster but
        let first = digits.charAt(0);
        //console.log(first)
        //console.log(last + "\n")
        let num = first + last; //appending digits
        sum += +num; //prepend with +x to make number
    })
    return sum;
}

var inputData = getInput()

//part 1
console.log("Part 1")
var calValSums = solution(inputData, false);
console.log(calValSums)

//part 2
console.log("\nPart 2")
var p2Sums = solution(inputData,true)
console.log(p2Sums)

