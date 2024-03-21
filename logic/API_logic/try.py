import requests
import json
from selenium import webdriver


def main():
    try:
        # Create a session
        session = requests.Session()

        # Define the URL to trigger the creation of session cookies
        trigger_url = 'https://parabank.parasoft.com/parabank/register.htm'
        loginEndPoint = 'https://parabank.parasoft.com/parabank/login.htm'

        # Make a preliminary request to trigger the creation of session cookies
        session.get(trigger_url)

        # Define the main URL and data
        url = 'https://parabank.parasoft.com/parabank/register.htm'
        data = {
            "customer": {
                "firstName": "Ahmd",
                "lastName": "Bdran",
                "address": {
                    "street": "0534266625",
                    "city": "ghajar village",
                    "state": "hazaffon",
                    "zipCode": "1244000"
                },
                "phoneNumber": "0534266625",
                "ssn": "123",
                "username": "ahmd2bdran",
                "password": "123"
            },
            "repeatedPassword": "123"
        }

        # Convert data to JSON
        json_data = json.dumps(data)

        # Now you can access the cookies from the session
        cookies_text = ""
        for cookie in session.cookies:
            cookies_text += cookie.name + "=" + cookie.value

        print("Cookies:", cookies_text)

        headers = {
            'Content-Type': 'application/json',
            'Cookie': cookies_text
        }

        headers = {
            "authority": "parabank.parasoft.com",
            "method": "POST",
            "path": "/parabank/register.htm",
            "scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",
            "Cache-Control": "max-age=0",
            "Content-Length": "308",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": cookies_text,
            "Origin": "https://parabank.parasoft.com",
            "Referer": "https://parabank.parasoft.com/parabank/register.htm",
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }

        # Make the request
        response = session.post(url, data=json_data, headers=headers)

        # Print response status
        print("Response Status:", response.status_code)

        login_data = {
            'username': 'ahmdbdran1',
            'password': '123'

        }
        json_login_data = json.dumps(login_data)

        # Make the request
        response = requests.post(loginEndPoint, data=json_login_data)
        print(response)

        # Now, initialize Selenium WebDriver with the same session cookies
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("ignore-certificate-errors")
        options.add_argument("disable-infobars")

        # Set cookies in Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(url)
        for cookie in session.cookies:
            driver.add_cookie({'name': cookie.name, 'value': cookie.value})



    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
