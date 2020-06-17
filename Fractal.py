import graphic as gr

window = gr.GraphWin('Fractal', 600, 600)
al = 0.2


def fr_rec(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

    A1 = (A[0] * (1 - al) + B[0] * al, A[1] * (1 - al) + B[1] * al)
    B1 = (B[0] * (1 - al) + C[0] * al, B[1] * (1 - al) + C[1] * al)
    C1 = (C[0] * (1 - al) + D[0] * al, C[1] * (1 - al) + D[1] * al)
    D1 = (D[0] * (1 - al) + A[0] * al, D[1] * (1 - al) + A[1] * al)

    fr_rec(A1, B1, C1, D1, deep - 1)


print(fr_rec((100, 100), (500, 100), (500, 500), (100, 500)))
