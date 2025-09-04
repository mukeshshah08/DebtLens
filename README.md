# DebtLens
This project leverages World Bank’s International Debt Statistics dataset to analyze debt patterns across nations from 1970 to the present. Using data science techniques, we perform exploratory analysis, statistical insights, clustering, and predictive modeling to understand global debt dynamics and provide actionable insights for policymakers.
# Global Debt Analysis using World Bank Data

This project analyzes global external debt using the World Bank International Debt Statistics (IDS) dataset.
![Uploading newplot (1).png…]()
<img width="1797" height="525" alt="newplot" src="https://github.com/user-attachments/assets/e7e98e46-127b-4fad-8976-79571023416a" />


## Content![Uploading newplot.png…]()
s
- `debt_analysis_notebook.ipynb` : Jupyter Notebook with full pipeline (fetch data, EDA, clustering, regression, ARIMA forecasting, visualizations)
- `streamlit_debt_dashboard.py` : Streamlit dashboard to visualize debt data interactively
- `processed_debt.csv` : Generated CSV after running the notebook (contains Debt, GDP, Debt-to-GDP ratios)
- `requirements.txt` : Python dependencies for easy setup

## How to Run

### Google Colab
1. Open [Google Colab](https://colab.research.google.com).
2. Upload `debt_analysis_notebook.ipynb`.
3. Run cells top-to-bottom. Internet access is required to fetch World Bank data.
4. After preprocessing, `processed_debt.csv` will be generated in Colab.

### Local Machine
1. Create & activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:
   ```bash
   jupyter notebook debt_analysis_notebook.ipynb
   ```
4. Run Streamlit dashboard:
   ```bash
   streamlit run streamlit_debt_dashboard.py
   ```

## Notes
- The notebook fetches data from World Bank API (https://data.worldbank.org/indicator/DT.DOD.DECT.CD).
- If API requests fail, ensure your internet is active and the URL uses HTTPS.
