import streamlit as st

# 앱 제목
st.set_page_config(page_title="MBTI 진로 추천기 🎯", page_icon="💫")
st.title("💫 MBTI로 알아보는 나의 진로 ✨")
st.write("안녕! 👋 너의 MBTI를 골라주면, 거기에 딱 어울리는 진로를 추천해줄게 😎")

# MBTI 목록
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 드롭다운으로 MBTI 선택
user_mbti = st.selectbox("너의 MBTI는 뭐야? 👀", mbti_list)

# MBTI별 진로 추천 데이터 (기본 파이썬 딕셔너리)
career_dict = {
    "ISTJ": ["공무원 👮‍♂️", "회계사 💼"],
    "ISFJ": ["간호사 💊", "교사 🍎"],
    "INFJ": ["심리상담사 🧠", "작가 ✍️"],
    "INTJ": ["연구원 🔬", "전략기획가 📊"],
    "ISTP": ["엔지니어 🔧", "파일럿 ✈️"],
    "ISFP": ["디자이너 🎨", "사진작가 📸"],
    "INFP": ["작가 ✏️", "사회운동가 🌱"],
    "INTP": ["데이터 분석가 💻", "발명가 ⚙️"],
    "ESTP": ["영업사원 🤝", "스포츠 코치 🏀"],
    "ESFP": ["배우 🎭", "이벤트 기획자 🎉"],
    "ENFP": ["마케터 📢", "콘텐츠 크리에이터 🎬"],
    "ENTP": ["스타트업 창업가 🚀", "기획자 💡"],
    "ESTJ": ["경영자 🧑‍💼", "프로젝트 매니저 📂"],
    "ESFJ": ["인사담당자 🗂️", "상담교사 🧑‍🏫"],
    "ENFJ": ["강사 🎤", "리더십 코치 🌟"],
    "ENTJ": ["CEO 💼", "전략 컨설턴트 🧭"]
}

# 선택한 MBTI에 맞는 진로 출력
if user_mbti:
    st.subheader(f"✨ {user_mbti} 유형에게 어울리는 진로는...")
    careers = career_dict[user_mbti]
    st.write(f"1️⃣ {careers[0]}")
    st.write(f"2️⃣ {careers[1]}")
    st.success("너의 강점을 살려 멋진 길을 만들어봐! 🌈")
