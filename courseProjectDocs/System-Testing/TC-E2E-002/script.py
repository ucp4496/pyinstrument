def work(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    print(work(10_000_000))
