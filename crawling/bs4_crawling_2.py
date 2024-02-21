import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import time
import random


def crawling(url, headers, soup):

    # <td class="pgRR"> <a href="/item/sise_day.naver?code=005930&page=693">
    # 제일 처음 오는 td 태그를 선택, 선택한 td의 a 태그로 이동, href 속성 선택
    # '=' 을 기준으로 문자열을 분열, 맨 뒤의 요소를 추출.
    last_page = int(soup.select_one('td.pgRR').a['href'].split('=')[-1])

    df=None
    count=0

    # 반복해서 원하는 분량의 페이지 추출
    for page in range (1, last_page + 1): # 범위는 마지막 페이지까지

        # 예시: https://finance.naver.com/item/sise_day.naver?code=005930&page=100
        url_page = f'{url}&page={page}'

        # HTTP 요청
        req_crawl = requests.get(url_page, headers=headers)

        # HTML 데이터에서 <table> 태그 파싱 후 pd 객체 리스트로 변환
        result_crawl = pd.read_html(req_crawl.text, encoding='euc-kr')[0]

        # df에 결합
        df = pd.concat([df, result_crawl], ignore_index = True)

        # 3페이지까지만 추출
        if count > 3:
            break
        count = count + 1

        # 2~4초 대기시간 부여하여 서버 부하 방지
        time.sleep(random.uniform(2,4))

    # 결측치 제거 후 df에 저장
    df.dropna(inplace=True)

    # index 초기화
    df.reset_index(drop=True, inplace=True)
    
    return df

def main():
    company_code = '005930'

    # HTTP 요청 변수
    url = 'https://finance.naver.com/item/sise_day.naver?code=' + company_code
    headers = {
    'referer': 'https://finance.naver.com/item/sise.naver?code=' + company_code,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    # HTTP 요청
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, 'html.parser')
    
    a = crawling(url, headers, soup)

    print(a)

if __name__ == '__main__':
    main()