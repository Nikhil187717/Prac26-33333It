import requests
from bs4 import BeautifulSoup

URL = "https://google.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # ---------------- PAGE INFO ----------------
    print("=" * 60)
    print("WEB SCRAPER OUTPUT")
    print("=" * 60)

    print("\n🔹 Page Title:")
    print(soup.title.text if soup.title else "No title found")

    meta_desc = soup.find("meta", attrs={"name": "description"})
    print("\n🔹 Meta Description:")
    print(meta_desc["content"] if meta_desc else "Not available")

    # ---------------- HEADINGS ----------------
    print("\n🔹 Headings Found:")
    for tag in ["h1", "h2", "h3"]:
        headings = soup.find_all(tag)
        for h in headings:
            print(f"{tag.upper()} -> {h.text.strip()}")

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

    for i, img in enumerate(images, start=1):
        src = img.get("src")
        alt = img.get("alt", "No alt text")
        print(f"{i}. Image: {src} | Alt: {alt}")

    # ---------------- SUMMARY ----------------
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Total Links   :", len(valid_links))
    print("Total Images :", len(images))
    print("Total H1     :", len(soup.find_all("h1")))
    print("Total H2     :", len(soup.find_all("h2")))
    print("Total H3     :", len(soup.find_all("h3")))

except requests.exceptions.RequestException as e:
    print("Error:", e)
