# Sites Monitoring Utility

The script checks the url address for availability and expiration date of the domain name, 
if it is more than 30 days from the current time.

# Quickstart

The script requires the installed Python interpreter version 3.6 and all dependencies from requirements.txt

To install dependencies you should run command:

```bash
$ pip install -r requirements.txt
```

You have to run the script with the `-f`, `--filepath` argument with the path to the file with urls 
and optional `-d`, `--days` argument (default 30) to specify number of days to check domain expiration period.

To call the help, run the script with the `-h` or `--help` option.

```bash
$ python3 check_sites_health.py -h
usage: check_sites_health.py [-h] -f FILEPATH [-d DAYS]

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        full path to the file with urls
  -d DAYS, --days DAYS  check if the domain expires after the specified number
                        of days
```


Example of script launch on Linux, Python 3.6:

```bash
$ python3 check_sites_health.py -f /home/urls.txt
Checking http://github.com:
Server respond with 200: True
Expiring in 30 days: False

Checking https://theframeworks.com:
Server respond with 200: False
Expiring in 30 days: False

Checking https://google.com:
Server respond with 200: True
Expiring in 30 days: False
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
