"""
Test the streamlit page creation
Author: Noah Perea
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest

class Test(TestCase):
    def test_title(self):
        at = AppTest.from_file("./app/NEA_Tracker.py")
        at.run()

        assert at.title[0].value.startswith("Near earth Objects")