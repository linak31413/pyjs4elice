// 중급 03: 화살표 함수 3단계

const addOld = function (x, y) {
  return x + y;
};

const add = (x, y) => {
  return x + y;
};

const double = x => x * 2;

console.log(addOld(2, 3));
console.log(add(2, 3));
console.log(double(5));

const isPass = tc => tc.actual === tc.expected;
console.log(isPass({ actual: 'OK', expected: 'OK' }));
