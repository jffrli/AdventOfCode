function getInput() {
    const fs = require('fs') // fs is the File System module

    let data = fs.readFileSync("input.txt") // read input.txt, store into data variable synchronously
    data = data.toString().trim().split("\n").map((e) => e.split(""))
    return data;
}

const inputData = getInput()

function findAdjacents(node,grid){
    let adjacents = []
    let [row,col] = node
    const curr = grid[row][col]

    if (curr == "|") {
        if (row-1 >= 0) adjacents.push([row-1, col]) // N
        if (row+1 < grid.length) adjacents.push([row+1,col]) // S
    } else if (curr == "-") {
        if (col-1 >= 0) adjacents.push([row,col-1]) // W
        if (col+1 < grid[row].length) adjacents.push([row,col+1]) //E

    } else if (curr == "L") {
        if (row-1 >= 0) adjacents.push([row-1, col]) // N
        if (col+1 < grid[row].length) adjacents.push([row,col+1]) //E
    } else if (curr == "J") {
        if (row-1 >= 0) adjacents.push([row-1, col]) // N
        if (col-1 >= 0) adjacents.push([row,col-1]) // W
    } else if (curr == "7") {
        if (row+1 < grid.length) adjacents.push([row+1,col]) // S
        if (col-1 >= 0) adjacents.push([row,col-1]) // W
    } else if (curr == "F") {
        if (row+1 < grid.length) adjacents.push([row+1,col]) // S
        if (col+1 < grid[row].length) adjacents.push([row,col+1]) //E
    } else if (curr == "S") {
        if (row-1 >= 0) {
			if (
					grid[row-1][col] == "|" ||
					grid[row-1][col] == "7" ||
					grid[row-1][col] == "F")
			{
				adjacents.push([row-1, col]) // N
			}
		}
        if (row+1 < grid.length) {
			if (
				grid[row+1][col] == "|" ||
				grid[row+1][col] == "L" ||
				grid[row+1][col] == "J")
			{
				adjacents.push([row+1,col]) // S
			}
		}
        if (col-1 >= 0) {
			if (
				grid[row][col-1] == "-" ||
				grid[row][col-1] == "L" ||
				grid[row][col-1] == "F")
			{
				adjacents.push([row,col-1]) // W
			}
		}
        if (col+1 < grid[row].length) {
			if (
				grid[row][col+1] == "-" ||
				grid[row][col+1] == "J" ||
				grid[row][col+1] == "7")
			{
				adjacents.push([row,col+1]) //E
			}
		}
    }
    // else would be "." does nothing

    return adjacents
}

// function countEnclosed(arr,grid) {

// 	let queue = [[0,0]]

// 	const vl = ["|","J","7"]
// 	const vr = ["|","L","F"]

// 	const hu = ["-","J","L"]
// 	const hd = ["-","7","F"]


// 	//replace unenclosed with 2
// 	while (queue.length > 0) {
		
// 		let [row,col] = queue.shift()
// 		//console.log(row + " " + col + " " + arr[row][col])
// 		arr[row][col] = 2

// 		if (row - 1 >= 0) { //up
// 			let r = row - 1
			
// 			//going between pipes
// 			let ld = r
// 			while (arr[ld][col] == 1 &&
// 				col +1 < arr[0].length &&
// 				vl.includes(grid[ld][col]) && 
// 				vr.includes(grid[ld][col+1])
// 			) {
// 				ld -= 1
// 			}
// 			let rd = r
// 			while (arr[rd][col] == 1 &&
// 				col - 1 >= 0 &&
// 				vr.includes(grid[rd][col]) && 
// 				vl.includes(grid[rd][col-1])
// 			) {
// 				rd -= 1
// 			}
// 			r = Math.min(ld,rd)

// 			if (arr[r][col] == 0) {
// 				arr[r][col] = 2
// 				queue.push([r,col])
// 			}
			
// 		}
// 		if (row + 1 < arr.length) { //down
// 			let r = row + 1

// 			//going between pipes
// 			let ld = r
// 			while (arr[ld][col] == 1 &&
// 				col +1 < arr[0].length &&
// 				vl.includes(grid[ld][col]) && 
// 				vr.includes(grid[ld][col+1])
// 			) {
// 				ld += 1
// 			}
// 			let rd = r
// 			while (arr[rd][col] == 1 &&
// 				col - 1 >= 0 &&
// 				vr.includes(grid[rd][col]) && 
// 				vl.includes(grid[rd][col-1])
// 			) {
// 				rd += 1
// 			}
// 			r = Math.max(ld,rd)

// 			if (arr[r][col] == 0) {
// 				arr[r][col] = 2
// 				queue.push([r,col])
// 			}
			
// 		}
// 		if (col - 1 >= 0) {//left
// 			let c = col - 1

// 			//going between pipes
// 			let ud = c
// 			while (arr[row][ud] == 1 &&
// 				row +1 < arr.length &&
// 				hu.includes(grid[row][ud]) && 
// 				hd.includes(grid[row+1][ud])
// 			) {
// 				ud -= 1
// 			}
// 			let dd = c
// 			while (arr[row][dd] == 1 &&
// 				row -1 >= 0 &&
// 				hd.includes(grid[row][ud]) && 
// 				hu.includes(grid[row-1][ud])
// 			) {
// 				dd -= 1
// 			}
// 			c = Math.min(ud,dd)



// 			if (arr[row][c] == 0) {
// 				arr[row][c] = 2
// 				queue.push([row,c])
// 			}
			
// 		}
// 		if (col + 1 >= 0) {
// 			let c = col + 1

// 			//going between pipes
// 			let ud = c
// 			while (arr[row][ud] == 1 &&
// 				row +1 < arr.length &&
// 				hu.includes(grid[row][ud]) && 
// 				hd.includes(grid[row+1][ud])
// 			) {
// 				ud += 1
// 			}
// 			let dd = c
// 			while (arr[row][dd] == 1 &&
// 				row -1 >= 0 &&
// 				hd.includes(grid[row][ud]) && 
// 				hu.includes(grid[row-1][ud])
// 			) {
// 				dd += 1
// 			}
// 			c = Math.max(ud,dd)
			
// 			if (arr[row][c] == 0) {
// 				arr[row][c] = 2
// 				queue.push([row,c])
// 			}
// 		}
// 	}

// 	for (let i = 0; i < arr.length; i++) {
//         console.log(arr[i].join(""))
//     }

// 	let count = 0
// 	for (let i = 0; i < arr.length; i++) {
// 		count += arr[i].filter((x) => x == 0).length
// 	}

// 	return count
// }

function countEnclosed(arr, grid) {
	return 0
}


function solution(input) {

    let queue = []
    let visited = Array.from({ length:input.length }, () => (
        Array.from({ length:input[0].length }, ()=> 0)
    ))
    

    let [row,col] = [-1,-1]
    while (col == -1) {
        col = input[++row].indexOf("S")
    }
    //console.log(row + " " + col)
    visited[row][col] = 1
    queue.push([[row,col],0])

    //TODO: add start to queue, visited, and reachable
    
	let furthest = 0
    while (queue.length > 0) {
        const [node, dist] = queue.shift()

		furthest = dist

        const adjacents = findAdjacents(node,input)
        
        //input[node[0]][node[1]] = dist
        // console.log(node)
        // console.log(adjacents)

        for (let i = 0; i < adjacents.length; i++) {
            const adjacent = adjacents[i]
            if (visited[adjacent[0]][adjacent[1]] == 1) {
                continue
            }

            const newdist = dist+1
            visited[adjacent[0]][adjacent[1]] = 1

            queue.push([adjacent,newdist])
        }


    }

    // for (let i = 0; i < input.length; i++) {
    //     console.log(input[i].join("\t\t"))
    // }
    // console.log()
    // for (let i = 0; i < visited.length; i++) {
    //     console.log(visited[i].join(""))
    // }
	const enclosed = countEnclosed(visited, input)

    return [furthest,enclosed]
}


const answer = solution(inputData)

console.log("Part 1")
console.log(answer[0])

console.log("Part 2")
console.log(answer[1])
