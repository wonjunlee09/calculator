import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

# 멋있는 배경과 스타일 설정
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-attachment: fixed;
    min-height: 100vh;
}

/* 메인 컨테이너 스타일 */
.main {
    background-color: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    margin: 20px;
}

/* 제목 스타일 */
h1 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.5em;
    margin-bottom: 10px;
    text-shadow: 0 2px 10px rgba(102, 126, 234, 0.2);
}

/* 설명 텍스트 스타일 */
.description {
    font-size: 1.1em;
    color: #555;
    margin-bottom: 20px;
}

/* 드롭다운 및 입력 필드 스타일 */
div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%) !important;
    color: #333 !important;
    border: 2px solid #667eea !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

div[data-baseweb="select"] span {
    color: #333 !important;
}

ul[role="listbox"] {
    background-color: white !important;
    border: 2px solid #667eea !important;
    border-radius: 10px !important;
}

ul[role="listbox"] li {
    color: #333 !important;
    padding: 10px !important;
}

ul[role="listbox"] li:hover {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
}

/* 버튼 스타일 */
button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 30px !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
}

button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
}

/* 성공 메시지 스타일 */
.stSuccess {
    background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%) !important;
    border-radius: 10px !important;
    padding: 15px !important;
    border-left: 5px solid #4CAF50 !important;
}

/* 에러 메시지 스타일 */
.stError {
    background: linear-gradient(135deg, #fa8072 0%, #ff6b6b 100%) !important;
    border-radius: 10px !important;
    padding: 15px !important;
    border-left: 5px solid #f44336 !important;
}

/* 입력 필드 스타일 */
.stNumberInput > div > div > input {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%) !important;
    border: 2px solid #667eea !important;
    border-radius: 10px !important;
    padding: 10px !important;
    color: #333 !important;
}

/* Expander 스타일 */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%) !important;
    border-radius: 10px !important;
    border: 2px solid #667eea !important;
}

/* 서브헤더 스타일 */
h3 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 20px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 계산기 웹앱")
st.markdown('<p class="description">사칙연산, 모듈러연산, 지수연산, 로그연산, 자연로그, 그래프 그리기를 지원합니다.</p>', unsafe_allow_html=True)

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
        "자연로그 (ln)",
        "그래프"
    ]
)

# 그래프 기능
if operation == "그래프":
    st.subheader("📈 함수 그래프 그리기")

    expression = st.text_input(
        "함수를 입력하세요",
        value="x**2",
        help="예시: x**2, np.sin(x), np.cos(x), x**3-2*x+1, np.log(x)"
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
                ax.plot(x, y, linewidth=2.5, color="#667eea")

                ax.set_title(f"y = {expression}", fontsize=14, fontweight='bold')
                ax.set_xlabel("x", fontsize=12)
                ax.set_ylabel("y", fontsize=12)
                ax.grid(True, alpha=0.3)
                ax.set_facecolor("#f8f9fa")

                st.pyplot(fig)

        except Exception as e:
            st.error(f"그래프를 그릴 수 없습니다: {e}")

# 로그 연산
elif operation == "로그 (log)":
    st.subheader("📊 로그 계산 (log)")
    number = st.number_input("로그를 계산할 숫자", value=1.0, min_value=0.001)
    base = st.number_input("로그 밑(base)", value=10.0, min_value=0.001)

    if st.button("계산하기"):
        try:
            if number <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
            elif base <= 0 or base == 1:
                st.error("로그의 밑은 0보다 크고 1이 아니어야 합니다.")
            else:
                result = math.log(number, base)
                st.success(f"✨ 결과: **{result:.6f}**")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 자연로그 연산
elif operation == "자연로그 (ln)":
    st.subheader("📊 자연로그 계산 (ln)")
    number = st.number_input("자연로그를 계산할 숫자", value=1.0, min_value=0.001)

    if st.button("계산하기"):
        try:
            if number <= 0:
                st.error("자연로그의 진수는 0보다 커야 합니다.")
            else:
                result = math.log(number)
                st.success(f"✨ 결과: **{result:.6f}**")
                st.info(f"📌 ln({number}) = {result:.6f}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 나머지 연산
else:
    st.subheader(f"🔢 {operation} 계산")
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

            st.success(f"✨ 결과: **{result}**")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 사용법 안내
with st.expander("📖 그래프 기능 사용법"):
    st.markdown("""
    **입력 예시**

    - `x**2` - 2차 함수
    - `x**3` - 3차 함수
    - `np.sin(x)` - 사인 함수
    - `np.cos(x)` - 코사인 함수
    - `np.tan(x)` - 탄젠트 함수
    - `np.exp(x)` - 지수 함수
    - `np.log(x+11)` - 로그 함수
    - `np.sqrt(x)` - 제곱근 함수

    **참고**
    - `x**2`는 x²를 의미합니다.
    - `np.sin(x)`는 사인 함수입니다.
    - X축 범위를 직접 설정할 수 있습니다.
    """)
