prod = lambda x1, x2, x3, x4 : x1 * x2 * x3 * x4
N = 12669528480
x = 1
while prod(x, x+1, x+2, x+3) != N:
    x += 1
print(f"Os catro números enteiros consecutivos buscados son {x} x {x+1} x {x+2} x {x+3} = {N}.")