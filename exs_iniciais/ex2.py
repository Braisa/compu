suc = lambda k : k**-1

threshold = .005
k = 1
sum = suc(k)

while abs(suc(k+1) - suc(k)) > threshold:
    k += 1
    sum += suc(k)

print(f"A condición se verifica para N = {k}, e a suma parcial dá S = {sum}.")
