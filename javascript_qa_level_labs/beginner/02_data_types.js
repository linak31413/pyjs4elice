// 초급 02: 데이터 타입

const title = 'Login Test';        // String
const count = 3;                   // Number
const passed = true;               // Boolean
let notAssigned;                   // undefined
const emptyValue = null;           // null
const cases = ['TC-001', 'TC-002']; // Array
const tc = { id: 'TC-001', result: 'PASS' }; // Object

console.log(typeof title, title);
console.log(typeof count, count);
console.log(typeof passed, passed);
console.log(typeof notAssigned, notAssigned);
console.log('null:', emptyValue);
console.log('array:', cases);
console.log('object:', tc);
