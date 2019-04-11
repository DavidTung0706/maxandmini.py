dict = {}
month = int(input("有幾個月份:"))
for i in range(month):
    num = int(input("請輸入第 %d 個月的支出金額" %(i + 1)))
    dict.update({i:num})
print("支出最多的金額為: %d" %(max(dict.values())))
print("支出最少的金額為: %d" %(min(dict.values())))
print("支出的總金額為: %d" %(sum(dict.values())))
print("支出金額由小到大排序為: %s" %(sorted(dict.values())))       