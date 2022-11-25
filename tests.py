import datetime
import uuid
from unittest import TestCase
from main import Embedded, EmbeddedArchitect, Mobile, MobileArchitect, Web, WebArchitect

"""Testing new absract methods"""


class TestEmbeddedArchitect(TestCase):
    def test_create_project(self):
        temp_list = ["No items implmented"]
        temp = uuid.uuid4()
        newEmbedded = Embedded(temp, "test", datetime.date, temp_list, 5, "TotalCross")
        newEmbeddedArchitect = EmbeddedArchitect
        self.assertEqual(
            newEmbeddedArchitect.create_project(EmbeddedArchitect, temp, "test", datetime.date, temp_list, 5,
                                                "TotalCross").title, newEmbedded.title)


class TestMobileArchitect(TestCase):
    def test_create_project(self):
        temp_list = ["No items implmented"]
        temp = uuid.uuid4()
        newMobile = Mobile(temp, "test", datetime.date, temp_list, 5, "React Native")
        newMobileArchitect = MobileArchitect
        self.assertEqual(
            newMobileArchitect.create_project(newMobileArchitect, temp, "test", datetime.date, temp_list, 5,
                                              "React Native").title, newMobile.title)


class TestWebArchitect(TestCase):
    def test_create_project(self):
        temp_list = ["No items implmented"]
        temp = uuid.uuid4()
        newWeb = Mobile(temp, "test", datetime.date, temp_list, 5, "Vue")
        newWebArchitect = WebArchitect
        self.assertEqual(
            newWebArchitect.create_project(newWebArchitect, temp, "test", datetime.date, temp_list, 5,
                                           "Vue").title, newWeb.title)
