# Instainf

Instainf is a tool to get informaion from a user's instagram like Userid, Phone number, Email id, Bio, etc


## Prerequisite
[Python for Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/)

#### [IMPORTANT] 
Get your instagram session id by going to your web browser and accessing your instagram and press Ctrl+Shift+I, it'll open the developer options then you can navigate to application tab from above and see cookies from their click the link below and you can see your session id which you need to copy and paste in the final step where it's asking for a sessionid. (Your instagram needs to be open on the page so the session id can work in the script.)

## Installation with linux
### With Github
```bash
git clone https://github.com/casterix193/instainf.git
cd instainf/
sudo python3 setup.py install
```

## Usage:
(To get information only) ``` instainf -u username -s instagramsessionid ```

(To get information directly in a textfile) ``` instainf -u username -s instagramsessionid > filename.txt/.csv ```

## Example
```
Informations about     : xxxusernamexxx
Full Name              : xxxusernamesxx | userID : 123456789
Verified               : False | Is buisness Account : False
Is private Account     : False
Follower               : xxx | Following : xxx
Number of posts        : x
Number of tag in posts : x
External url           : http://example.com
IGTV posts             : x
Biography              : example biography
Public Email           : public@example.com
Public Phone           : +00 0 00 00 00 00
Obfuscated email       : me********s@examplemail.com
Obfuscated phone       : +00 0xx xxx xx 00
------------------------
Profile Picture        : https://scontent-X-X.cdninstagram.com/
```
