import urllib.parse

alerts = {
    "CAT": '"Caterpillar" (analyst OR economist OR forecast OR upgrade OR downgrade OR price target OR outlook)',
    "WULF": '"TeraWulf" (analyst OR economist OR forecast OR upgrade OR downgrade OR price target OR AI OR HPC)',
    "CSCO": '"Cisco Systems" (analyst OR economist OR forecast OR price target OR earnings OR AI OR outlook)',
    "NVDA": '"NVIDIA" (analyst OR economist OR forecast OR price target OR AI OR GPU OR earnings)',
    "GOLD": '("gold price" OR "gold forecast") (economist OR analyst OR central bank OR inflation OR interest rates)',
    "SILVER": '("silver price" OR "silver forecast") (economist OR analyst OR demand OR solar OR industrial OR inflation)'
}

base_url = "https://www.google.com/alerts?hl=en#"

print("🔔 Google Alerts Linkleri:\n")
for name, query in alerts.items():
    encoded_query = urllib.parse.quote(query)
    alert_link = f"{base_url}q={encoded_query}"
    print(f"{name}: {alert_link}\n")
