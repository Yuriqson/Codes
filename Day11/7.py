import cmath
def solve_quadratic_equation(a,b,c):
    res=(b**2)-(4*a*c)
    res1=(-b-cmath.sqrt(res))/(2*a)
    res2=(-b+cmath.sqrt(res))/(2*a)
    return res1,res2
print(solve_quadratic_equation(1,-2,3))