function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().split("\n").map((e) => e.split(/\s+/))
    if (data[data.length-1].length == 0) {
        data.pop()
    }
    return data; //convert data to string and split by EOL
}

var inputData = getInput()

function part1(input) {
    /**
     * speed = race_time - running_time
     * speed * running_time > record
     * (race_time - running_time) * running_time > record
     */

    const race_times = input[0].slice(1).map((e) => parseInt(e));
    const records = input[1].slice(1).map((e) => parseInt(e));

    let moe = 1;
    
    for (let i = 0; i < race_times.length; i++) {
        let race_time = race_times[i];
        let record = records[i];

        let range_start;
        let range_end;

        // assuming each race is possible
        for (let j = 0; j < race_time; j++) {
            if ((race_time-j)*j > record) {
                range_start = j
                break
            }
        }
        for (let j = race_time-1; j >= range_start; j--) {
            if ((race_time-j)*j > record) {
                range_end = j
                break
            }
        }

        moe *= range_end - range_start + 1
    }



    return moe
}

console.log("Part 1")
console.log(part1(inputData))

function part2(input) {
    let race_time = parseInt(input[0].slice(1).join(''));
    let record = parseInt(input[1].slice(1).join(''));
    // console.log(race_time)
    // console.log(record)

    let range_start;
    let range_end;

    // assuming each race is possible
    for (let j = 0; j < race_time; j++) {
        if ((race_time-j)*j > record) {
            range_start = j
            break
        }
    }
    for (let j = race_time-1; j >= range_start; j--) {
        if ((race_time-j)*j > record) {
            range_end = j
            break
        }
    }

    return range_end - range_start + 1
}

console.log("Part 2")
console.log(part2(inputData))