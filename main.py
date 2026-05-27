import streamlit as st
import math

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

st.title("🧮 계산기 웹앱")
st.write("사칙연산, 모듈러연산, 지수연산, 로그연산을 할 수 있습니다.")

# 연산 선택
operation = st.selectbox(
    "연산을 선택하세요",
    [
        "덧셈 (+)",
        "뺄셈 (-)",
        "곱셈 (×)",
        "나눗셈 (÷)",
        "모듈러 (%)",
        "지수 (x^y)",
        "로그 (log)"
    ]
)

# 사칙연산, 모듈러, 지수
if operation != "로그 (log)":
    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=0.0)

    if st.button("계산하기"):
        try:
            if operation == "덧셈 (+)":
                result = num1 + num2
            elif operation == "뺄셈 (-)":
                result = num1 - num2
            elif operation == "곱셈 (×)":
                result = num1 * num2
            elif operation == "나눗셈 (÷)":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                else:
                    result = num1 / num2
                    st.success(f"결과: {result}")
                    st.stop()
            elif operation == "모듈러 (%)":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                else:
                    result = num1 % num2
            elif operation == "지수 (x^y)":
                result = num1 ** num2

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 로그 연산
else:
    number = st.number_input("로그를 계산할 숫자", value=1.0)
    base = st.number_input("로그 밑(base)", value=10.0)

    if st.button("계산하기"):
        try:
            if number <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
            elif base <= 0 or base == 1:
                st.error("로그의 밑은 0보다 크고 1이 아니어야 합니다.")
            else:
                result = math.log(number, base)
                st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")
