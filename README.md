# VTOP Login Automator

This project provides a Python script to automate the login process for the VIT (Vellore Institute of Technology) student portal, VTOP. It uses Playwright to control a web browser, enter user credentials, and handle the captcha.

## Features

-   **Automated Login:** Automatically navigates to the VTOP login page and enters your credentials.
-   **Captcha Handling:** Prompts the user to manually enter the captcha displayed on the page.
-   **Dashboard Screenshot:** Takes a screenshot of the user's dashboard after a successful login and saves it as `dashboard.png`.
-   **Modern Automation:** Built with `playwright` for reliable and modern browser automation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.7+
-   `pip` (Python package installer)

### Installation & Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Raghavvram/vtop-automation-playwrite.git
    cd vtop-automation-playwrite
    ```

2.  **Create and activate a virtual environment:**
    -   **Linux/macOS:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    -   **Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Playwright browsers:**
    Playwright requires browser binaries to be installed. Run the following command to install them:
    ```bash
    playwright install
    ```
    This will download the necessary browser executables for Chromium, Firefox, and WebKit.

## Usage

1.  Make sure you are in the project directory and your virtual environment is activated.

2.  Run the script from your terminal:
    ```bash
    python login_automator_new.py
    ```

3.  The script will open a browser window and navigate to the VTOP login page.

4.  In your terminal, you will be prompted to enter your username, password, and the captcha visible on the browser page.

5.  After you enter the required information, the script will attempt to log in.

6.  If the login is successful, a screenshot named `dashboard.png` will be saved in the project directory, and the script will exit.

## How It Works

The script uses the `playwright` library to perform the following steps:
1.  Launches a new Chromium browser instance.
2.  Navigates to the VTOP login page: `https://vtop.vit.ac.in/vtop/vtopLogin`.
3.  Waits for the page to load completely.
4.  Prompts the user for their credentials and the captcha.
5.  Fills the username, password, and captcha fields on the webpage.
6.  Clicks the "Login" button.
7.  Waits for the dashboard to load after successful login.
8.  Captures a screenshot of the dashboard.
9.  Closes the browser.

## Dependencies

This project relies on the following Python libraries:

-   `beautifulsoup4==4.12.3`: For parsing HTML and XML documents.
-   `lxml==5.2.2`: A high-performance XML and HTML parsing library.
-   `playwright==1.46.0`: For browser automation.
-   `requests==2.32.3`: For making HTTP requests (though `playwright` handles most of this).

These are all listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have ideas for improvements or have found a bug, please open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m '''Add some AmazingFeature'''`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. (Note: You will need to create a `LICENSE` file if you wish to include one).
