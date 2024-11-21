# Road Accident Prediction System

The **Road Accident Prediction System** is a web-based application designed to help users predict the likelihood of road accidents based on specific factors such as location, time, vehicle load, and more. It integrates data from a CSV file into an SQLite database and provides a user-friendly interface for querying accident records.

## Features

- User authentication with secure password storage.
- Query accident records based on various conditions.
- Data visualization and result display for predictions.
- Easy-to-use web interface.

## Technologies Used

- **Python** (Flask for web application)
- **SQLite** (Database management)
- **Pandas** (Data processing)
- **HTML/CSS** (Frontend templates)
- **Werkzeug** (Password hashing)

## Prerequisites

1. Python 3.x installed.
2. Flask and other dependencies installed via `pip install -r requirements.txt`.
3. The `Road_Accidents.csv` file in the project directory.
4. SQLite for database management.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/road-accident-prediction.git
   cd road-accident-prediction
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000/
File Structure
app.py: Main application script.
config.py: Configuration file for Flask and database setup.
Road_Accidents.csv: Dataset used for predictions.
templates/: Contains HTML templates for the web interface.
static/: Contains CSS, JavaScript, and image assets.
Usage
Sign Up: Create a user account.
Log In: Access the dashboard.
Query Data: Enter state, time, and other parameters to search for accident records.
View Results: Check the retrieved accident data and details.
Database Initialization
The app.py script automatically initializes the SQLite database on startup. It reads the Road_Accidents.csv file and populates the database.

Future Enhancements
Integrate machine learning models for accident prediction.
Add support for data visualization (e.g., charts and graphs).
Extend the database schema for more detailed records.
License
This project is licensed under the MIT License.
