# https://www.youtube.com/watch?v=73FRQspzFzo&ab_channel=Indently

var:int = 10
name:str = 'Bob3'

print(f'{var=}')
print(f'{name=}')

print(f'{len(name)=}')
print(f'{10 + 10 = }')

user:str = 'Bob'
print(f'{user:_^11}')
print(f'{user: ^11}')
print(f'{user:_<11}')
print(f'{user:_>11}')

## Nested curly braces

width = 12
print(f'{user:_>{width}}')

pi:float = 3.141592653589793
places:int = 2
print(f'{pi:.{places}f}')

users: dict[int,str] = {1:'Bob', 2:'Alice', 3:'Charlie'}
print(f'{users[1]=}')
print(f'{users[2]=}')
# print(f'{users[5]=}')  # key error

if 5 in users:
    print(f'{users[5]=}')

print(users.get(6))
print(users.get(6, 'Not found'))
print(users.setdefault(5, "not found2"))
print(users.get(8))


def make_request() -> None:
    # this is better than "pass"
    raise NotImplementedError('I will code this later. --Bob')

def make_download() -> None:
    raise NotImplementedError('Mr. Download needs to fix this!')

make_request()