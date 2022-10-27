import numpy as gh
import matplotlib.pyplot as plt
subject=gh.array(["tamil","english",
"maths","science","social"])
mark=gh.array([77,76,48,72,86])
plt.bar(subject,mark)
plt.title("Result")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()

