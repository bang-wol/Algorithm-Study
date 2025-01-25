function solution(s) {
    const map = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ];

    map.forEach((word, index) => {
        const regex = new RegExp(word, "g");
        s = s.replace(regex, index);
    });

    return parseInt(s, 10);
}