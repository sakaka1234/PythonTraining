def __getattr__(name):
    if name == 'sa':
        return '1.0'
    raise AttributeError

def test():
    print("Test running")

if __name__ == "__main__":
    test()