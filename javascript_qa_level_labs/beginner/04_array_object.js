// 초급 04: 배열과 객체

const results = ['PASS', 'FAIL', 'PASS'];
console.log('첫 번째 결과:', results[0]);
results[1] = 'PASS';
console.log('변경 후:', results);

const testCase = {
  id: 'TC-LOGIN-001',
  title: '정상 로그인',
  expected: 'SUCCESS',
  actual: 'SUCCESS',
  result: 'PASS'
};

console.log('점 표기법:', testCase.id);
console.log('대괄호 표기법:', testCase['result']);

testCase.result = 'RECHECK';
console.log('수정 후:', testCase);
