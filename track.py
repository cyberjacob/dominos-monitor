import requests
import json

TRACKING_ID = "MTM4MjI5NzY1fGQwYTYyNWRjLWEzMzgtNGM5NS1hYTg2LTE2ZjYwZDNkNzI1Ng%3D%3D"
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
json_request= json.loads(api_request.content)
status_id   = json_request['statusId']
status_desc = statuses[status_id]

print status_desc
