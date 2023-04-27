import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

df = pd.read_pickle("resources/audio_data.csv")

X = df["feature"].values
X = np.concatenate(X, axis=0).reshape(len(X), 40)

y = np.array(df["class_label"].tolist())
y = to_categorical(y)

# split for training and testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42, shuffle=True)

# build the model

# TODO: consider using convolutional layers
model = Sequential([
    Dense(256, input_shape=x_train[0].shape),
    Activation('relu'),
    Dropout(0.3),
    Dense(256),
    Activation('relu'),
    Dropout(0.3),
    Dense(2, activation='softmax')
])

print("How the model looks like: \n")
print(model.summary())

model.compile(
    loss="categorical_crossentropy",
    optimizer='adam',
    metrics=['accuracy']
)

print("Model Score: \n")
history = model.fit(x_train, y_train, epochs=1000)
model.save("saved_model/WWD.h5")
score = model.evaluate(x_test, y_test)
print(score)

# Classification Report
print("Model Classification Report: \n")
clf = SVC(random_state=0)
clf.fit(x_train, np.argmax(y_train, axis=1))
SVC(random_state=0)
predictions = clf.predict(x_test)
cm = confusion_matrix(np.argmax(y_test, axis=1), predictions, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot()
plt.show()
