fun = lambda a, b : (a + b, a * b, a**2 + b**2)

a, b = (input("Introduza un número a: "), input("Introduza outro número b: "))
print(f"A suma, o produto, e a suma de cadrados de a e b resultan: {fun(int(a),int(b))}")