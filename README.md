# Web_Crawler_Selenium

1. Install python3-selenium 
```
sudo apt install python3-selenium 
```
or 
```
pip3 install selenium
```
2. Install PhantomJS (Optional)
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
