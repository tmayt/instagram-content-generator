from main import make_lines,make_bg
import unittest
import cv2

class TestStringMethods(unittest.TestCase):

    def test_make_lines(self):
        self.assertEqual(
            make_lines('In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available. Wikipedia'), 
            ['In publishing and graphic design, Lorem ipsum is a ', ' placeholdertext commonly used to demonstrate the ', ' visualform of a document or a typeface without ', ' relyingon meaningful content. Lorem ipsum may be used ', ' asa placeholder before final copy is available. ', ' Wikipedia']
        )

    def test_make_bg(self):
        obj1 = cv2.imencode('.jpg', make_bg((255,255,255)))[1].tobytes()
        obj2 = cv2.imencode('.jpg', cv2.imread('test-template.png'))[1].tobytes()
        self.assertEqual(obj1, obj2)

        
if __name__ == '__main__':
    unittest.main()
