# Support Vector Machine Classifier
This project is an implementation of a support vector machine (SVM) model to classify images of cats and dogs. This is the Third out of Five tasks presented to the Prodigy InfoTech Machine Learning Internship.

## Creating the CSV File
In order to use the images in the provided dataset, a csv file had to be initialized with the images paths, IDs and labels : <i><b>0</b> for cats and <b>1</b> for dogs<i/>.
```python
Sample
ID,Label,Path
c0.jpg,0,dataset\cat.0.jpg
c1.jpg,0,dataset\cat.1.jpg
c10.jpg,0,dataset\cat.10.jpg
c100.jpg,0,dataset\cat.100.jpg
c1000.jpg,0,dataset\cat.1000.jpg
c10000.jpg,0,dataset\cat.10000.jpg
d0.jpg,1,dataset\dog.0.jpg
d1.jpg,1,dataset\dog.1.jpg
d10.jpg,1,dataset\dog.10.jpg
d100.jpg,1,dataset\dog.100.jpg
d1000.jpg,1,dataset\dog.1000.jpg
d10000.jpg,1,dataset\dog.10000.jpg
```
## Runtime Output
The dataset was too large so the processing time was really slow. Consequently, it was decided to reduce the amount of images used, thus reducing the accuracy of the model.
```python
Confusion Matrix:
[[1478  638]
 [ 605 1479]]

Classification Report:
                   precision    recall  f1-score   support

           0       0.71      0.70      0.70      2116
           1       0.70      0.71      0.70      2084

    accuracy                           0.70      4200
   macro avg       0.70      0.70      0.70      4200
weighted avg       0.70      0.70      0.70      4200

Accuracy: 0.7040
Precision: 0.7041
Recall: 0.7040
F1-Score: 0.7040
  
```
