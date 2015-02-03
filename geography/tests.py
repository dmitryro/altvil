from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from models import RoadSegment,Site,RoadSegmentRaw
from models import HouseHold,HouseHoldRaw
# Create your tests here.
def setUp(self):
    pass


def tearDown(self):
    pass

class PropertyTest(TestCase):
    def test_serialization(self):
        pass

"""
 Test Room creation
"""

class RoadSegmentTestCase(TestCase):

    def setUp(self):
        pass 


    def tearDown(self):
        pass

    def test_segment_creation(self):
        print '- - - -'
        hhr = HouseHoldRaw.objects.all()
        print hhr.count()
        for h in hh:
            try:

                #st = RoadSegment.objects.create(id=sg.segment_id,service_area_id=sg.service_area_id,
                 #                               node_from_id=sg.node_from_id,node_to_id=sg.node_to_id,
                  #                              shape=sg.shape,length=sg.length)
             #   print sg.id
               # st.save()
                pass
            except:
                print 'could not save'

#        self.assertEqual(rooms.rooms,'mock')

# Create your tests here.
