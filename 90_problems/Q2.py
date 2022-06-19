N = int(input())

if N % 2:
    print()
    exit()

for i in range(2**N):
    ch = format(i, f"0{N}b")
    right = 0
    left = 0
    for num in ch:
        if int(num) == 0:
            left += 1
        else:
            right += 1
        if right > left:
            break
    if right != left:
        continue
    strs = ["(" if int(char) == 0 else ")" for char in ch]
    print("".join(strs))
