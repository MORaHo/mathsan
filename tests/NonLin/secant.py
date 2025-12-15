from src.NonLin.secant import secant

# Example from Calcolo Scientifico by Alfio Quarteroni

v = 1000
M = 6000
f = lambda r: (M - v*(1+r)*((1+r)**5-1)/r)
kmax = 1000
toll = 1E-12
x0 = 0.3
x1 = 0.1

if abs(secant(f,x0,x1,toll,kmax)[0]-0.0614024115365)>1E-6 or secant(f,x0,x1,toll,kmax)[1] != 6:
    raise Exception("Secant method not working as expected!")

x1 = -0.3

if abs(secant(f,x0,x1,toll,kmax)[0]-0.0614024115365)>1E-6 or secant(f,x0,x1,toll,kmax)[1] != 8:
    raise Exception("Secant method not working as expected!")

print("Secant method tests passed!")
