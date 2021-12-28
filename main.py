# this is a demo project that receives different data (meant to be mercury) from various industry monthly and plots a graph
import matplotlib.pyplot as plt

plt.title(input("What industry are you from: cement, agriculture, manufacturing?\n"))
x = [-6, -3, 3, 6, 9, 12, 15]
plt.xlabel("Power of 3")
y = ["Dec", "Oct", "Jan", "Feb", "Mar", "Apr", "May"]
plt.ylabel("Months")
plt.bar(x, y)
plt.show()
