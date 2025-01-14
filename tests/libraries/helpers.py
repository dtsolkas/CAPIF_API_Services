import requests
import re
import pandas as pd
from urllib.parse import urlparse
from OpenSSL.crypto import (dump_certificate_request, dump_privatekey,
                            PKey, TYPE_RSA, X509Req)
from OpenSSL.SSL import FILETYPE_PEM
import socket


def parse_url(input):
    return urlparse(input)


def get_db_host(input):
    p = re.compile('^(http|https):\/\/([^:/]+):?([0-9]{1,6})?.*')
    m = p.match(input)
    if m:
        if m.lastindex == 3:
            return m[2], m[3]
        return m[2], 80
    else:
        raise Exception('Host is not present at ' + input)


def get_subscriber_and_subscription_from_location(input):
    p = re.compile('^.*/v1/([a-zA-Z0-9]+)/subscriptions/([a-zA-Z0-9]+)/?')
    m = p.match(input)
    if m:
        if m.lastindex == 2:
            return m[1], m[2]
        raise Exception('Only match ' + m.lastindex + ' and the expected is 2')
    else:
        raise Exception('Host is not present at ' + input)

def get_registration_id(input):
    p = re.compile('^.*/v1/registrations/([a-zA-Z0-9]+)/?')
    m = p.match(input)
    if m:
        if m.lastindex == 1:
            return m[1]
        raise Exception('Only match ' + m.lastindex + ' and the expected is 1')
    else:
        raise Exception('registration id is not present at ' + input)


def store_in_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(bytes(data, 'utf-8'))
        f.close()


def cert_tuple(cert_file, key_file):
    return (cert_file, key_file)


def add_dns_to_hosts(ip_address, host_name):
    capif_dns = "{}      {}".format(ip_address, host_name)
    dns_file = open("/etc/hosts", "a")
    dns_file.write("{}\n".format(capif_dns))
    dns_file.close()

def create_csr(csr_file_path, private_key_path, cn):
    # create public/private key
    key = PKey()
    key.generate_key(TYPE_RSA, 2048)

    # Generate CSR
    req = X509Req()
    req.get_subject().CN = cn
    req.get_subject().O = 'Telefonica I+D'
    req.get_subject().OU = 'Innovation'
    req.get_subject().L = 'Madrid'
    req.get_subject().ST = 'Madrid'
    req.get_subject().C = 'ES'
    req.get_subject().emailAddress = 'inno@tid.es'
    req.set_pubkey(key)
    req.sign(key, 'sha256')

    with open(csr_file_path, 'wb+') as f:
        f.write(dump_certificate_request(FILETYPE_PEM, req))
        f.close()
        csr_request = dump_certificate_request(FILETYPE_PEM, req)
    with open(private_key_path, 'wb+') as f:
        f.write(dump_privatekey(FILETYPE_PEM, key))
        f.close()

    return csr_request

def get_ip_from_hostname(hostname):
    return socket.gethostbyname(hostname)
