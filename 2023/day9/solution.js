function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().trim().split("\n").map((e) => e.split(" ").map((x) => parseInt(x)))
    //console.log(data.slice(195))
    return data;
}

const inputData = getInput()



function solution(input){

    let futsTotals = 0
    let pastsTotals = 0
    
    for (let i = 0; i < input.length; i++) {
        let seqs = [[...input[i]]] //shallow copy (doesn't copy references)

        // gets current vals/sequences
        while (seqs[seqs.length-1].filter((e) => e == 0).length != seqs[seqs.length-1].length) {//while end is not all 0s
            let x = []

            for (let j = 0; j < seqs[seqs.length-1].length-1; j++) {
                x.push(seqs[seqs.length-1][j+1]-seqs[seqs.length-1][j])
            }
            seqs.push(x)
            //console.log(seqs)
        }

        for (let j = seqs.length-1; j > 0; j--) {
            //future extrapolation
            seqs[j-1].push(seqs[j][seqs[j].length-1] + seqs[j-1][seqs[j-1].length-1])

            //past extrapolation
            seqs[j-1].unshift(seqs[j-1][0] - seqs[j][0])

        }
        //console.log(seqs)
        futsTotals += seqs[0][seqs[0].length-1]
        pastsTotals += seqs[0][0]

        //console.log("\n\n")
    }

    
    return [futsTotals, pastsTotals]
}



const answer = solution(inputData)

console.log("Part 1")
console.log(answer[0])

console.log("Part 2")
console.log(answer[1])
