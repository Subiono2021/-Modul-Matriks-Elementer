```markdown
# OBE Matrix Module 

Modul Python untuk membentuk **Matriks Elementer** (Operasi Baris Elementer - OBE) dengan pendekatan interaktif menggunakan `SymPy`.

## ✨ Fitur
- Menukar dua baris (E1)
- Mengalikan baris dengan skalar (E2)
- Menambahkan kelipatan baris ke baris lain (E3)
- Dukungan tampilan LaTeX di Jupyter Notebook
- Contoh lengkap dalam `example.py` dan `example.ipynb`

## 🔧 Instalasi
Pastikan sudah menginstal `sympy`:
```bash
pip install sympy
```

## 🚀 Contoh Penggunaan

```python
from elementary_matrix import ElementaryMatrix
import sympy as sp

A = sp.Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 11]
])

em = ElementaryMatrix(4)
E1, E2, E3 = em.get_all(swap_rows=(1, 2), scale_row=(2, 5), add_row=(3, 1, -2))
em.display_results(A, E1, E2, E3)
```

## 📔 Notebook Interaktif

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<USERNAME>/obe-matrix-module/blob/main/example.ipynb)

---

## 🧠 Lisensi
MIT License.
```

> `Subiono2021`.

---

### 🧪 2. `example.py`

```python
from elementary_matrix import ElementaryMatrix
import sympy as sp

# Matriks A 4x4
A = sp.Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 11]
])

# Buat instance
em = ElementaryMatrix(4)

# Dapatkan matriks elementer
E1, E2, E3 = em.get_all(swap_rows=(1, 2), scale_row=(2, 5), add_row=(3, 1, -2))

# Tampilkan
em.display_results(A, E1, E2, E3)
```

---

### 📓 3. `example.ipynb`

```markdown
# Elementary Matrix Operations with SymPy

Langkah-langkah operasi baris elementer (OBE) dengan Python

```python
from elementary_matrix import ElementaryMatrix
import sympy as sp
```

```python
A = sp.Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 11]
])
```

```python
em = ElementaryMatrix(4)
E1, E2, E3 = em.get_all(swap_rows=(1, 2), scale_row=(2, 5), add_row=(3, 1, -2))
em.display_results(A, E1, E2, E3)
```
```
