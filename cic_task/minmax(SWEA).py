T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num = max(num_list)
    min_num = min(num_list)

    difference = max_num - min_num

    print(f"#{tc} {difference}")
        