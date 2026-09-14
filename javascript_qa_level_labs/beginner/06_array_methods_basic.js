// 초급 06: 배열 기본 메서드

const testResults = [];

testResults.push('TC-001: PASS');
testResults.push('TC-002: FAIL');
console.log('push 후:', testResults);

const removed = testResults.pop();
console.log('pop:', removed);
console.log('남은 배열:', testResults);

testResults.unshift('HEADER');
console.log('unshift 후:', testResults);

testResults.shift();
console.log('shift 후:', testResults);

const scenarios = ['정상로그인', '중복항목', '로그아웃'];
scenarios.splice(1, 1, '비밀번호오류');
console.log('splice 후:', scenarios);
