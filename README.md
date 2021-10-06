# DataCollections
데이터 수집
1. 크롤링  
  -> 셀레니움.. 신세계 + 더불어서 HTML, CSS 구조에 대해서 익숙하면 좀 더 원활하게 데이터를 모아올 수 있을 것이다.
2. 곰 자막 scrapping

------

from unknown error: cannot determine loading status  
from tab crashed  
-> 크롬드라이버에 shm 메모리가 부족해서 나오는 문제 -> option에 파라미터 추가  
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')  
driver = webdriver.Chrome(chrome_options = chrome_options)  
-------
서버에는 셀레니움 서버로 설치하지
https://oslinux.tistory.com/33  
