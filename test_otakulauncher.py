# test_otakulauncher.py
"""
Tests for OtakuLauncher module.
"""

import unittest
from otakulauncher import OtakuLauncher

class TestOtakuLauncher(unittest.TestCase):
    """Test cases for OtakuLauncher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OtakuLauncher()
        self.assertIsInstance(instance, OtakuLauncher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OtakuLauncher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
