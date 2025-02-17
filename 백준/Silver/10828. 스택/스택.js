const fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const stack = [];
const result = [];

for (let i = 1; i <= N; i++) {
    const command = input[i];
    
    if (command.startsWith("push")) {
        const [, num] = command.split(" ");
        stack.push(Number(num));
    } else if (command === "pop") {
        result.push(stack.length ? stack.pop() : -1);
    } else if (command === "size") {
        result.push(stack.length);
    } else if (command === "empty") {
        result.push(stack.length ? 0 : 1);
    } else if (command === "top") {
        result.push(stack.length ? stack[stack.length - 1] : -1);
    }
}

console.log(result.join("\n"));
