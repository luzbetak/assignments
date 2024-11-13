REQUIREMENTS
============

## DAE Work Sample Instructions

### Scenario:
A new data asset has been acquired from an external vendor. This dataset is untested and may or may not be ready for analysis. You are tasked with doing initial data exploration on the data and are to assist a data scientist with preparing the data for modeling.

**NOTE:** This is all fabricated data. Any similarity to real data is coincidental. The provided files are only to be used for the purpose of this exercise. Do not post or share these files or your work.

### Before Starting:
- Steps 1 and 2 should be done entirely in a Jupyter notebook with code and output together.
- Code comments are encouraged.
- All tables can join with a one-to-one relationship.
- The output dataset should only include cleaned results. Verify that the data contents are expected, and account for any anomalies in the output dataset.
- All reasoning should be documented in a markdown cell.
- Questions should be answered in a markdown cell below the code used to justify the answer.
- In Step 2, rounding in any form is discouraged.
- For Step 3, you may use a text editor of your choice.
- Write-ups and communications should be formatted for easy understanding by the reader (complete sentences, paragraphs, etc.). File formats can include .txt, .doc, or .docx.
- Any reasoning should be documented along with your answers.
- All necessary components to complete this exercise are contained in this docker image: `jupyter/all-spark-notebook:x86_64-spark-3.5.0`.

### Instructions:

#### Step 1: Data Engineering
In a Jupyter notebook titled "Data Engineering", please combine the three provided CSV files into one data frame, using either Spark or Pandas.

- The goal is to create one dataset that can be used for analysis and for model training.
- Be sure to clean up any artifacts that may persist from importing CSV files.
- Provide the schema of your final output along with a record count in the last cell(s) of your Jupyter notebook.
- Save your final results in parquet format, to be used in the remaining steps.

#### Step 2: Data Analysis
In a Jupyter notebook titled "Data Analysis", answer the following questions. Answers should be given for active households:

1. What is the average number of cars per household?
2. How many cars are there by model year?
3. How many cars are there by make?
4. Which cars are the safest? What variables did you consider to define “safe”?
5. Which states have the largest households (defined as number of customers in a household)?
6. How many active households are there as of 1/1/2021?
7. What is the average age of customers?
8. How much does age vary by region?
9. Which age group has the most expensive claims?

#### Step 3: Training Data Preparation
In a document titled "Training Prep", answer the following questions as they relate to your data research in Steps 1 and 2. You may use any text editor of your choice.

- Are there any insights or interesting findings in the data that would be important to share with your data scientist partner?
- What strategy did you use for dealing with the missing and duplicate data?
- Thinking about this from an insurance standpoint, what additional features would you like to add to this data?
- What features (if any) would you recommend removing from the final data set? Why?

### Step 4: Submission
Please submit the following files back to us. Do not clear the output in your Jupyter notebook files.

- The `Data Engineering.ipynb` notebook as described in Step 1.
- The `Data Analysis.ipynb` notebook as described in Step 2.
- The `Training Prep` document as described in Step 3.

Include all requested files in a single `.zip` file, along with a list of attachments so we can verify that we have received everything. All code must be submitted as an email attachment.

**Note:** 
- Do not submit your files via a shared cloud drive (e.g., Google Drive, Dropbox).
- Do not submit your resulting dataset, parquet file, or the original data back to us.
- Do not include your name in the body of the documents or in any of the file names.
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

