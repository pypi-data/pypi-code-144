"""
A module containing LUTs for irreducible polynomials over GF(5^2).

Sage:
    def integer(coeffs, order):
        i = 0
        for d, c in enumerate(coeffs[::-1]):
            i += (c.integer_representation() * order**d)
        return i

    order = 5**2
    degree =1
    list_ = []
    R = GF(order, repr="int")["x"]
    for f in R.polynomials(degree):
        if f.is_monic() and f.is_irreducible():
            list_.append(f.coefficients(sparse=False)[::-1])

    # Sort in lexicographically-increasing order
    if not is_prime(order):
        list_ = sorted(list_, key=lambda item: integer(item, order))

    print(f"IRREDUCIBLE_POLYS_{order}_{degree} = {list_}")
"""

# LUT items are poly coefficients in degree-descending order

IRREDUCIBLE_POLYS_25_1 = [
    [1, 0],
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [1, 6],
    [1, 7],
    [1, 8],
    [1, 9],
    [1, 10],
    [1, 11],
    [1, 12],
    [1, 13],
    [1, 14],
    [1, 15],
    [1, 16],
    [1, 17],
    [1, 18],
    [1, 19],
    [1, 20],
    [1, 21],
    [1, 22],
    [1, 23],
    [1, 24],
]

IRREDUCIBLE_POLYS_25_2 = [
    [1, 0, 5],
    [1, 0, 7],
    [1, 0, 9],
    [1, 0, 10],
    [1, 0, 13],
    [1, 0, 14],
    [1, 0, 15],
    [1, 0, 16],
    [1, 0, 17],
    [1, 0, 20],
    [1, 0, 21],
    [1, 0, 23],
    [1, 1, 6],
    [1, 1, 8],
    [1, 1, 9],
    [1, 1, 12],
    [1, 1, 13],
    [1, 1, 14],
    [1, 1, 15],
    [1, 1, 16],
    [1, 1, 19],
    [1, 1, 20],
    [1, 1, 22],
    [1, 1, 24],
    [1, 2, 5],
    [1, 2, 6],
    [1, 2, 8],
    [1, 2, 10],
    [1, 2, 11],
    [1, 2, 14],
    [1, 2, 16],
    [1, 2, 17],
    [1, 2, 18],
    [1, 2, 21],
    [1, 2, 22],
    [1, 2, 24],
    [1, 3, 5],
    [1, 3, 6],
    [1, 3, 8],
    [1, 3, 10],
    [1, 3, 11],
    [1, 3, 14],
    [1, 3, 16],
    [1, 3, 17],
    [1, 3, 18],
    [1, 3, 21],
    [1, 3, 22],
    [1, 3, 24],
    [1, 4, 6],
    [1, 4, 8],
    [1, 4, 9],
    [1, 4, 12],
    [1, 4, 13],
    [1, 4, 14],
    [1, 4, 15],
    [1, 4, 16],
    [1, 4, 19],
    [1, 4, 20],
    [1, 4, 22],
    [1, 4, 24],
    [1, 5, 1],
    [1, 5, 2],
    [1, 5, 4],
    [1, 5, 5],
    [1, 5, 6],
    [1, 5, 7],
    [1, 5, 12],
    [1, 5, 13],
    [1, 5, 14],
    [1, 5, 15],
    [1, 5, 17],
    [1, 5, 18],
    [1, 6, 1],
    [1, 6, 2],
    [1, 6, 3],
    [1, 6, 6],
    [1, 6, 7],
    [1, 6, 9],
    [1, 6, 15],
    [1, 6, 16],
    [1, 6, 18],
    [1, 6, 20],
    [1, 6, 21],
    [1, 6, 24],
    [1, 7, 5],
    [1, 7, 7],
    [1, 7, 8],
    [1, 7, 11],
    [1, 7, 12],
    [1, 7, 13],
    [1, 7, 15],
    [1, 7, 18],
    [1, 7, 19],
    [1, 7, 21],
    [1, 7, 23],
    [1, 7, 24],
    [1, 8, 1],
    [1, 8, 2],
    [1, 8, 3],
    [1, 8, 5],
    [1, 8, 8],
    [1, 8, 9],
    [1, 8, 11],
    [1, 8, 13],
    [1, 8, 14],
    [1, 8, 20],
    [1, 8, 22],
    [1, 8, 23],
    [1, 9, 1],
    [1, 9, 2],
    [1, 9, 4],
    [1, 9, 10],
    [1, 9, 11],
    [1, 9, 13],
    [1, 9, 15],
    [1, 9, 16],
    [1, 9, 19],
    [1, 9, 21],
    [1, 9, 22],
    [1, 9, 23],
    [1, 10, 1],
    [1, 10, 3],
    [1, 10, 4],
    [1, 10, 10],
    [1, 10, 12],
    [1, 10, 13],
    [1, 10, 16],
    [1, 10, 17],
    [1, 10, 18],
    [1, 10, 20],
    [1, 10, 23],
    [1, 10, 24],
    [1, 11, 2],
    [1, 11, 3],
    [1, 11, 4],
    [1, 11, 5],
    [1, 11, 7],
    [1, 11, 8],
    [1, 11, 16],
    [1, 11, 17],
    [1, 11, 19],
    [1, 11, 20],
    [1, 11, 21],
    [1, 11, 22],
    [1, 12, 2],
    [1, 12, 3],
    [1, 12, 4],
    [1, 12, 5],
    [1, 12, 6],
    [1, 12, 9],
    [1, 12, 10],
    [1, 12, 12],
    [1, 12, 14],
    [1, 12, 21],
    [1, 12, 23],
    [1, 12, 24],
    [1, 13, 1],
    [1, 13, 3],
    [1, 13, 4],
    [1, 13, 7],
    [1, 13, 8],
    [1, 13, 9],
    [1, 13, 10],
    [1, 13, 11],
    [1, 13, 14],
    [1, 13, 15],
    [1, 13, 17],
    [1, 13, 19],
    [1, 14, 6],
    [1, 14, 7],
    [1, 14, 9],
    [1, 14, 10],
    [1, 14, 11],
    [1, 14, 12],
    [1, 14, 17],
    [1, 14, 18],
    [1, 14, 19],
    [1, 14, 20],
    [1, 14, 22],
    [1, 14, 23],
    [1, 15, 1],
    [1, 15, 3],
    [1, 15, 4],
    [1, 15, 10],
    [1, 15, 12],
    [1, 15, 13],
    [1, 15, 16],
    [1, 15, 17],
    [1, 15, 18],
    [1, 15, 20],
    [1, 15, 23],
    [1, 15, 24],
    [1, 16, 6],
    [1, 16, 7],
    [1, 16, 9],
    [1, 16, 10],
    [1, 16, 11],
    [1, 16, 12],
    [1, 16, 17],
    [1, 16, 18],
    [1, 16, 19],
    [1, 16, 20],
    [1, 16, 22],
    [1, 16, 23],
    [1, 17, 1],
    [1, 17, 3],
    [1, 17, 4],
    [1, 17, 7],
    [1, 17, 8],
    [1, 17, 9],
    [1, 17, 10],
    [1, 17, 11],
    [1, 17, 14],
    [1, 17, 15],
    [1, 17, 17],
    [1, 17, 19],
    [1, 18, 2],
    [1, 18, 3],
    [1, 18, 4],
    [1, 18, 5],
    [1, 18, 6],
    [1, 18, 9],
    [1, 18, 10],
    [1, 18, 12],
    [1, 18, 14],
    [1, 18, 21],
    [1, 18, 23],
    [1, 18, 24],
    [1, 19, 2],
    [1, 19, 3],
    [1, 19, 4],
    [1, 19, 5],
    [1, 19, 7],
    [1, 19, 8],
    [1, 19, 16],
    [1, 19, 17],
    [1, 19, 19],
    [1, 19, 20],
    [1, 19, 21],
    [1, 19, 22],
    [1, 20, 1],
    [1, 20, 2],
    [1, 20, 4],
    [1, 20, 5],
    [1, 20, 6],
    [1, 20, 7],
    [1, 20, 12],
    [1, 20, 13],
    [1, 20, 14],
    [1, 20, 15],
    [1, 20, 17],
    [1, 20, 18],
    [1, 21, 1],
    [1, 21, 2],
    [1, 21, 4],
    [1, 21, 10],
    [1, 21, 11],
    [1, 21, 13],
    [1, 21, 15],
    [1, 21, 16],
    [1, 21, 19],
    [1, 21, 21],
    [1, 21, 22],
    [1, 21, 23],
    [1, 22, 1],
    [1, 22, 2],
    [1, 22, 3],
    [1, 22, 5],
    [1, 22, 8],
    [1, 22, 9],
    [1, 22, 11],
    [1, 22, 13],
    [1, 22, 14],
    [1, 22, 20],
    [1, 22, 22],
    [1, 22, 23],
    [1, 23, 5],
    [1, 23, 7],
    [1, 23, 8],
    [1, 23, 11],
    [1, 23, 12],
    [1, 23, 13],
    [1, 23, 15],
    [1, 23, 18],
    [1, 23, 19],
    [1, 23, 21],
    [1, 23, 23],
    [1, 23, 24],
    [1, 24, 1],
    [1, 24, 2],
    [1, 24, 3],
    [1, 24, 6],
    [1, 24, 7],
    [1, 24, 9],
    [1, 24, 15],
    [1, 24, 16],
    [1, 24, 18],
    [1, 24, 20],
    [1, 24, 21],
    [1, 24, 24],
]
