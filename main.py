# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Variable import varsFunc
import Func as fc
import Func2 as fc2
import Func3_if_elif as fc3
import Func4_For_White as fc4

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
    """
    print("1,3,5,7,9 의 합은 ? ", fc.func_for1())
    print("1~10 까지의 곱은 ? ", fc.func_for2())
    print("* 7단 * ")
    fc.func_for3()
    print("\n* 7단 거꾸로 * ")
    fc.func_for4()
    
    fc.func_for2_1()
    fc.func_for2_2()
    print("2의 3승은 ", fc.func_for2_3(2, 3), " 입니다.")
    fc.greet()
    
    fc.int_div(11,3)
    fc.bet_num(1,5)

    fc2.list_basic()
    
    fc2.idx_list()
   
    fc2.idx_string()
    
    print(fc2.sum_all([1,2,3,4,5,6,7,8,9,10]))
    fc2.show_reverse([1,2,3,4,5])
    print("")
    fc2.show_reverse("Hello World")
     
    fc2.apend_pop_list2()
    fc2.clear_list()
    fc2.for_list_01()
    fc2.for_list_02()
    fc2.slice_li()
   
    fc2.str_func_2()
    st = "070609-2011xxx"
    print(fc2.birth_only(st))
    st = "090716-1012xxx"
    print(fc2.birth_only(st))
     """
    fc3.is_zero(-0.1)
    fc3.is_one(2)
    fc3.what_size(12)
    fc3.what_multi(5)
    fc3.what_size_two(20)
    #fc3.check_phone_number()
   # fc3.get_multiple_val(input("정수를 입력하세요 : "))
    fc4.zero_to_nine()
    print("")
    fc4.nine_to_zero()
    print("")
    fc4.what_number()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
