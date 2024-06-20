# Blood Group Predictor

This is a simple web application that predicts the possible blood groups of a child based on the blood groups of the parents. The application is built using Flask for the backend, HTML and CSS for the frontend, and ReportLab for generating PDF reports.

## Features

- Input the blood groups of the mother and father to predict the possible blood groups of the child.
- Download the prediction results as a PDF.
- Responsive design with a clean user interface.
- Animated "Predict" button for enhanced user experience.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- ReportLab

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/blood-group-predictor.git
    ```
2. Change to the project directory:
    ```sh
    cd blood-group-predictor
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the blood groups of the mother and father in the provided fields and click the "Predict" button to see the possible blood groups of the child.

4. To download the prediction results as a PDF, click the "Download as PDF" button on the results page.

## Project Structure

- `static/`: Contains static files such as CSS and images.
- `templates/`: Contains HTML templates for rendering the web pages.
- `app.py`: The main Flask application file.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
