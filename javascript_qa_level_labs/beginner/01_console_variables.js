// 초급 01: console과 변수
// 실행: node 01_console_variables.js

console.log('=== console 실습 ===');

let testerName = '홍길동';
let executedTC = 12;
const projectName = 'Web QA';

console.log('프로젝트:', projectName);
console.log('테스터:', testerName);
console.log('실행 TC:', executedTC);

console.table([
  { id: 'TC-001', result: 'PASS' },
  { id: 'TC-002', result: 'FAIL' },
  { id: 'TC-003', result: 'PASS' }
]);

console.warn('경고 예시: 재확인이 필요합니다.');
console.error('오류 예시: TC-002 실패');
