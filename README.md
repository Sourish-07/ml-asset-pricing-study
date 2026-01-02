This project studies short horizon stock return predictability using large scale daily equity data and standard machine learning models.

I constructed a unified panel of U.S. equities by processing raw daily price files into a clean return dataset containing over fourteen million observations. The pipeline includes price validation, return construction, lagged feature generation, and volatility estimation.

The primary goal of this project is not to claim strong predictability of daily returns, but to empirically evaluate how much signal remains after standard preprocessing and feature engineering. This mirrors the central challenge in modern asset pricing, where noise dominates at short horizons.

Data Construction

Raw daily price files were aggregated into a single panel and cleaned for missing values and structural issues. Daily returns were computed at the stock level. I then constructed lagged return features at one, five, and twenty day horizons along with rolling twenty day volatility estimates.

Models

I evaluated two baseline models commonly used in empirical finance and machine learning.

A linear regression model serves as a benchmark for linear predictability.

A random forest model captures potential nonlinear interactions between lagged returns and volatility.

Models were evaluated out of sample using mean squared error and R squared.

Results

Both models produced negative out of sample R squared values, with the random forest outperforming the linear model in terms of error reduction. This outcome is consistent with prior research showing that short horizon equity returns are difficult to predict even with flexible nonlinear models.

Rather than treating this as a failure, the results reinforce a key lesson in asset pricing: apparent in sample patterns often fail to generalize, and careful evaluation is essential.

Structure

scripts contains data processing pipelines
notebooks contains the modeling and analysis notebook
results contains model evaluation outputs
figures contains feature importance visualizations