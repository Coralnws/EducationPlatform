# test_educationplatform.py
"""
Tests for EducationPlatform module.
"""

import unittest
from educationplatform import EducationPlatform

class TestEducationPlatform(unittest.TestCase):
    """Test cases for EducationPlatform class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EducationPlatform()
        self.assertIsInstance(instance, EducationPlatform)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EducationPlatform()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
