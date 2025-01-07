const [N, K] = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

class Queue {
    items = [];
    front = 0;
    rear = 0;

    push(item) {
        this.items.push(item);
        this.rear++;
    }

    size() {
        return this.rear - this.front;
    }

    pop() {
        if (this.size() === 0) throw new Error("Queue is empty");
        const item = this.items[this.front++];
        if (this.front > this.items.length / 2) {
            this.reset();
        }
        return item;
    }

    reset() {
        this.items = this.items.slice(this.front);
        this.rear -= this.front;
        this.front = 0;
    }
}

function solution(N, K) {
    const queue = new Queue();
    const result = [];

    for (let i = 1; i <= N; i++) {
        queue.push(i); 
    }

    while (queue.size() > 0) {
        for (let i = 0; i < K - 1; i++) {
            queue.push(queue.pop());
        }
        result.push(queue.pop()); 
    }

    return `<${result.join(", ")}>`;
}

console.log(solution(N, K));