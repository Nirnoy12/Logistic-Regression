# 🌌 Imbalanced Astrophysics: Pulsar Star Identification

Detecting Pulsar stars from radio frequency interference (RFI) and background space noise. 

This project is a complete, mathematically grounded pipeline for handling **highly imbalanced datasets**. It demonstrates why standard accuracy is a deceptive metric in astrophysics and how to use weighted loss functions and probability threshold tuning to build a scientifically viable predictive model.

---

## 🚀 1. The Astrophysics Challenge: The Needle in the Haystack

Space is massive and incredibly noisy. In the HTRU2 dataset, roughly **90%** of the recorded signals are background noise, and only **10%** are actual Pulsars. 

**The Accuracy Trap:** If a machine learning model simply hardcoded its output to guess "Noise" every single time, it would achieve **90% accuracy**. However, its scientific value would be exactly zero. To solve this, we must look under the hood of Logistic Regression and mathematically force the algorithm to care about the rare Pulsars.

---

## 🧮 2. The Engine: Logistic Regression Mathematics

Despite the word "regression," Logistic Regression is a classification algorithm. It does not output a hard "Yes" or "No"—it outputs a **probability**. 

### Step 2.1: The Linear Combination
First, the model takes your input features (the statistical measurements of the radio signal, denoted as $X$) and multiplies them by learned weights ($W$), adding a bias term ($b$).

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

* **Often Overlooked:** This equation just outputs a number anywhere from $-\infty$ to $+\infty$. We cannot use this raw number as a probability because probabilities must live strictly between 0 and 1.

### Step 2.2: The Sigmoid Squishification
To convert $z$ into a valid probability, we pass it through the **Sigmoid (Logistic) Function**:

$$\hat{y} = P(y=1|x) = \frac{1}{1 + e^{-z}}$$

* Where $\hat{y}$ is the predicted probability that the signal is a Pulsar.
* **Why Euler's Number ($e$)?** We use $e \approx 2.718$ because its derivative is extremely clean ($\frac{d}{dx}e^x = e^x$). This makes the calculus required to train the model (Gradient Descent) highly efficient. The Sigmoid curve forms an "S" shape, perfectly squishing any number between 0 and 1.

---

## ⚖️ 3. The Training: Penalizing Mistakes

How does the model actually learn the correct weights ($W$)? By measuring its mistakes using a **Loss Function** and minimizing that loss.

### Step 3.1: Binary Cross-Entropy (Log Loss)
Beginners often ask: *Why not just use Mean Squared Error (MSE) like in linear regression?* Because passing MSE through a Sigmoid function creates a non-convex math landscape full of "local minima" (valleys where the algorithm gets permanently stuck). 

Instead, we use **Log Loss**:

$$J = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \right]$$

* **How it works:** If the true label is a Pulsar ($y=1$), the second half of the equation disappears. We are left with $\log(\hat{y})$. If the model predicts a low probability (e.g., 0.01) for a true Pulsar, $\log(0.01)$ yields a massive negative number, heavily penalizing the model for being *confidently wrong*.

### Step 3.2: Solving the Imbalance with Class Weights
Standard Log Loss treats all errors equally. To fix our 90/10 data imbalance, we use `class_weight='balanced'` in scikit-learn. This alters the loss function to penalize errors on the minority class more heavily.

Scikit-learn calculates these weights using this specific formula:
$$W_j = \frac{N_{total}}{N_{classes} \times N_j}$$

For our dataset:
* Weight for Noise ($W_0$) $\approx \frac{100}{2 \times 90} \approx 0.55$
* Weight for Pulsar ($W_1$) $\approx \frac{100}{2 \times 10} \approx 5.0$

**The Weighted Log Loss Equation:**
$$J_{weighted} = - \frac{1}{N} \sum_{i=1}^{N} \left[ W_1 y_i \log(\hat{y}_i) + W_0 (1-y_i) \log(1-\hat{y}_i) \right]$$
Now, missing a single Pulsar costs the model roughly **9 times** more "loss" than misclassifying noise!

---

## 🎯 4. The Tuning: Shifting the Goalposts

By default, Logistic Regression predicts Class 1 if $\hat{y} \ge 0.5$. 

Because we applied heavy class weights, our model became highly sensitive—it started flagging everything as a Pulsar to avoid that massive penalty. This increased our False Positives. 

To fix this, we ran a Python loop to test every possible threshold from 0.1 to 0.99. We discovered the mathematical peak of our model's performance was at **0.84**. 
* **The New Rule:** A signal now needs an 84% probability score before we officially classify it as a Pulsar.

---

## 📊 5. Evaluation Metrics: Beyond Accuracy

To measure success, we discard accuracy and focus on the **Confusion Matrix**:
* **True Positives (TP):** Model says Pulsar, it IS a Pulsar.
* **False Positives (FP):** Model says Pulsar, it is Noise (False Alarm).
* **False Negatives (FN):** Model says Noise, it IS a Pulsar (Missed Discovery).

### Precision (0.92)
When the model claims it found a Pulsar, how often is it right?
$$Precision = \frac{TP}{TP + FP}$$
*Crucial because telescope time is expensive. We want to minimize false alarms.*

### Recall (0.88)
Out of all the actual Pulsars in space, how many did we successfully find?
$$Recall = \frac{TP}{TP + FN}$$
*Crucial because we don't want to miss scientific discoveries.*

### The F1-Score (0.90)
The F1-Score combines Precision and Recall into a single metric.
$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

* **Often Overlooked: Why the Harmonic Mean?** Why not just use the arithmetic average $\frac{P + R}{2}$? If a terrible model predicts "Pulsar" for every single signal, Recall is 1.0, but Precision is near 0.0. An arithmetic average would be 0.5 (making the model look okay). The **Harmonic Mean** heavily punishes extreme values. If Precision drops to near zero, the entire F1-Score drops to near zero, accurately reflecting the model's failure.

---

## 🛠️ Project Structure & Running Locally

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/Nirnoy12/Pulsar-Classification.git](https://github.com/Nirnoy12/Pulsar-Classification.git)