import matplotlib.pyplot as plt
import numpy as np

# 读取数据
r1 = np.loadtxt("rewards_eps0.1.csv")
r2 = np.loadtxt("rewards_eps0.2.csv")

# 打印前10个数据，看看差异
print("epsilon=0.1 前10个奖励:", r1[:10])
print("epsilon=0.2 前10个奖励:", r2[:10])

# 画图：蓝色实线，橙色虚线
plt.figure(figsize=(10, 6))
plt.plot(r1, label='epsilon=0.1', linewidth=2, alpha=0.8)
plt.plot(r2, label='epsilon=0.2', linewidth=2, alpha=0.8, linestyle='--')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Q-learning Performance Comparison')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()