def solution(numbers):
    sarr = list(map(str, numbers))
    
    # 정렬 기준: 두 수를 이어붙였을 때 큰 순서대로 정렬
    sarr.sort(key=lambda x: x * 10, reverse=True)
    
    # 만약 가장 큰 숫자가 0이면 전체가 0이므로 '0' 반환
    if sarr[0] == "0":
        return "0"
    
    return "".join(sarr)
