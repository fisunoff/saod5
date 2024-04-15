def digit_sort(mas):
    tmp = [[] for _ in range(10)]
    n = len(str(max(mas)))  # длина наибольшего числа
    for i in range(n):
        for x in mas:
            digit = (x // 10 ** i) % 10
            tmp[digit].append(x)
        mas = []
        for row in tmp:
            mas.extend(row)
        tmp = [[] for _ in range(10)]
    return mas
