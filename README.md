# Location-Based Recommendation System

This project implements a location-based recommendation system for cities in India. It utilizes geographical clustering and geocoding to recommend cities similar to a user-specified city based on their coordinates.

## Features

- **Geocoding:** Uses the `geopy` library to fetch latitude and longitude for each city listed in the dataset.
- **Clustering:** Applies K-Means clustering to group cities based on their geographical coordinates.
- **Recommendation:** Recommends cities in the same cluster as a user-provided city, excluding the input city itself.
- **Visualization:** Optional visualization of city clusters using matplotlib.

## Usage

1. **Setup:**
   - Ensure Python 3.x is installed along with necessary libraries (`pandas`, `geopy`, `scikit-learn`, `matplotlib`).

2. **Data Preparation:**
   - Prepare a CSV file (`locations (1).csv`) containing a list of cities in India with their names.

3. **Running the Code:**
   - Open the notebook or script in your preferred environment (e.g., Jupyter Notebook, Google Colab, VS Code).
   - Execute the code cells or script to load data, perform clustering, and recommend cities.

4. **Interacting with the System:**
   - Enter a city name when prompted to receive recommendations for similar cities.
   - View the recommended cities based on geographical clustering.

## Example

```python
# Example usage in Python script or notebook
# Ensure 'locations (1).csv' is correctly formatted with city names


## Dependencies

- Python 3.x
- `pandas`, `geopy`, `scikit-learn`, `matplotlib`

## Future Improvements

- Incorporate real-time data for weather, population, and other factors.
- Enhance user interface for better interaction and feedback.
- Implement multi-criteria recommendation system based on user preferences.
