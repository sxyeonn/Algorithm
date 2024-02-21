from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    an = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    
    # 분자
    an_numer = an.numerator
    # 분모
    an_demom = an.denominator
    
    answer = [an_numer, an_demom]
    return answer