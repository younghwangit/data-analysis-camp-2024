# step by step 해설은 ipyb 파일 참조

import requests
import json
import pandas as pd
import xmltodict
import random

# .env 환경변수 읽기
# .env 파일에 API 인증키를 보관함
from dotenv import load_dotenv
import os
load_dotenv()

# 공공데이터 API 크롤링
def pubulic_api_crawling():
        
    # 기술문서의 서비스 URL과 요정 메시지 명세 조합
    # 아파트 매매 신고정보 조회 기술문서.hwp 참조
    PUBLIC_SERVICE_KEY = os.getenv('PUBLIC_KEY')
    LAWD_CD = 11500 # 지역코드
    DEAL_YMD = 000000 #계약연월

    #빈 데이터프레임 생성
    df=None

    for i in range(1, 13): # list(range(1,13)):[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        DEAL_YMD = 202000 + i

        # 요청메세지
        url = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey={PUBLIC_SERVICE_KEY}&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}'

        # 데이터프레임 생성
        req = requests.get(url)
        content = xmltodict.parse(req.text)

        # 기술문서 5쪽 응답메세지 참조
        result=pd.DataFrame(content['response']['body']['items']['item'])

        #df에 결합
        df=pd.concat([df, result])

    df=df.reset_index(drop=True)

    return df

# 서울시 API 크롤링
# https://data.seoul.go.kr/dataList/OA-21275/S/1/datasetView.do

def seoul_api_crawling():

    # 기술문서의 서비스 URL과 요정 메시지 명세 조합
    SEOUL_SERVICE_KEY = os.getenv('SEOUL_KEY')
    TYPE = 'json' # 기술문서: json 파일을 제공함.
    SERVICE = 'tbLnOpendataRtmsV'

    #빈 데이터프레임 생성
    df=None

    for i in range (1, 3):
        
        url_seoul = f'http://openapi.seoul.go.kr:8088/{SEOUL_SERVICE_KEY}/{TYPE}/{SERVICE}/{1+(i-1)*1000}/{i*1000}/'
        
        req= requests.get(url_seoul)
        content = req.json()
        
        # 샘플 URL의 예제 참조
        result=pd.DataFrame(content[SERVICE]['row'])
        df=pd.concat([df, result])
    
    df.reset_index(drop=True)

    return df

def main():
    
    # 두 api 크롤링 중 하나를 랜덤으로 선택
    crawl = random.choice([pubulic_api_crawling, seoul_api_crawling])
    print(crawl.__name__)

    df_result = crawl()
    print(df_result)

if __name__ == '__main__':
    main()