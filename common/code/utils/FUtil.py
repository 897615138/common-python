# Author Jill
# Date 2021/3/8

"""写文件"""
import pickle
import warnings


def open_write_close(file_name, context):
    with open(file_name, 'w') as f:
        f.write(context)


"""追加写文件"""


def open_write_append_close(file_name, context):
    with open(file_name, 'a') as f:
        f.write(context)


"""读文件"""


def open_read_close(file_name):
    # r is default mode
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end='')


"""存储数据"""


def open_save_object_close(file_name, obj):
    with open(file_name, 'wb') as f:
        # pickling
        pickle.dump(obj, f)


"""加载数据"""


def open_load_object_close(file_name):
    with open(file_name, 'rb') as f:
        # unpickling
        obj = pickle.load(f)
        print(obj)
        return obj


try:
    open_write_close('test.txt', 'test')
    open_read_close('test.txt')
    shop_list = ['apple', 'mango', 'carrot']
    open_save_object_close('objTest.txt', shop_list)
    obj1 = open_load_object_close('objTest.txt')
except RuntimeWarning:
    warnings.warn("FUtil has run time exception", RuntimeWarning)
