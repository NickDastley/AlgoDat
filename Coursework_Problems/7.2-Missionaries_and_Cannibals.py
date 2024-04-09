from shortest_path import shortest_path_search


def successors():
    def sc(state):
        left_missionaries, left_cannibals, right_missionaries, right_cannibals = state
        possible_successors = {
            (left_missionaries - 1, left_cannibals - 1, right_missionaries + 1, right_cannibals + 1): "lm - 1, lc - 1",
            (left_missionaries - 2, left_cannibals, right_missionaries + 2, right_cannibals): "lm - 2",
            (left_missionaries, left_cannibals - 2, right_missionaries, right_cannibals + 2): "lc - 2",
            (left_missionaries + 1, left_cannibals + 1, right_missionaries - 1, right_cannibals - 1): "lm + 1, lc + 1",
            (left_missionaries + 2, left_cannibals, right_missionaries - 2, right_cannibals): "lm + 2",
            (left_missionaries, left_cannibals + 2, right_missionaries, right_cannibals - 2): "lc + 2",
            (left_missionaries - 1, left_cannibals, right_missionaries + 1, right_cannibals): "lc - 1",
            (left_missionaries + 1, left_cannibals, right_missionaries - 1, right_cannibals): "lc + 1",
            (left_missionaries, left_cannibals - 1, right_missionaries, right_cannibals + 1): "lc - 1",
            (left_missionaries, left_cannibals + 1, right_missionaries, right_cannibals - 1): "lc + 1",
        }

        successors = {}
        for possibility in possible_successors.keys():
            if _apply_rules(possibility):
                successors[possibility] = possible_successors[possibility]

        return successors

    return sc


def _apply_rules(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals = state
    if (_not_outnumber(left_missionaries, left_cannibals) and _not_outnumber(right_missionaries, right_cannibals)
            and left_missionaries >= 0 and left_cannibals >= 0 and right_missionaries >= 0 and right_cannibals >= 0):
        return True
    else:
        return False

def _not_outnumber(number_of_missionaries, number_of_cannibals):
    if (number_of_missionaries >= number_of_cannibals):
        return True
    elif (number_of_missionaries == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    res = shortest_path_search((3, 3, 0, 0), successors(), lambda state: state == (0, 0, 3, 3))
    print(res)
    print('%s transitions' % (int(len(res) / 2)))
