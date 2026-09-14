// 고급 03: JSON 응답 Contract 검증
// [응용 확장] 실제 API 호출 대신 응답 객체를 검증한다.

const response = {
  status: 200,
  body: {
    userId: 101,
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

console.table(checks.map(([check, ok]) => ({ check, result: ok ? 'PASS' : 'FAIL' })));
