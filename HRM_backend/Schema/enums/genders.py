from enum import Enum

# class Genders(Enum):
#     Female = {'id': 1, 'name': 'Female'}
#     Male = {'id': 2, 'name': 'Male'}
#     Others = {'id': 3, 'name': 'N/A'}

#     def to_dict(self):
#         return {'id': self.value['id'], 'name': self.value['name']}

class Genders(str, Enum):
    Female = 'Female'
    Male = 'Male'
    N_A = 'N/A'
