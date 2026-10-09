import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Test_Data/data.csv")

print(df.head())

print("Average Height: ", round(np.mean(df["Height"]), 2))
print("Average Weight: ", round(np.mean(df["Weight"]), 2))

tallest = df.loc[df["Height"].idxmax()]

print("Tallest Pokemon")
print(tallest["Name"])
print("Height: ", tallest["Height"])

heaviest = df.loc[df["Weight"].idxmax()]

print("Heaviest Pokemon")
print(heaviest["Name"])
print("Weight: ", heaviest["Weight"])

type_counts = df["Type1"].value_counts()
# print(type_counts)

plt.figure(figsize = (10, 5))
type_counts.plot(kind = "bar", color = "red")

plt.title("Pokemon Type Distribution")
plt.xlabel("Type")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

top10 = df.nlargest(10, "Weight")

print(top10[["Name", "Weight"]])

plt.figure(figsize = (10, 5))

plt.barh(
    top10["Name"],
    top10["Weight"],
    color="orange"
)

plt.title("Top 10 Heaviest Pokemon")
plt.xlabel("Weight (kg)")
plt.gca().invert_yaxis()

plt.show()

plt.figure(figsize = (10, 6))

plt.scatter(
    df["Height"],
    df["Weight"],
    alpha=0.7,
    c="red"
)

plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.grid(True)
plt.show()

legendary = df[df["Legendary"] == 1]

print(legendary[["Name", "Type1", "Height", "Weight"]])

df["PowerIndex"] = (
    df["Weight"] * 10 +
    df["Height"] * 50
)

top_power = df.nlargest(
    10,
    "PowerIndex"
)

print(top_power[["Name", "PowerIndex"]])