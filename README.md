# Web Scraper of Financial Data

## Project Description

**Web Scraper of Financial Data** is a program that collects historical USD exchange rates from multiple banks in Ukraine, including PrivatBank and OshadBank. It uses the Selenium library to scrape data from the website **https://minfin.com.ua/ua/currency/banks/**, predicts currency fluctuations using linear regression, stores the data in a file, and generates visual graphs for better understanding.

This project demonstrates the USD exchange rate in Ukraine over annual periods, allows forecasting of future exchange rates, and provides the ability for users to view and update the data.

---

## Key Features

1. **Data Collection**: The program collects USD exchange rates for multiple banks (PrivatBank, OshadBank) over a user-defined period.
2. **Currency Forecast**: Using linear regression, the program predicts future exchange rates based on the historical data.
3. **Data Storage**: All collected data is saved in a text file `curr_data.txt` for later use.
4. **Visualization**: The program visualizes the historical exchange rates and forecasts using graphs, making it easier to interpret the data.
5. **User Interaction**: A simple command-line interface (CLI) allows the user to:
   - Forecast exchange rates for selected banks.
   - Display the graphical representation of the exchange rates.
   - Update the data for different time periods.

**Note**: The program does not support scraping data from PUMB (Privatbank, OshadBank, PUMB), as the bank's data appears at different positions on the website on different dates, causing issues with the XPath query.

---

## Functions

### 1. `find_k_b(a)`

This function performs linear regression to calculate the slope (`k`) and y-intercept (`b`) of the best-fit line for the data.

#### Parameters:
- `a`: List of exchange rate values.

#### Returns:
- `k`: The slope of the regression line.
- `b`: The y-intercept of the regression line.

---

### 2. `get_and_store_data()`

This function prompts the user to enter a date range and scrapes the USD exchange rates from **minfin.com.ua** for the specified period. It saves the collected data to a text file and returns the data in the form of a list containing dates and corresponding exchange rates for the banks.

#### Returns:
- A list containing:
  - `date_list`: A list of dates.
  - `curr_usd_priv_list`: A list of USD exchange rates from PrivatBank.
  - `curr_usd_oshad_list`: A list of USD exchange rates from OshadBank.

---

### 3. `graphic(data)`

This function generates a graph of the historical exchange rates for PrivatBank and OshadBank, along with their predicted future rates based on linear regression.

#### Parameters:
- `data`: A list containing the collected data (dates, PrivatBank rates, OshadBank rates).

#### Output:
- Displays a line graph with:
  - A line for PrivatBank's USD exchange rates.
  - A line for OshadBank's USD exchange rates.
  - Forecasted values for both PrivatBank and OshadBank based on the regression model.

---

### 4. Main Program Flow

The program offers a simple CLI with the following options:
1. **Forecast currency for a bank**: Predict the next currency rate for PrivatBank or OshadBank using linear regression.
2. **Show graphic**: Display a graphical representation of the exchange rate data.
3. **Update data**: Allow the user to fetch updated data for a specific date range.
4. **Exit**: Exit the program.

The program prompts the user until a valid choice is made. In case of any errors during data collection or processing, the program raises an exception with an error message.

---

## Requirements

1. **Python 3.x**
2. **Libraries**:
   - `matplotlib` (for plotting graphs)
   - `selenium` (for web scraping)
   - `datetime` (for handling dates)

3. **Chromedriver**: You need to install [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) to interact with Chrome for scraping.

---

## Usage

1. Install the required libraries:
    ```bash
    pip install matplotlib selenium
    ```

2. Make sure that **chromedriver** is installed and added to your system's PATH.

3. Run the script:
    ```bash
    python financial_data_scraper.py
    ```

4. Follow the instructions in the CLI to forecast currency, view graphics, or update the data.

---

## Example Output

1. Forecast currency for bank
2. Show graphic
3. Update data
4. Exit


---

## Notes

- The program currently supports scraping data for USD exchange rates from **PrivatBank** and **OshadBank** only. The code for **PUMB** has been commented out because the bank's data appears at different positions on the page on different dates, making it difficult to scrape reliably.
- The forecasting is based on linear regression, which assumes a linear trend in the data. This method may not always be accurate for predicting real-world financial trends.
- The program handles exceptions and will notify the user in case of errors during the data collection process.

---
