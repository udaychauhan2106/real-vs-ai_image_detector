# AI-Generated Image Detector

A deep learning project that detects whether a given image is AI-generated or real using a Convolutional Neural Network and Transfer Learning (MobileNetV2).

## 👨‍💻 Technologies Used
- Python
- TensorFlow / Keras
- NumPy, Matplotlib
- MobileNetV2 (Transfer Learning)
- Grad-CAM (for explainability)

## 📚 Dataset
- [140k Real and Fake Faces](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces)

## 🧠 Approach
- Images preprocessed and resized to 160x160.
- Data was split into training and validation.
- Used data augmentation and dropout to improve generalization.
- Trained the model using MobileNetV2 base with fine-tuning.
- Grad-CAM used for visual explanation of predictions.

## 📈 Model Performance
- Validation Accuracy: 91%
- Precision/Recall/F1 Score: 93/90/91

## 📌 Note
This project is not deployed yet. However, all code for training and prediction is included in the notebook file `detector.ipynb`.


