import os.path as path
import time


class ORIGINAL_IMG_PATH:
    def __init__(self,month,day):
        self.SPHINX_1 = self.SPHINX_1(month,day)
        self.SPHINX_2 = self.SPHINX_2(month,day)
        self.SPHINX_3 = self.SPHINX_3(month,day)
        self.SPHINX_4 = self.SPHINX_4(month,day)
        self.SPHINX_5 = self.SPHINX_5(month,day)
        self.SPHINX_6 = self.SPHINX_6(month,day)
        self.SPHINX_7 = self.SPHINX_7(month,day)
        self.SPHINX_8 = self.SPHINX_8(month,day)
        self.SPHINX_9 = self.SPHINX_9(month,day)
        self.SPHINX_10 = self.SPHINX_10(month,day)
        self.SPHINX_11 = self.SPHINX_11(month,day)
        self.SPHINX_15 = self.SPHINX_15(month,day)
        self.SPHINX_16 = self.SPHINX_16(month,day)
        self.BANFF2_1 = self.BANFF2_1(month,day)
        self.BANFF2_3 = self.BANFF2_3(month,day)
        self.BENTAL_1 = self.BENTAL_1(month,day)
        self.BANFF1_5 = self.BANFF1_5(month,day)
        self.BANFF1_6 = self.BANFF1_6(month,day)

    class SPHINX_1:
        def __init__(self,month,day):
            self._first = f'//10.114.237.217/eq_01_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.217/eq_01_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.217/eq_01_3/CMI_Results/2025/{month}/{day}'
    class SPHINX_2:
        def __init__(self,month,day):
            self._first = f'//10.114.237.218/eq_02_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.218/eq_02_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.218/eq_02_3/CMI_Results/2025/{month}/{day}'

    class SPHINX_3:
        def __init__(self,month,day):
            self._first = f'//10.114.237.219/eq_03_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.219/eq_03_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.219/eq_03_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_4:
        def __init__(self,month,day):
            self._first = f'//10.114.237.220/eq_04_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.220/eq_04_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.220/eq_04_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_5:
        def __init__(self,month,day):
            self._first = f'//10.114.237.221/eq_05_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.221/eq_05_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.221/eq_05_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_6:
        def __init__(self,month,day):
            self._first = f'//10.114.237.222/eq_06_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.222/eq_06_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.222/eq_06_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_7:
        def __init__(self,month,day):
            self._first = f'//10.114.237.223/eq_07_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.223/eq_07_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.223/eq_07_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_8:
        def __init__(self,month,day):
            self._first = f'//10.114.237.224/eq_08_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.224/eq_08_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.224/eq_08_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_9:
        def __init__(self,month,day):
            self._first = f'//10.114.237.225/eq_09_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.225/eq_09_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.225/eq_09_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_10:
        def __init__(self,month,day):
            self._first = f'//10.114.237.226/eq_10_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.226/eq_10_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.226/eq_10_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_11:
        def __init__(self,month,day):
            self._first = f'//10.114.237.227/eq_11_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.227/eq_11_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.227/eq_11_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_15:
        def __init__(self,month,day):
            self._first = f'//10.114.237.130/eq_15_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.130/eq_15_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.130/eq_15_3/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_16:
        def __init__(self,month,day):
            self._first = f'//10.114.237.127/eq_16_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.127/eq_16_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.127/eq_16_3/CMI_Results/2025/{month}/{day}'
    
    class BANFF2_1:
        def __init__(self,month,day):
            self._first = f'//10.114.237.121/eq_01_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.121/eq_01_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.121/eq_01_3/CMI_Results/2025/{month}/{day}'
    
    class BANFF2_3:
        def __init__(self,month,day):
            self._first = f'//10.114.237.123/eq_03_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.123/eq_03_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.123/eq_03_3/CMI_Results/2025/{month}/{day}'
    
    class BENTAL_1:
        def __init__(self,month,day):
            self._first = f'//10.114.237.228/eq_01_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.237.228/eq_01_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.237.228/eq_01_3/CMI_Results/2025/{month}/{day}'
    
    class BANFF1_5:
        def __init__(self,month,day):
            self._first = f'//10.114.183.39/eq_05_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.183.39/eq_05_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.183.39/eq_05_3/CMI_Results/2025/{month}/{day}'
    
    class BANFF1_6:
        def __init__(self,month,day):
            self._first = f'//10.114.183.40/eq_06_1/CMI_Results/2025/{month}/{day}'
            self._second = f'//10.114.183.40/eq_06_2/CMI_Results/2025/{month}/{day}'
            self._third = f'//10.114.183.40/eq_06_3/CMI_Results/2025/{month}/{day}'
    
    def __str__(self):
        s = '1\'s root is ' + str(self.SPHINX_1.address) + '\n' + \
            '2\'s root is ' + str(self.SPHINX_2.address) + '\n' + \
            '3\'s root is ' + str(self.SPHINX_3.address) + '\n' + \
            '4\'s root is ' + str(self.SPHINX_4.address) + '\n' + \
            '5\'s root is ' + str(self.SPHINX_5.address) + '\n' + \
            '6\'s root is ' + str(self.SPHINX_6.address) + '\n' + \
            '7\'s root is ' + str(self.SPHINX_7.address) + '\n' + \
            '8\'s root is ' + str(self.SPHINX_8.address) + '\n' + \
            '9\'s root is ' + str(self.SPHINX_9.address) + '\n' + \
            '10\'s root is ' + str(self.SPHINX_10.address) + '\n' + \
            '11\'s root is ' + str(self.SPHINX_11.address) + '\n' + \
            '15\'s root is ' + str(self.SPHINX_15.address) + '\n' + \
            '16\'s root is ' + str(self.SPHINX_16.address) + '\n'

        return s