## Monitoring Your Twilio App With Datadog and Twilio

With Twilio's [Annual Signal Conference](https://signal.twilio.com/) having come to a conclusion October 1st, I thought it would be fitting to create an update to [the last blog post Datadog has done regarding how to use Twilio alongside Datadog made in 2014](https://www.datadoghq.com/blog/send-alerts-sms-customizable-webhooks-twilio/). As a member of the [Twilio Champion Program](https://www.twilio.com/champions), my goal is to spread education and to inspire others to start creating, and what better way to do that alongside a product that will help you gather all of your data in one place.

In this blog post, I will outline how to use Datadog's comprehensive Synthetics suite to monitor your Twilio app's endpoints, as well as using the power of Twilio's API to send alerts through SMS on your monitors. So in the end you can use a Twilio notification to notify you if your Twilio app is down.

## Getting Started With Your Twilio App

If you are reading this, I suspect you already have a Twilio app deployed and ready to go. As such, I decided to follow [this "Hello, World!" style app using Twilio, Heroku and Python](https://www.twilio.com/blog/2017/02/stripe-sms-notifications-via-twilio-heroku-and-python.html) as a simple starting place. This gives us the starting point of a Flask app deployed on Heroku that will respond back to any number that texts it.

Now that we have that set up, we can add this endpoint to a Datadog Synthetics test. To start, navigate to [this page](https://app.datadoghq.com/synthetics/create), which will bring up the New API Test page. Here we will create a test emulating a real world call to our app's endpoint and recording the response for our monitoring purposes.

![](1.png)

https://docs.datadoghq.com/integrations/webhooks/#sending-sms-through-twilio
https://www.twilio.com/blog/2017/02/stripe-sms-notifications-via-twilio-heroku-and-python.html
