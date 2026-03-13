class TraceBlock:
    def message(self,arg):
        print('running',arg)
    def __enter__(self):
        print('[starting with block]')
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print('[exited normally]\n')
        else:
            print(f'[propagating exception] : {exc_type}')
            return False

if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test1')
        print('reached')
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')