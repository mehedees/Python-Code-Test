import pytest
from bongo_1 import print_depth
from bongo_2 import Person, print_depth as print_depth_obj
from bongo_3 import Node, lca

def test_bongo_1(capfd):
    data = {
        'k1': 1,
        'k2': {
            'k3': 1,
            'k4': {
                'k5': 4,
                'k6': 6
            }
        }
    }
    print_depth(data)
    out, err = capfd.readouterr()
    assert out == "k1 1\nk2 1\nk3 2\nk4 2\nk5 3\nk6 3\n"


def test_bongo_2(capfd):
    p1 = Person(1, None)
    p2 = Person(2, p1)
    data = {
        'k1': 1,
        'k2': {
            'k3': 1,
            'k4': {
                'k5': p2,
                'k6': 6
            }
        }
    }
    print_depth_obj(data)
    out, err = capfd.readouterr()
    assert out == "k1 1\nk2 1\nk3 2\nk4 2\nk5 3\nx 4\ny 4\nx 5\ny 5\nk6 3\n"


def test_bongo_3(capfd):
    n1 = Node(1, None)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)

    assert lca(n3, n7) == 3