// 초급 03: 함수, 매개변수, 인자, return

function calcPassRate(passCount, totalCount) {
  if (totalCount === 0) return 0;
  return (passCount / totalCount) * 100;
}

const rate = calcPassRate(8, 10);
console.log(`PASS 비율: ${rate}%`);

function checkExpected(actual, expected) {
  return actual === expected;
}

console.log('TC-001:', checkExpected('SUCCESS', 'SUCCESS') ? 'PASS' : 'FAIL');
console.log('TC-002:', checkExpected('ERROR', 'SUCCESS') ? 'PASS' : 'FAIL');
