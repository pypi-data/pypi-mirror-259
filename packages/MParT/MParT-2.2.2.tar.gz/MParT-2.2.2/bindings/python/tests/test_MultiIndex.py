# MultiIndex test

import mpart

def test_init_with_length():
    
    length = 4
    multi = mpart.MultiIndex(length)
    assert len(multi) == length
    assert multi.count_nonzero() == 0
    assert multi[0] == 0
    assert multi.max() == 0
    assert multi.sum() == 0

    multi[0] = 4
    assert multi[0] == 4
    assert multi.max() == 4
    assert multi.sum() == 4

    multi[1] = 3
    assert multi[1] == 3
    assert multi.max() == 4
    assert multi.sum() == 4 + 3

def test_init_with_length_and_val():
    
    length = 4
    val = 2
    multi = mpart.MultiIndex(length,val)
    assert len(multi) == length
    assert multi.count_nonzero() == length
    assert multi[0] == val
    assert multi.max() == val
    assert multi.sum() == length*val


def test_init_with_list():
    
    idx = [2, 3, 0, 0, 100]
    multi = mpart.MultiIndex(idx)
    assert len(multi) == len(idx)
    assert multi.count_nonzero() == 3
    assert multi[0] == idx[0]
    assert multi.max() == 100
    assert multi.sum() == 105
    assert multi.tolist() == idx
