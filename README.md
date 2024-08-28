# SoaD-Notifier
learning Experiment in Web Scraping and Mobile Notifications
Using IFTTT to Get Notified of New Tour Dates

This code checks the official System of a Down website for upcoming tour dates. If any tour dates are found, it triggers a notification using IFTTT (If This Then That). Here’s how you can set it up:

Create a New Applet:

Click on "Create" to start a new applet.
For the "If This" part, select "Webhooks" as the service. Choose "Receive a web request" and give it an event name (e.g., "tour_notification").
For the "Then That" part, choose an action that you want to happen when a new tour date is found. For example, you can select "Notifications" or "Email" to get a message.
Get Your IFTTT Webhooks Key:

Go to the Webhooks service on IFTTT and click on "Documentation".
Here, you will find your Webhooks key.
Update the Python Script:

In the code you provided, replace your_event_name with the event name you chose (e.g., "tour_notification").
Replace your_webhooks_key with your IFTTT Webhooks key.


