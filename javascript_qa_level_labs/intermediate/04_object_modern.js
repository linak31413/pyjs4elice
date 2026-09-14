// 중급 04: 객체 조회/수정, 단축문법, 구조분해, spread

const testCase = {
  id: 'TC-001',
  title: '로그인',
  expected: 'SUCCESS'
};

console.log(testCase.id);
console.log(testCase['title']);

testCase.actual = 'SUCCESS';
testCase.result = 'PASS';

const { id, result } = testCase;
console.log('구조분해:', id, result);

const environment = 'Staging';
const execution = { environment, ...testCase };
console.log('spread:', execution);
