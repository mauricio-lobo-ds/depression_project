import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import time
from sklearn.preprocessing import StandardScaler


st.set_page_config(
    page_title="Depression Project",
    page_icon="📉",
    layout="wide",
)

st.title("🔍Exploratory Data Analysis")

# Sidebar progress bar
with st.sidebar:
    progress_bar = st.progress(0)
    status_placeholder = st.empty()

# Simulate actual tasks
tasks = ["Loading data", "Processing data", "Generating visualizations"]
total_tasks = len(tasks)

for i, task in enumerate(tasks):
    # Display the current task in the sidebar
    status_placeholder.text(f"Step {i + 1}/{total_tasks}: {task}")
    
    # Simulate the real work for each task (replace this with real operations)
    time.sleep(1)  # Replace or remove this delay with actual processing
    
    # Update the progress bar
    progress_bar.progress((i + 1) / total_tasks)

# Remove the progress bar and status message
status_placeholder.empty()
progress_bar.empty()

# Finalize loading
st.sidebar.success("Loaded successfully!")

st.sidebar.write("Author: [Mauricio Lobo](https://github.com/mauricio-lobo-ds)")

# Function to load data
@st.cache_data
def load_data():
    return pd.read_csv('data/Depression_Professional_Dataset.csv')

# Load the data
df = load_data()

# Display the first few rows of the dataset
st.write("##### Dataset Preview (Top Rows):")
st.dataframe(df.head())

# Display basic statistics
st.write("##### Dataset Summary Statistics:")

# Calculate the height dynamically based on the number of rows
num_rows = df.describe(include="all").transpose().shape[0]
row_height = 38  # Adjust the row height if needed
table_height = num_rows * row_height

st.dataframe(df.describe(include="all").transpose(), height=table_height)

# Display missing values and data types
st.write("##### Missing Values and Data Types:")
missing_info = pd.DataFrame({
    "Data Type": df.dtypes,
    "Missing Values": df.isnull().sum(),
    "Missing (%)": (df.isnull().sum() / len(df)) * 100
})
st.dataframe(missing_info)


################################

# Adiciona uma linha divisória
st.divider()

st.write("### Visualizing the data")


# Primeiro gráfico - Distribuição de Idade
col1, col2 = st.columns([6, 4])  # Cria três colunas lado a lado

with col1:
    fig, ax = plt.subplots(figsize=(8, 4))  # Ajusta o tamanho da figura
    sns.histplot(df['Age'], bins=10, kde=True, ax=ax)

    # Ajusta os tamanhos das fontes
    ax.set_title("Age Distribution", fontsize=14)  # Título
    ax.set_xlabel("Age", fontsize=12)  # Rótulo do eixo X
    ax.set_ylabel("Frequency", fontsize=12)  # Rótulo do eixo Y
    ax.tick_params(axis='both', labelsize=10)  # Tamanho das legendas nos eixos
    st.pyplot(fig, transparent=True)

# Segundo gráfico - Contagem de Depressão
with col2:
    # Count the occurrences of "Yes" and "No" in the "Depression" column
    depression_counts = df['Depression'].value_counts()

    # Create the bar plot
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.barplot(
        x=depression_counts.index, 
        y=depression_counts.values, 
        palette="coolwarm", 
        ax=ax3
    )

    # Add titles and labels
    ax3.set_title("Depression Counts in Dataset", fontsize=14)
    ax3.set_xlabel("Depression (Yes/No)", fontsize=12)
    ax3.set_ylabel("Count", fontsize=12)
    ax3.tick_params(axis='both', labelsize=10)

    # Display the plot in Streamlit
    st.pyplot(fig3)


col1, col2 = st.columns([6, 4])  # Define a proporção das colunas: 70% e 30%

# Primeiro gráfico - Boxplots
with col1:
    # List of numeric columns to plot
    numeric_columns_b = ['Work Pressure', 'Job Satisfaction', 'Financial Stress']

    # Create the boxplot
    fig1, ax1 = plt.subplots(figsize=(12, 5))  # Ajusta o tamanho do gráfico
    sns.boxplot(data=df[numeric_columns_b], ax=ax1)

    # Ajusta os tamanhos das fontes e remove rótulos
    ax1.set_title('Boxplots: Work Pressure, Job Satisfaction and Financial Stress', fontsize=14)  # Título
    ax1.set_xlabel("")  # Remove rótulo do eixo X
    ax1.set_ylabel("")  # Remove rótulo do eixo Y
    ax1.tick_params(axis='both', labelsize=12)  # Tamanho das legendas nos eixos
    st.pyplot(fig1, transparent=True)

# Segundo gráfico - Boxplots
with col2:
    numeric_columns_a = ['Work Hours']

    # Create the boxplot
    fig2, ax2 = plt.subplots(figsize=(8, 4))  # Ajusta o tamanho do gráfico
    sns.boxplot(data=df[numeric_columns_a], ax=ax2)

    # Ajusta os tamanhos das fontes e remove rótulos
    ax2.set_title("Boxplot: Work Hours", fontsize=14)  # Título
    ax2.set_xlabel("")  # Remove rótulo do eixo X
    ax2.set_ylabel("")  # Remove rótulo do eixo Y
    ax2.tick_params(axis='both', labelsize=12)  # Tamanho das legendas nos eixos
    st.pyplot(fig2, transparent=True)



##############################

# Adiciona uma linha divisória
st.divider()
st.write("### Depression vs Feature")

# Identificar colunas categóricas ou booleanas, incluindo "Dietary Habits"
categorical_boolean_columns = [
    'Gender', 
    'Have you ever had suicidal thoughts ?', 
    'Family History of Mental Illness', 
    'Dietary Habits',
    'Sleep Duration',
    'Work Hours',
    'Work Pressure'
]


# 1ª Linha: 3 primeiros gráficos lado a lado
cols_1 = categorical_boolean_columns[:3]
columns_1 = st.columns(3)

for i, col in enumerate(cols_1):
    with columns_1[i]:
        depression_counts = df.groupby([col, 'Depression']).size().reset_index(name='Counts')
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            x=col,
            y='Counts',
            hue='Depression',
            data=depression_counts,
            ax=ax,
            palette='coolwarm'
        )
        ax.set_title(f"Depression vs {col}", fontsize=12)
        ax.tick_params(axis='both', labelsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        st.pyplot(fig)

# 2ª Linha: 2 próximos gráficos lado a lado
cols_2 = categorical_boolean_columns[3:5]
columns_2 = st.columns(2)

for i, col in enumerate(cols_2):
    with columns_2[i]:
        depression_counts = df.groupby([col, 'Depression']).size().reset_index(name='Counts')
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            x=col,
            y='Counts',
            hue='Depression',
            data=depression_counts,
            ax=ax,
            palette='coolwarm'
        )
        ax.set_title(f"Depression vs {col}", fontsize=12)
        ax.tick_params(axis='both', labelsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        st.pyplot(fig)

# 3ª Linha: 2 últimos gráficos lado a lado
cols_3 = categorical_boolean_columns[5:]
columns_3 = st.columns(2)

for i, col in enumerate(cols_3):
    with columns_3[i]:
        depression_counts = df.groupby([col, 'Depression']).size().reset_index(name='Counts')
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            x=col,
            y='Counts',
            hue='Depression',
            data=depression_counts,
            ax=ax,
            palette='coolwarm'
        )
        ax.set_title(f"Depression vs {col}", fontsize=12)
        ax.tick_params(axis='both', labelsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        st.pyplot(fig)

#############################
# Adiciona uma linha divisória
st.divider()

st.write("### Exploratory Data Analysis Summary and Machine Learning Plan")

# Parágrafo 1 - Análise Exploratória
st.write("""
Based on the exploratory data analysis, several important patterns emerge from the dataset. 
The distribution of age shows that most respondents fall within the 30–50 age range, with fewer younger or older individuals. 
There is a significant imbalance in the "Depression" variable, where the majority of the individuals reported not having depression. 
This suggests that depression is a minority condition in this dataset, which could impact modeling decisions, especially in handling class imbalance.
""")

# Parágrafo 2 - Fatores Relevantes
st.write("""
Several potential predictors of depression stand out. 
For example, individuals who reported suicidal thoughts are more likely to experience depression, as shown by the stark difference in depression counts between "Yes" and "No" categories. 
Similarly, dietary habits, sleep duration, work pressure, and family history of mental illness show patterns that could influence depression.
Work hours exhibit a wide range, but the relationship with depression is less obvious and might require deeper modeling to uncover insights.
""")

# Parágrafo 3 - Estratégia de Machine Learning
st.write("""
Given the nature of the target variable (depression) and the class imbalance, a Zero-Inflated Poisson Regression (ZIP) model could be suitable. 
This approach can account for the overrepresentation of zeros (i.e., individuals without depression) and model the count nature of the data effectively.
The ZIP model will allow us to analyze both the occurrence of depression (binary component) and the underlying predictors that contribute to its frequency or severity.
""")
