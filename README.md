# website-privacy-inspector
## PACKAGES REQUIRED

•	Node JS

•	NPM

•	Puppeteer

•	Git

•	Blacklight

## PACKAGE INSTALLATION

### • NodeJS
Refresh your local package index by:
 
 `$ sudo apt update`
 
Install Node JS using:
 
 `$ sudo apt install nodejs`

### •	NPM
After installing Nodejs, we need to install NPM i.e., Node Package Manager using:

`$ sudo apt install npm`



### •	Puppeteer
Puppeteer is a Node library whose API is used to run and control chrome browser. Puppeteer runs headless chrome by default although it can be configured to run non-headless chrome. To install Puppeteer, use following command:

`$ npm i puppeteer`

Note: Since Puppeteer is a Node library, make sure nodejs and nvm are installed on the system.

After installing puppeteer, check if its working using the following steps:

1.	Create a file example.js
2.	Copy below code in the file and save it.
```
const puppeteer = require('puppeteer');

(async () => {

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({ path: 'example.png'});

  await browser.close();
})();
```

3.	  Run the code using:

`$  node example.js`

4.	  You should see an “example.png” file in the same directory as example.js.
 

#### Troubleshooting:

##### In case the below error is observed,

`(node:50464) UnhandledPromiseRejectionWarning: Error: Failed to launch the browser process!`

1)	Check the node version using:

`$ node -v`

2)	If it is below 12, update to the latest stable version of node using:

1-	Clear the npm cache:

`$ npm cache clean -f`

2-	Install n, node’s version manager:

`$ npm install -g n`

3-	Install the latest available node version:

`$ sudo n stable`

4-	Restart terminal for effects to take place.

In case  the same error occurs again,

1)	Open example.js with a text editor and  use the –no-sandbox parameter in the launch function arguments as shown below:
```
const browser = await puppeteer.launch({
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});
```

##### In case below error is observed

```
node:internal/modules/cjs/loader:936
  throw err;
  ^

Error: Cannot find module 'semver'
```

Run the below commands on the terminal

```
sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove
sudo apt-get install nodejs npm
```

##### In case you face error related to chrome dependencies
Install below libraries using sudo apt-get install
```
ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release xdg-utils
```



### •	Git
To use blacklight, we need to clone the blacklight-collector github repository. For that we need to install git on the linux machine. Use below steps.

1)	Check if Git is already installed on your pc using:

`$ git –version`

2)	If git is not installed, install using:

`$ sudo apt install git-all`

3)	Setup your github account
```
$ git config --global user.name "<your github username>"
$ git config --global user.email <your github email id>
```


### •	Blacklight
After installing git, clone the Blacklight repository using:

`$ git clone https://github.com/the-markup/blacklight-collector.git`

#### Build
After cloning Blacklight, we need to install and build in order to run scripts.
1) To install , go to the `blacklight-collector` directory and run

`npm install`

2) To build run in the same `blacklight-collector` directory

`npm run build`


## RUNNING THE WEBSITE PRIVACY INSPECTOR

The website privacy inspector is built using FAST API 

### Setup
Python is required to run FAST API.Install python if not already present.

After installing python, install  using:

`$ pip install fastapi`

An ASGI server is required to for production e.g. uvicorn or hypercorn:

`$ pip install hypercorn`


### Running the website privacy inspector

Run the main app (in main.py) file using hypercorn.

`hypercorn main:app`

The above command runs the on the loopback IP. To globally access it, run as below

`hypercorn main:app --bind 0.0.0.0:80`

to access the API, use one of the following

1) Run on browser using the serverIP

`<Server IP:80/docs`

2) Run using curl

`curl -X POST "http://<Server IP>/privacy/" -H  "accept: application/json" -H  "Content-Type: application/json" -d '{"urls":[<list of Urls to be tested>]}'`

A logfile(logFile.txt) is created in the current directory which records all the progress and can be used for troubleshooting. The results are stored in /output_directory folder.


### Using Multiple Cores

We can use multiple cores to initiate parallel processes and get results faster. In the file `multicore_processing.py`, we have used the `Pool` Class of Python's `Multiprocessing` Module to execute processing using multiple cores.  It takes urls saved in file data.csv as input. Although it can be manipulated to fetch data from a database.

**NOTE** : In 'multicore_processing.py' we are assuming that the API is running on loopback i.e.(127.0.0.1:8000), the server url can be changed as required

![image](https://user-images.githubusercontent.com/26647470/146258384-b0e6223b-48c5-42dd-8f9f-9fecb9a13907.png)
