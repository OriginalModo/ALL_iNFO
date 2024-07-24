def parse_response(value: str | tuple | list | dict) -> str:
    match value:
        case {'key': 1000, **rest}:
            return rest['id']
        case ('error', message) | ('error', message, *_):
            raise ValueError(message)
        case {'meta': val, **rest} if not rest:
            return val['id']
        case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, _]}:
            return f'{error}, {allowed}'
        case (set() as x, _) if len(x) == 2:
            return max(x)
        case _:
            raise ValueError(f'Unknown value: {value}')


if __name__ == '__main__':
    first = {'key': 1000, 'id': 999}
    second = ['error', 'Slow network connection!']
    third = {'meta': {'id': 999}}
    fourth = {'meta': {'code': 200, 'error': 'no'}, 'info': [{'allowed': 'yes'}, 111]}
    fifth = ({10, 11}, 5)
    print(parse_response(fifth))
