// 고급 종합: TC → 실행 → 판정 → 요약 → 실패 추출
// [응용 확장]

const testCases = [
  { id: 'PAY-001', input: '1,000원', expected: 1000 },
  { id: 'PAY-002', input: '12,500원', expected: 12500 },
  { id: 'PAY-003', input: '무료', expected: 0 },
  // TC 추가 데이터
  { id: 'PAY-004', input: '0원', expected: 0 },
  { id: 'PAY-005', input: '-500원', expected: -500 }, 
  // 의도적인 FAIL을 발생시켜 reason 수집을 확인하기 위한 케이스
  { id: 'PAY-006', input: '오류값', expected: 0 } 
];

const normalizePrice = text => {
  if (text === '무료') return 0;
  const parsed = Number(text.replace('원', '').replace(',', ''));
  return Number.isNaN(parsed) ? null : parsed;
};

const results = testCases.map(tc => {
  const actual = normalizePrice(tc.input);
  const isPass = actual === tc.expected;
  
  // FAIL의 reason을 리포트에 보존
  return { 
    ...tc, 
    actual, 
    result: isPass ? 'PASS' : 'FAIL',
    reason: isPass ? null : `Expected ${tc.expected} but got ${actual}`
  };
});

const failures = results.filter(r => r.result === 'FAIL');

// 최종 리포트를 위한 객체 생성
const report = {
  summary: {
    total: results.length,
    pass: results.length - failures.length,
    fail: failures.length
  },
  failures: failures
};

// JSON 문자열로 출력
console.log(JSON.stringify(report, null, 2));