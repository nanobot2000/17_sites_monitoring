import whois
import argparse
import requests
from datetime import datetime
from urllib.parse import urlparse


def get_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        help='full path to the file with urls',
        required=True
    )
    args = parser.parse_args()
    return args


def load_urls4check(path):
    with open(path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]


def is_server_respond_with_200(url):
    try:
        return requests.get(
            url,
            timeout=(10, 10)
        ).status_code == requests.codes.ok
    except requests.exceptions.RequestException:
            return False


def is_expiry_date_close(expiration_date, min_expiration_period):
    time_left = expiration_date - datetime.now()
    return time_left.days < min_expiration_period


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    expiration_date = domain_info.expiration_date
    if expiration_date is None:
        return None
    elif isinstance(expiration_date, list):
        return expiration_date[0]
    else:
        return expiration_date


def print_site_health(url, server_response, expiration_date):
    print('Checking {}:'.format(url))
    print('Server respond with 200: {}'.format(server_response))
    if expiration_date is None:
        print('No expiry date for {}'.format(url))
    else:
        print('Expiring in a month: {}\n'.format(
            is_expiry_date_close(
                expiration_date,
                min_expiration_period=31
            )
        ))


if __name__ == '__main__':
    args = get_command_line_args()
    loaded_urls = load_urls4check(args.filepath)
    for url in loaded_urls:
        domain_name = urlparse(url).netloc
        domain_expiration_date = get_domain_expiration_date(domain_name)
        server_response = is_server_respond_with_200(url)
        print_site_health(url, server_response, domain_expiration_date)
