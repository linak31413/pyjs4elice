// 고급 06: 데이터 주도 QA 파이프라인
// [응용 확장]

const dataset = [
  { id: 1, priceText: '1,500원', expected: 1500 },
  { id: 2, priceText: '9,900원', expected: 9900 },
  { id: 3, priceText: '0원', expected: 0 }
];

const parsePrice = text => Number(text.replace('원', '').replace(',', ''));

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
  summary: results.reduce((acc, r) => {
    acc[r.result] = (acc[r.result] || 0) + 1;
    return acc;
  }, {})
};

console.log(JSON.stringify(report, null, 2));
