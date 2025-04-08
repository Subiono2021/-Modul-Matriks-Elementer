
import sympy as sp
from sympy import Matrix
from IPython.display import display, Math

class ElementaryMatrix:
    def __init__(self, n):
        self.n = n
        self.I = sp.eye(n)  # Matriks identitas ukuran n

    def create_E1(self, swap_rows=(1, 2)):
        E1 = self.I.copy()
        i, j = swap_rows
        i -= 1
        j -= 1
        if i < self.n and j < self.n:
            E1[i, i], E1[j, j] = 0, 0
            E1[i, j], E1[j, i] = 1, 1
        return E1

    def create_E2(self, scale_row=(2, 5)):
        E2 = self.I.copy()
        r, k = scale_row
        r -= 1
        if r < self.n:
            E2[r, r] = k
        return E2

    def create_E3(self, add_row=(3, 1, -2)):
        E3 = self.I.copy()
        r1, r2, m = add_row
        r1 -= 1
        r2 -= 1
        if r1 < self.n and r2 < self.n:
            E3[r1, r2] += m
        return E3

    def get_all(self, swap_rows=(1, 2), scale_row=(2, 5), add_row=(3, 1, -2)):
        E1 = self.create_E1(swap_rows)
        E2 = self.create_E2(scale_row)
        E3 = self.create_E3(add_row)
        return E1, E2, E3

    def display_results(self, A, E1, E2, E3):
        from sympy import latex
        display(Math(f"\\text{{Matrix Elementer: }} E_1 = {latex(E1)};~E_2 = {latex(E2)};~E_3 = {latex(E3)}"))
        display(Math(f"A = {latex(A)}"))
        display(Math(f"E_1 A = {latex(E1 @ A)}"))
        display(Math(f"E_2 A = {latex(E2 @ A)}"))
        display(Math(f"E_3 A = {latex(E3 @ A)}"))
