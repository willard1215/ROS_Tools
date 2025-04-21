import os.path as path

class HANDLER:
    def __init__(self,year,month,day):
        _SPHINX_1 = f'//10.114.237.157/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_2 = f'//10.114.237.162/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_3 = f'//10.114.237.167/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_4 = f'//10.114.237.172/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_5 = f'//10.114.237.177/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_6 = f'//10.114.237.182/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_7 = f'//10.114.237.187/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_8 = f'//10.114.237.192/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_9 = f'//10.114.237.197/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_10 = f'//10.114.237.202/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_11 = f'//10.114.237.207/d/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_15 = f'//10.114.237.76/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _SPHINX_16 = f'//10.114.237.61/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _BANFF2_1 = f'//10.114.237.31/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _BANFF2_3 = f'//10.114.237.41/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _BENTAL_1 = f'//10.114.183.31/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _BANFF1_5 = f'//10.114.183.41/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        _BANFF1_6 = f'//10.114.183.46/CMI6500_Handler/LOG/OutTray/{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}'
        
        if path.isdir(_SPHINX_1):
            self.SPHINX_1 = _SPHINX_1
        else:
            self.SPHINX_1 = None

        if path.isdir(_SPHINX_2):
            self.SPHINX_2 = _SPHINX_2
        else:
            self.SPHINX_2 = None

        if path.isdir(_SPHINX_1):
            self.SPHINX_3 = _SPHINX_3
        else:
            self.SPHINX_3 = None

        if path.isdir(_SPHINX_4):
            self.SPHINX_4 = _SPHINX_4
        else:
            self.SPHINX_4 = None

        if path.isdir(_SPHINX_5):
            self.SPHINX_5 = _SPHINX_5
        else:
            self.SPHINX_5 = None

        if path.isdir(_SPHINX_6):
            self.SPHINX_6 = _SPHINX_6
        else:
            self.SPHINX_6 = None

        if path.isdir(_SPHINX_7):
            self.SPHINX_7 = _SPHINX_7
        else:
            self.SPHINX_7 = None

        if path.isdir(_SPHINX_8):
            self.SPHINX_8 = _SPHINX_8
        else:
            self.SPHINX_8 = None

        if path.isdir(_SPHINX_9):
            self.SPHINX_9 = _SPHINX_9
        else:
            self.SPHINX_9 = None

        if path.isdir(_SPHINX_10):
            self.SPHINX_10 = _SPHINX_10
        else:
            self.SPHINX_10 = None

        if path.isdir(_SPHINX_11):
            self.SPHINX_11 = _SPHINX_11
        else:
            self.SPHINX_11 = None

        if path.isdir(_SPHINX_15):
            self.SPHINX_15 = _SPHINX_15
        else:
            self.SPHINX_15 = None

        if path.isdir(_SPHINX_16):
            self.SPHINX_16 = _SPHINX_16
        else:
            self.SPHINX_16 = None

        if path.isdir(_BANFF2_1):
            self.BANFF2_1 = _BANFF2_1
        else:
            self.BANFF2_1 = None

        if path.isdir(_BANFF2_3):
            self.BANFF2_3 = _BANFF2_3
        else:
            self.BANFF2_3 = None

        if path.isdir(_BENTAL_1):
            self.BENTAL_1 = _BENTAL_1
        else:
            self.BENTAL_1 = None

        if path.isdir(_BANFF1_5):
            self.BANFF1_5 = _BANFF1_5
        else:
            self.BANFF1_5 = None

        if path.isdir(_BANFF1_6):
            self.BANFF1_6 = _BANFF1_6
        else:
            self.BANFF1_6 = None

    def __str__(self):
        s = '1\'s root is ' + str(self.SPHINX_1) + '\n' + \
            '2\'s root is ' + str(self.SPHINX_2) + '\n' + \
            '3\'s root is ' + str(self.SPHINX_3) + '\n' + \
            '4\'s root is ' + str(self.SPHINX_4) + '\n' + \
            '5\'s root is ' + str(self.SPHINX_5) + '\n' + \
            '6\'s root is ' + str(self.SPHINX_6) + '\n' + \
            '7\'s root is ' + str(self.SPHINX_7) + '\n' + \
            '8\'s root is ' + str(self.SPHINX_8) + '\n' + \
            '9\'s root is ' + str(self.SPHINX_9) + '\n' + \
            '10\'s root is ' + str(self.SPHINX_10) + '\n' + \
            '11\'s root is ' + str(self.SPHINX_11) + '\n' + \
            '15\'s root is ' + str(self.SPHINX_15) + '\n' + \
            '16\'s root is ' + str(self.SPHINX_16) + '\n'

        return s

if __name__ == "__main__":
    handler = HANDLER(2025,1,1)
    print(handler)