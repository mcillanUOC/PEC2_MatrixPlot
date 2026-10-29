import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df_penguins = sns.load_dataset("penguins")

# Scatterplot matrix
sns_plot = sns.pairplot(df_penguins, kind="scatter", hue="species", markers=["o", "s", "D"], palette="colorblind")
sns_plot.figure.suptitle("Matriz de diagramas de dispersión: Palmer Penguins", fontsize=14, fontweight="bold", y=1.02)

# Save fig
sns_plot.savefig("scatterplot_matrix_penguins.png", dpi=300, bbox_inches="tight")
