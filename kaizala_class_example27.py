# save Kaizala27.py in the working directory
# import the Kaizala class
from Kaizala27 import Kaizala
import base64

with open("def.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    #print(str)
    x=str

# dictionary containing fields necessary to initialize object
# enter values as strings
data = {
    'app_id': "309a884d-61d6-47d9-9f4a-b0f558d6d44d",
    'app_secret': "HEUQ78FVR1",
    'refresh_token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46bWljcm9zb2Z0OmNyZWRlbnRpYWxzIjoie1wicGhvbmVOdW1iZXJcIjpcIisxNTYzMjM1Mzk0M1wiLFwiY0lkXCI6XCJcIixcInRlc3RTZW5kZXJcIjpcImZhbHNlXCIsXCJhcHBOYW1lXCI6XCJjb20ubWljcm9zb2Z0Lm1vYmlsZS5rYWl6YWxhYXBpXCIsXCJhcHBsaWNhdGlvbklkXCI6XCIzMDlhODg0ZC02MWQ2LTQ3ZDktOWY0YS1iMGY1NThkNmQ0NGRcIixcInBlcm1pc3Npb25zXCI6XCI4LjRcIixcImFwcGxpY2F0aW9uVHlwZVwiOi0xLFwiZGF0YVwiOlwie1xcXCJBcHBOYW1lXFxcIjpcXFwiVFhfU2hvcF9GbG9vcl9EYXNoYm9hcmRcXFwiLFxcXCJVc2VyVGVuYW50SWRzXFxcIjpcXFwiW1xcXFxcXFwiMzliMDM3MjItYjgzNi00OTZhLTg1ZWMtODUwZjA5NTdjYTZiXFxcXFxcXCJdXFxcIn1cIn0iLCJ1aWQiOiJNb2JpbGVBcHBzU2VydmljZTpmMzZlOGUxMS1kZWIyLTRkZWItOTgzZi03NjA4OTYxOWNhN2FAMSIsInZlciI6IjIiLCJuYmYiOjE1NzE0MzM5MDIsImV4cCI6MTYwMjk2OTkwMiwiaWF0IjoxNTcxNDMzOTAyLCJpc3MiOiJ1cm46bWljcm9zb2Z0OndpbmRvd3MtYXp1cmU6enVtbyIsImF1ZCI6InVybjptaWNyb3NvZnQ6d2luZG93cy1henVyZTp6dW1vIn0.Tq9RDkF5lG7f2ci2BE6T2AIvUh79RezNhV_Z1xPcCMA",
    'group_id': "11b0986e-7be6-41eb-a0f4-d362fe075d40@1"
}

# example message to post to Kaizala
"""msg = '{0}: {1} completed in {2} minutes. \n\nThis message posted from JDAAT.'.format(
    '26JP0300R',
    '1E0560MDAKK457202',
    '11.6'
)"""

#msg="GOOD MORNING "

msg="load.gif"

# initialize object by sending dictionary to __init__
# data must include fields app_id, app_secret, refresh_token, and group_id
k = Kaizala(data)

# call post_message function in the newly created k object
k.post_media(x)
