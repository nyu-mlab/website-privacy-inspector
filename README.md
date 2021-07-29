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

`$ nvm i puppeteer`

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

In case the below error is observed,

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
