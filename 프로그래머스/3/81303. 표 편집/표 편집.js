function solution(n, k, cmd) {
  const deleted = [];
  const table = Array.from({ length: n }, (_, i) => ({
    prev: i - 1,
    next: i + 1,
  }));
  table[0].prev = null;
  table[n - 1].next = null;

  let cursor = k;

  for (let command of cmd) {
    const [op, X] = command.split(" ");
    if (op === "U") {
      for (let i = 0; i < +X; i++) cursor = table[cursor].prev;
    } else if (op === "D") {
      for (let i = 0; i < +X; i++) cursor = table[cursor].next;
    } else if (op === "C") {
      deleted.push(cursor);
      const prev = table[cursor].prev;
      const next = table[cursor].next;
      if (prev !== null) table[prev].next = next;
      if (next !== null) table[next].prev = prev;
      cursor = next !== null ? next : prev;
    } else if (op === "Z") {
      const restore = deleted.pop();
      const prev = table[restore].prev;
      const next = table[restore].next;
      if (prev !== null) table[prev].next = restore;
      if (next !== null) table[next].prev = restore;
    }
  }

  const result = Array(n).fill("O");
  for (let index of deleted) result[index] = "X";
  return result.join("");
}