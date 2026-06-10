import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

# 드롭다운 색상 강제 지정
st.markdown("""
<style>
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

div[data-baseweb="select"] span {
    color: black !important;
}

ul[role="listbox"] {
    background-color: white !important;
}

ul[role="listbox"] li {
    color: black !important;
}

ul[role="listbox"] li:hover {
    background-color: #f0f0f0 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 계산기 웹앱")
st.write("사칙연산, 모듈러연산, 지수연산, 로그연산, 그래프 그리기를 지원합니다.")

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
        "로그 (log)",
        "그래프"
    ]
)

# 그래프 기능
if operation == "그래프":
    st.subheader("📈 함수 그래프 그리기")

    expression = st.text_input(
        "함수를 입력하세요",
        value="x**2",
        help="예시: x**2, np.sin(x), np.cos(x), x**3-2*x+1"
    )

    col1, col2 = st.columns(2)

    with col1:
        x_min = st.number_input("X 최소값", value=-10.0)

    with col2:
        x_max = st.number_input("X 최대값", value=10.0)

    if st.button("그래프 그리기"):
        try:
            if x_min >= x_max:
                st.error("X 최소값은 최대값보다 작아야 합니다.")
            else:
                x = np.linspace(x_min, x_max, 500)

                y = eval(
                    expression,
                    {
                        "__builtins__": {},
                        "np": np,
                        "x": x
                    }
                )

                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(x, y, linewidth=2)

                ax.set_title(f"y = {expression}")
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.grid(True)

                st.pyplot(fig)

        except Exception as e:
            st.error(f"그래프를 그릴 수 없습니다: {e}")

# 로그 연산
elif operation == "로그 (log)":
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

# 나머지 연산
else:
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
                    st.stop()
                result = num1 / num2

            elif operation == "모듈러 (%)":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                    st.stop()
                result = num1 % num2

            elif operation == "지수 (x^y)":
                result = num1 ** num2

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 사용법 안내
with st.expander("📖 그래프 기능 사용법"):
    st.markdown("""
    **입력 예시**

    - `x**2`
    - `x**3`
    - `np.sin(x)`
    - `np.cos(x)`
    - `np.tan(x)`
    - `np.exp(x)`
    - `np.log(x+11)`

    **참고**
    - `x**2`는 x²를 의미합니다.
    - `np.sin(x)`는 사인 함수입니다.
    - X축 범위를 직접 설정할 수 있습니다.
    """)
