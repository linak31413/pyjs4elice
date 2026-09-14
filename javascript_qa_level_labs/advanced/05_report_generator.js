// 고급 05: QA 결과 리포트 생성
// [응용 확장]

const results = [
  { id: 'TC-001', result: 'PASS', duration: 120 },
  { id: 'TC-002', result: 'FAIL', duration: 450, reason: 'Timeout' },
  { id: 'TC-003', result: 'PASS', duration: 180 }
];

const report = {
  generatedAt: new Date().toISOString(),
  total: results.length,
  pass: results.filter(r => r.result === 'PASS').length,
  fail: results.filter(r => r.result === 'FAIL').length,
  totalDuration: results.reduce((acc, r) => acc + r.duration, 0),
  failures: results.filter(r => r.result === 'FAIL')
};

console.log(JSON.stringify(report, null, 2));
