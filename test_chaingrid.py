# test_chaingrid.py
"""
Tests for ChainGrid module.
"""

import unittest
from chaingrid import ChainGrid

class TestChainGrid(unittest.TestCase):
    """Test cases for ChainGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainGrid()
        self.assertIsInstance(instance, ChainGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
