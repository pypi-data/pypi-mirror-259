'''
Author: 2-mo 1982800736@qq.com
Date: 2024-02-27 19:10:38
LastEditors: 2-mo 1982800736@qq.com
LastEditTime: 2024-02-27 19:15:13
FilePath: /a2pip/test/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import sys , os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from example_package_tiu2 import example

print(example.add_one(2))



