import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Depression Project",
    page_icon="📉",
    layout="wide",
)

st.sidebar.write("Author: [Mauricio Lobo](https://github.com/mauricio-lobo-ds)")


st.title("💡 Plan")

# Data Preprocessing
st.write("#### 1. Data Preprocessing")
st.write("1.1 Converting 'Yes'/'No' Variables to Binary:")
st.write("- Transform all binary categorical variables ('Yes'/'No') into 0 and 1.")

st.write("1.2 Encoding Non-Ordered Categorical Variables:")
st.write("- Apply one-hot encoding (dummy variables) to categorical variables that have no intrinsic order, such as 'Dietary Habits' or 'Sleep Duration'.")

st.write("1.3 Standardizing Numerical Variables:")
st.write("- Apply z-score standardization to numerical variables (e.g., 'Age', 'Work Hours', 'Work Pressure') to ensure they have a mean of zero and a standard deviation of one.")

st.write("1.4 Ensuring Same Scale (Scaling):")
st.write("- Ensure that all numerical variables are on the same scale to improve the efficiency of optimization algorithms and the overall performance of the model.")

st.write("1.5 Feature Engineering:")
st.write("- **1.5.1 Age Grouping:** Create age categories (e.g., 20-30, 31-40, 41-50) to capture non-linear effects.")
st.write("- **1.5.2 Variable Interactions:** Create new features by combining existing variables.")
st.write("- **1.5.3 Mathematical Transformations:** Apply logarithm or square root transformations to variables with skewed distributions.")

# Cross-Validation
st.write("#### 2. Cross-Validation")
st.write("2.1 Implementing k-Fold Cross-Validation:")
st.write("- Implement k-fold cross-validation (e.g., k=5 or k=10) to consistently evaluate the model's performance and avoid overfitting.")

st.write("2.2 Stratifying Folds:")
st.write("- Stratify the folds to maintain the proportion of classes ('Yes'/'No') in each split.")

# Model Training
st.write("#### 3. Model Training")
st.write("3.1 Model Objective:")
st.write("- Predict the probability of an individual having depression ('Yes' or 'No') based on the input features.")

st.write("3.2 Models to be Used:")
st.write("- **Zero-Inflated Poisson Regression (ZIP):** Useful if the response variable were a count with many zeros. However, since 'Depression' is binary ('Yes'/'No'), logistic regression may be more appropriate.")
st.write("- **Binary Logistic Regression:** Standard model for binary classification.")

st.write("3.3 Consideration for ZIP:")
st.write("- ZIP is suited for count data with excess zeros.")
st.write("- If 'Depression' is binary, ZIP may not be necessary.")
st.write("- **Suggestion:** Review if ZIP is appropriate or if logistic regression better suits the objective.")

# Evaluation Metrics
st.write("#### 4. Evaluation Metrics")
st.write("4.1 Metrics for Binary Classification:")
st.write("- **Accuracy:** The proportion of correct predictions.")
st.write("- **Precision, Recall, F1-Score:** Metrics that account for false positives and false negatives.")
st.write("- **Confusion Matrix:** To visualize the model's performance across different classes.")
st.write("- **ROC AUC:** Area under the ROC curve to evaluate the model's discriminative power.")
st.write("- **Precision-Recall Curve:** Particularly useful for imbalanced datasets.")

# Comparison with Alternative Models
st.write("#### 5. Comparison with Alternative Models")
st.write("5.1 Models to Compare:")
st.write("- **Logistic Regression:** A linear model for binary classification.")
st.write("- **Random Forest:** An ensemble model capable of capturing non-linear interactions.")
st.write("- **Gradient Boosting Machines (e.g., XGBoost, LightGBM):** May offer superior performance for classification tasks.")

st.write("5.2 Evaluation:")
st.write("- Apply the same preprocessing and cross-validation process to all models.")
st.write("- Compare evaluation metrics to determine the most suitable model.")
