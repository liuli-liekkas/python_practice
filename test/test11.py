#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

print(fib(10))