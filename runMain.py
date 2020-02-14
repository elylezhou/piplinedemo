#-*-coding=utf-8 -*-
# import os,sys

import unittest
path ="/home/zjy/Documents/project/piplinedemo/test_case"
discover = unittest.defaultTestLoader.discover(path,pattern = '*.py')

# 测试
if __name__ == "__main__":
    runner =unittest.TextTestRunner()
    runner.run(discover)