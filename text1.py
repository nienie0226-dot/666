total = int(input("請輸入一個正整數："))

# text1.py 檔案內容
def calculate_sum(n):  # 這裡的名稱要對
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(total)