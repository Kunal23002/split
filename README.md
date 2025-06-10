# split
cba to split bills manually after going out 

# Split App

A user-friendly web application for splitting bills and expenses among friends. Built with Streamlit, this app makes it easy to track shared expenses and calculate how much each person owes.

## Features

- **Add/Remove People**: Easily manage the list of people sharing expenses
- **Track Food Items**: Add food items with their prices
- **Assign Items to People**: Select which people shared each food item
- **Automatic Calculations**: Automatically calculates how much each person owes
- **Real-time Updates**: See changes immediately as you add or remove items
- **Error Handling**: Robust error handling for all operations
- **Session Management**: Maintains state between interactions

## Technical Stack

- **Frontend**: Streamlit
- **State Management**: Streamlit Session State
- **Error Handling**: Python Exception Handling
- **Data Structures**: Python Dictionaries for efficient data management

## Prerequisites

- Python 3.x
- Streamlit
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd split_app
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv virt
source virt/bin/activate  # On Windows: virt\Scripts\activate
```

3. Install dependencies:
```bash
pip install streamlit
```

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Access the application at `http://localhost:8501`

## Usage Guide

1. **Adding People**:
   - Enter a name in the "Enter name" field
   - Click "Add Person"
   - Repeat for all participants

2. **Adding Food Items**:
   - Enter the food item name
   - Enter the price
   - Click "Add Food Item"

3. **Assigning Items to People**:
   - For each food item, select the people who shared it
   - Click "Add?" to confirm the selection

4. **Calculating Splits**:
   - Click "Calculate total" to see how much each person owes
   - The app will automatically divide the cost among selected people

## Project Structure

```
split_app/
├── streamlit_app.py    # Main application file
├── logic.py           # Core business logic
├── ui.py             # UI components
├── app.py            # Application entry point
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Data Management

The app uses Streamlit's session state to manage three main data structures:

1. **People Dictionary**: Tracks participants and their owed amounts
2. **Food Prices Dictionary**: Stores food items and their prices
3. **Prices List Dictionary**: Maps food items to the people who shared them

## Error Handling

The application includes comprehensive error handling for:
- Invalid inputs
- Missing data
- Key errors
- General exceptions

## Contributing

Feel free to submit issues and enhancement requests!

## Future Enhancements

- Export functionality for calculations
- Multiple bill support
- Tax and tip calculations
- Payment tracking
- History of previous splits 
