#유형별 문제 풀이 - hash와 dict
# hash와 dict 정리
"""
hash는 데이터를 고정된 크기의 해시값으로 변환해서 빠르게 조회할 수 있도록 해주는 기술
내부적으로는 대부분 해시 테이블 자료구조를 사용

해시 테이블
Key 값을 **해시 함수(hash function)**에 넣으면 → 고유한 정수(인덱스)가 나옴
이 인덱스를 배열의 위치로 사용해서 값을 저장
이때의 배열은 인덱스에 직접 접근시 핵심적인 역할을 하고 평균 O(1)의 탐색 성능을 가짐

해시 충돌이 발생할 수 있기 때문에, 각 언어는 충돌 해결 방식을 갖고 있음
충돌을 해결하는 방법에는 크게 두 가지 Open addressing, Seperate Chaining이 있음

Open addressing => 배열 안에서 다른 빈 자리를 찾아 저장
Seperate Chaining => 같은 해시 인덱스에 LinkedList 또는 다른 구조로 여러 값을 저장


자바 :
Map 계열 => HashMap
Key와 Value를 저장, 이때 Key는 해시된다
해시 충돌 시 체이닝 방식을 사용
Key는 equals()와 hashCode() 메서드를 잘 구현해야 한다

Set 계열 => HashSet
내부적으로는 HashMap을 이용해서 이중 Key만 저장한다




파이썬 :
dict(Map 역할)
Key와 Value를 저장, 이때 Key는 해시된다
해시 충돌 시 최적화된 Open Addressing 방식 사용

set
내부적으로는 dict를 활용해 key만 저장

"""