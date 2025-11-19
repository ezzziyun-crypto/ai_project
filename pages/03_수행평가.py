import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 데이터 로드
# 파일 경로와 이름은 현재 환경에 맞춰 조정되어야 합니다.
file_path = "보건복지부_전국 지역보건의료기관 현황_20221231.csv"
df = pd.read_csv(file_path)

# 1. 시도별 기관 유형별 개수 계산
df_grouped = df.groupby(['시도', '기관유형']).size().reset_index(name='개수')

# 2. 시도별 총 기관 수 계산
df_total = df_grouped.groupby('시도')['개수'].sum().reset_index(name='총 개수')

# 3. 비율 계산 (Merge 후)
df_merged = pd.merge(df_grouped, df_total, on='시도')
df_merged['비율'] = (df_merged['개수'] / df_merged['총 개수']) * 100
df_merged['비율_반올림'] = df_merged['비율'].round(2)

# 4. 시도 목록 (드롭다운 메뉴용)
sido_list = sorted(df_merged['시도'].unique())

# 5. 그래프 생성 (초기값: '서울특별시')
initial_sido = '서울특별시'
initial_data = df_merged[df_merged['시도'] == initial_sido].sort_values(by='비율', ascending=False)

# 색상 설정 함수
def get_colors(series):
    # 가장 높은 비율을 가진 항목의 인덱스
    max_index = series.idxmax()
    
    # 빨간색을 제외한 나머지 항목에 적용할 파란색 계열 그라데이션 (밝은 파랑 -> 진한 파랑)
    blue_scale = px.colors.sequential.Blues_r 
    
    # 비율 순서대로 내림차순 정렬 후 색상 인덱스 부여 (빨간색 제외)
    sorted_series = series[series.index != max_index].sort_values(ascending=False)
    
    # 색상 딕셔너리 초기화
    color_map = {}
    
    # 빨간색 (1등) 설정
    if not series.empty:
        color_map[series.index[series.argmax()]] = 'red'
    
    # 나머지 그라데이션 설정
    num_other = len(sorted_series)
    if num_other > 0:
        # 그라데이션 스케일에서 균등하게 색상 선택
        blue_indices = [int(i * (len(blue_scale) - 1) / (num_other - 1)) if num_other > 1 else 0 
                        for i in range(num_other)]
        
        for i, (idx, _) in enumerate(sorted_series.items()):
            color_map[idx] = blue_scale[blue_indices[i]]

    return [color_map[i] for i in series.index]

# 초기 색상 설정
initial_colors = get_colors(initial_data.set_index('기관유 유형')['비율'])

fig = go.Figure(
    data=[
        go.Bar(
            x=initial_data['기관유형'], 
            y=initial_data['비율_반올림'], 
            marker_color=initial_colors,
            name=initial_sido,
            customdata=initial_data['개수'],
            hovertemplate="<b>%{x}</b><br>비율: %{y:.2f}%<br>개수: %{customdata}개<extra></extra>"
        )
    ],
    layout=go.Layout(
        title={
            'text': f'<b>{initial_sido}</b> 지역 보건의료기관 유형별 비율',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis={'title': '기관 유형'},
        yaxis={'title': '비율 (%)', 'range': [0, 100]},
        template='plotly_white'
    )
)

# 드롭다운 메뉴 생성
dropdown_buttons = []

for sido in sido_list:
    sido_data = df_merged[df_merged['시도'] == sido].sort_values(by='비율', ascending=False).reset_index(drop=True)
    
    # 해당 시도의 색상 설정
    sido_colors = get_colors(sido_data.set_index('기관유형')['비율'])
    
    # Plotly update trace를 위한 데이터 구성
    update_data = {
        'x': [sido_data['기관유형']],
        'y': [sido_data['비율_반올림']],
        'marker.color': [sido_colors],
        'customdata': [sido_data['개수']],
        'name': [sido]
    }
    
    # 업데이트할 레이아웃 (제목 변경)
    update_layout = go.Layout(
        title={
            'text': f'<b>{sido}</b> 지역 보건의료기관 유형별 비율',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    
    dropdown_buttons.append(
        dict(
            label=sido,
            method="update",
            args=[update_data, update_layout]
        )
    )

fig.update_layout(
    updatemenus=[
        dict(
            buttons=dropdown_buttons,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.01,
            xanchor="left",
            y=1.1,
            yanchor="top",
            bgcolor="#E6E6FA" # 배경색 추가
        )
    ]
)

fig.show()
