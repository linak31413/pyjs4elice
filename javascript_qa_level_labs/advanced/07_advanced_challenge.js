// 고급 종합: TC → 실행 → 판정 → 요약 → 실패 추출
// [응용 확장]

const testCases = [
  { id: 'PAY-001', input: '1,000원', expected: 1000 },
  { id: 'PAY-002', input: '12,500원', expected: 12500 },
  { id: 'PAY-003', input: '무료', expected: 0 }
];

const normalizePrice = text => {
  if (text === '무료') return 0;
  return Number(text.replace('원', '').replace(',', ''));
};

const results = testCases.map(tc => {
  const actual = normalizePrice(tc.input);
  return { ...tc, actual, result: actual === tc.expected ? 'PASS' : 'FAIL' };
});

const failures = results.filter(r => r.result === 'FAIL');
const summary = {
  total: results.length,
  pass: results.length - failures.length,
  fail: failures.length
};

console.table(results);
console.log('summary=', summary);
console.log('failures=', failures);
