import unittest


def suite():
    return unittest.TestLoader().discover("bestsellers_app.tests", pattern="*.py")