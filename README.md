# intercom
whole house text to speech intercom via sonos and microsoft bing voice API

1) First install https://github.com/jishi/node-sonos-http-api/
2) Then set up Microsoft Speech API and put keys in settings.json 
{
	  "microsoft": {
	    "key": "Your api for Bing speech API",
	    "name": "ZiraRUS"
	  }
	}
  See Jishi instructions for TTS set up.
  
 3) intercom.html can be deployed to apache server in /var/www/html just change the ip to localhost where applicable.
 4) enigmacom.py can be run from any terminal for a command line intercom interface, just change the ip to localhost where applicable.
 
 
