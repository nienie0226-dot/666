from text1 import calculate_sum

# 讓使用者輸入 N
try:
    n_value = int(input("請輸入一個正整數 N："))
    
    if n_value < 1:
        print("請輸入大於 0 的整數。")
    else:
        # 使用載入的函式計算結果
        result = calculate_sum(n_value)
        print(f"從 1 累加到 {n_value} 的結果為：{result}")

except ValueError:
    print("輸入錯誤！請確保您輸入的是數字。")