The aim of this sample is to provide a example of how websockets can work in python.
i am using flask-socketio it has wide support for both 2.7 and 3.3+ it should work in most 
nix environments made after 2012 .  

the web socket specification was newly introduced specification by engineers at google in 2011.
the whole specification can be found at https://tools.ietf.org/html/rfc6455.

the need for websockets came from google maps and other realtime applications which needed to update
state in near realtime and could not wait to complete a request ack cycle each and everytime there was a change.

this is a tiny piece of the abstract from the specification
"
   The WebSocket Protocol enables two-way communication between a client
   running untrusted code in a controlled environment to a remote host
   that has opted-in to communications from that code. 
"
encapsulates some of the main objectives of the web socket protocol


what we are going to do

we will be implementing a slight modification of the example code mentioned in the socketio documentation page.

index.html
the index.html will serve as our client sending instructions to the server

server.py
the server.py file will create an endpoint in local host for the javascipt client in index.html to connect to.



