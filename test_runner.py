import unittest
import HtmlTestRunner

if __name__ == '__main__':
    # 创建测试套件
    test_suite = unittest.defaultTestLoader.discover('.', pattern='*_tests.py')

    # 使用 HTMLTestRunner 运行测试并生成报告
    with open('test-report.html', 'w') as report:
        runner = HtmlTestRunner.HTMLTestRunner(stream=report, verbosity=2)
        runner.run(test_suite)
