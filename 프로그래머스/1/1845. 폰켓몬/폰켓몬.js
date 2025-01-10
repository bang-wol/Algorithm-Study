function solution(nums) {
    const unique = new Set(nums);
    return Math.min(unique.size, nums.length / 2);
}