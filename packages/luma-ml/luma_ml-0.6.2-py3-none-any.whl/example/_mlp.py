import __local__
from luma.neural.multi_layer import MLPClassifier
from luma.neural.optimizer import *
from luma.preprocessing.scaler import StandardScaler
from luma.model_selection.split import TrainTestSplit

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt


X, y = load_digits(return_X_y=True)

sc = StandardScaler()
X_sc = sc.fit_transform(X)

X_train, X_test, y_train, y_test = TrainTestSplit(X_sc, y,
                                                  test_size=0.2,
                                                  random_state=42).get

optimizers = [SGDOptimizer(), MomentumOptimizer(), RMSPropOptimizer()]

for opt in optimizers:
    mlp = MLPClassifier(input_size=64,
                        hidden_sizes=[128, 32],
                        output_size=10,
                        max_epoch=1000,
                        batch_size=100,
                        learning_rate=0.0001,
                        momentum=0.9,
                        decay_rate=0.9, 
                        lambda_=0.01,
                        dropout_rate=0.2,
                        activation='relu',
                        optimizer=opt,
                        random_state=42,
                        verbose=True)

    print(type(opt).__name__)
    mlp.fit(X_train, y_train)
    score = mlp.score(X_test, y_test)
    print(score)
    
    plt.plot(range(mlp.max_epoch), mlp.epoch_losses_, 
             label=f'{type(opt).__name__[:-9]} [Acc: {score:.3f}]')

plt.title('MLP with Various Optimizers')
plt.xlabel('Epoch')
plt.ylabel('Loss (Cross-Entropy)')
plt.legend()
plt.tight_layout()
plt.show()
