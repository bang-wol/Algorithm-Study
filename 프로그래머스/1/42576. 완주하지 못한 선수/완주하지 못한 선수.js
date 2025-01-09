function solution(participant, completion) {
    const map = new Map();

    for (let player of participant) {
        map.set(player, (map.get(player) || 0) + 1);
    }

    for (let player of completion) {
        map.set(player, map.get(player) - 1);
    }

    for (let [player, count] of map) {
        if (count > 0) return player;
    }
}