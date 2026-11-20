# Compare (0.4a):
1. python-dotenv read the .env and loaded it into the os environment by itself with just a single function call. It took me to write the file read and set to environment those variables by myself manually.
2. Packages hides all the edge case implementation of the loading dotenv and give us a single method which does it all.
3. I would use python-dotenv as it saves my time. 

# Compare (0.4b):
The SDK handles the entire http requests and give us a object oriented packages to work with and it also handles all the different types of exceptions and errors like Wrong key, Wrong model ID etc. While in scratch we need it needs using to handle all the errors or exceptions and we just wrote a single exception which checks the status code and then does SystemExit(1). Also in scratch we need to call the http requests by ourself and gives responses in json (dict). Obiously I will use SDK. It provides easier methods and objects. Also It handles the errors by default. It gives advanced features and saves my time.