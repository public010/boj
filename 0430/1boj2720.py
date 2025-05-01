class changeCoin:
    coins = {
        "QUARTER": 25,
        "DIME": 10,
        "NICKEL": 5,
        "PENNY": 1
    }

    def __init__(self, i):
        self.count = i
        self.a = []
        self.b = []
    def _coin_dict(self):
        for _ in range(self.count):
            self.a.append(int(input()))
    def _change_to_coins(self):
        for x in self.a:
            tmp_dict = {}
            for i, j in changeCoin.coins.items():
                tmp_dict[i], x = map(int, divmod(x, j))
            self.b.append(tmp_dict)
    def getter(self):
        for i in self.b:
            print(' '.join([str(i[x]) for x in i]))

a = changeCoin(int(input()))
a._coin_dict()
a._change_to_coins()
a.getter()
