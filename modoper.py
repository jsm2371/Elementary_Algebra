


"""
GCD(a, b) : 유클리드 알고리즘으로 a와 b의 최대공약수 구하
Input : 정수 a, b
Output : 최대공약수 (a, b)
"""
def GCD(a, b, opt = 0):

    iquo = []
    
    ### Step 1. a > b 변환
    if a < b:
        a, b = b, a

    ### Step 2. 유클리드 알고리즘 연산
    while b != 0:
        d = a % b
        iquo.append(a//b)
        a = b
        b = d        

    ### Step 3. (a,b) 출력
    ### Extra. 옵션 "quo"추가시 몫도 출력하도록 설정
    if opt == "quo":
        return a, iquo
    
    return a

"""
재귀적 처리
def GCD(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
"""


"""
Int_Inv(a, n) : mod n 위에서 a의 역원 구하기
Input : 정수 a, 모듈러 n
Output : a^{-1} mod n
"""
def Int_inv(a, n):

    ### Step 0. a 인코딩 : a mod n 구하기
    if a > n:
        a = a%n

    ### Step 1. (a,n)과 유클리드 연산 과정 중의 몫 리스트 구하기
    x, y_list = GCD(n, a, "quo")

    ### Step 2. (a,n)=1 이 아닌경우, 역원이 존재하지 않음
    if x != 1:
        raise Exception("역원이 존재하지 않습니다.")

    ### Step 3. 역원 점화식 연산을 위한 초기값 설정
    """
    Cnt_Num : 점화식의 최대 반복 횟수
    Iter_List : 점화식의 초기값 [x_{0}, y_{0}, z_{0}]
    """
    Cnt_Num = len(y_list) - 2
    Iter_List = [-y_list[Cnt_Num], -y_list[Cnt_Num-1], 1]

    ### Step 4. 점화식 계산
    """
    계산하고자 하는 점화식은 다음과 같다.
    x_{n+1} = x_{n}*y_{n} + z_{n}
    y_{n+1} = the value in Iter_LIst
    z_{n+1} = x_{n}
    """
    for rnd in range(Cnt_Num):
        temp = Iter_List[0]
        Iter_List[0] = Iter_List[0]*Iter_List[1]+Iter_List[2]
        Iter_List[1] = -y_list[Cnt_Num-2-rnd]
        Iter_List[2] = temp

    ### Step 5. 역원 출력.
    """
    Step 4에서 최종적으로 구한 x_{n}가 Output 값으로 채택된다.
    여기서 x_{n}이 음수인 경우 mod n에서의 음수처리를 취한다.
    """
    if Iter_List[0] < 0:
        return n+Iter_List[0]
    else:
        return Iter_List[0]



"""
EEA(a, n) : Extended Euclidean Algorithm
 >> Inv_int와 GCD를 완전히 통합한 효율적인 유한체 역원 연산보조 알고리
Input : 정수 a, b
Output : 최대공약수 (a, b), "quot"-[a의 잉여, b의 잉여]

Option
"quot"  : 추가적인 출력 옵션. return값으로 a와 b의 잉여값을 확인할 수 있음
"print" : 주어진 계산 과정에 사용된 모든 Iter 리스트들을 출력한다.
"""
def EEA(a, b, opt="quot"):
    
    ### Step 1. a > b 변환
    if a < b:
        a, b = b, a

    ### Step 2. 초기값 생성
    """
    Iter_Last, Iter_Now, Iter_Next : 점화식 리스트 {n-1}, {n}, {n+1}
    Iter = [a_{i}, b_{i}, c_{i}, q_{i+1}*, s_{i}, t_{i}]
      *i+1이라고 함은 n=3이라면 q_{i+1}은 q_{4}로써 취급이 된다는 의미.
    """
    iquo = a//b
    irem = a%b
    Iter_Last = [a, b, irem, iquo, 1, 0]
    Iter_Now = [b, irem, b%irem, b//irem, 0, 1]
    ### Extra. 옵션 "print"가 선언되면 점화식 리스트 Iter들이 출력된다.
    if opt=="print":
        print(Iter_Last)
        print(Iter_Now)

    ### Step 2. 확장 유클리드 알고리즘 연산
    """
    아래의 점화식을 계산하는 과정이 된다.
    Iter_Next = [b_{i-1}, c_{i-1}, b_{i-1}%c_{i-1}, b_{i-1}//c_{i-1},
                 s_{i-2} - q_{i-1}*s_{i-1}, t_{i-2} - q_{i-1}*t_{i-1}]
    """
    while Iter_Now[2] != 0:
        Iter_Next = [Iter_Now[1], Iter_Now[2],
                     Iter_Now[1]%Iter_Now[2], Iter_Now[1]//Iter_Now[2],
                     Iter_Last[4]-Iter_Last[3]*Iter_Now[4],
                     Iter_Last[5]-Iter_Last[3]*Iter_Now[5]]
        if opt=="print":
            print(Iter_Next)
        Iter_Last = Iter_Now
        Iter_Now = Iter_Next

    ### Step 3. 역원 출력
    if opt == "quot" or opt == "print":
        return [Iter_Now[1],
                Iter_Last[4]-Iter_Last[3]*Iter_Now[4],
                Iter_Last[5]-Iter_Last[3]*Iter_Now[5]]
    else:
        return Iter_Now[1]


