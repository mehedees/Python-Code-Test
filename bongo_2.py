def print_depth(data, **kwargs):
    depth = kwargs.get('depth') or 1
    if data:
        for k, v in data.items():
            print(f"{k} {depth}")
            if isinstance(v, dict):
                print_depth(v, depth=depth+1)
            elif hasattr(v, '__dict__'):
                print_depth(v.__dict__, depth=depth+1)
                

class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
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
    print_depth(data)