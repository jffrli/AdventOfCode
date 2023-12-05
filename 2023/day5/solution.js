function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().trim()
    return data;
}

var inputData = getInput()



function sortFunction2D(a,b) {
    if (a[0] === b[0]) { // === strict equality, need to be similar type
        return 0;
    }
    return (a[0] < b[0]) ? -1 : 1; //condition ? if true : if false
}

function sortFunctionInts(a,b) {
    if (a === b) return 0;
    return (a < b) ? -1 : 1;
}

function findAdjustment(guides,value) {
    let start = 0
    let end = guides.length-1
    //console.log(guides)
    while (end >= start) {
        let midpoint = Math.floor((end-start)/2)+start
        // console.log(start)
        // console.log(end)
        // console.log(midpoint)
        // console.log()
        if (value < guides[midpoint][0]) {
            end = midpoint-1
        }
        else if (value >= guides[midpoint][0] && value <= guides[midpoint][1]) {
            return value - guides[midpoint][2];
        }
        else {
            start = midpoint+1
        }
        
    }
    //console.log("not found")

    return value
}

function getTranslations(maps) {
    let translations = Array.from(Array(maps.length-1), () => []); //create an array of empty lists
    
    //console.log(translations)
    for (let i = 0; i < maps.length-1; i++) { //do i+1 when accessing maps
        let guides = maps[i+1].slice(1)

        for (let j = 0; j < guides.length; j++) {
            let vals = guides[j].split(" ").map((e) => parseInt(e))
            let guide = [vals[1], vals[1] + vals[2] -1, vals[1] - vals[0]]
            translations[i].push(guide)
        }
        
        translations[i].sort(sortFunction2D)
        //console.log(translations[i])
    }
    return translations
}

function solution(input) {
    let tables = input.split("\n\n")
    let maps = tables.map((e) => e.split("\n"))
    let seeds = maps[0][0].split(":")[1].trim().split(" ").map((e) => parseInt(e))
    
    let translations = getTranslations(maps)

    for (let i = 0; i < seeds.length; i ++){
        let seedVal = seeds[i]
 //       console.log(seedVal)
        for (let j = 0; j < translations.length; j++) {
            seedVal = findAdjustment(translations[j], seedVal)
            
        }
        seeds[i] = seedVal
    }
    seeds.sort(sortFunctionInts)
    return seeds[0]
}

console.log("Part 1")
console.log(solution(inputData))


function part2(input) {
    let tables = input.split("\n\n")
    let maps = tables.map((e) => e.split("\n"))
    let seeds = maps[0][0].split(":")[1].trim().split(" ").map((e) => parseInt(e))
    
    let translations = getTranslations(maps)

    let lowest = -1
    for (let i = 0; i < seeds.length; i += 2) {
        for (let j = seeds[i]; j < seeds[i] + seeds[i+1]; j++) {
            let seedVal = j
            for (let k = 0; k < translations.length; k++) {
                seedVal = findAdjustment(translations[k], seedVal)
            }
            if (seedVal < lowest || lowest == -1) {
                lowest = seedVal
            }
        }
    }
    return lowest
}

console.log("Part 2")
console.log(part2(inputData))