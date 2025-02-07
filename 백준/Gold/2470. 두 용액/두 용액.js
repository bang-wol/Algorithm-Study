const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);

let left = 0, right = n-1;
let minDiff = Infinity;
let answer = [0, 0];

while (left < right) {
    let sum = arr[left] + arr[right];
    
    if (Math.abs(sum) < minDiff) {
        minDiff = Math.abs(sum);
        answer = [arr[left], arr[right]];
    }
    
    if (sum < 0) {
        left++;
    } else {
        right--;
    }
}

console.log(answer[0], answer[1]);