# Test file for the Main fill

import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function...')

    def test_do_stuff(self):
        '''HIIIIII!'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = 'sfjsdkf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def tearDown(self):
        print('Cleaning up')

if __name__ == '__main__':
    unittest.main()
