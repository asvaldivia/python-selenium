from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from search_tests import SearchTests
from register_new_user import RegisterNewUser

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)
register_new_user_test = TestLoader().loadTestsFromTestCase(RegisterNewUser)
#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_test, register_new_user_test])
#para generar los reporters
kwargs = {
    "output": 'reports/smoke-report-HtmlTestRunner',
    "combine_reports": True,
    "add_timestamp": True
}

runner = HTMLTestRunner(**kwargs)
#corro el rurner con la suite de prueba
runner.run(smoke_test)
