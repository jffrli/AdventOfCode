function getInput() {
    const fs = require('fs') // fs is the File System module
    const os = require('os')

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().split("\n")
    if (data[data.length-1].length == 0) {
        data.pop()
    }
    return data; //convert data to string and split by EOL
}

var inputData = getInput()

function solution(input) {
    var ids = 0;
    var powers = 0;

    input.forEach((line) => {
        let highR = 0
        let highB = 0
        let highG = 0

        parts = line.split(":")

        let gameID = parts[0].match(/Game (\d+)/)
        //console.log(gameID[1])
        showings = parts[1].split(";")
        for (let i = 0; i < showings.length; i++) {
            //console.log(showings[i])
            let R = showings[i].match(/(\d+) red/)
            let B = showings[i].match(/(\d+) blue/)
            let G = showings[i].match(/(\d+) green/)
            if (R && (R[1] > highR)) {
                //console.log("R update " + highR + " => " + R[1])
                highR = +R[1]
            }
            if (B && (B[1] > highB)) {
                //console.log("B update " + highB + " => " +  B[1])
                highB = +B[1]
            }
            if (G && (G[1] > highG)) {
                //console.log("G update " + highG + " => " +  G[1])
                highG = +G[1]
            }
        }
        powers += highR * highB * highG;

        //console.log(line)
        if (highR <= 12 && highB <= 14 && highG <= 13) {
            // console.log("PASSED")
            // console.log(gameID[1])
            // console.log(highR)
            // console.log(highG)
            // console.log(highB)
            // console.log()
            ids += +gameID[1];
        }
        // else{
        //     console.log("FAILED")
        //     console.log(gameID[1])
        //     console.log(highR)
        //     console.log(highG)
        //     console.log(highB)
        //     console.log()
        // }
        
    })
    return [ids,powers]
}

console.log("Part 1")
console.log(solution(inputData)[0])

console.log("Part 2")
console.log(solution(inputData)[1])