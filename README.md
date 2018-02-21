# Facebook_2FA-login
A small script to login on Facebook from Python to get the "secret" for an App that uses "Login with Facebook". You will need your Facebook username and password along with the app's "Client ID" (its numeric ID)

# Requirements/Dependencies
The script requires `Python3`, `RoboBrowser` and `lxml` (used by RoboBrowser to parse the HTML). It is working on Python 3.5.4 and RoboBrowser 0.5.4 (installed by pip).
I am using a Conda environment so the Python build is from them.
Specifically, I have the 64-bit build dated Aug 14 2017.

I have `lxml` 4.1.1, again installed by pip in the Conda environment.
I have other (useless at the moment) in the environment so it is pointless to share my `requirements.txt`


# Use
You have to set the CLIENT_ID (which is the App ID) in the script. You can change the User Agent as well but it should not be needed. You can use the script by calling the *get_access_token* method with your email and password as parameters. For local use/testing you can also write your credentials in the script.
**BE CAREFUL: Do not share the script with your login information in it!**
If you have 2FA you will be prompted to insert your 2FA auth code in the terminal (you will probably get a notification on your phone immediately, too).
## Getting the token
The function prints out the token and returns it as well, so you can use it either as "standalone" or as part of a project.
Note that (at least when I used it), the returned token is just the token Facebook generates. To really login in the App you will need to fake a login on their API, too.
I provide an example for Tinder, as I am working on a small project that involves logging in on Tinder.
Not that this is App dependent as you have to put the right headers in the request.
I found the needed headers online, you should be able to find them for widely used apps.
```
    curl -X POST https://api.gotinder.com/auth --data '{"facebook_token": "TOKEN FROM MY SCRIPT IN DOUBLE QUOTES", "facebook_id":"App ID in Double Quotes eg 464891386855067"}' -H "Content-type: application/json" -H "User-agent: Tinder/3.0.4 (iPhone; iOS 7.1; Scale/2.00)"
```
# Notes
Note that depending on how the app is implemented, you may get a "short" token (it is the case for Tinder at least). I have not found a workaround yet, you can try to do a MITM when you login on Tinder and sniff the key (this is not related to this script, just an FYI). Or you can keep creating short tokens (they last 12-24 hours, did not test).



# Why did I do this?
I needed a "quick and dirty" way to get the token from Facebook, without having to do everything from the browser's developer tools.

# Other info
I have created this small script by trying to login with the script and looking at the page returned by Facebook. As you can see, in case you don't have 2FA enabled (or Facebook "remembers" your browser), the 2FA is bypassed by catching an exception and skipping that part of code. This is clearly an "heuristic" solution but it seems to be working fine.

# Thanks
I would have never been able to figure out how some of this work without all the info scattered around by the community.
The link to login on Facebook was found on pynder repo/issues. The headers for Tinder were on StackOverflow (I don't have the link but GIYF, isn't it? ;-) )
