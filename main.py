import streamlit as st

# 계산을 수행하는 함수
def calculate(expression):
    try:
        # eval은 간단한 계산기에는 유용하지만, 보안상 위험할 수 있으니 주의가 필요합니다.
        result = eval(expression)
        return result
    except Exception as e:
        return "에러"

# Streamlit 앱 설정
st.set_page_config(page_title="버튼 계산기", page_icon="🧮")

# 세션 상태 초기화
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# 디스플레이 설정
st.title("🧮 버튼 기반 계산기")

# 현재 수식을 표시
st.text_input("계산기", st.session_state.expression, key="display", disabled=True)

# 버튼 레이아웃
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']  # 클리어 버튼
]

# 버튼 클릭 처리
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == 'C':
                st.session_state.expression = ""
            elif button == '=':
                result = calculate(st.session_state.expression)
                st.session_state.expression = str(result)
            else:
                st.session_state.expression += button

# 스타일링 (옵션)
st.markdown(
    """
    <style>
    .stButton>button {
        height: 60px;
        width: 60px;
        font-size: 24px;
    }
    .stTextInput>div>div>input {
        font-size: 24px;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
