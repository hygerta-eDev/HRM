# from enum import Enum

# class MaritalStatus(Enum):
#     Single = {'id': 1, 'name': 'Single'}
#     Married = {'id': 2, 'name': 'Married'}
#     Divorced = {'id': 3, 'name': 'Divorced'}
#     Widowed = {'id': 4, 'name': 'Widowed'}

#     def to_dict(self):
#         return {'id': self.value['id'], 'name': self.value['name']}


from enum import Enum

class MaritalStatus(str, Enum):
    Single = 'Single'
    Married = 'Married'
    Divorced = 'Divorced'
    Widowed = 'Widowed'