import requests
import sys

TRACKING_ID = sys.argv[1]
TRACKING_URL= "https://www.dominos.co.uk/pizzaTracker/getOrderDetails"

statuses = {
	0: "Init",
	1: "Cancelled",
	2: "Collected",
	3: "Delivered",
	5: "Baking",
	6: "Order",
	7: "Prep",
	8: "Quality",
	9: "Delivery",
	10:"Collection"
}

api_request = requests.get(TRACKING_URL+"?id="+TRACKING_ID)
json_request= api_request.json()
status_id   = json_request['statusId']
status_desc = statuses[status_id]

print status_desc
