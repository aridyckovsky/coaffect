'''

@class Resource

'''

from ..utils.trackable_object import TrackableObject

class Resource(TrackableObject):

    def __init__(self, unique_id):
        ''' Initialize a Resource with a unique identifier.

        '''
        super().__init__()
        self._unique_id = unique_id

    def __repr__(self):
        return 'Resource({})'.format(self._unique_id)
