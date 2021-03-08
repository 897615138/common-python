#!/usr/bin/python
# encoding:utf-8
"""
联系人程序
用于增加，删除，修改，查找联系人
"""
import pickle


# the name of the file where we will store the object

class Contacts:
    """
    类：联系人
    """

    def __init__(self, name):
        self.name = name
        self.info = None

    def add(self, address_book_out):
        self.info = input('请输入联系人的电话号码：\n')
        self.info = self.info.replace('\r', '')
        address_book_out[self.name] = self.info

    def delete(self, address_book_out):
        del_info = address_book_out[self.name]
        del address_book_out[self.name]
        print('联系人：', self.name, '{', del_info, '}  已被删除！')

    def search(self, address_book_out):
        if self.name in address_book_out.keys():
            print('联系人查找成功！')
            print('姓名：', self.name, '移动号码：', address_book_out[self.name])
        else:
            print('没有此联系人！')

    def modify(self, address_book_out):
        if self.name in address_book_out.keys():
            address_book_out[self.name] = input('请输入联系人的电话号码：\n')
            address_book_out[self.name] = address_book_out[self.name].replace('\r', '')
            print('修改成功！')
        else:
            print(self.name, '联系人不存在，无法修改！')

    @staticmethod
    def print_all(address_book_out):
        print('\nName\t Mobile\n')
        for key in address_book_out.keys():
            print(key, '\t', address_book_out[key])
        print()

    @staticmethod
    def print_item(name_out, address_book_out):
        print(name_out, address_book_out[name_out])


try:
    print('Welcome to the contacts program!')
    # 打开地址薄（如果不存在则创建）
    contacts_file = 'contacts_file.data'
    try:
        f = open(contacts_file, 'rb')
        address_book = pickle.load(f)
        f.close()
    except Exception:
        f = open(contacts_file, 'wb')
        address_book = {}
    flag = True
    # 对地址薄进行处理
    while flag:
        flag = (input("\n1:add\t2:delete\t3:search\t4:modify\t5:display\t0:quit\n-->"))
        flag = flag.replace('\r', '')
        if flag == '0':
            break

        elif flag == '1':
            name = input('请输入要添加的联系人的姓名：\n')
            name = name.replace('\r', '')
            while name in address_book.keys():
                print('该联系人已经存在！')
                name = input('请重新输入要添加的联系人的姓名：\n')
                name = name.replace('\r', '')
            contact = Contacts(name)
            contact.add(address_book)

        elif flag == '2':
            name = input('请输入要删除的联系人的姓名：\n')
            name = name.replace('\r', '')
            if name not in address_book.keys():
                print('该联系人不存在')
                continue
            contact = Contacts(name)
            contact.delete(address_book)

        elif flag == '3':
            name = input('请输入要查找的联系人的姓名：\n')
            name = name.replace('\r', '')
            contact = Contacts(name)
            contact.search(address_book)

        elif flag == '4':
            name = input('请输入要修改的联系人的姓名：\n')
            name = name.replace('\r', '')
            contact = Contacts(name)
            contact.modify(address_book)

        elif flag == '5':
            Contacts.print_all(address_book)

        else:
            print("你到底想干嘛？请对应下面的序号重新输入")

    f = open(contacts_file, 'wb')
    pickle.dump(address_book, f)
finally:
    f.close()
