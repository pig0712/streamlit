import streamlit as st

if "aaa" not in st.session_state:
    st.session_state.aaa = ""

aaa = st.session_state.aaa

st.header("계산기")
col1, col2, col3, col4, col5 = st.columns(5)

with col2:
    if st.button("7"):
        aaa = aaa + "7"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("4"):
        aaa = aaa + "4"
        st.session_state.aaa = aaa
        print(aaa)


    if st.button("1"):
        aaa = aaa + "1"
        st.session_state.aaa = aaa
        print(aaa)

with col3:
    if st.button("8"):
        aaa = aaa + "8"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("5"):
        aaa = aaa + "5"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("2"):
        aaa = aaa + "2"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("0"):
        aaa = aaa + "0"
        st.session_state.aaa = aaa
        print(aaa)


with col4:
    if st.button("9"):
        aaa = aaa + "9"
        st.session_state.aaa = aaa
        print(aaa)


    if st.button("6"):
        aaa = aaa + "6"
        st.session_state.aaa = aaa
        print(aaa)


    if st.button("3"):
        aaa = aaa + "3"
        st.session_state.aaa = aaa
        print(aaa)

with col5:
    if st.button("/"):
        aaa = aaa + "/"
        st.session_state.aaa = aaa
        print(aaa)


    if st.button("x"):
        aaa = aaa + "*"
        st.session_state.aaa = aaa
        print(aaa)


    if st.button("더하기"):
        aaa = aaa + "+"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("−"):
        aaa = aaa + "-"
        st.session_state.aaa = aaa
        print(aaa)

    if st.button("="):
        result = None
        exec(f"result = {aaa}")
        st.write("결과:",result)
        print(result)

st.subheader(aaa)