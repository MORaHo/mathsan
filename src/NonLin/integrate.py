from src.NonLin import midpoint,trapezoid,simpson

def integrate(a,b,N:int,f,method_:int=3):
    match method_:
        case 1:
            return midpoint(a,b,N,f)
        case 2:
            return trapezoid(a,b,N,f)
        case 3:
            return simpson(a,b,N,f)
        case _:
            return simpson(a,b,N,f)