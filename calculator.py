#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单计算器 - 适合初学者的 Python 项目
功能：加、减、乘、除
"""

class Calculator:
    """计算器类"""
    
    def add(self, a, b):
        """加法"""
        return a + b
    
    def subtract(self, a, b):
        """减法"""
        return a - b
    
    def multiply(self, a, b):
        """乘法"""
        return a * b
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("不能除以零！")
        return a / b


def main():
    """主函数 - 命令行交互"""
    print("=" * 40)
    print("       🧮 欢迎使用简单计算器")
    print("=" * 40)
    
    calc = Calculator()
    
    while True:
        print("\n请选择操作：")
        print("1. 加法 (+)")
        print("2. 减法 (-)")
        print("3. 乘法 (*)")
        print("4. 除法 (/)")
        print("5. 退出")
        
        choice = input("\n输入选项 (1-5): ")
        
        if choice == '5':
            print("感谢使用，再见！👋")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("❌ 无效选项，请重新选择")
            continue
        
        try:
            num1 = float(input("输入第一个数字: "))
            num2 = float(input("输入第二个数字: "))
        except ValueError:
            print("❌ 请输入有效的数字！")
            continue
        
        if choice == '1':
            result = calc.add(num1, num2)
            print(f"✅ {num1} + {num2} = {result}")
        elif choice == '2':
            result = calc.subtract(num1, num2)
            print(f"✅ {num1} - {num2} = {result}")
        elif choice == '3':
            result = calc.multiply(num1, num2)
            print(f"✅ {num1} × {num2} = {result}")
        elif choice == '4':
            try:
                result = calc.divide(num1, num2)
                print(f"✅ {num1} ÷ {num2} = {result}")
            except ValueError as e:
                print(f"❌ {e}")


if __name__ == "__main__":
    main()
