import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA

# Load Breast Cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target
class_names = list(data.target_names)  # ['malignant', 'benign']

# Reduce to 2 components for plotting
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3, random_state=42)

# Initialize classifiers
svm_clf = SVC(kernel='linear')
tree_clf = DecisionTreeClassifier(random_state=42)
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train classifiers
svm_clf.fit(X_train, y_train)
tree_clf.fit(X_train, y_train)
rf_clf.fit(X_train, y_train)

# Predict
y_pred_svm = svm_clf.predict(X_test)
y_pred_tree = tree_clf.predict(X_test)
y_pred_rf = rf_clf.predict(X_test)

# Visualization function
def plot_classifier(title, model, X, y):
    h = 0.5  # increased step size to avoid memory issues
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(6, 4))
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm)
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolor='k')
    plt.legend(handles=scatter.legend_elements()[0], labels=class_names)
    plt.title(title)
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot decision boundaries
plot_classifier("SVM Classifier (Binary)", svm_clf, X_test, y_test)
plot_classifier("Decision Tree Classifier (Binary)", tree_clf, X_test, y_test)
plot_classifier("Random Forest Classifier (Binary)", rf_clf, X_test, y_test)

# Print reports
print("=== SVM Classification Report ===")
print(classification_report(y_test, y_pred_svm, target_names=class_names))

print("=== Decision Tree Classification Report ===")
print(classification_report(y_test, y_pred_tree, target_names=class_names))

print("=== Random Forest Classification Report ===")
print(classification_report(y_test, y_pred_rf, target_names=class_names))
