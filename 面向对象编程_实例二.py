#购物车实例
#商品
class Items:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}: {self.price}元 {self.quantity}个"
    def change(self,name=None,price=None,quantity=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

#购物车(增，改，删，查）
class ShopCar:
    def __init__(self):
        self.items = []
    def add(self):#增
        name = input('请输入商品名：')
        for s in self.items:
            if s.name == name:
                print('已有该商品')
                return
        try:
            price = int(input('请输入商品价格:'))
            quantity = int(input('请输入商品个数：'))
        except ValueError:
            print('请输入一个数字')
            return
        it = Items(name,price,quantity)
        self.items.append(it)
        print("商品添加成功！")
        print(it)
    def change(self,name): #改

        for s in self.items:
            if s.name == name:
                try:
                    print(f"原名称为{s.name}")
                    name = input("请输入新的商品名称：")
                    print(f"原价格为{s.price}")
                    price = int(input('请输入商品价格:'))
                    print(f"原数量为{s.quantity}")
                    quantity = int(input('请输入商品个数：'))
                    s.change(name,price,quantity)
                    print(s)
                    print ("修改成功")
                    return
                except ValueError:
                    print('请输入一个数字')
                    return

    def change_more(self):
        name = input('请输入要修改的商品名称：')
        for s in self.items:
            if s.name == name:
                print("请选择您的操作 ： 1.修改名称 2.修改价格 3.修改数量 4.全部修改 ")
                try:
                    f = int(input())
                    match f:
                        case 1:
                            print(f"原名称为{s.name}")
                            name = input("请输入新的商品名称：")
                            s.change(name, s.price, s.quantity)
                            print("修改完成")
                            print(s)
                            return
                        case 2:
                            try:
                                print(f"原价格为{s.price}")
                                price = int(input("请输入新的商品价格："))
                                s.change(s.name, price, s.quantity)
                                print("修改完成")
                                print(s)
                                return
                            except ValueError:
                                print('请输入一个数字')
                        case 3:
                            try:
                                print(f"原数量为{s.quantity}")
                                quantity = int(input("请输入新的商品数量："))
                                s.change(s.name, s.price, quantity)
                                print("修改完成")
                                print(s)
                                return
                            except ValueError:
                                print('请输入一个数字')
                                return
                        case 4:
                            self.change(s.name)
                        case _:
                            print("暂无功能！")
                            return
                except ValueError:
                    print('请输入一个数字')
                    return
        print("未发现该商品！")
    def show(self):
        name = input("请输入商品名称：")
        for s in self.items:
            if s.name == name:
                print(s)
                return
        print("未找到该商品!")
    def kill(self):
        name = input('请输入要删除的商品名称：')
        for s in self.items:
            if s.name == name:
                print(f"已删除商品{s.name}")
                self.items.remove(s)
                return
        print("未找到该商品！")
    def show_all(self):
        all_price = 0
        if len(self.items) > 0:
            for s in self.items:
                print(s)
                all_price += s.price * s.quantity
            print(f"共需要{all_price}元")
        else:
            print("暂无商品！")
    def run(self):
        while True:
            print("##########################################")
            print("欢迎来到购物车界面")
            print("请选择您的操作 ： 1.新填商品 2.修改商品 3.查询商品 4.删除商品 5.查看购物车 5.退出")
            print("##########################################")
            try:
                a = int(input())
                match a:
                    case 1:
                        self.add()
                    case 2:
                        self.change_more()
                    case 3:
                        self.show()
                    case 4:
                        self.kill()
                    case 5:
                        self.show_all()

                    case 6:
                        print("bye")
                        break
                    case _:
                        print("请重新输入")
            except ValueError:
                print('请输入一个数字')


start = ShopCar()
start.run()




