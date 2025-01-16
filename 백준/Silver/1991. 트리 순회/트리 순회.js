const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const tree = {};

for (let i = 1; i <= N; i++) {
    const [parent, left, right] = input[i].split(" ");
    tree[parent] = [left, right];
}

const result = {
    preorder: [],
    inorder: [],
    postorder: []
};

// 전위순회: 방문 → 왼쪽 → 오른쪽
function preorder(node) {
    if (node === ".") return;
    result.preorder.push(node);
    preorder(tree[node][0]);
    preorder(tree[node][1]);
}

// 중위순회: 왼쪽 → 방문 → 오른쪽
function inorder(node) {
    if (node === ".") return;
    inorder(tree[node][0]);
    result.inorder.push(node);
    inorder(tree[node][1]);
}

// 후위순회: 왼쪽 → 오른쪽 → 방문
function postorder(node) {
    if (node === ".") return;
    postorder(tree[node][0]);
    postorder(tree[node][1]);
    result.postorder.push(node);
}

preorder("A");
inorder("A");
postorder("A");

console.log(result.preorder.join(""));
console.log(result.inorder.join(""));
console.log(result.postorder.join(""));