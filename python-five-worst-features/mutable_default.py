## MUTABLE default could be a list or dict

def add_name(name: str, target: list[str] = []) -> list[str]:
    target.append(name)
    return target

print(add_name('Bob'))
print(add_name('James'))  # we expect to get back ONE name in one list if we don't specify a target
print(add_name('Maria'))
print(add_name('Jane', []))

