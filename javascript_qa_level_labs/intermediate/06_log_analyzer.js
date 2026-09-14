// 중급 06: 로그 문자열 분석기
// 첨부자료의 includes / indexOf / split / replace 응용

const logs = [
  '[INFO] TC-001 Login Success',
  '[ERROR] TC-002 Connection Timed Out',
  '[WARN] TC-003 Retry',
  '[ERROR] TC-004 404 Not Found'
];

const errors = logs
  .filter(line => line.includes('[ERROR]'))
  .map(line => ({
    raw: line,
    tcId: line.split(' ')[1],
    message: line.substring(line.indexOf(' ') + 1)
  }));

console.table(errors);
