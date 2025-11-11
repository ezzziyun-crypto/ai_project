# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Seoul Top10 Map (Folium)", layout="wide")

st.title("📍 서울 Top 10 관광지 — 외국인 인기 명소")
st.markdown(
    "아래 지도에서 각 장소를 클릭하면 간단한 설명이 보여요. "
    "지도는 Folium으로 만들었고 streamlit_folium로 임베드했습니다."
)

# 주요 명소 목록 (이름, 위도, 경도, 한줄설명)
places = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.580467,
        "lon": 126.976944,
        "desc": "조선의 법궁. 전통 한복체험 포인트."
    },
    {
        "name": "Changdeokgung Palace (창덕궁)",
        "lat": 37.579254,
        "lon": 126.992150,
        "desc": "유네스코 세계유산으로 유명한 궁궐."
    },
    {
        "name": "N Seoul Tower (남산타워 / N서울타워)",
        "lat": 37.551170,
        "lon": 126.988228,
        "desc": "서울 전망 명소 — 야경이 특히 예뻐요."
    },
    {
        "name": "Bukchon Hanok Village (북촌 한옥마을)",
        "lat": 37.582532,
        "lon": 126.985747,
        "desc": "전통 한옥 골목 산책 코스."
    },
    {
        "name": "Myeongdong (명동 쇼핑거리)",
        "lat": 37.564128,
        "lon": 126.985022,
        "desc": "쇼핑·스트리트푸드 핫스팟."
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.574165,
        "lon": 126.984910,
        "desc": "전통 공예품과 찻집이 많은 거리."
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",
        "lat": 37.566900,
        "lon": 127.009400,
        "desc": "모던한 건축과 야간 마켓으로 유명."
    },
    {
        "name": "Hongdae (홍대 — 홍익대 주변)",
        "lat": 37.555280,
        "lon": 126.923330,
        "desc": "젊음의 거리, 스트리트 공연·카페 많음."
    },
    {
        "name": "Gwangjang Market (광장시장)",
        "lat": 37.569922,
        "lon": 126.999000,
        "desc": "전통 길거리 음식(빈대떡, 마약김밥 등) 맛집."
    },
    {
        "name": "Lotte World Tower (롯데월드타워 / 잠실)",
        "lat": 37.511234,
        "lon": 127.098030,
        "desc": "높은 전망대(Seoul Sky)와 쇼핑몰."
    },
]

# 지도 초기 중심(서울 중심)
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=12)

# Add markers
for p in places:
    popup_html = f"""
    <b>{p['name']}</b><br>
    {p['desc']}<br>
    <a href="https://www.google.com/maps/search/?api=1&query={p['lat']},{p['lon']}" target="_blank">
        지도에서 열기
    </a>
    """
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=p["name"],
    ).add_to(m)

# Optional: draw a cluster (if many)
# folium.plugins.MarkerCluster().add_to(m)  # not used to keep simple

# Display map in Streamlit
st.subheader("🗺️ 인터랙티브 지도 (Folium)")
st.write("지도는 아래의 인터랙티브 뷰어로 표시됩니다.")
st_data = st_folium(m, width=1000, height=600)

st.sidebar.header("목록으로 이동")
place_names = [p["name"] for p in places]
selected = st.sidebar.selectbox("장소 선택", ["전체 보기"] + place_names)

if selected != "전체 보기":
    # 찾아서 간단히 정보 표시
    p = next(filter(lambda x: x["name"] == selected, places))
    st.sidebar.markdown(f"**{p['name']}**")
    st.sidebar.write(p["desc"])
    st.sidebar.markdown(f"- 좌표: `{p['lat']}, {p['lon']}`")
    st.sidebar.markdown(
        f"[지도에서 열기](https://www.google.com/maps/search/?api=1&query={p['lat']},{p['lon']})"
    )

st.markdown("---")
st.caption("데이터: 일반 공개 여행정보/관광사이트 기반. (좌표는 공개 소스 참고)")
