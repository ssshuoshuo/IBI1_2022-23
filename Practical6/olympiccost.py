import matplotlib.pyplot as plt

costs = [1,8,15,7,5,14,43,40]
sorted_costs = sorted(costs)

print("Sorted costs:", sorted_costs)

colors = ['r', 'coral', 'gold', 'c', 'chartreuse', 'plum', 'pink']

plt.bar(range(len(sorted_costs)), sorted_costs, color=colors)
plt.xlabel("Olympic Games")
plt.ylabel("Cost (in $ billions)")
plt.title("Cost of Hosting the Summer Olympic Games")
plt.show()

