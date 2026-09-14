// 기존 코드 (01_parameterized_tc.js)
const cases = [
  { id: 'LOGIN-001', input: { user: 'admin', pw: '1234' }, expected: 'SUCCESS' },
  { id: 'LOGIN-002', input: { user: 'admin', pw: 'wrong' }, expected: 'FAIL' },
  { id: 'LOGIN-003', input: { user: '', pw: '' }, expected: 'FAIL' },
  { id: 'LOGIN-ERR-003', input: { user: '', pw: 'error' }, expected: 'SUCCESS' }  // Designed to be fail the test
];

function login({ user, pw }) {
  return user === 'admin' && pw === '1234' ? 'SUCCESS' : 'FAIL';
}

const results = cases.map(tc => {
  const actual = login(tc.input);
  return { ...tc, actual, result: actual === tc.expected ? 'PASS' : 'FAIL' };
});

console.log("=== 전체 테스트 결과 ===");
console.table(results.map(({ id, expected, actual, result }) => ({ id, expected, actual, result })));

// [여기부터 추가] 교재 수행 절차: 실패 건만 filter한다.
const failedResults = results.filter(tc => tc.result === 'FAIL');

console.log("=== 실패한 TC 목록 ===");
console.table(failedResults.map(({ id, expected, actual, result }) => ({ id, expected, actual, result })));