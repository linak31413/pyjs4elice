// 고급 06: 데이터 주도 QA 파이프라인
// [응용 확장]

const dataset = [
  { id: 1, priceText: '1,500원', expected: 1500 },
  { id: 2, priceText: '9,900원', expected: 9900 },
  // 잘못된 입력 적용 및 기대 결과(0)
  { id: 3, priceText: '무료', expected: 0 }, 
  // 예상치 못한 문자열 입력 케이스 추가 (기대 결과 null)
  { id: 4, priceText: '가격없음', expected: null } 
];

const parsePrice = text => {
  if (text === '무료') return 0; // '무료'는 0으로 처리
  
  const parsed = Number(text.replace('원', '').replace(',', ''));
  // 숫자로 변환할 수 없는 경우(NaN) null을 반환하도록 정책 정의
  return Number.isNaN(parsed) ? null : parsed; 
};

const results = dataset.map(row => {
  const actual = parsePrice(row.priceText);
  return {
    ...row,
    actual,
    result: actual === row.expected ? 'PASS' : 'FAIL'
  };
});

const report = {
  results,
  // 결과별 개수 요약 집계
  summary: results.reduce((acc, r) => {
    acc[r.result] = (acc[r.result] || 0) + 1;
    return acc;
  }, {})
};

console.log(JSON.stringify(report, null, 2));