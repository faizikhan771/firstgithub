#Steps involved in data visualisation
#Step-01--Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#Step-02--seta theme
sns.set_theme(style="ticks", color_codes=True) #Seaborn has five built-in themes to style its plots: darkgrid , whitegrid , dark , white , and ticks.

#step-03--import data set(can import your own data)
kashti = sns.load_dataset("titanic")
# print(kashti)

#step-04--Plot basic graph with 1 variable (count plot)
p =sns.countplot(x="sex", data=kashti)
plt.show()

#step-05--Plot basic graph with 2 variables (count plot)
p =sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("Baba Amar ka count plot for kashti")
plt.show()


