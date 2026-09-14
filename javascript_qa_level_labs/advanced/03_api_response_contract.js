// 고급 03: JSON 응답 Contract 검증
// [응용 확장] 실제 API 호출 대신 응답 객체를 검증한다.

const response = {
  status: 404,    // FAIL
  body: {
    userId: "as", // FAIL
    name: 'tester',
    roles: ['qa', 'viewer']
  }
};

const checks = [
  ['status=200', response.status === 200],
  ['userId 존재', typeof response.body.userId === 'number'],
  ['name 문자열', typeof response.body.name === 'string'],
  ['roles 배열', Array.isArray(response.body.roles)],
  ['qa role 포함', response.body.roles.includes('qa')]
];

// 1. 전체 검증 결과를 객체 배열로 매핑
const results = checks.map(([check, ok]) => ({ check, result: ok ? 'PASS' : 'FAIL' }));

console.log("=== 전체 검증 결과 ===");
console.table(results);

// 2. 교재 수행 절차: FAIL 검증만 추출한다.
const failedChecks = results.filter(item => item.result === 'FAIL');

console.log("=== 실패한 검증 목록 ===");
console.table(failedChecks);