import unittest
from DAconvertDateTime import DAConvertDate
from DAconvertDateTime.DAClassLibrary import DaParsiDateTime, DAexception


class TestDaParsiDateTime(unittest.TestCase):

    def test_newDAconvertDateTime(self):


        try:
            DaParsiDateTime(-1)

            self.fail(msg="dont raise exception - year -1")
        except DAexception:
            pass


        try:
            DaParsiDateTime(9223372036854775808)

            self.fail(msg="dont raise exception - year larg")
        except DAexception:
            pass

        try:
            DaParsiDateTime(month=0)

            self.fail(msg="dont raise exception - month")
        except DAexception:
            pass

        try:
            DaParsiDateTime(month=13)

            self.fail(msg="dont raise exception - month")
        except DAexception:
            pass

        try:
            DaParsiDateTime(hour=-1)

            self.fail(msg="dont raise exception - hour -1")
        except DAexception:
            pass

        try:
            DaParsiDateTime(hour=24)

            self.fail(msg="dont raise exception - hour 24")
        except DAexception:
            pass

        try:
            DaParsiDateTime(minute=-1)

            self.fail(msg="dont raise exception - minute -1")
        except DAexception:
            pass

        try:
            DaParsiDateTime(minute=60)

            self.fail(msg="dont raise exception - minute 60")
        except DAexception:
            pass

        try:
            DaParsiDateTime(second=-1)

            self.fail(msg="dont raise exception - second -1")
        except DAexception:
            pass

        try:
            DaParsiDateTime(microsecond=-1)

            self.fail(msg="dont raise exception - microsecond -1")
        except DAexception:
            pass

        try:
            DaParsiDateTime(microsecond=1000000)

            self.fail(msg="dont raise exception - microsecond 1000000")
        except DAexception:
            pass



if __name__ == '__main__':
    unittest.main()