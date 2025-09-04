#### КАК РЕШАТЬ ЗАДАНИЯ:
- В каждом задании есть комментарий с пояснением
- Каждая из программ может быть некорректно написана, если это так, то нужно об этом написать и указать на ошибку

```python
# 1. bool. напиши, что выведет программа

a, b, c = True, False, False
expr = a or b and c
print(expr)

# 2. поставь скобки в предыдущей программе так, чтобы результат вычисления сменился на обратный

a, b, c = True, False, False
expr = a or b and c
print(expr)

# 3. if. что выведет эта программа?

x = 5
if not x:
    print("A")
elif x > 10:
    print("B")
elif x > 3:
    print("C")
else:
    print("D")

# 4. for. напиши код вместо прочерков, чтобы программа вывела числа от 1 до n включительно

n = 5
for i in _____:
    print(i)

# 5. while. что выведет программа?

n = 10
while n > 0:
    n //= 2
    print(n)

# 6. scope. напиши, что выведет программа?

x = 10
def foo():
    x = 20
    print(x)

foo()
print(x)

# 7. execution order. что вычисляет эта программа?

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

print(f(5))

# 8. какая асимптотическая сложность f(n) из прошлого задания? перепиши ее эффективнее










# 9. set. напиши функцию unique, которая принимает список чисел и возвращает количество уникальных чисел в этом списке


def unique(lst):
    # ваш код


# пример использования
a = [1, 2, 3, 2, 7, 2, 43, 10, 1]
print(unique(a)) # выведет 6


# 10. dict. что выведет программа и почему?

d = {"x": 1, "y": 2, "x": 3}
print(d)


# 11. в чём смысл параметра encoding при открытии файла в Python?


# 12. что выведет эта программа?

try:
    raise FileNotFoundError
    print("Not found!")
except FileNotFoundError:
    print("Handling!")
finally:
    print("Finally!")
print("After try!")
```
