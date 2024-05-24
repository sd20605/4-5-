

class Bun:
    def __init__(self,name,price2):
        self.contents=name
        self.price=price2
        self.total=0


    def sell(self):
        self.total+=self.price
        print(self.contents+"붕어빵이 팬매되었습니다.")
cream_bun=Bun("크림",1000)
# print(cream_bun.contents,cream_bun.price)

cream_bun.sell()
cream_bun.sell()
print("누적 판매금은",cream_bun.total, "원입니다")