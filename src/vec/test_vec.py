from vec import Vec

# class TestVec:

def test_init():
    try:
        Vec()
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        Vec([])
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        Vec([5, 'six', "seven", 8])
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        Vec(67)
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_is_Vec():
    v = Vec([1, 3, 5])
    assert isinstance(v, Vec)

def test_elements_is_tuple():
    v = Vec([1, 3, 5])
    assert isinstance(v.elements, tuple)

def test_repr():
    v = Vec([67, 67, 67])
    assert v.elements == (67, 67, 67)

def test_length():
    v1 = Vec([1, 3, 5, 7, 9])
    assert len(v1) == 5

    v2 = Vec([-1])
    assert len(v2) == 1

    v2 = Vec([0, 0, 0])
    assert len(v2) == 3

def test_neg():
    v1 = Vec([6, 7])
    v2 = -v1
    assert v2.elements == (-6, -7)

    v3 = -v2
    assert v3.elements == (6, 7)

def test_add():
    v1 = Vec([23, -32])
    v2 = Vec([44, 99])
    v3 = v1 + v2
    assert v3.elements == (67, 67)

    try:
        v1 + (7, 9)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        v1 + Vec([67])
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_sub():
    v1 = Vec([23, -32])
    v2 = Vec([44, 99])
    v3 = v1 - v2
    assert v3.elements == (-21, -131)

    try:
        v1 - (7, 9)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        v1 - Vec([67])
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_rmul():
    v1 = Vec([67, 63])
    v2 = 5 * v1
    assert v2.elements == (335, 315)

    try:
        'v' * v1
        assert False, "Expected TypeError"
    except TypeError:
        pass




if __name__ == "__main__":
    test_init()
    test_is_Vec()
    test_elements_is_tuple()
    test_length()
    test_repr()
    test_neg()
    test_add()
    test_sub()
    test_rmul()