#pip install matplotlib

import matplotlib.pyplot as plt
year=[]
for i in range(2004,2020):
    year.append(i)
runs=[19,895,821,1103,1097,1198,600,
764,524,753,418,640,278,788,275,600]
plt.plot(year,runs,color="r")
plt.title("Dhoni ODI runs")
plt.xlabel("year")
plt.ylabel("runs")
plt.show()

