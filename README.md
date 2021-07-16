# Web_Crawler_Selenium
This script was created to search the available appointments on from a service and print them on command line. Firstly, I use Selenium because the data is created dynamic via Javascript. Secondly, I use the package Beautiful Soup for parsing HTML tags.
<br>
<br>
It is important to find the right paths of the urls. I use the "Developer Tools"->Network for grabbing the GET requests and analyse the right paths.
<h3> Install python3-selenium </h3> 

```
sudo apt install python3-selenium 
```
or 
```
pip3 install selenium
```
<h3> Install PhantomJS (Optional)</h3>

Dependent package installation

```
sudo apt-get install build-essential g++ flex bison gperf ruby perl libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev libpng-dev libjpeg-dev python libx11-dev libxext-dev
```
Download Phantom
```
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
```
Make changes
```
tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 
sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/ 
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
```
