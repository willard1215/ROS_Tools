import os.path as path
import time


class REVIEW_IMG_PATH:
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
            self.v1 = f'//10.114.237.158/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.159/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.160/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.161/CMI_Results/2025/{month}/{day}'
    class SPHINX_2:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.163/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.164/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.165/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.166/CMI_Results/2025/{month}/{day}'

    class SPHINX_3:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.168/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.169/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.170/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.171/CMI_Results/2025/{month}/{day}'
            
    class SPHINX_4:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.173/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.174/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.175/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.176/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_5:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.178/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.179/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.180/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.181/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_6:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.183/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.184/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.185/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.186/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_7:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.188/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.189/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.190/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.191/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_8:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.193/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.194/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.195/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.196/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_9:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.198/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.199/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.200/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.201/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_10:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.203/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.204/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.205/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.206/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_11:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.208/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.209/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.210/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.211/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_15:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.77/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.78/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.79/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.80/CMI_Results/2025/{month}/{day}'
    
    class SPHINX_16:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.62/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.63/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.64/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.65/CMI_Results/2025/{month}/{day}'
    
    class BANFF2_1:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.32/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.33/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.34/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.35/CMI_Results/2025/{month}/{day}'
    
    class BANFF2_3:
        def __init__(self,month,day):
            self.v1 = f'//10.114.237.42/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.237.43/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.237.44/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.237.45/CMI_Results/2025/{month}/{day}'
    
    class BENTAL_1:
        def __init__(self,month,day):
            self.v1 = f'//10.114.183.32/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.183.33/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.183.34/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.183.35/CMI_Results/2025/{month}/{day}'
    
    class BANFF1_5:
        def __init__(self,month,day):
            self.v1 = f'//10.114.183.42/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.183.43/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.183.44/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.183.45/CMI_Results/2025/{month}/{day}'
    
    class BANFF1_6:
        def __init__(self,month,day):
            self.v1 = f'//10.114.183.47/CMI_Results/2025/{month}/{day}'
            self.v2 = f'//10.114.183.48/CMI_Results/2025/{month}/{day}'
            self.v3 = f'//10.114.183.49/CMI_Results/2025/{month}/{day}'
            self.v4 = f'//10.114.183.50/CMI_Results/2025/{month}/{day}'