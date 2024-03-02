import requests
class BIM360:
    def __init__(self,token):
        self.token = token
        self.host = "https://developer.api.autodesk.com"
    def get_hubs(self):
        headers = {'Authorization': 'Bearer ' + self.token.access_token}
        url = "https://developer.api.autodesk.com/project/v1/hubs"
        response = requests.get(url, headers=headers)
        return response.json()
