// 중급 02: JSON stringify / parse

const result = {
  id: 'TC-001',
  result: 'PASS',
  duration: 132,
  tags: ['smoke', 'login']
};

const jsonString = JSON.stringify(result, null, 2);
console.log('=== stringify ===');
console.log(jsonString);

const receivedData = '{"id":"TC-002","result":"FAIL","duration":420}';
const parsed = JSON.parse(receivedData);
console.log('=== parse ===');
console.log(parsed.id, parsed.result, parsed.duration);
