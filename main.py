import streamlit as st

# 앱의 제목
st.title("간단한 계산기")

# 사용자 입력 받기
number1 = st.number_input("첫 번째 숫자를 입력하세요", value=0)
number2 = st.number_input("두 번째 숫자를 입력하세요", value=0)

# 연산자 선택
operation = st.selectbox("연산을 선택하세요", ["+", "-", "*", "/"])

# 계산 버튼
if st.button("계산"):
    try:
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            if number2 != 0:
                result = number1 / number2
            else:
                st.error("0으로 나눌 수 없습니다.")
                result = None
        if result is not None:
            st.success(f"결과: {result}")
    except Exception as e:
        st.error(f"에러 발생: {e}")
