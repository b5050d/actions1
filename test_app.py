import unittest

from app import MyApp



class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.myApp = MyApp()

    def test_init(self):
        self.assertEqual(self.myApp.myString,"Hello")
        self.assertEqual(type(self.myApp.timeout),int)
        # self.assertEqual(10,12)

    def test_fakeMethod(self):
        ans = self.myApp.fakeMethod(68)
        self.assertEqual("Our current iteration = 68",ans)

if __name__=="__main__":
    unittest.main()