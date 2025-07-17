# my_calculator_lib/calculator.py

# 순수 계산 함수들
def _add(num1: int, num2: int) -> int:
    return num1 + num2

def _subtract(num1: int, num2: int) -> int:
    return num1 - num2

def _multiply(num1: int, num2: int) -> int:
    return num1 * num2

def _divide(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return num1 / num2

# 연산자 매핑 딕셔너리
_OPERATION_MAP = {
    '+': _add,
    '-': _subtract,
    '*': _multiply,
    '/': _divide,
}

# 외부에서 호출될 메인 계산 함수
def calculate_result(a_str: str, b_str: str, op_type: str):
    """
    주어진 문자열 숫자와 연산자로 계산을 수행합니다.

    Args:
        a_str (str): 첫 번째 숫자 문자열.
        b_str (str): 두 번째 숫자 문자열.
        op_type (str): 연산자 문자열 (+, -, *, / 등).

    Returns:
        int or float: 계산 결과.

    Raises:
        ValueError: 입력이 유효하지 않거나 지원하지 않는 연산자일 경우.
    """
    # 1. 숫자 유효성 검사 및 변환 (계산 라이브러리 책임)
    try:
        num1 = int(a_str)
        num2 = int(b_str)
    except (ValueError, TypeError):
        # 숫자로 변환 불가능한 경우 (예: "hello")
        raise ValueError("유효하지 않은 숫자 입력입니다. 숫자만 입력해주세요.")

    # 2. 연산자 유효성 검사 및 함수 선택 (계산 라이브러리 책임)
    operation_func = _OPERATION_MAP.get(op_type)
    if not operation_func:
        raise ValueError(f"지원하지 않는 연산자입니다: '{op_type}'. 지원 연산자: {list(_OPERATION_MAP.keys())}")

    # 3. 실제 연산 수행 (계산 라이브러리 책임)
    return operation_func(num1, num2)