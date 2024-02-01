import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, f1_score, \
    recall_score
from skimage import feature
from skimage.transform import resize

data = pd.read_csv('imageLabels.csv')
paths = data['Path'].tolist()
target = data['Label']
xTrain, xTest, yTrain, yTest = train_test_split(paths, target, test_size=0.3, random_state=42)


def extractHogFeatures(imgPath):
    img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale using OpenCV
    imgResized = resize(img, (64, 64))  # Resize the image for consistency
    hogFeatures = feature.hog(imgResized, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                              block_norm='L2-Hys')
    return hogFeatures


xTrain = [extractHogFeatures(path) for path in xTrain]
xTest = [extractHogFeatures(path) for path in xTest]

svmModel = SVC(kernel='linear')
print("Training SVM")
svmModel.fit(xTrain, yTrain)
print("Predicting SVM")
predictions = svmModel.predict(xTest)

accuracy = accuracy_score(yTest, predictions)
precision = precision_score(yTest, predictions, average='weighted')
f1 = f1_score(yTest, predictions, average='weighted')
recall = recall_score(yTest, predictions, average='weighted')
confusion = confusion_matrix(yTest, predictions)
report = classification_report(yTest, predictions)

print(f"Confusion Matrix: {confusion}")
print(f"Classification Report: {report}")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
