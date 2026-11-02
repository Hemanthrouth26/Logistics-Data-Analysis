# Logistics Data Analysis | Delivery Performance & Predictive Optimization

<p align="center">
  <strong>Python • Data Analytics • Exploratory Data Analysis • Machine Learning</strong>
</p>

## Project Overview

Logistics Data Analysis is an end-to-end data analytics project focused on understanding shipment performance, identifying delivery delays, analyzing transportation costs, and predicting delivery duration using machine learning techniques.

The project demonstrates how Python-based analytics can help logistics organizations improve operational efficiency, monitor key performance indicators, and make data-driven decisions.

This project was developed as part of the **YuvaIntern – Logistics Data Analyst Internship (4 Weeks)**.

The project follows a structured workflow covering strategic planning, data collection, data preprocessing, exploratory data analysis, visualization, predictive modeling, and optimization recommendations.

## Project Objectives

- Analyze shipment and logistics performance.
- Identify factors influencing delivery delays.
- Clean and preprocess logistics datasets.
- Perform Exploratory Data Analysis (EDA).
- Analyze transportation costs and delivery trends.
- Predict shipment delivery duration using machine learning.
- Recommend strategies to improve logistics efficiency.

## Technologies & Tools

| Technology | Application |
|---|---|
| Python | Data analysis and programming |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| Jupyter Notebook | Data analysis environment |
| Git & GitHub | Version control |

## Project Structure

```text
Logistics-Data-Analysis/
│
├── Logistics Data Analysis/
│   │
│   ├── Week 1 - Strategic Planning/
│   │   └── Week_1_Report.docx
│   │
│   ├── Week 2 - Data Preprocessing/
│   │   └── Week_2_Report.docx
│   │
│   ├── Week 3 - EDA and Visualization/
│   │   ├── Week_3_Report.docx
│   │   └── Visualizations/
│   │
│   ├── Week 4 - Predictive Modeling/
│   │   └── Week_4_Report.docx
│   │
│   ├── Dataset/
│   │   └── logistics_simulated_dataset.csv
│   │
│   └── Python_Code/
│       └── logistics_analysis.py
│
└── README.md
```

*Note: Update the folder and file names in this structure to match the actual uploaded files.*

## Four-Week Project Implementation

### Week 1: Strategic Planning and Data Exploration

**Objective:** Define the logistics problem and establish an analytical strategy.

Key activities:
- Defined a hypothetical logistics delivery scenario.
- Identified operational challenges.
- Established important Key Performance Indicators (KPIs).
- Explored data science methodologies.
- Designed an end-to-end analytical roadmap.

**Key Performance Indicators:**
- On-Time Delivery Rate
- Average Delivery Time
- Average Shipping Cost
- Delivery Delay Rate
- Cost per Kilometre

### Week 2: Data Collection, Cleaning and Preprocessing

**Objective:** Prepare a reliable dataset for analysis and machine learning.

Key activities:
- Simulated logistics dataset collection.
- Identified missing values and duplicate records.
- Applied median and mode imputation.
- Detected potential outliers using the IQR method.
- Applied standardization and categorical encoding.
- Prepared the dataset for further analysis.

### Week 3: Exploratory Data Analysis and Visualization

**Objective:** Identify patterns, trends, and relationships in logistics data.

Key activities:
- Performed descriptive statistical analysis.
- Analyzed delivery time distributions.
- Compared average delivery duration across shipping modes.
- Examined regional transportation costs.
- Studied correlations between numerical variables.
- Generated visualizations using Matplotlib and Seaborn.

**Visualizations included:**
- Delivery Time Distribution
- Average Delivery Time by Shipping Mode
- Average Shipping Cost by Region
- Correlation Matrix

### Week 4: Predictive Modeling and Optimization

**Objective:** Predict shipment delivery duration and recommend operational improvements.

Key activities:
- Defined delivery-time prediction as a regression problem.
- Selected Random Forest Regression.
- Performed feature selection and preprocessing.
- Trained and tested the machine learning model.
- Evaluated model performance.
- Proposed logistics optimization strategies.

## Dataset Description

The project uses a simulated dataset containing **2,400 shipment records**.

The dataset includes:

| Feature | Description |
|---|---|
| Shipment_ID | Unique shipment identifier |
| Region | Shipment operating region |
| Shipping_Mode | Delivery service category |
| Distance_km | Shipment distance |
| Shipment_Weight_kg | Shipment weight |
| Order_Quantity | Number of ordered items |
| Weather | Weather conditions |
| Traffic_Level | Traffic conditions |
| Scheduled_Delivery_Days | Expected delivery duration |
| Actual_Delivery_Days | Actual delivery duration |
| Shipping_Cost_USD | Transportation cost |

**Dataset Reference:** [DataCo Smart Supply Chain Dataset – Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

The DataCo dataset is used as a reference for logistics data structure. The dataset used in this project is independently simulated for educational purposes.

## Machine Learning Model

**Algorithm:** Random Forest Regressor

**Problem Type:** Supervised Machine Learning – Regression

**Target Variable:** Actual_Delivery_Days

**Input Features:**
- Region
- Shipping Mode
- Distance
- Shipment Weight
- Order Quantity
- Weather
- Traffic Level
- Scheduled Delivery Days

### Model Performance

The model was evaluated using the following metrics on a held-out test dataset:

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 0.479 days |
| Root Mean Squared Error (RMSE) | 0.597 days |
| R² Score | 0.605 |

**Interpretation:**

- MAE measures the average absolute prediction error.
- RMSE gives greater weight to larger prediction errors.
- R² measures how much variation in delivery duration is explained by the model.

*These are experimental results from the simulated dataset and should not be interpreted as real-world logistics performance.*

## Business Insights & Recommendations

The analytical framework supports the following recommendations:

1. **Delivery Monitoring:** Monitor shipments that are predicted to exceed scheduled delivery times.
2. **Route Optimization:** Investigate routes associated with consistently longer delivery durations.
3. **Cost Management:** Analyze transportation costs across regions and shipping modes.
4. **Resource Allocation:** Allocate delivery capacity based on shipment priorities and predicted delivery risks.
5. **Performance Tracking:** Regularly monitor logistics KPIs to identify operational bottlenecks.

## Installation & Execution

### 1. Clone the repository

```bash
git clone https://github.com/Hemanthrouth26/Logistics-Data-Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Logistics-Data-Analysis
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 4. Run the Python script

```bash
python "Logistics Data Analysis/Python_Code/logistics_analysis.py"
```

Ensure that the dataset path in the script matches its actual location in your repository.

## Learning Outcomes

Through this project, I developed practical experience in:

- Python programming for data analytics.
- Data collection and preprocessing.
- Exploratory Data Analysis.
- Statistical analysis and visualization.
- Regression-based machine learning.
- Model evaluation techniques.
- Logistics and supply chain performance analysis.
- Translating analytical findings into business recommendations.

## Project Information

| Detail | Information |
|---|---|
| Project | Logistics Data Analysis |
| Organization | YuvaIntern |
| Internship Role | Logistics Data Analyst Intern |
| Duration | 4 Weeks |
| Mode | Virtual |
| Domain | Logistics & Supply Chain Analytics |
| Programming Language | Python |
| Machine Learning Algorithm | Random Forest Regression |

## Developed By

**Routhu Hemanth**

- GitHub: [@Hemanthrouth26](https://github.com/Hemanthrouth26)
- Project Repository: [Logistics-Data-Analysis](https://github.com/Hemanthrouth26/Logistics-Data-Analysis)

## Disclaimer

This project was developed for educational and internship purposes. The dataset and model evaluation results are simulated. They do not represent actual company operational records or verified business savings.

---

<p align="center">
  <strong>Learning • Analyzing • Predicting • Optimizing</strong>
</p>
