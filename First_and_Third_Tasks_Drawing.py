import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# First Task
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots(1, 1, figsize = (10, 10), dpi=100)
plt.plot(x, np.sin(x))
ax.set_title("Sinusoid line plot")
plt.show()

# Third Task
tips_df = sns.load_dataset('tips')
tips_df["tip_percentage"] = tips_df["tip"] / tips_df["total_bill"]
pivot = tips_df.pivot_table(
    index=["day"],
    columns=["size"],
    values="tip_percentage",
    aggfunc=np.average)
sns.heatmap(pivot).set_title('Heatmap')
plt.show()



