# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Variable import varsFunc
import Func as fc

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    print_hi("PSY")
    varsFunc()
    fc.FuncTutorial()
    fc.FuncPractice_1("PSY")
    fc.FuncPractice_2(-50)
    fc.FuncPractice_3(3, 4)
    print("-4 의 반대 부호는 ", fc.adder3(-4), " 입니다.")
    print("3과 5의 평균 값은 ", fc.avger3(3, 5), " 입니다.")
    
    fc.input_func1()
    """

    print("1,3,5,7,9 의 합은 ? ", fc.func_for1())
    print("1~10 까지의 곱은 ? ", fc.func_for2())
    print("* 7단 * ")
    fc.func_for3()
    print("\n* 7단 거꾸로 * ")
    fc.func_for4()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
