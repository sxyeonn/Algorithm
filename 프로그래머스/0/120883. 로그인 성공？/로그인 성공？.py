def solution(id_pw, db):
    for id, pw in db:
        # id가 일치하는 회원이 있는지 확인
        if id_pw[0] == id:
            # id가 일치할 때 pw도 일치하면 로그인 성공
            if id_pw[1] == pw:
                return "login"
            # id는 일치하지만 pw가 일치하지 않으면 비밀번호 틀림
            else:
                return "wrong pw"
            
    # id가 일치하는 회원이 없으면 로그인 실패
    return "fail"
