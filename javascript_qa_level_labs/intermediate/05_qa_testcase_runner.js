// 중급 05: 데이터 기반 간이 TC Runner

const testCases = [
  { id: 'TC-001', input: 'admin', expected: 'ALLOW' },
  { id: 'TC-002', input: 'guest', expected: 'DENY' },
  { id: 'TC-003', input: '', expected: 'DENY' }
];

const authorize = user => user === 'admin' ? 'ALLOW' : 'DENY';

const results = testCases.map(tc => {
  const actual = authorize(tc.input);
  return {
    ...tc,
    actual,
    result: actual === tc.expected ? 'PASS' : 'FAIL'
  };
});

console.table(results);
console.log('FAIL:', results.filter(r => r.result === 'FAIL').length);
