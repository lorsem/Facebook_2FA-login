import re
import robobrowser # tested on 0.5.3 and Python 3.5.4 On Conda (Python 3.5.4 :: Continuum Analytics, Inc

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
CLIENT_ID = '464891386855067' # Tinder
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb"+CLIENT_ID+"%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id="+CLIENT_ID+"&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

def get_access_token(email='', password=''):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app##
    f = s.get_form()

    code = input('token 2FA: ')
    f['approvals_code'] = str(code)

    s.submit_form(f, submit = f.submit_fields['submit[Submit Code]'])# 'checkpointSubmitButton'
    print('met')
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['submit[Continue]'])

    # confirm browser (security)
    f = s.get_form()
    try:
        s.submit_form(f, submit=f.submit_fields['submit[Continue]'])
        print('confirmed browser')
        # submit "this was me" question
        f = s.get_form()
        s.submit_form(f, submit=f.submit_fields['submit[This was me]'])
        print('Confirmation "This was me"')
        # Do not save browser
        f = s.get_form()
        #f['name_action_selected']='dont_save'
        s.submit_form(f, submit=f.submit_fields['submit[Continue]'])
        print('Continue on "Save this browser" using default answer') # TODO should change the radio button
    except:
        pass
    # confirm the App
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]

    print('Your facebook secret is: \n"'+ access_token+ '"' )
    print('')
    print("Use it in curl command and then look for token\n")



    return access_token
