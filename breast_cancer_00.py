from ucimlrepo import fetch_ucirepo
import seaborn as sns
import matplotlib.pyplot as plt

# fetch dataset
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)

# data (as pandas dataframes)
X = breast_cancer_wisconsin_diagnostic.data.features
y = breast_cancer_wisconsin_diagnostic.data.targets

# metadata
print(breast_cancer_wisconsin_diagnostic.metadata)

# variable information
print(breast_cancer_wisconsin_diagnostic.variables)

# Extract features names from dataframe
features = X.columns.values
num_graf = len(features) / 6  # number of grafics

sns.set(style='whitegrid', palette="flare", font_scale=1.1, rc={"figure.figsize": [8, 5]})

i = 0
for count in range(int(num_graf)):
    fig, ax = plt.subplots(2, 3, figsize=(15, 7))
    for variable, subplot in zip(features[i:i + 6], ax.flatten()):
        sns.histplot(X, x=variable, ax=subplot)
    i = count + 6
plt.show()

# quantity of samples per category
num_category = y.value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
pl = num_category.plot(kind='bar', ax=ax)
# TODO: Change the color and font of the plots


# Scatter plots to explore visual correlation of features


# TODO: read about the features idk
# heatmap to explore correlation
corr_mat = X.corr()
figCorr, axCorr = plt.subplots(figsize=(10, 15))
sns.heatmap(corr_mat)

