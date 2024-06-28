from copy import copy


def matrix_chain_order(p):
    matrices = []
    for i in range(1, len(p)):
        matrices.append((p[i - 1], p[i]))

    print(matrices)

    matrices_parenthesis_possibilities = []
    matrices_left = []
    matrices_right = []
    for i in range(0, len(matrices) - 1):
        for j in range(i + 1):
            matrices_left.append(matrices[j])

        for j in range(i + 1, len(matrices)):
            matrices_right.append(matrices[j])

        matrices_parenthesis_possibilities.append((copy(matrices_left), copy(matrices_right)))
        matrices_left.clear()
        matrices_right.clear()
    print(matrices_parenthesis_possibilities)


def calculate_cost_recursive(placement):
    if len(placement) == 2:
        return placement[0][0] * placement[0][1] * placement[1][1]



matrix_chain_order([40, 20, 30, 10, 30])
