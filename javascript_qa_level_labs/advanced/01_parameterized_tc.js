// 고급 01: 파라미터화 TC 실행
// [응용 확장] 첨부자료의 배열/객체/map/arrow function을 QA TC 자동화 구조로 확장

const cases = [
  { id: 'LOGIN-001', input: { user: 'admin', pw: '1234' }, expected: 'SUCCESS' },
  { id: 'LOGIN-002', input: { user: 'admin', pw: 'wrong' }, expected: 'FAIL' },
  { id: 'LOGIN-003', input: { user: '', pw: '' }, expected: 'FAIL' }
];

function login({ user, pw }) {
  return user === 'admin' && pw === '1234' ? 'SUCCESS' : 'FAIL';
}

const results = cases.map(tc => {
  const actual = login(tc.input);
  return { ...tc, actual, result: actual === tc.expected ? 'PASS' : 'FAIL' };
});

console.table(results.map(({ id, expected, actual, result }) => ({ id, expected, actual, result })));
