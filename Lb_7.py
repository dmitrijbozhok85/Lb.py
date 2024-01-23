def compute_modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def solve_discrete_problem(g, h, q):
    m = int(q**0.5) + 1

    table_dict = {pow(g, i, q): i for i in range(m)}

    inv_g_m = pow(compute_modular_inverse(g, q), m, q)
    value = h
    for j in range(m):
        if value in table_dict:
            return j * m + table_dict[value]
        value = (value * inv_g_m) % q

    return None

param1, param2, param3 = [int(i) for i in input().split()]
result = solve_discrete_problem(param1, param2, param3)

print(result)
