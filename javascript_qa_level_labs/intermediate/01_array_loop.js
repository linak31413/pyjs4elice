// 중급 01: ES6+ 배열 순회 메서드

const cases = [
  { id: 'TC-001', duration: 120, result: 'PASS' },
  { id: 'TC-002', duration: 350, result: 'FAIL' },
  { id: 'TC-003', duration: 220, result: 'PASS' },
  { id: 'TC-004', duration: 510, result: 'FAIL' }
];

console.log('--- forEach ---');
cases.forEach(tc => console.log(tc.id, tc.result));

console.log('--- map ---');
const ids = cases.map(tc => tc.id);
console.log(ids);

console.log('--- filter ---');
const failed = cases.filter(tc => tc.result === 'FAIL');
console.table(failed);

console.log('--- find ---');
const slow = cases.find(tc => tc.duration >= 500);
console.log(slow);

console.log('--- reduce ---');
const totalDuration = cases.reduce((acc, tc) => acc + tc.duration, 0);
console.log('총 수행시간:', totalDuration);
