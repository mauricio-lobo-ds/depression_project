# 🔹 Depression Analysis Project

## About the Project
The **Depression Analysis Project** is an initiative to explore and analyze factors associated with depression using the [Depression Professional Dataset](https://www.kaggle.com/datasets/ikynahidwin/depression-professional-dataset/data). The dataset contains 2054 entries and 11 columns, offering information on:
- **Demographics**: Gender, Age
- **Work-Related Factors**: Work Pressure, Job Satisfaction
- **Lifestyle**: Sleep Duration, Dietary Habits
- **Mental Health**: Suicidal Thoughts, Financial Stress, Family History of Mental Illness
- **Target Variable**: Depression (Yes/No)

This project aims to uncover meaningful insights about depression by analyzing trends, correlations, and the impact of different variables. These insights are made accessible through an interactive **Streamlit web application**.

## Project Objectives
1. **Analyze Depression Factors**:
   - Identify correlations between work, lifestyle, and mental health factors.
   - Highlight significant predictors of depression, such as work pressure, sleep patterns, or financial stress.
   - Provide visual insights into how these factors vary across different groups (e.g., gender or age).

2. **Deliver Interactive Data Exploration**:
   - Develop a user-friendly interface using Streamlit.
   - Allow users to explore the dataset interactively, including data visualizations, filtering options, and summaries.

3. **Build a Foundation for Predictive Modeling**:
   - Lay the groundwork for future predictive models, focusing on feature engineering and data preprocessing for high-quality input.

## Features
- **Streamlit Web Application**:
  - Dynamic web app to make the dataset accessible to end users.
  - Clear and concise user interface for exploring the data ana analysis.

## File Structure
```
DEPRESSION_PROJECT/
├── .streamlit/ # Streamlit configuration
├── data/ # Dataset (Depression_Professional_Dataset.csv)
├── pages/ # Multipage app files
│ ├── 1_🔍_Exploratory_Data_Analysis.py
│ ├── 2_💡_Plan.py
│ └── 3_🤖_Machine_Learning.py
├── _🔹_About.py # Main app page
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/mauricio-lobo-ds/depression_project.git
   cd depression-analysis
