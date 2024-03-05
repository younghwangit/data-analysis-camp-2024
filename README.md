# 34회차 데이터분석&엔지니어 취업 캠프
- 2023년 12월 26일부터 멀티캠퍼스의 데이터분석&엔지니어 취업 캠프에서 학습한 내용을 정리하는 프로젝트입니다.

# 프로젝트 주요 개발환경 요약
  + Programming Languages : Python(ver. 3.12.1)
  + Machine Learning Platform : Google colab

## 가상환경 설치
- 폴더 최상위 경로에서 가상환경을 설치합니다.

```bash
pip install virtualenv #기존에 설치한 가상환경이 있다면 생략 가능
virtualenv venv
```

- 가상환경에 접속합니다.
```bash
source venv/Scripts/activate
```

- 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

- 일반적인 파이썬 `.py` 파일을 실행할 경우
```bash
python a.py
```

## 주요 라이브러리 버전 및 설명
  + 버전: [requirements.txt](requirements.txt) 파일 참조
### jupyterlab
- 인터랙티브 개발환경으로, 데이터 과학과 과학적 컴퓨팅을 위해 설계되었습니다. 웹 기반 인터페이스를 통해 코드 작성, 데이터 시각화, 텍스트 작성 등 다양한 작업을 수행할 수 있습니다.

### numpy
- 다차원 배열 객체를 제공하고, 데이터 구조를 조작하기 위한 다양한 고급 수학 함수를 제공합니다.

### pandas
- 데이터 구조와 데이터 분석 도구를 제공하는 오픈 소스 라이브러리입니다.데이터 처리 기능, 파일의 입출력 기능도 제공합니다.

### requests
- 파이썬에서 HTTP 요청을 보내기 위해 사용되는 라이브러리입니다. JSON 형식의 응답을 파이썬 객체로 쉽게 변환할 수 있습니다.

### xmltodict
- 파이썬에서 XML을 JSON 형식처럼 쉽게 다룰 수 있게 해주는 라이브러리입니다. XML 문서를 파이썬의 딕셔너리 구조로 변환하여 마치 JSON처럼 취급할 수 있게 해줍니다.

### python-dotenv
- 파이썬 애플리케이션에서 환경변수를 관리하기 위한 라이브러리입니다.

### beautifulsoup4

### selenium

### lxml
- XML, HTML을 파싱하는 기능을 제공합니다.

### tabulate
- 

# 폴더 설명

| Functions | Location | Description |
|---|---|---|
| update_requirements_txt | req_ver_check.py  | for checking and updating package version |
