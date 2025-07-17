# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

# 당신이 만든 계산 라이브러리에서 핵심 계산 함수를 임포트
# (프로젝트 구조에 따라 import 경로가 달라질 수 있습니다. 예: from .my_calculator_lib.calculator import calculate_result)
from calculator import calculate_result

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    # 1. 요청에서 JSON 데이터 추출 (app.py 책임)
    data = request.get_json()

    # 필수 필드 누락 검사 (app.py 책임 - 웹 요청의 기본 필수값 확인)
    if not all(k in data for k in ['a', 'b', 'op']):
        return jsonify({'error': '필수 입력값 (a, b, op)이 누락되었습니다.'}), 400

    a_str = data.get('a')
    b_str = data.get('b')
    op_type = data.get('op')

    # 2. 계산 라이브러리에 실제 계산 위임 (app.py -> 라이브러리)
    try:
        # calculate_result 함수가 모든 숫자 변환, 연산자 유효성, 실제 연산 처리를 담당
        result = calculate_result(a_str, b_str, op_type)
        
        # 3. 성공 결과 JSON 응답 (app.py 책임)
        return jsonify({'result': result})

    # 4. 계산 라이브러리에서 발생한 예외 처리 (app.py 책임)
    except ValueError as e:
        # calculate_result 함수에서 발생시킨 ValueError를 잡아서 클라이언트에게 전달
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # 예상치 못한 다른 모든 에러 (내부 서버 에러) 처리
        # 실제 서비스에서는 에러 로그를 남기고, 사용자에게는 일반적인 메시지 전달
        print(f"예상치 못한 서버 오류: {e}")
        return jsonify({'error': '서버 내부 오류가 발생했습니다.'}), 500

if __name__ == '__main__':
    app.run(debug=True)