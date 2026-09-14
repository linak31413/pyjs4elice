// 중급 종합: 실행 결과 요약 생성

const rawResults = [
  'TC-001|PASS|120',
  'TC-002|FAIL|450',
  'TC-003|PASS|180',
  'TC-004|FAIL|520'
];

const rows = rawResults.map(line => {
  const [id, result, duration] = line.split('|');
  return { id, result, duration: Number(duration) };
});

const summary = {
  total: rows.length,
  pass: rows.filter(r => r.result === 'PASS').length,
  fail: rows.filter(r => r.result === 'FAIL').length,
  slowCases: rows.filter(r => r.duration >= 500).map(r => r.id)
};

console.table(rows);
console.log(JSON.stringify(summary, null, 2));
