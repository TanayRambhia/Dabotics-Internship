import pyshorteners

def shorten_url(url):
    # Initialize the URL shortener
    s = pyshorteners.Shortener()

    # Shorten the given URL using the service (default is TinyURL)
    shortened_url = s.tinyurl.short(url)
    
    return shortened_url

if __name__ == "__main__":
    original_url = input("Enter the URL to shorten: ")
    shortened = shorten_url(original_url)
    print(f"Shortened URL: {shortened}")
