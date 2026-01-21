import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# ---------------- INPUT URL ----------------
url = input("Enter website URL to scrape: ").strip()

# Add scheme if missing
if not urlparse(url).scheme:
    url = "https://" + url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("\n" + "=" * 60)
    print("WEB SCRAPER OUTPUT")
    print("=" * 60)

    # ---------------- PAGE INFO ----------------
    print("\n🔹 URL:", url)
    print("🔹 Page Title:",
          soup.title.text.strip() if soup.title else "Not available")

    meta_desc = soup.find("meta", attrs={"name": "description"})
    print("🔹 Meta Description:",
          meta_desc["content"].strip() if meta_desc else "Not available")

    # ---------------- HEADINGS ----------------
    print("\n🔹 Headings Found:")
    for tag in ["h1", "h2", "h3"]:
        headings = soup.find_all(tag)
        for h in headings:
            print(f"{tag.upper():<3} -> {h.text.strip()}")

    # ---------------- LINKS ----------------
    print("\n🔹 Hyperlinks:")
    links = soup.find_all("a")
    valid_links = []

    for link in links:
        text = link.get_text(strip=True)
        href = link.get("href")

        if href and href.startswith("http"):
            valid_links.append((text, href))

    for i, (text, href) in enumerate(valid_links, start=1):
        print(f"{i:02d}. {text if text else 'No Text'}")
        print(f"    URL: {href}")

    # ---------------- IMAGES ----------------
    print("\n🔹 Images:")
    images = soup.find_all("img")

    if images:
        for i, img in enumerate(images, start=1):
            src = img.get("src", "Not available")
            alt = img.get("alt", "No alt text")
            print(f"{i:02d}. SRC: {src} | ALT: {alt}")
    else:
        print("No images found")

    # ---------------- SUMMARY ----------------
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Total Links   :", len(valid_links))
    print("Total Images :", len(images))
    print("Total H1     :", len(soup.find_all("h1")))
    print("Total H2     :", len(soup.find_all("h2")))
    print("Total H3     :", len(soup.find_all("h3")))

except requests.exceptions.ConnectTimeout:
    print("Connection timed out. Try again later.")

except requests.exceptions.ConnectionError:
    print("Network error or website blocked.")

except requests.exceptions.InvalidURL:
    print("Invalid URL entered.")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
