# -*- coding: utf-8 -*-

from io import StringIO
import sys
import unittest

#from __builtin__ import unicode

import HTMLTestRunner

import DlPic
# from InsPic import InsPic
from DlPic import GetImg
from ut_target import SplitZero, EqualToZero


# ----------------------------------------------------------------------

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


# ----------------------------------------------------------------------
# Sample tests to drive the HTMLTestRunner

class SampleTest0(unittest.TestCase):
    """ A class that passes.

    This simple class has only one test case that passes.
    """

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def test_pass_no_output(self):
        """        test description
        """
        pass


class SampleTest1(unittest.TestCase):
    """ A class that fails.

    This simple class has only one test case that fails.
    """

    def test_fail(self):
        u""" test description """
        self.fail()




def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)





class SampleOutputTestBase(unittest.TestCase):
    """ Base TestCase. Generates 4 test cases x different content type. """

    def test_1(self):
        print(self.MESSAGE)
        #pass

    def test_2(self):
        #print >> sys.stderr, self.MESSAGE
        eprint(self.MESSAGE)
        #pass

    def test_3(self):
        self.fail(self.MESSAGE)
        #pass

    def test_4(self):
        raise RuntimeError(self.MESSAGE)
        #pass


class SampleTestBasic(SampleOutputTestBase):
    MESSAGE = 'basic test'


class SampleTestHTML(SampleOutputTestBase):
    MESSAGE = 'the message is 5 symbols: <>&"\'\nplus the HTML entity string: [&copy;] on a second line'


class SampleTestLatin1(SampleOutputTestBase):
    MESSAGE = u'the message is Latin'.encode('latin-1')


class SampleTestUnicode(SampleOutputTestBase):
    u""" Unicode test """
    MESSAGE = u'the message is \u8563'

    # 2006-04-25 Note: Exception would show up as
    # AssertionError: <unprintable instance object>
    #
    # This seems to be limitation of traceback.format_exception()
    # Same result in standard unittest.

    # 2011-03-28 Note: I think it is fixed in Python 2.6
    def test_pass(self):
        u""" A test with Unicode docstring """
        pass


class SzTestCase(unittest.TestCase):
    def setUp(self):
        print('test start')

    def tearDown(self):
        print('test stop')

    def testSzBig(self):
        num = 10
        sz = SplitZero()
        self.assertEqual(sz.splitzero(num), 'num is bigger than zero')

    def testSzSmall(self):
        num = -10
        sz = SplitZero()
        self.assertEqual(sz.splitzero(num), 'num is smaller than zero')

    def testSzEqual(self):
        num = 0
        sz = SplitZero()
        self.assertRaises(EqualToZero, sz.splitzero, num)


# ------------------------------------------------------------------------
# This is the main test on HTMLTestRunner

class Test_HTMLTestRunner(unittest.TestCase):
    def test0(self):
        self.suite = unittest.TestSuite()
        buf = StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        # didn't blow up? ok.
        self.assert_('</html>' in buf.getvalue())

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest0),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest1),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestBasic),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestHTML),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestLatin1),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestUnicode),
            unittest.defaultTestLoader.loadTestsFromTestCase(SzTestCase),
        ])

        # Invoke TestRunner
        #buf = StringIO.StringIO()
        buf = StringIO()
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='<Demo Test>',
            description='This demonstrates the report output by HTMLTestRunner.'
        )
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test output for debugging & demo
        print(byte_output)
        # HTMLTestRunner pumps UTF-8 output
        output = byte_output
        #self._checkoutput(output, EXPECTED)

    def _checkoutput(self, output, EXPECTED):
        i = 0
        for lineno, p in enumerate(EXPECTED.splitlines()):
            if not p:
                continue
            j = output.find(p, i)
            if j < 0:
                self.fail(safe_str('Pattern not found lineno %s: "%s"' % (lineno + 1, p)))
            i = j + len(p)


##############################################################################
# Executing this module from the command line
##############################################################################



if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv = ['CreateTestHtml.py', 'Test_HTMLTestRunner']

    unittest.main(argv=argv)

    # Testing HTMLTestRunner with HTMLTestRunner would work. But instead
    # we will use standard library's TextTestRunner to reduce the nesting
    # that may confuse people.
    # HTMLTestRunner.main(argv=argv)
