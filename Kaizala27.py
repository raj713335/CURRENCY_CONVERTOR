import sys
import requests

class Kaizala(object):

    def __init__(self, data):
        self.app_id = data['app_id']
        self.app_secret = data['app_secret']
        self.refresh_token = data['refresh_token']
        self.group_id = data['group_id']
        self.token = self.get_token()


    def get_token(self):
        url = 'https://kms1.kaiza.la/v1/accessToken'

        headers = {
            'applicationId': self.app_id,
            'applicationSecret': self.app_secret,
            'refreshToken': self.refresh_token
        }

        try:
            r = requests.get(url, headers = headers)
            data = r.json()

           

            if 'errorCode' in data:
                print("{0}: {1}".format(data['errorCode'], data['message']))
                sys.exit()
            else:
                token = data['accessToken']
                return token
        except Exception as e:
            print("{0}: {1}".format(e.message, e.args))
            sys.exit()


    def post_message(self, msg):
        url = "https://kms1.kaiza.la/v1/groups/{group_id}/messages".format(
            group_id = self.group_id
        )

        payload = {'message': msg}

        headers = {
            'accesstoken': self.token,
            'content-type': 'application/json'
        }

        try:
            r = requests.post(url, json = payload, headers = headers)
            data = r.json()

            

            if 'errorCode' in data:
                print("{0}: {1}".format(data['errorCode'], data['message']))
                sys.exit()
                
        except Exception as e:
            print("{0}: {1}".format(e.message, e.args))
            sys.exit()


    def post_media(self, msg):
        url = "https://kms1.kaiza.la/v1/groups/{group_id}/actions".format(
            group_id = self.group_id
            
        )

        payload = {
                  'actionType': "Image",
                  'actionBody': {
                  'caption':"Image caption",
                  'mediaResource': {msg}  }
}

        headers = {
            'accesstoken': self.token,
            'content-type': 'application/json'
           
        }

        try:
            r = requests.post(url, json = payload, headers = headers)
            data = r.json()

            if 'errorCode' in data:
                print("{0}: {1}".format(data['errorCode'], data['message']))
                sys.exit()
                
        except Exception as e:
            print("{0}: {1}".format(e.message, e.args))
            sys.exit()
