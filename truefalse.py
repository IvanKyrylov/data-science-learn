one_is_less_than_two = 1<2
true_equals_false=True==False
x=None

print(one_is_less_than_two)
print(true_equals_false)
print(x)

assert x == None, "not py style"
assert x is None, "py style"

print("Not False" if False else "False")
print("Not False" if None else "False")
print("Not False" if [] else "False")
print("Not False" if {} else "False")
print("Not False" if set() else "False")
print("Not False" if "" else "False")
print("Not False" if 0 else "False")
print("Not False" if 0.0 else "False")

def some_function_that_returns_a_string():
    return "test"

s=some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

print(first_char)

first_char= s and s[0]
print(first_char)

print("True" if s and s[0] else "False")

print(s[0] and s)

x=None
safe_x=x or 0
print(safe_x)
safe_x=x if x is not None else 0
print(safe_x) 

print("all([True, 1, {3}])", all([True, 1, {3}]))
print("all([True, 1, {}])", all([True, 1, {}]))
print("any([True, 1, {}])", any([True, 1, {}]))
print(all([]))
print(any([]))
print("all dict", all({1:False,2:False}))
print("any dict", any({1:False,2:True}))
