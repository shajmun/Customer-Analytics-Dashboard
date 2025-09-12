# Customer Analytics Dashboard for Brazilian E-Commerce

### [View the Live Interactive Dashboard on Tableau Public](https://public.tableau.com/authoring/OlistCustomerAnalyticsDashboard/Dashboard1#1)

---

## 1. Project Overview
This project is an end-to-end analysis of the Olist e-commerce dataset. The primary goal is to explore customer and sales data to uncover key insights into customer distribution, sales trends, and shipping performance. The final output is a fully interactive dashboard built in Tableau that allows for easy data exploration.

---

## 2. Tech Stack
* **Database:** SQLite
* **Data Extraction:** SQL
* **Data Analysis & Cleaning:** Python (Pandas)
* **Data Visualization:** Tableau
* **Necessary Data:** [Data](https://drive.google.com/drive/folders/1t_9tf264QpWWFYv4NMBmxdRkVIbJ8AGj?usp=sharing)

---

## 3. Project Workflow
1.  **Data Extraction (SQL):** An initial dataset was created by running a SQL query with an `INNER JOIN` on a local SQLite database (`Olist_Store.db`) to combine customer and order information.
2.  **Data Cleaning (Python):** Using the Pandas library, the script performs essential cleaning tasks, such as converting all date-related columns from text to a proper `datetime` format.
3.  **Feature Engineering (Python):** A new feature, `shipping_time`, is calculated to analyze logistics performance.
4.  **Data Export:** The final, cleaned DataFrame is saved as `cleaned_olist_data.csv`, ready for visualization.
5.  **Dashboarding (Tableau):** The cleaned data is connected to Tableau to build an interactive dashboard featuring a geographic map of customers and a sorted bar chart of customer counts by state.

---

## 4. Dashboard Preview
![Olist Customer Analytics Dashboard](https://public.tableau.com/authoring/OlistCustomerAnalyticsDashboard/Dashboard1#1)
<img width="858" height="710" alt="dashboard_screenshot" src="https://github.com/user-attachments/assets/80841863-a144-428f-a2eb-8e837b2131fb" />


---

## 5. How to Reproduce
1.  Clone or download this repository.
2.  Open the `Olist_Store.db` file to view the database.
3.  Alternatively, run the `main.py` script to regenerate the `cleaned_olist_data.csv` file.
4.  Open Tableau and connect to `cleaned_olist_data.csv` to explore the data or rebuild the dashboard.
