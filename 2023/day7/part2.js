function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().split("\n")
    if (data[data.length-1].length == 0) {
        data.pop()
    }
    data = data.map((e) => e.split(" "))
    return data; //convert data to string and split by EOL
}

const inputData = getInput()

function handType(hand) {
    const uniqs = new Map()
    for (let i = 0; i < hand[0].length; i++) {


        let k = uniqs.get(hand[0][i])
        if (k === undefined) {
            k = 1;
        }
        else {
            k += 1;
        }
        uniqs.set(hand[0][i],k)
    }
    // uniqs.forEach((v,k) => {
    //     console.log(k + " " + v)
    // })

    let wilds = uniqs.get('J')
    uniqs.delete('J')
    if (wilds === 5) return 6
    if (isNaN(wilds)) wilds = 0;

    let scores = Array.from(uniqs, ([name, value]) => value)

    if (scores.includes(5-wilds)) return 6
    if (scores.includes(4-wilds)) return 5

    if (wilds == 2 && scores.includes(2)) return 4 //full house
    if (wilds == 2 && !scores.includes(2)) return 3// 3 of a kind
    const isPair = (element) => element == 2

    if (wilds == 1 && scores.includes(2)) {
        if (scores.findIndex(isPair) != scores.findLastIndex(isPair)) {
            return 4 //full house (2 pairs + wild)
        }
        return 3 //3 of a kind
    }
    if (wilds == 1) return 1 //1 pair

    if (scores.includes(3)) {
        if (scores.includes(2)) return 4
        return 3
    }
    if (scores.includes(2)) {
        if (scores.findIndex(isPair) != scores.findLastIndex(isPair)) return 2
        return 1
    }
    return 0

}

function getVal(hand, index) {
    let x = parseInt(hand[0][index])
    if (isNaN(x)) {
        x = hand[0][index];
        if (x == 'T') return 10
        if (x == 'J') return 1
        if (x == 'Q') return 12
        if (x == 'K') return 13
        if (x == 'A') return 14

        throw new Error("Not a valid card: " + x)
    } else {
        return x
    }

}


// return -1 if a smaller than b
function compareHands(a,b) {
    if (handType(a) < handType(b)) {
        return -1;
    }
    else if (handType(a) > handType(b)) {
        return 1;
    }
    else {
        for (let i = 0; i < a[0].length; i++) {
            let av = getVal(a, i)
            let bv = getVal(b,i)
            if (av < bv) return -1
            if (av > bv) return 1

        }
    }

    return 0

}

function solution(input) {

    input.sort(compareHands)

    let winnings = 0;

    for (let i = 0; i < input.length; i++) {
        // console.log(input[i])
        // console.log(input[i][1])
        // console.log(parseInt(input[i][1]))
        // console.log()
        winnings += (i+1) * parseInt(input[i][1])
    }


    return winnings
}

// console.log(handType(inputData[2]))

console.log("Part 2")
console.log(solution(inputData))
