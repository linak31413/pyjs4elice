const lengthCases = [
  { id: 'LEN-001', input: '1234567', expected: false },
  { id: 'LEN-002', input: '12345678', expected: true },
  { id: 'LEN-003', input: '12345678901234567890', expected: true },
  { id: 'LEN-004', input: '123456789012345678901', expected: false },
  { id: 'LEN-004', input: '', expected: true }
];

// 문자열 타입인지 확인하고, 길이가 8 이상 20 이하인지 판정하는 함수
const isValidLength = str => typeof str === 'string' && str.length >= 8 && str.length <= 20;

const results = lengthCases.map(tc => {
  const actual = isValidLength(tc.input);
  return { ...tc, actual, result: actual === tc.expected ? 'PASS' : 'FAIL' };
});

console.table(results);