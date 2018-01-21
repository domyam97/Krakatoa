# Dependencies
- Ngrok https://ngrok.com/download
- Boto3 *sudo pip install boto3*
- Tmdb3 *sudo pip install tmdb3*

# AWS Setup


# Running the program
Run *app.py* from within the *streaming* directory.  Ensure that a *tmp* directory exists under the *streaming* directory for it to run properly.  Logs will be stored in the *Log* directory in case any issue arises.  Running *app.py* will start the Ngrok service, and print to the terminal the address which the web front-end can be reached.  This is also uploaded to the AWS bucket for remote access.

# Overview of Files
### app.py
The main python script run for the program, this file is the foundation of the system and calls all other files when necessary.  The Flask framework is setup in this file, as well as the system wide logging.  Ngrok is also started here, and the details are uploaded for remote access to the Pi.  The web interface, built with HTML in the *templates* directory, is setup and hosted in this file using the Flask framework, used to control the raspberry pi camera remotely.  When the button is pressed on the web interface, this file handles taking the video, uploading to AWS, and analyzing the video for facial recognition, done by passing control to the following files.

### detect.py
Detect uses the Detektion service as part of AWS to find the celebrity names from uploaded video files.  Pulling the video from the AWS bucket, the names of the celebrities are gathered, and then analyzed using the IMDB database.  This allows us to see which films each actor has been in.  Cross-referencing is then used, utilizing the intersection function with Python sets, to determine the common films which would be the most likely for the video.  This program is also capable of detecting celebrity faces from images reference in the AWS bucket.  It will download the image and superimpose boxes and names around each celebrity detected, and then attempt to determine the film they are in if enough information is available in the image.  

### aws.py
Holds all communication functions for the Amazon Web Server integration.  Used heavily in the other programs in order to send files, delete files, and analyze faces using the Detektion service.
