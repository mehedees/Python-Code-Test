def print_depth(data, **kwargs):
    depth = kwargs.get('depth') or 1
    if data:
        for k, v in data.items():
            if type(v) != dict:
                print(f"{k} {depth}")
            else:
                print(f"{k} {depth}")
                print_depth(v, depth=depth+1)

if __name__ == "__main__":
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