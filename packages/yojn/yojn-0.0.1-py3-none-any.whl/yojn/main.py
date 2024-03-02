# mypackage/__init__.py
import requests

class yojn:
    def __init__(self, url):
        self.base_url = url
    
    def _make_request(self, endpoint, config):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, **config)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during {endpoint} API call:", e)
            raise

    def initializeYojn(self, config):
        return self._make_request("initializeYojn", config)

    def completion(self, config):
        return self._make_request("runYojn", config)

    def historyYojn(self, config):
        return self._make_request("userHistory", config)
    
    def updateFeedback(self,config):
        return self._make_request("updateUserFeedback",config)