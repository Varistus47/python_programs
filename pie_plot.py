import numpy as gh
import matplotlib.pyplot as plt
subject=["physics","maths","social",
"programming","english"]
mark=gh.array([35,53,78,91,67])
plt.pie(mark,labels=subject)
plt.title("Marks")
plt.show()

