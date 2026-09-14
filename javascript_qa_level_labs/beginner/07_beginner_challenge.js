// 초급 종합 실습: 결과 문자열을 분석해 PASS/FAIL 출력하기
// TODO 1: resultText에 "FAIL"이 포함되어 있는지 확인한다.
// TODO 2: tcId와 status를 split()으로 분리한다.
// TODO 3: 객체로 정리하여 console.table()로 출력한다.

const resultText = 'TC-LOGIN-003|FAIL';

const hasFail = resultText.includes('FAIL');
const [tcId, status] = resultText.split('|');
const summary = [{ tcId, status, needsReview: hasFail }];

console.table(summary);
