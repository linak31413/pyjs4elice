// 고급 02: 경계값/동등분할 사고를 코드로 표현
// [응용 확장]

const ageCases = [
  { id: 'AGE-001', age: -1, expected: false },
  { id: 'AGE-002', age: 0, expected: true },
  { id: 'AGE-003', age: 120, expected: true },
  { id: 'AGE-004', age: 121, expected: false }
];

const isValidAge = age => Number.isInteger(age) && age >= 0 && age <= 120;

const results = ageCases.map(tc => {
  const actual = isValidAge(tc.age);
  return { ...tc, actual, result: actual === tc.expected ? 'PASS' : 'FAIL' };
});

console.table(results);
