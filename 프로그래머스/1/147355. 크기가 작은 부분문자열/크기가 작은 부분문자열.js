function solution(t, p) {
    const targetLength = p.length;
    const pValue = parseInt(p, 10);
    let count = 0;

    for (let i = 0; i <= t.length - targetLength; i++) {
        const substring = t.slice(i, i + targetLength);
        if (parseInt(substring, 10) <= pValue) {
            count++;
        }
    }

    return count;
}