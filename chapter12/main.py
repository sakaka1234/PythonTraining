state = 'kaka'
match state:
    case 'go' | 'proceed' | 'start':
        print('green')
        print('means go')
    case 'stop' | 'halt' as what:
        print('red')
        print('means', what)
    case other:
        print('catchall',other)

for stmt in ['if', 'while', 'try']:
    match stmt:
        case 'if' | 'match':
            print('logic')
        case 'for' | 'while' as which:
            print('loop')
        case other:
            print('tbd')
tone = 'formal'
a = 'code' if tone == 'formal' else 'hack'
b= ['hack','code'][tone == 'formal']
print(a, b)