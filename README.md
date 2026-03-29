# 🌌 Imbalanced Astrophysics: Pulsar Star Identification

Detecting Pulsar stars from radio frequency interference (RFI) and background space noise. 

This project demonstrates how to handle **highly imbalanced datasets** using Logistic Regression. Rather than relying on misleading standard accuracy, this project utilizes class-weighted loss functions and custom probability threshold tuning to maximize the **F1-Score**.

## 🚀 The Astrophysics Challenge

Space is incredibly noisy. In the HTRU2 dataset, roughly **90%** of the recorded signals are background noise, and only **10%** are actual Pulsars. 

If a model simply guessed "Noise" every single time, it would achieve 90% accuracy, but it would be scientifically useless. To solve this, we must penalize the model for missing the rare Pulsars and tune the mathematical threshold for what qualifies as a positive detection.

## 🧮 The Mathematics Behind the Code

### 1. The Core Model: Logistic Regression
Logistic Regression doesn't output a hard class (0 or 1) immediately; it outputs a **probability**. 
First, it calculates a linear combination of the input features (the radio signal metrics):

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

Then, it passes this value through the **Sigmoid Function** to map it to a probability between 0 and 1:

$$\hat{y} = P(y=1|x) = \frac{1}{1 + e^{-z}}$$

*Where $\hat{y}$ is the probability that the signal is a Pulsar.*

### 2. Handling Imbalance: Weighted Log Loss
Standard Logistic Regression minimizes the Binary Cross-Entropy (Log Loss) function. However, because our data is 90% noise, the standard loss function will naturally optimize for the majority class. 

By setting `class_weight='balanced'` in `scikit-learn`, we alter the loss function to penalize errors on the minority class more heavily:

$$J_{weighted} = - \frac{1}{N} \sum_{i=1}^{N} \left[ W_1 y_i \log(\hat{y}_i) + W_0 (1-y_i) \log(1-\hat{y}_i) \right]$$

Here, $W_1$ (the weight for Pulsars) is mathematically set much higher than $W_0$ (the weight for noise), inversely proportional to their class frequencies. 

### 3. Threshold Tuning
By default, the algorithm predicts a Pulsar if $\hat{y} \ge 0.5$. Because we applied heavy class weights, our model became highly sensitive and eager to predict Pulsars, leading to many False Positives. 

To fix this, we extracted the raw probabilities (`.predict_proba()`) and iterated through thresholds to find the mathematical peak of our model's performance. The optimal threshold was discovered to be **0.84**. A signal now needs an 84% probability score before we trigger the telescope.

## 📊 Evaluation Metrics

To measure success, we discard standard accuracy and focus on the confusion matrix components: True Positives (TP), False Positives (FP), and False Negatives (FN).

* **Precision (0.92):** When the model claims it found a Pulsar, how often is it right?

$$Precision = \frac{TP}{TP + FP}$$

* **Recall (0.88):** Out of all the actual Pulsars in space, how many did we successfully find?

$$Recall = \frac{TP}{TP + FN}$$

* **F1-Score (0.90):** The harmonic mean of Precision and Recall. This is our primary target metric, as it balances the trade-off between false alarms and missed discoveries.

$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

## 🛠️ Project Structure

* `notebook.ipynb`: The primary exploratory data analysis, model training, threshold tuning loop, and visualizations (ROC and PR curves).
* `app.py`: The interactive Streamlit web application for real-time predictions.
* `pulsar_model.pkl`: The serialized, pre-trained Logistic Regression model.
* `pulsar_scaler.pkl`: The serialized StandardScaler to ensure new input data matches the training distribution.
* `pulsar_stars.csv`: The original HTRU2 dataset (Not included due to size, available on Kaggle/UCI).

## 💻 Running the Web App Locally

1. Clone this repository.
2. Ensure you have the required libraries installed (see `requirements.txt` below):
   ```bash
   pip install -r requirements.txt