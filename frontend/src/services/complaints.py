import requests

class ComplaintService:
    def __init__(self) -> None:
        pass

    def getComplaint(self):
        print(requests.get("http://localhost:4002/api/complaints").content)
                                                                                                                                                           