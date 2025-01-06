function solution(progresses, speeds) {
  const remainingDays = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );

  const result = [];
  let maxDay = remainingDays[0];
  let count = 0;

  for (let day of remainingDays) {
    if (day <= maxDay) {
      count++;
    } else {
      result.push(count);
      count = 1;
      maxDay = day;
    }
  }

  result.push(count);
  return result;
}
