#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
#程序分析：关键是计算出每一项的值。
def suma(a,n):
    sum = 0
    for i in range(1,n+1):
        def num(i):
            if i == 1:
                return a
            else:
                return (num(i-1) + (a * (10**(i-1))))
        sum = sum + num(i)
    return sum
print(suma(2,3))