import __local__
from luma.classifier.tree import DecisionTreeClassifier
from luma.reduction.linear import PCA
from luma.visual.evaluation import DecisionRegion

from sklearn.datasets import load_iris


X, y = load_iris(return_X_y=True)

pca = PCA(n_components=2)
X = pca.fit_transform(X)

model = DecisionTreeClassifier(max_depth=5,
                               criterion='gini',
                               min_samples_split=2,
                               min_samples_leaf=1,
                               max_features=None,
                               min_impurity_decrease=0.01,
                               max_leaf_nodes=None,
                               random_state=42)
model.fit(X, y)

DecisionRegion(model, X, y).plot(show=True)
