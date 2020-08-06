def print_depth(data, **kwargs):
    depth = kwargs.get('depth') or 1
    if data:
        for k, v in data.items():
            print(f"{k} {depth}")
            if isinstance(v, dict):
                print_depth(v, depth=depth+1)
    else:
        return None
                

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