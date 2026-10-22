import requests
from datetime import datetime
from urllib.parse import urlparse

SECURITY_HEADERS = {
    "Strict-Transport-Security":
        "Encourages browsers to use secure HTTPS connections.",
    "Content-Security-Policy":
        "Helps control which sources a browser can load content from.",
    "X-Content-Type-Options":
        "Helps prevent browsers from guessing a different content type.",
    "X-Frame-Options":
        "Helps control whether a page can be displayed in a frame.",
    "Referrer-Policy":
        "Controls how much referrer information a browser sends.",
    "Permissions-Policy":
        "Controls access to certain browser features."
}


def check_website(url):
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed_url = urlparse(url)

    if not parsed_url.hostname:
        print("Invalid website address.")
        return

    if parsed_url.scheme not in ("https", "http"):
        print("Only HTTP and HTTPS addresses are supported.")
        return

    print("\nWEB SECURITY HEADER CHECKER")
    print("=" * 40)
    print(f"Website: {url}")
    print("Checking response headers...\n")

    try:
        response = requests.get(
            url,
            timeout=15,
            allow_redirects=True
        )

        print(f"HTTP status: {response.status_code}")
        print(f"Final URL: {response.url}")
        print("\nHEADER CHECK RESULTS")
        print("-" * 40)

        found_count = 0
        missing_count = 0

        for header, description in SECURITY_HEADERS.items():
            value = response.headers.get(header)

            if value:
                print(f"[FOUND] {header}: {value}")
                found_count += 1
            else:
                print(f"[MISSING] {header}")
                print(f"  Note: {description}")
                missing_count += 1

        print("\nSUMMARY")
        print("-" * 40)
        print(f"Headers found: {found_count}")
        print(f"Headers missing: {missing_count}")
        print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nNote: Missing headers need review; they do not")
        print("automatically prove a website is vulnerable.")

    except requests.exceptions.Timeout:
        print("Error: The website took too long to respond.")
    except requests.exceptions.SSLError:
        print("Error: Secure connection failed. Check the URL/certificate.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check internet and website address.")
    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")


if __name__ == "__main__":
    target = input("Enter a website you own or are authorized to test: ").strip()

    if target:
        check_website(target)
    else:
        print("Please enter a website address.")