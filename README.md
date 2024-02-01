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
## Extracting Features
```python
def extract_hog_features(img_path):
    """
    Extract HOG features from an image.

    Parameters:
    - img_path (str): Path to the image file.

    Returns:
    - hog_features (numpy.ndarray): Array of HOG features.
    """
```
