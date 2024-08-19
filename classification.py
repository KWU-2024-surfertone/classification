# 분류 기능 구현
# 1. 카테고리별 대분류
# 2. 대분류 별 소분류
# 3. 주변 상권 분석
# 4. 오늘의 상점 추천 
# 개발 날짜: 20240819 - 20240820
import pandas as pd
import random

# 카테고리 대분류
def classification(cate):
    # 엑셀 파일 로드
    filename = '카테고리분류.xlsx'
    # df = pd.read_excel(filename, engine='openpyxl')
    df = pd.read_excel(filename, sheet_name=cate, engine='openpyxl')
    # 빈 리스트 사전 생성
    categories_dict = {}

    # 첫 번째 행을 카테고리 이름으로, 이후 행의 데이터를 리스트로 저장
    for column in df.columns:
        categories_dict[column] = df[column].tolist()
    # 결과 출력
    for category_name, items in categories_dict.items():
        print(f'{category_name}: {items}')
        
    # 각 열의 유효한 값 개수 세기 (NaN 제외)
    ### 주변 상권 분석(대분류)
    column_counts = df.count()
    for column, count in column_counts.items():
        print(f'"{column}" : {count} 건') #test how many elements
        
    ### count 값이 가장 작은 열 찾기
    min_column = column_counts.idxmin()  # 최소 count 값을 가진 열의 이름
    min_count = column_counts.min()      # 최소 count 값
    print(f'"{min_column}" 카테고리에서 {min_count} 건으로 가장 작은 상권을차지하고 있습니다.')  # count 값이 가장 작은 열 출력


# 오늘의 가게 추천
def recommend_shop(cate):
    # 엑셀 파일 로드
    filename = '카테고리분류.xlsx'
    # df = pd.read_excel(filename, engine='openpyxl')
    df = pd.read_excel(filename, sheet_name=cate, engine='openpyxl')
    # 모든 열에서 유효한 (NaN이 아닌) 요소들만 모아 리스트로 변환
    valid_elements = df.dropna(how='all').stack().tolist()

    # 유효한 요소들 중에서 랜덤으로 하나 선택
    selected_element = random.choice(valid_elements)

    # 결과 출력
    print(f'오늘의 추천 가게: {selected_element}')
    
    
    
    
# test code   
cate = "음식"
classification(cate) # 대분류 테스트 
recommend_shop(cate) # 오늘의 가게 추천

# 카테고리 소분류

