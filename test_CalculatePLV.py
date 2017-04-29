import unittest
import CalculatePLV

class testing_CalculatePLV(unittest.TestCase):

    def test_ambiguity(self):
        PLVobject = CalculatePLV.CalcPLV()
        input_num = [[1, 2, 3, 4], [4, 6, 8, 2], [9, 12, 3, 6], [16, 4, 8, 12]]
        current = PLVobject.ambiguity(input_num)
        correct = [[ (10.+0.j),  (-2.+2.j),  (-2.+0.j),  (-2.-2.j)],[ (20.+0.j),(-4.-4.j),(4.+0.j),(-4.+4.j)],[(30.+0.j),(6.-6.j),(-6.+0.j),(6.+6.j)],[(40.+0.j),(8.+8.j),(8.+0.j),(8.-8.j)]]
        self.assertEqual(current,correct)

    def test_autocorrelation(self):
        PLVobject = CalculatePLV.CalcPLV()
        input_num = [1,2,3,4]
        current = PLVobject.autocorrelation(input_num)
        correct =[[1, 2, 3, 4], [4, 6, 8, 2], [9, 12, 3, 6], [16, 4, 8, 12]]
        self.assertEqual(current,correct)

if __name__  == '__main__':

    unittest.main()