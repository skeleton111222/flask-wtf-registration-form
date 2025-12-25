# Flask-WTF Registration Form

This is a simple Flask application that demonstrates the use of Flask-WTF for form handling. It includes a registration form with various fields, such as name, email, password, gender, and country selection. The form also includes a checkbox for agreeing to terms and conditions. On form submission, the data is validated, and a success message is displayed.

## Project Structure

```

flask-wtf-registration-form/
│
├── .gitignore
├── .env
├── app.py # Main Flask application
├── requirements.txt # List of Python dependencies
├── templates/ # HTML templates
│ └── register.html # Registration form
├── static/ # Static files
│ └── style.css # Form styling
└── README.md # Project documentation

````

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/skeleton111222/flask-wtf-registration-form.git
    cd your-flask-app
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # For Linux/Mac
    venv\Scripts\activate       # For Windows
    ```

3. **Install dependencies**:
    Use the `requirements.txt` file to install the necessary libraries.
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**:
    You can generate a random secret key using the following Python code:
    ```python
    import secrets
    print(secrets.token_hex(16))
    ```
    
5. **Run the Flask application**:
    ```bash
    python app.py
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000/` to view the registration form.

## How the Application Works

- When you visit the main page, a registration form is displayed.
- The form fields include:
    - **Name**: Text field (required)
    - **Email**: Email field (required, must be a valid email address)
    - **Password**: Password field (required)
    - **Gender**: Radio buttons for Male/Female selection
    - **Country**: Dropdown menu for country selection (Nepal, India)
    - **Agree to terms**: Checkbox (required)
- Upon submitting the form, the server validates the data and displays a success message if everything is correct.

## Dependencies

This project requires the following Python libraries:

- **Flask**: A micro web framework for Python.
- **Flask-WTF**: An extension for Flask that simplifies working with forms.
- **WTForms**: A flexible forms library.
- **python-dotenv**: A library to load environment variables from a `.env` file.

Install the dependencies by running:

```bash
pip install -r requirements.txt
````
