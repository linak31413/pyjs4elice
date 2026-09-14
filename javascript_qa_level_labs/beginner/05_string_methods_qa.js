// 초급 05: 문자열 메서드와 QA 활용

const message = 'Error: 404 Not Found';
console.log('길이:', message.length);
console.log('Error 포함?', message.includes('Error'));
console.log('Error 위치:', message.indexOf('Error'));

const csvLine = 'TC-001,LOGIN,PASS';
const parts = csvLine.split(',');
console.log('split 결과:', parts);

const sanitized = '1,500원'.replace('원', '').replace(',', '');
console.log('정제된 금액:', sanitized, '=>', Number(sanitized));

const filenameParts = ['20260914', 'Staging', 'TC-001', 'Result'];
console.log('파일명:', filenameParts.join('_') + '.csv');
