// 고급 04: 외부 라이브러리 없이 만드는 미니 QA Framework
// [응용 확장]

const tests = [];

function test(name, fn) {
  tests.push({ name, fn });
}

function expect(actual) {
  return {
    toBe(expected) {
      if (actual !== expected) {
        throw new Error(`expected=${expected}, actual=${actual}`);
      }
    },
    toInclude(expected) {
      if (!actual.includes(expected)) {
        throw new Error(`"${expected}"가 포함되어 있지 않음`);
      }
    }
  };
}

function run() {
  const results = [];
  for (const t of tests) {
    try {
      t.fn();
      results.push({ name: t.name, result: 'PASS', reason: '' });
    } catch (err) {
      results.push({ name: t.name, result: 'FAIL', reason: err.message });
    }
  }
  console.table(results);
  return results;
}

test('로그인 성공 메시지', () => {
  expect('Login SUCCESS').toInclude('SUCCESS');
});

test('합계 계산', () => {
  expect([10, 20, 30].reduce((a, b) => a + b, 0)).toBe(60);
});

run();
