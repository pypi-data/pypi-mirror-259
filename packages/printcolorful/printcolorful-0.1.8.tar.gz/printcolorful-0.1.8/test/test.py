# 导入需要的库
import pytest
from io import StringIO
import sys
# 假设你的函数位于一个名为 colored_box.py 的文件中
from printk import print_colored_box_line, print_colored_box

# 测试 print_colored_box_line 函数
def test_print_colored_box_line():
    # 捕获输出
    captured_output = StringIO()
    sys.stdout = captured_output
    print_colored_box_line('Test Title', 'Test message')
    sys.stdout = sys.__stdout__  # 重置输出到正常的标准输出
    assert 'Test Title' in captured_output.getvalue()
    assert 'Test message' in captured_output.getvalue()

# 测试 print_colored_box 函数
def test_print_colored_box():
    # 捕获输出
    captured_output = StringIO()
    sys.stdout = captured_output
    print_colored_box('Hello, World!')
    sys.stdout = sys.__stdout__  # 重置输出到正常的标准输出
    assert 'Hello, World!' in captured_output.getvalue()

# 注意：这些测试假设你的函数能够执行而不抛出任何错误，并且输出中包含了特定的文本。
# 实际的打印结果（包括颜色和格式）在这种测试中是不被直接验证的。
