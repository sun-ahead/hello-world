#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
计算器测试文件
用于验证 calculator.py 的功能是否正确
"""

from calculator import Calculator


def test_add():
    """测试加法"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    print("✅ 加法测试通过")


def test_subtract():
    """测试减法"""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -2) == -1
    print("✅ 减法测试通过")


def test_multiply():
    """测试乘法"""
    calc = Calculator()
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0
    print("✅ 乘法测试通过")


def test_divide():
    """测试除法"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5
    assert calc.divide(0, 5) == 0
    print("✅ 除法测试通过")


def test_divide_by_zero():
    """测试除零错误处理"""
    calc = Calculator()
    try:
        calc.divide(10, 0)
        assert False, "应该抛出 ValueError"
    except ValueError as e:
        assert str(e) == "不能除以零！"
        print("✅ 除零错误处理测试通过")


def run_all_tests():
    """运行所有测试"""
    print("=" * 40)
    print("       🧪 开始运行测试")
    print("=" * 40)
    
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    
    print("=" * 40)
    print("       ✅ 所有测试通过！")
    print("=" * 40)


if __name__ == "__main__":
    run_all_tests()
