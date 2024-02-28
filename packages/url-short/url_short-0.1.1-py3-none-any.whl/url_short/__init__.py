# url_short.py

import requests

def shorten_url(url, alias):
    """
    Shortens a given URL using the TinyURL service.

    Args:
        url (str): The original long URL to be shortened.
        alias (str): An optional custom alias for the shortened URL.

    Returns:
        None: Prints the shortened URL or an error message.

    Example:
        shorten_url("https://mail.google.com/mail/u/0/#inbox", "GMail")
    """
    tinyurl_domain = "tinyurl.com"
    # Define the API endpoint for TinyURL
    api_url = f"https://{tinyurl_domain}/api-create.php?url={url}"

    try:
        # Send a GET request to the TinyURL API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            shortened_url = response.text
            print(f"Shortened URL: {shortened_url}")
        else:
            print(f"Error: Unable to shorten URL. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example data
    url_to_shorten = "https://mail.google.com/mail/u/0/#inbox"
    alias_name = "GMail"

    # Call the function to shorten the URL
    shorten_url(url_to_shorten, alias_name)
