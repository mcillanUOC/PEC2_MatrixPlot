import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df_penguins = sns.load_dataset("penguins")

# Scatterplot matrix
sns_plot = sns.pairplot(df_penguins, kind="scatter", hue="species", markers=["o", "s", "D"], palette="colorblind")

# Save fig
sns_plot.savefig("scatterplot_matrix_penguins.png", dpi=300, bbox_inches="tight")
