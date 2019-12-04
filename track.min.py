import requests as r,sys;print r.get("https://www.dominos.co.uk/pizzaTracker/getOrderDetails?id="+sys.argv[1]).json()['statusId']]
