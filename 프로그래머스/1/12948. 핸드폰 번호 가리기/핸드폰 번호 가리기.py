def solution(phone_number):
    answer = ''
    # 전체 폰 번호에서 뒷 4자리를 제외한 만큼 * 더함
    answer += (len(phone_number)-4)*('*')
    # # 폰 뒷자리 추가
    answer += phone_number[-4:]
    return answer