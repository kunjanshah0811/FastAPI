# FastAPI Prediction Service

This is a simple FastAPI application that provides a prediction endpoint based on a rule-based demo model.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Visit `http://127.0.0.1:8000/predicttt` in your browser or send a GET request with parameters `age` and `sex`.

## Prediction Endpoint

### URL
