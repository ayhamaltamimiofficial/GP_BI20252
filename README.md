# Business Intelligence Graduation Project Template

**University of Petra, Graduation Projects, Business Intelligence, 20252**

---

## How to Use This Template

This repository serves as a **template for Business Intelligence graduation projects**. Students should **fork this repository** and use it as the foundation for their project work. All project-related files and documentation should be organized within this single repository.

### For Students: Quick Start
1. **Fork this repository** (Click on **Use this template** then **Create new repository** button in the top right corner) to fork your own copy.

![use-this-template](images/use-template.png)

2. **Clone your fork** to your local machine
3. **Follow the sections below** to structure your project documentation in markdown format
4. **Push your work** regularly to track progress

---

## Project Structure

```
# Analyzing the Impact of Economic Indicators on Unemployment Rates Using Neural Networks: A Case Study of Jordan and Selected Arab Countries

**University of Petra | Faculty of Administrative and Financial Sciences** **Department of Business Intelligence and Data Analytics** ---

##  Project Overview & Authors
* **Course:** 307498 – Graduation Project
* **Semester:** Second Semester, 2025/2026
* **Prepared by:** Ayham Altamimi
* **Supervised by:** Prof. Ayman Mansour
* **Date:** June 2026

---

##  Abstract
This study aims to analyze the relationship between multi-dimensional economic indicators and unemployment rates in Jordan, alongside a comparative analysis of selected Arab countries, including Egypt, Lebanon, Morocco, and Tunisia. Given the increasing economic challenges in the region, understanding the drivers of unemployment is crucial for informed policymaking. 

The research utilizes a Business Intelligence (BI) approach, leveraging a longitudinal dataset of 21 variables sourced from the World Bank (1960–2025). Central to this study is the implementation of advanced Artificial Intelligence (AI) algorithms, specifically Artificial Neural Networks (ANN), to identify complex, non-linear patterns and predict future unemployment trends. These indicators encompass macroeconomic factors such as GDP growth, Inflation, and FDI, as well as structural drivers including High-Technology Exports, ICT services, and Energy Imports. By employing Machine Learning (ML) techniques, the model achieved a predictive accuracy of **79.87%**, providing a robust data-driven foundation to support sustainable economic strategies and forward-looking governance in the Hashemite Kingdom of Jordan.

---

##  Repository Project Structure
The files and deployment artifacts in this repository are structured as follows:
Analyzing-Unemployment-BI/
__ README.md                 # Project executive summary & overview (This File)
 requirements.txt          # Python dependencies (Pandas, Scikit-Learn, etc.)
── .gitignore                # Git configuration file to exclude local cache
── docs/

│   └── documentation.md      # Full Graduation Project Chapters & Technical Report
── data/
│|___   ├── raw/                  # Original longitudinal dataset extracted from World Bank
│   └── processed/            # Normalized and cleaned economic data for ANN input
── notebooks/                # Jupyter Notebooks containing Exploratory Data Analysis (EDA)
── src/

│   └── app.py                # Python source code for training & optimizing the ANN model
└── dashboards/

└── Unemployment_BI.pbix  # Completed Power BI Interactive Dashboard file


---

##  Table of Contents & Quick Links
The full detailed report is fully documented in Markdown format inside the **[docs/documentation.md](docs/documentation.md)** file. Click on any section below to navigate directly to the comprehensive content:

1.  [Title Page & Authors](docs/documentation.md#title-page-authors)
2.  [Abstract](docs/documentation.md#abstract)
3.  [Acknowledgment](docs/documentation.md#acknowledgment)
4.  [Business Intelligence Project Description and Objectives](docs/documentation.md#business-intelligence-project-description-and-objectives)
5.  [Data Research and Acquiring Effort](docs/documentation.md#data-research-and-acquiring-effort)
6.  [Data Description and Understanding](docs/documentation.md#data-description-and-understanding)
7.  [Data Primary Cleaning and Transformation](docs/documentation.md#data-primary-cleaning-and-transformation)
8.  [Data Visualization and Insights](docs/documentation.md#data-visualization-and-insights)
9.  [Dashboard Design & Business Insights](docs/documentation.md#dashboard-design--business-insights)
10.  [Advanced Analytics and AI Modeling (ANN)](docs/documentation.md#advanced-analytics-and-ai-modeling)
11.  [Tools Research and Selection Effort](docs/documentation.md#tools-research-and-selection-effort)
12.  [Project Deployment Effort – Use Case](docs/documentation.md#project-deployment-effort-use-case)
13.  [Results & National Recommendations](docs/documentation.md#results)
14.  [References](docs/documentation.md#references)

---

##  Core Project Answers (Executive Brief)

### 1. Business Intelligence Project Description & Objectives
* **Domain:** Macroeconomics, Public Policy, and Predictive Analytics.
* **Problem Statement:** Traditional static economic models fail to capture non-linear interactions affecting unemployment spikes. This project decodes these complexities to prevent structural labor mismatches.
* **Strategic Objective:** To transition Jordan's policymaking from reactive methods into a proactive **"Continuous Intelligence"** model using AI and Interactive Visualizations.

### 2. Advanced Analytics & AI Modeling
* **Model Type:** Multilayer Perceptron (MLP) Artificial Neural Network (ANN).
* **Target Feature:** National Unemployment Rate.
* **Key Performance Metric:** Achieved an empirical predictive accuracy of **79.87%**.
* **Key Finding:** Synaptic weight evaluation highlighted **High-Technology Exports** and **ICT Service Exports** as the strongest structural anchors driving down systemic unemployment.

### 3. Toolchain Selection Effort
* **Data Engineering & AI Modeling:** `Python 3.10`, `Pandas`, `NumPy`, and `Scikit-Learn` for model execution and data ingestion.
* **Data Visualization & BI Layer:** `Power BI Desktop` for real-time descriptive dashboards and interactive policy questions exploration.

### 4. Deployment Use Case
* **Operational Execution:** The project provides a **Strategic Analytics Implementation for Economic Forecasting (SAIEF)** framework. National economic ministries can utilize the Power BI dashboard and automated Python pipelines to run live simulations and forecast quarterly labor shifts based on trade and industrial data updates.

---

##  Code Setup and Local Dependencies Execution
To run the Neural Network model and data processing scripts locally:

1. **Clone your repository fork:** ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
Navigate into the directory:

Bash
cd your-repository-name
Install dependencies:

Bash
pip install -r requirements.txt
Execute the core script:

Bash
python src/app.py
Developed as an official undergraduate milestone for the Department of Business Intelligence and Data Analytics at the University of Petra, 2026.
---

**Good luck with your Business Intelligence graduation project!** 
