# test_runner.py

import unittest
from tests.test_nup import TestNupPdf

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestNupPdf)

    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)
