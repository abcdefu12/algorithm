# 배열이 필요한 이유
# ① 같은 종류의 데이터를 효율적으로 관리하기 위해
# ② 같은 종류의 데이터를 순차적으로 저장

# 배열의 장점
# 빠른 접근이 가능하다.
# 배열의 단점
# ① 추가/삭제가 쉽지 않다.
# ② 미리 최대길이를 지정해야 한다.

# 파이썬 리스트를 사용한 배열
data1 = [[1,2,3],[4,5,6],[7,8,9]]
print(data1[0][0]) #1
print(data1[0][1]) #2

#예제> 빈도수 출력
dataset = ["mango", "mint", "move"]
m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == "M":
            m_count +=1
print(m_count)