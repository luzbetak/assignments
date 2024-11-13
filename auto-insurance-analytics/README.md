# Combined Dataset Preparation

This project combines data from three CSV files (`CARS.csv`, `CUSTOMERS.csv`, and `HOUSEHOLDS.csv`) into a single, cleaned dataset for analysis and model training.

## Project Overview

The goal of this project is to merge data from three distinct CSV files into one comprehensive dataset. The combined dataset will be cleaned and prepared for further analysis and machine learning model training.

### Input Files

1. **CARS.csv**
   - Contains details about vehicles, including `Car ID`, `Status`, `State`, `Model Year`, `Make`, `Body Style`, `Vehicle Value`, and insurance-related details.

2. **CUSTOMERS.csv**
   - Contains customer information, including `CUST_ID`, `Date of Birth`, `Marital Status`, `Employment Type`, and `Income`.

3. **HOUSEHOLDS.csv**
   - Contains household-related information, including `HH_ID`, `CUST_ID`, `CAR_ID`, `Active HH`, `HH Start Date`, `Phone Number`, `ZIP`, `State`, `Country`, and `Referral Source`.

### Steps to Combine and Clean the Data

1. **Load CSV Files**: Each of the three CSV files is loaded into a separate Pandas DataFrame.

2. **Merge DataFrames**:
   - The `HOUSEHOLDS.csv` file is merged with `CUSTOMERS.csv` on the `CUST_ID` key.
   - The resulting DataFrame is then merged with the `CARS.csv` file on the `CAR_ID` key.

3. **Clean the Data**:
   - Any duplicate columns that arise from the merge (e.g., `Car ID` and `CAR_ID`) are removed.
   - Rows or columns that are entirely NaN (empty) are dropped to ensure a clean dataset.
   - Indexes are reset to maintain data integrity.

4. **Save the Combined Data**:
   - The final cleaned dataset is saved as `combined_dataset.csv`.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library

### Running the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd your-repository-name
    ```

3. Place 
