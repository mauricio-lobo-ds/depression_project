import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Depression Project",
    page_icon="📉",
    layout="wide",
)

st.title("🤖 Machine Learning Model")

# Barra lateral com opções de subpáginas
page = st.sidebar.radio("Select a Section:", [
    "1. Data Preprocessing",
    "2. Cross-Validation",
    "3. Model Training",
    "4. Evaluation Metrics",
    "5. Comparison with Alternative Models"
])

st.sidebar.write("Author: [Mauricio Lobo](https://github.com/mauricio-lobo-ds)")

# Conteúdo de cada subpágina
if page == "1. Data Preprocessing":
    st.write("### 1. Data Preprocessing")
    st.markdown("""
    #### 1.1 Converting 'Yes'/'No' Variables to Binary:
    - Transform all binary categorical variables ('Yes'/'No') into 0 and 1.
    
    #### 1.2 Encoding Non-Ordered Categorical Variables:
    - Apply one-hot encoding (dummy variables) to categorical variables that have no intrinsic order, such as 'Dietary Habits' or 'Sleep Duration'.
    
    #### 1.3 Standardizing Numerical Variables:
    - Apply z-score standardization to numerical variables (e.g., 'Age', 'Work Hours', 'Work Pressure') to ensure they have a mean of zero and a standard deviation of one.
    
    #### 1.4 Ensuring Same Scale (Scaling):
    - Ensure that all numerical variables are on the same scale to improve the efficiency of optimization algorithms and the overall performance of the model.
    
    #### 1.5 Feature Engineering:
    - **1.5.1 Age Grouping:** Create age categories (e.g., 20-30, 31-40, 41-50) to capture non-linear effects.
    - **1.5.2 Variable Interactions:** Create new features by combining existing variables.
    - **1.5.3 Mathematical Transformations:** Apply logarithm or square root transformations to variables with skewed distributions.
    """)

elif page == "2. Cross-Validation":
    st.write("### 2. Cross-Validation")
    st.markdown("""
    #### 2.1 Implementing k-Fold Cross-Validation:
    - Implement k-fold cross-validation (e.g., k=5 or k=10) to consistently evaluate the model's performance and avoid overfitting.
    
    #### 2.2 Stratifying Folds:
    - Stratify the folds to maintain the proportion of classes ('Yes'/'No') in each split.
    """)

elif page == "3. Model Training":
    st.write("### 3. Model Training")
    st.markdown("""
    #### 3.1 Model Objective:
    - Predict the probability of an individual having depression ('Yes' or 'No') based on the input features.
    
    #### 3.2 Models to be Used:
    - **Zero-Inflated Poisson Regression (ZIP):** Useful if the response variable were a count with many zeros. However, since 'Depression' is binary ('Yes'/'No'), logistic regression may be more appropriate.
    - **Binary Logistic Regression:** Standard model for binary classification.
    
    #### 3.3 Consideration for ZIP:
    - ZIP is suited for count data with excess zeros.
    - If 'Depression' is binary, ZIP may not be necessary.
    - **Suggestion:** Review if ZIP is appropriate or if logistic regression better suits the objective.
    """)

elif page == "4. Evaluation Metrics":
    st.write("### 4. Evaluation Metrics")
    st.markdown("""
    #### 4.1 Metrics for Binary Classification:
    - **Accuracy:** The proportion of correct predictions.
    - **Precision, Recall, F1-Score:** Metrics that account for false positives and false negatives.
    - **Confusion Matrix:** To visualize the model's performance across different classes.
    - **ROC AUC:** Area under the ROC curve to evaluate the model's discriminative power.
    - **Precision-Recall Curve:** Particularly useful for imbalanced datasets.
    """)

elif page == "5. Comparison with Alternative Models":
    st.write("### 5. Comparison with Alternative Models")
    st.markdown("""
    #### 5.1 Models to Compare:
    - **Logistic Regression:** A linear model for binary classification.
    - **Random Forest:** An ensemble model capable of capturing non-linear interactions.
    - **Gradient Boosting Machines (e.g., XGBoost, LightGBM):** May offer superior performance for classification tasks.
    
    #### 5.2 Evaluation:
    - Apply the same preprocessing and cross-validation process to all models.
    - Compare evaluation metrics to determine the most suitable model.
    """)
