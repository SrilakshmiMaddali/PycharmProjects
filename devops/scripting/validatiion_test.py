import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("Bhuvan",2),True)
    def test_too_short(self):
        self.assertEqual(validate_user("inv",5),False)
    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user",3),False)
    def test_invalid_minlength(self):
        self.assertRaises(ValueError,validate_user,"user",-1)

#Run the tests
unittest.main()