import requests
from bs4 import BeautifulSoup as BeSo

# URL of the website
url = "https://systemofadown.com"

tour_date_info = []

# Saving the HTML code of the page
webcode = requests.get(url)

# Parsing the HTML code
soup = BeSo(webcode.text, "html.parser")

# Finding all <h3> elements with the class "m-0"
tour_dates = soup.findAll("h3", attrs={"class": "m-0"})

# Adding all tour dates to the list tour_date_info
for tour_date in tour_dates:
    tour_date_info.append(tour_date.text.strip())

# Checking if tour dates are available
if "No tourdates currently" in tour_date_info:
    tourdates_found = False
else:
    tourdates_found = True

# Triggering the IFTTT webhook if tour dates were found
if tourdates_found == True:
    event_name = "your_event_name"  # Replace with chosen event name (IFTTT)
    ifttt_key = "your_webhooks_key"  # Replace with your webhooks key (IFTTT)
    url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{ifttt_key}"

    # All tour dates as a consolidated message
    tour_details = "\n".join(tour_date_info)
    
    # Data to be sent to IFTTT
    params = {
        "value1": tour_details 
    }
    
    # Sending the HTTP request to IFTTT
    response = requests.post(url, data=params)

    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Error sending notification: {response.status_code}")
