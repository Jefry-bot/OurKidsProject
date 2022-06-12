
from entities.Complaint import Complaint


class Converter:
    @staticmethod
    def complaint(complaint_json):
        complaint = Complaint()
        
        complaint.name = complaint_json['name']
        complaint.description = complaint_json['description']
        complaint.status = complaint_json['status']
        complaint.id = complaint_json['id']

        return complaint

    @staticmethod
    def complaints(json):
        complaints = []

        for complaint_json in json:
            complaints.append(Converter.complaint(complaint_json))

        return complaints