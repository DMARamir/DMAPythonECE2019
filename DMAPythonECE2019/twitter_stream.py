from twython import TwythonStreamer
from gpiozero import LED #so we can use LEDs!
from time import sleep #so we can turn on the LED for a certain amount of time
 
from auth import ( #import the keys from our auth.py file!
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
 )
 
led = LED(17) #set up an instance of the LED class on GPIO pin 17.
 
class MyStreamer(TwythonStreamer): #define a new class that EXTENDS the TwythonStreamer class
  def on_success(self, data): #here, we're redefining the TwythonStreamer method "on_success"
      if 'text' in data: #if there's any text in the tweet
          username = data['user']['screen_name'] #finds the username of the person who posted the tweet
          tweet = data['text'] #the actual text of the tweet
          print("@%s: %s" % (username, tweet)) #prints the tweet and username
          led.on()
          sleep(1)
          led.off()
          sleep(1)
 
stream = MyStreamer(consumer_key,consumer_secret,access_token,access_token_secret) #sets up an actual instance of the MyStreamer class we just defined
 
stream.statuses.filter(track='raspberry pi') #sets up a streamer and tracks for the text 'raspberry pi' in tweets