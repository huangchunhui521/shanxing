# -*- coding: utf-8 -*-


from shanxingapi.RunTest import *
import datetime

if __name__ == '__main__':
    nowtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H_%M_%S')
    # testcase_dir = "D:\shanxing\TestCase"
    testcase_dir= "D:\fuxiutang\shanxingapi\testacse"
    # report_dir = "D:\shanxing\TestReport"
    report_dir= ""
    result = br(unittest.defaultTestLoader.discover(testcase_dir, "TestCase_Login.py"))
    result.report(
        filename="善行"+nowtime+'自动化测试报告',
        description='善行-安卓ui自动化测试',
        report_dir=report_dir,
    )
