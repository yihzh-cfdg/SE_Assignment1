import unittest
import coverage

if __name__ == '__main__':
    # 创建 coverage 对象
    cov = coverage.Coverage()

    # 开始记录覆盖率数据
    cov.start()

    # 执行测试
    test_suite = unittest.defaultTestLoader.discover('.', pattern='*_tests.py')
    unittest.TextTestRunner().run(test_suite)

    # 结束记录覆盖率数据
    cov.stop()

    # 生成覆盖率报告
    cov.save()
    cov.report()
