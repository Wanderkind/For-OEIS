
R = 0

while True:
    Count = 0

    for I in range(2*R + 1):
        i = I - R

        for J in range(2*R + 1):
            j = J - R

            for K in range(2*R + 1):
                k = K - R

                for L in range(2*R + 1):
                    l = L - R
                    
                    if R == 0 or (2*R - 1)**2 <= 4*(i**2 + j**2 + k**2 + l**2) <= (2*R + 1)**2:
                        Count += 1

    print(Count)
    R += 1
