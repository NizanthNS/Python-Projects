import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("D:/Test_Data/data.csv")


plt.style.use("dark_background")


fig = plt.figure(figsize=(14, 10))
fig.suptitle(
    "POKEMON ANALYTICS DASHBOARD",
    fontsize=20,
    color="cyan",
    fontweight="bold"
)

ax1 = plt.subplot(2, 2, 1)

type_counts = df["Type1"].value_counts()

ax1.bar(
    type_counts.index,
    type_counts.values,
    color="deepskyblue"
)

ax1.set_title("Pokemon by Type")
ax1.tick_params(axis='x', rotation=45)

ax2 = plt.subplot(2, 2, 2)

top10 = df.nlargest(10, "Weight")

ax2.barh(
    top10["Name"],
    top10["Weight"],
    color="orange"
)

ax2.set_title("Top 10 Heaviest Pokemon")
ax2.invert_yaxis()

ax3 = plt.subplot(2, 2, 3)

ax3.hist(
    df["Height"],
    bins=15,
    color="lime",
    edgecolor="white"
)

ax3.set_title("Height Distribution")

ax4 = plt.subplot(2, 2, 4)

legendary_counts = df["Legendary"].value_counts()

labels = ["Normal", "Legendary"]

ax4.pie(
    legendary_counts,
    labels=labels,
    autopct="%1.1f%%",
    colors=["dodgerblue", "gold"]
)

ax4.set_title("Legendary Pokemon")

plt.tight_layout()

plt.show()