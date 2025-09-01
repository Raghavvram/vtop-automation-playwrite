import requests
import base64
from playwright.sync_api import sync_playwright
import time

CAPTCHA_URL = "https://cap.va.synaptic.gg/captcha"

def solve_captcha_with_original_logic(captcha_src_string: str):
    """
    Sends the CAPTCHA data to the solving service using the original double-encoding logic.
    """
    try:
        print("Attempting to solve CAPTCHA automatically...")
        img_string = base64.urlsafe_b64encode(captcha_src_string.encode()).decode()
        
        response = requests.post(CAPTCHA_URL, json={"imgstring": img_string})
        response.raise_for_status()
        solution = response.text
        print(f"✅ CAPTCHA service returned solution: '{solution}'")
        return solution
        
    except requests.RequestException as e:
        print(f"❌ Error calling CAPTCHA solver API: {e}")
        return None

def run_login_automation():
    # --- 🔒 HARDCODE YOUR CREDENTIALS HERE ---
    username = "22BCEXXXX"  # Replace with your actual username
    password = "Password"  # Replace with your actual password
    # -----------------------------------------

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        try:
            print("Navigating to https://vtop.vitap.ac.in/vtop/login...")
            page.goto("https://vtop.vitap.ac.in/vtop/login")

            print("Looking for the 'Student' card to click...")
            page.locator('form#stdForm a').click()
            print("Clicked on the 'Student' card.")
            
            print("Waiting for the login page to load...")
            page.wait_for_selector("#username", timeout=10000)
            print("Login page loaded. Using hardcoded credentials.")

            page.locator("#username").fill(username)
            page.locator("#password").fill(password)

            print("Finding CAPTCHA image on the page...")
            captcha_img_src = page.locator("img.img-fluid").get_attribute("src")

            if not captcha_img_src or 'base64,' not in captcha_img_src:
                raise Exception("Could not find the CAPTCHA image source code.")
            
            captcha_solution = solve_captcha_with_original_logic(captcha_img_src)

            if not captcha_solution:
                 raise Exception("Failed to get a solution from the CAPTCHA service.")

            page.locator("#captchaStr").fill(captcha_solution)

            # --- ADDED TIME DELAY ---
            # Wait for 1 second (1000 milliseconds) to allow any client-side
            # validation scripts on the page to run before clicking submit.
            print("Pausing for 10 second before submission...")
            page.wait_for_timeout(10000)
            # ------------------------

            print("Submitting login form...")
            page.locator("#submitBtn").click()

            print("\n✅ Login attempt finished. Check the browser to see the result.")
            input("Press Enter to close the browser...")

        except Exception as e:
            print(f"\n❌ An error occurred during the login process: {e}")
            input("Press Enter to close the browser...")

        finally:
            browser.close()

run_login_automation()
