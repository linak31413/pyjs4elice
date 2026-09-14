# QA Automation Kit - Capstone Project

## 1. 요구사항 명세 (Requirements)
- **REQ-01**: 응답 객체는 필수 키 `id`, `status`, `elapsed_ms`를 반드시 포함해야 한다.
- **REQ-02**: `id`는 정수(int) 타입이어야 한다.
- **REQ-03**: `status`는 `"ok"` 또는 `"fail"` 중 하나의 값만 허용한다.
- **REQ-04**: `elapsed_ms`는 숫자(int, float)여야 하며, 0 이상의 값이어야 한다(음수 금지).
- **REQ-05**: 검증 실패 시 구체적인 오류 원인(reason)과 재현을 위한 evidence 경로가 리포트에 남아야 한다.

## 2. 요구사항-테스트 추적성 (Traceability Matrix)
| REQ ID | 요구사항 내용 | Risk | 관련 TC ID | 자동화 상태 |
| :--- | :--- | :--- | :--- | :--- |
| REQ-01 | 필수 키 존재 검증 | High | TC-001 ~ TC-005, TC-011, TC-012, TC-013 | 완료 |
| REQ-02 | `id` 데이터 타입 검증 | Medium | TC-001 ~ TC-005, TC-014, TC-015 | 완료 |
| REQ-03 | `status` 허용값 검증 | High | TC-001 ~ TC-005, TC-016, TC-017 | 완료 |
| REQ-04 | `elapsed_ms` 타입 및 하한 경계값(>=0) | High | TC-001 ~ TC-010, TC-018, TC-019, TC-020 | 완료 |
| REQ-05 | 리포팅 및 실패 원인/Evidence 수집 | Medium | 전체 TC (TC-001 ~ TC-020) | 완료 |

## 3. 실행 방법
### pytest 단위 테스트 실행
```bash
pytest tests/ -v
```

### 자동화 파이프라인 일괄 실행
```bash
python run.py
```

## 4. 산출물 위치
- 종합 실행 리포트: artifacts/results.json
- 실패 케이스 전용 리포트: artifacts/failed_cases.csv