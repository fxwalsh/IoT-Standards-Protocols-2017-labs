# Sigfox Node App

A Sigfox-based app that publishes temperature and light intensity data to PubNub. Logs data to MongoDB. Corresponding Freeboard dashboard to visualise data. 



##.env file
An *.env* file containing the following entries is required in the root directory of the node application:

~~~bash
dbURL=mongodb://YOUR_MONGODB_URL
publishKey=YOUR_PUBNUB_PUBLISH_KEY
subscribeKey=YOUR_PUBNUB_SUBSCRIBE_KEY
secretKey=YOUR_PUBNUB_SECRET_KEY
~~~ 