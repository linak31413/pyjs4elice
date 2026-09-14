// 고급 05: QA 결과 리포트 생성
// [응용 확장]

const results = [
  { id: 'TC-001', result: 'PASS', duration: 120 },
  { id: 'TC-002', result: 'FAIL', duration: 450, reason: 'Timeout' },
  { id: 'TC-003', result: 'PASS', duration: 180 },
  { id: 'TC-004', result: 'PASS', duration: 600 } 
];

const totalCount = results.length;
const passCount = results.filter(r => r.result === 'PASS').length;

const report = {
  generatedAt: new Date().toISOString(),
  total: totalCount,
  pass: passCount,
  fail: results.filter(r => r.result === 'FAIL').length,
  
  // 교재 변형 과제 반영
  passRate: totalCount > 0 ? ((passCount / totalCount) * 100).toFixed(1) + '%' : '0%',
  
  totalDuration: results.reduce((acc, r) => acc + r.duration, 0),
  failures: results.filter(r => r.result === 'FAIL'),
  
  // 500ms 이상 Slow TC 목록 추출
  slowTCs: results.filter(r => r.duration >= 500)
};

console.log(JSON.stringify(report, null, 2));