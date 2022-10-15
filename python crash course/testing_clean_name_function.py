import unittest
from hello import get_clean_name

class CleanNameTestCase(unittest.TestCase):
    """Test for 'clean_name function'."""

    def test_first_last_name(self):
        """Do names like 'Tomiwa Toba' work?"""
        formatted_name = get_clean_name('tomiwa', 'toba')
        self.assertEqual(formatted_name, 'Tomiwa Toba')

    def test_first_middle_last_name(self):
        """Do names like 'Tomiwa Samuel Toba' work? """
        formatted_name = get_clean_name('tomiwa', 'samuel', 'toba')
        self.assertEqual(formatted_name, 'Tomiwa Samuel Toba')

if '__name__' == '__main__':
    unittest.main() 

# when a test fails, don't change the test code,
# instead, fix the code that caused the test to fail. 