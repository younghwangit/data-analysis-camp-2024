
import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawling(soup):

    """ crawling 대상: 노래 차트 100의 노래 제목들

    <tbody>에서 제목 크롤링

    <p class="title" adult_yn="N">
    <a href="javascript:;" adultcheckval="1" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('6234117',true);
    " title="홀씨" aria-label="새창">홀씨</a>
    </p>
    """

    result = []

    # tbody 태그 추출
    tbody = soup.find('tbody')

    # p 태그에서 "title" class 추출
    # title 클래스의 text만 추출, list에 추가
    for p in tbody.find_all('p', attrs = {'class' : 'title'}):
        result.append(p.get_text().strip())

    return result

def main():
    # HTTP 요청 변수
    url = 'https://music.bugs.co.kr/chart'
    custom_header = {
    'referer': 'https://music.bugs.co.kr/', # 요청이 발생하는 원본 페이지
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'  # 요청을 보내는 클라이언트의 유형
    }
    
    # HTTP 요청
    req = requests.get(url, headers=custom_header)

    # 전달받은 HTTP를 text 형태로 변환하고 html 코드로 변환
    soup = BeautifulSoup(req.text, 'html.parser')

    # 크롤링
    crawling(soup)

    # 데이터프레임화
    titles = crawling(soup)
    print(pd.DataFrame({"노래제목" : titles}))

if __name__ == "__main__" :
    main()