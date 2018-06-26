# Sites Monitoring Utility

The script checks the url address for availability and expiration date of the domain name, 
if it is more than 30 days from the current time.

# Quickstart

The script requires the installed Python interpreter version 3.6 and all dependencies from requirements.txt

To install dependencies you should run command:

```bash
$ pip install -r requirements.txt
```

You have to run the script with the `-f`, `--filepath` argument with the path to the file with urls.

To call the help, run the script with the `-h` or `--help` option.

```bash
$ python3 check_sites_health.py -h
usage: check_sites_health.py [-h] -f FILEPATH

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        full path to the file with urls
```


Example of script launch on Linux, Python 3.6:

```bash
$ python3 check_sites_health.py -f /home/urls.txt
Checking http://github.com:
Server respond with 200: True
Expiring in a month: False

Checking https://theframeworks.com:
Server respond with 200: False
Expiring in a month: False

Checking https://google.com:
Server respond with 200: True
Expiring in a month: False
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
