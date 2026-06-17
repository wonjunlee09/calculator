import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

# 사이버펑크 스타일의 배경과 스타일 설정
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 50%, #0d1b2a 100%);
    background-attachment: fixed;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        linear-gradient(0deg, transparent 24%, rgba(0, 255, 255, 0.05) 25%, rgba(0, 255, 255, 0.05) 26%, transparent 27%, transparent 74%, rgba(0, 255, 255, 0.05) 75%, rgba(0, 255, 255, 0.05) 76%, transparent 77%, transparent),
        linear-gradient(90deg, transparent 24%, rgba(255, 0, 255, 0.05) 25%, rgba(255, 0, 255, 0.05) 26%, transparent 27%, transparent 74%, rgba(255, 0, 255, 0.05) 75%, rgba(255, 0, 255, 0.05) 76%, transparent 77%, transparent);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: 0;
}

/* 메인 컨테이너 스타일 */
.main {
    background: linear-gradient(135deg, rgba(10, 14, 39, 0.8) 0%, rgba(26, 26, 62, 0.85) 100%);
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.3), inset 0 0 20px rgba(255, 0, 255, 0.1);
    margin: 20px;
    border: 2px solid rgba(0, 255, 255, 0.3);
    position: relative;
    z-index: 1;
}

/* 제목 스타일 */
h1 {
    background: linear-gradient(135deg, #00ffff 0%, #ff00ff 50%, #00ffff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.5em;
    margin-bottom: 10px;
    text-shadow: 0 0 20px rgba(0, 255, 255, 0.5), 0 0 40px rgba(255, 0, 255, 0.3);
    font-weight: 900;
    letter-spacing: 2px;
}

/* 설명 텍스트 스타일 */
.description {
    font-size: 1.1em;
    color: #00ffff;
    margin-bottom: 20px;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

/* 드롭다운 및 입력 필드 스타일 */
div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%) !important;
    color: #00ffff !important;
    border: 2px solid #00ffff !important;
    border-radius: 8px !important;
    padding: 10px !important;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2) !important;
}

div[data-baseweb="select"] span {
    color: #00ffff !important;
}

ul[role="listbox"] {
    background-color: rgba(10, 14, 39, 0.95) !important;
    border: 2px solid #00ffff !important;
    border-radius: 8px !important;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
}

ul[role="listbox"] li {
    color: #00ffff !important;
    padding: 10px !important;
    border-bottom: 1px solid rgba(0, 255, 255, 0.1) !important;
}

ul[role="listbox"] li:hover {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.3) 0%, rgba(255, 0, 255, 0.3) 100%) !important;
    color: #ffffff !important;
    box-shadow: inset 0 0 10px rgba(0, 255, 255, 0.2) !important;
}

/* 버튼 스타일 */
button {
    background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%) !important;
    color: #000 !important;
    border: 2px solid #00ffff !important;
    border-radius: 8px !important;
    padding: 12px 30px !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5), 0 0 40px rgba(255, 0, 255, 0.3) !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.7), 0 0 60px rgba(255, 0, 255, 0.5) !important;
}

/* 성공 메시지 스타일 */
.stSuccess {
    background: linear-gradient(135deg, rgba(0, 255, 100, 0.1) 0%, rgba(0, 255, 200, 0.1) 100%) !important;
    border-radius: 8px !important;
    padding: 15px !important;
    border-left: 4px solid #00ff64 !important;
    border: 2px solid rgba(0, 255, 100, 0.5) !important;
    color: #00ff99 !important;
    box-shadow: 0 0 15px rgba(0, 255, 100, 0.2) !important;
}

/* 에러 메시지 스타일 */
.stError {
    background: linear-gradient(135deg, rgba(255, 0, 100, 0.1) 0%, rgba(255, 50, 100, 0.1) 100%) !important;
    border-radius: 8px !important;
    padding: 15px !important;
    border-left: 4px solid #ff0080 !important;
    border: 2px solid rgba(255, 0, 100, 0.5) !important;
    color: #ff4080 !important;
    box-shadow: 0 0 15px rgba(255, 0, 100, 0.2) !important;
}

/* 입력 필드 스타일 */
.stNumberInput > div > div > input {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%) !important;
    border: 2px solid #00ffff !important;
    border-radius: 8px !important;
    padding: 10px !important;
    color: #00ffff !important;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2) inset !important;
}

.stNumberInput > div > div > input::placeholder {
    color: rgba(0, 255, 255, 0.5) !important;
}

/* 텍스트 입력 필드 */
.stTextInput > div > div > input {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%) !important;
    border: 2px solid #00ffff !important;
    border-radius: 8px !important;
    padding: 10px !important;
    color: #00ffff !important;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2) inset !important;
}

/* Expander 스타일 */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 255, 0.1) 100%) !important;
    border-radius: 8px !important;
    border: 2px solid #00ffff !important;
    color: #00ffff !important;
}

/* 서브헤더 스타일 */
h3 {
    background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 20px;
    margin-bottom: 15px;
    font-weight: 800;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
}

/* 일반 텍스트 */
p, li {
    color: #00ffff;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ 사이버펑크 계산기")
st.markdown('<p class="description">🔮 삼각함수, 사칙연산, 모듈러연산, 지수연산, 로그연산, 자연로그, 그래프 그리기를 지원합니다.</p>', unsafe_allow_html=True)

# 연산 선택
operation = st.selectbox(
    "🎯 연산을 선택하세요",
    [
        "덧셈 (+)",
        "뺄셈 (-)",
        "곱셈 (×)",
        "나눗셈 (÷)",
        "모듈러 (%)",
        "지수 (x^y)",
        "로그 (log)",
        "자연로그 (ln)",
        "사인 (sin)",
        "코사인 (cos)",
        "탄젠트 (tan)",
        "역사인 (arcsin)",
        "역코사인 (arccos)",
        "역탄젠트 (arctan)",
        "그래프"
    ]
)

# 삼각함수 - 사인 (sin)
if operation == "사인 (sin)":
    st.subheader("📐 사인 계산 (sin)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        angle = st.number_input("각도를 입력하세요", value=0.0)
        angle_unit = st.radio("단위 선택", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - sin(0°) = 0
        - sin(90°) = 1
        - sin(180°) = 0
        - sin(270°) = -1
        """)
    
    if st.button("계산하기"):
        try:
            if angle_unit == "도 (°)":
                angle_rad = math.radians(angle)
            else:
                angle_rad = angle
            
            result = math.sin(angle_rad)
            st.success(f"✨ sin({angle}°) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 삼각함수 - 코사인 (cos)
elif operation == "코사인 (cos)":
    st.subheader("📐 코사인 계산 (cos)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        angle = st.number_input("각도를 입력하세요", value=0.0)
        angle_unit = st.radio("단위 선택", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - cos(0°) = 1
        - cos(90°) = 0
        - cos(180°) = -1
        - cos(270°) = 0
        """)
    
    if st.button("계산하기"):
        try:
            if angle_unit == "도 (°)":
                angle_rad = math.radians(angle)
            else:
                angle_rad = angle
            
            result = math.cos(angle_rad)
            st.success(f"✨ cos({angle}°) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 삼각함수 - 탄젠트 (tan)
elif operation == "탄젠트 (tan)":
    st.subheader("📐 탄젠트 계산 (tan)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        angle = st.number_input("각도를 입력하세요", value=0.0)
        angle_unit = st.radio("단위 선택", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - tan(0°) = 0
        - tan(45°) = 1
        - tan(90°)는 정의되지 않음
        - tan(180°) = 0
        """)
    
    if st.button("계산하기"):
        try:
            if angle_unit == "도 (°)":
                angle_rad = math.radians(angle)
            else:
                angle_rad = angle
            
            result = math.tan(angle_rad)
            st.success(f"✨ tan({angle}°) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 역삼각함수 - 역사인 (arcsin)
elif operation == "역사인 (arcsin)":
    st.subheader("📐 역사인 계산 (arcsin)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("값을 입력하세요 (-1 ~ 1)", value=0.0, min_value=-1.0, max_value=1.0)
        result_unit = st.radio("결과 단위", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - arcsin(0) = 0°
        - arcsin(1) = 90°
        - arcsin(-1) = -90°
        - 입력값 범위: -1 ~ 1
        """)
    
    if st.button("계산하기"):
        try:
            result = math.asin(value)
            if result_unit == "도 (°)":
                result = math.degrees(result)
            st.success(f"✨ arcsin({value}) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 역삼각함수 - 역코사인 (arccos)
elif operation == "역코사인 (arccos)":
    st.subheader("📐 역코사인 계산 (arccos)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("값을 입력하세요 (-1 ~ 1)", value=0.0, min_value=-1.0, max_value=1.0)
        result_unit = st.radio("결과 단위", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - arccos(1) = 0°
        - arccos(0) = 90°
        - arccos(-1) = 180°
        - 입력값 범위: -1 ~ 1
        """)
    
    if st.button("계산하기"):
        try:
            result = math.acos(value)
            if result_unit == "도 (°)":
                result = math.degrees(result)
            st.success(f"✨ arccos({value}) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 역삼각함수 - 역탄젠트 (arctan)
elif operation == "역탄젠트 (arctan)":
    st.subheader("📐 역탄젠트 계산 (arctan)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("값을 입력하세요", value=0.0)
        result_unit = st.radio("결과 단위", ["도 (°)", "라디안 (rad)"])
    
    with col2:
        st.markdown("""
        **참고 정보**
        - arctan(0) = 0°
        - arctan(1) = 45°
        - arctan(-1) = -45°
        - 입력값 범위: 모든 실수
        """)
    
    if st.button("계산하기"):
        try:
            result = math.atan(value)
            if result_unit == "도 (°)":
                result = math.degrees(result)
            st.success(f"✨ arctan({value}) = **{result:.6f}**")
        except Exception as e:
            st.error(f"오류 발생: {e}")

# 그래프 기능
elif operation == "그래프":
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

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(x, y, linewidth=3, color="#00ffff", label=f"y = {expression}")
                
                ax.set_title(f"⚡ y = {expression}", fontsize=16, fontweight='bold', color="#00ffff")
                ax.set_xlabel("x", fontsize=12, color="#00ffff")
                ax.set_ylabel("y", fontsize=12, color="#00ffff")
                ax.grid(True, alpha=0.2, color="#ff00ff")
                ax.set_facecolor("#0a0e27")
                fig.patch.set_facecolor("#0a0e27")
                
                ax.spines['bottom'].set_color('#00ffff')
                ax.spines['left'].set_color('#00ffff')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.tick_params(colors='#00ffff')
                ax.legend(facecolor='#0a0e27', edgecolor='#00ffff', labelcolor='#00ffff')

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
with st.expander("📖 기능 사용법"):
    st.markdown("""
    **삼각함수 입력**
    - 각도를 도(°) 또는 라디안(rad)으로 입력
    - sin, cos, tan는 모든 각도 지원
    - arcsin, arccos는 -1 ~ 1 범위만 지원
    
    **그래프 그리기 입력 예시**
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

# 푸터
st.markdown("""
---
<div style='text-align: center; color: #00ffff; text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);'>
🤖 **사이버펑크 계산기** v2.0 ⚡
</div>
""", unsafe_allow_html=True)
