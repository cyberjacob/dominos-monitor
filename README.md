# dominos-monitor
Pizza tracking in 327 Characters

Python script for use with server monitoring sytems (e.g. Zabbix) for tracking Dominos Pizza Orders.
Uses the order's tracking ID with the API that power's Domino's pizza tracking website ("Dom")

The tracking ID is a base64-encoded string which is displayed in the URL to Domino's pizza tracking website.
For example, the tracking ID for a recent order was MTM4MjI5NzY1fGQwYTYyNWRjLWEzMzgtNGM5NS1hYTg2LTE2ZjYwZDNkNzI1Ng==, which decodes to the string 138229765|d0a625dc-a338-4c95-aa86-16f60d3d7256
The first section (138229765) is the order number, confirmed against the confirmation email sent from Dominos when the order is placed.
The seccond setion is in the format of a GUID or UUID, however I am unsure what it represends.
The two sections are seperated by a pipe character.