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

var symbolsRegex = /[^\d\.]/gi; //match all non-digits and non "."s
var numbersRegex = /(\d+)/gi

function solution(input) {
    partNums = 0;
    let linelength = input[0].length

    //make empty 2d array of empty lists of same size as input
    let adjVals = Array.from({length: input.length}, e => Array.from(
        {length: linelength
        }, e => Array(0)))

    for (let i = 0; i < input.length; i++) {
        
        let numberMatches = [...input[i].matchAll(numbersRegex)] //matchAll() returns an iterator
        //console.log(numberMatches)
        for (let j = 0; j < numberMatches.length; j++) {
            let num = numberMatches[j][0]
            let ind = numberMatches[j].index

            //take a slice of the grid
            let section = input.slice(Math.max(0,i-1), Math.min(input.length,i+2)).map(k => k.slice(Math.max(ind-1,0),Math.min(ind+num.length+1,linelength)))
            let added = false;

            for (let k = 0; k < section.length; k++) {
                
                let adjSym = [...section[k].matchAll(symbolsRegex)]
                if (adjSym.length != 0) {
                    // console.log("Num has adjacent symbol!")
                    // console.log(adjSym)
                    if (!added) {
                        partNums += +num
                        added = true
                    }
                    for (let x = 0; x < adjSym.length; x++) {
                        adjVals[Math.max(0,i-1)+k][Math.max(ind-1,0)+adjSym[x].index].push(+num)
                    }
                }
            }
        }

    }

    let ratios = 0;
    for (let i = 0; i < adjVals.length; i++) {
        for (let j = 0; j < linelength; j++) {
            if (adjVals[i][j].length == 2) {
                ratios += adjVals[i][j][0] * adjVals[i][j][1]
            }
        }
    }

    return [partNums,ratios]
}

console.log("Part 1")
answers = solution(inputData)
console.log(answers[0])
console.log()



console.log("Part 2")
console.log(answers[1])
console.log()