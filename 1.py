import matplotlib.pyplot as plt
time = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
postage_prices = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]
# 绘制阶梯图
plt.figure()
plt.title('1995-2009年美国邮票价格')
plt.xlabel('时间')
plt.ylabel('邮费价格')
plt.xticks(time)
plt.yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])
plt.step(time, postage_prices, where='post')
plt.grid(True)
# 显示具体的数据项信息
for i in range(len(time)):
    plt.text(time[i], postage_prices[i], f"{postage_prices[i]}", ha='center', va='bottom')
plt.show()
# 绘制折线图
plt.figure()
plt.title('1995-2009年美国邮票价格')
plt.xlabel('时间')
plt.ylabel('邮费价格')
plt.xticks(time)
plt.yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])
plt.plot(time, postage_prices, marker='o')
plt.grid(True)
# 显示具体的数据项信息
for i in range(len(time)):
    plt.text(time[i], postage_prices[i], f"{postage_prices[i]}", ha='center', va='bottom')
plt.show()