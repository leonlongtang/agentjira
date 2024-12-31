import json
import datetime
class Task:
    def __init__(self, _id: str, name: str, description: str, status: str):
        self._id = _id
        self.name = name
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }


