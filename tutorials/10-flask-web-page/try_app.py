"""Visit the pages of app.py without opening a browser, using Flask's test client."""

from app import app

client = app.test_client()

for path in ["/", "/receipt/7650106", "/receipt/9999999"]:
    response = client.get(path)
    print(f"GET {path}  ->  {response.status}")
    text = response.get_data(as_text=True)
    for line in text.splitlines():
        if "<td>" in line or "<th>TOTAL" in line or "<p>" in line:
            print("   ", line.strip())
    print()
