from unittest import TestCase

import tommy

class TestRun(TestCase):
  def test_is_string(self):
    s = tommy.run()
    self.assertTrue(isinstance(s, basestring))
