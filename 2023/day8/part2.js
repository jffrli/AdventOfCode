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

// From Geeksforgeeks
function gcd(a, b) { 
    for (let temp = b; b !== 0;) { 
        b = a % b; 
        a = temp; 
        temp = b; 
    } 
    return a; 
} 
  
function lcmFunction(a, b) { 
    const gcdValue = gcd(a, b); 
    return (a * b) / gcdValue; 
} 

function solution(input) {
    let instructions = input[0][0]
    let locations = input.slice(2).map((e) => e[0])
    let destinations = input.slice(2).map((e) => e[1].replace(/[\(\)]/g, '').split(", "))

    //console.log(instructions)

    let curr = locations.reduce((a,e,i) => {
        if (e[2] == "A") a.push(i);
        return a;
    }, []);

    let steps = 0

    let lcm = 1

    while (curr.length) {
        for (let i = 0; i < curr.length; i++) {
            if (locations[curr[i]][2] == "Z") {
                lcm = lcmFunction(lcm, steps)
                curr.splice(i, 1)
            }
        }
        


        if (instructions[steps % instructions.length] == 'L') {
            for (let i = 0; i < curr.length; i++) {
                curr[i] = locations.indexOf(destinations[curr[i]][0])
            } 
        }
        else {
            for (let i = 0; i < curr.length; i++) {
                curr[i] = locations.indexOf(destinations[curr[i]][1])
            } 
        }

        steps++
    }

    return lcm
}

console.log("Part 2")
console.log(solution(inputData))