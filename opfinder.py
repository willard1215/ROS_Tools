import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import os
import pandas as pd
import socket
import re

from asset.handler import HANDLER
from asset.original_img import ORIGINAL_IMG_PATH


class App:
    def __init__(self):
        self.DEBUGMODE = False
        self.app = tk.Tk()
        self.app.geometry('800x420')
        self.app.title('판정자검색')
        self.app.resizable(0, 0)

        self.leftContainer = ttk.Frame(self.app, width=400, height=710)
        self.leftContainer.grid(row=0, column=0, rowspan=10, padx=5, pady=5, sticky="ns")
        self.leftContainer.configure(relief='solid')

        self.searchTab = ttk.Notebook(self.leftContainer, width=400, height=700)
        self.searchTab.pack(fill='both', expand=True)

        self.menu_imageVerify = ttk.Frame(self.searchTab, width=400, height=600)
        self.searchTab.add(self.menu_imageVerify, text='판정자검색')

        self.searchTab.bind('< < NotebookTabChanged>>', self.on_tab_change)

        self.label_lotinput_month_desc = tk.Label(self.menu_imageVerify, text='month:')
        self.label_lotinput_month_desc.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.list_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.list_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

        self.combo_lotinput_month = ttk.Combobox(self.menu_imageVerify, values=self.list_months, width=5)
        self.combo_lotinput_month.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_lotinput_day_desc = tk.Label(self.menu_imageVerify, text='day:')
        self.label_lotinput_day_desc.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.combo_lotinput_day = ttk.Combobox(self.menu_imageVerify, values=self.list_days, width=5)
        self.combo_lotinput_day.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        def setDayAuto(month, day):
            self.combo_lotinput_month.set(month)
            self.combo_lotinput_day.set(day)

        self.btn_lotinput_day_auto_today = ttk.Button(self.menu_imageVerify, text='오늘', command=lambda: setDayAuto(datetime.now().month, datetime.now().day), width=5)
        self.btn_lotinput_day_auto_today.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.btn_lotinput_day_auto_yesterday = ttk.Button(self.menu_imageVerify, text='어제', command=lambda: setDayAuto((datetime.now() - timedelta(1)).month, (datetime.now() - timedelta(1)).day), width=5)
        self.btn_lotinput_day_auto_yesterday.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        self.label_lotinput_model_desc = tk.Label(self.menu_imageVerify, text='모델/호기:')
        self.label_lotinput_model_desc.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.list_machine = ['SPHINX_1', 'SPHINX_2', 'SPHINX_3', 'SPHINX_4', 'SPHINX_5', 'SPHINX_6', 'SPHINX_7', 'SPHINX_8', 'SPHINX_9', 'SPHINX_10', 'SPHINX_11', 'SPHINX_15', 'SPHINX_16', 'BENTAL_1', 'BANFF2_1', 'BANFF2_3', 'BANFF1_5', 'BANFF1_6']
        self.combo_lotinput_model = ttk.Combobox(self.menu_imageVerify, values=self.list_machine, width=10)
        self.combo_lotinput_model.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="w")

        self.btn_lotinput_search = ttk.Button(self.menu_imageVerify, text='검색', width=53)
        self.btn_lotinput_search.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

        self.btn_lotinput_search.configure(command=self.get_lot_info)
        
        self.tree_lotinput_lotID = ttk.Treeview(self.menu_imageVerify, columns=['Lot ID', '시간'], show='headings')
        self.tree_lotinput_lotID.heading('Lot ID', text='Lot Id', anchor='c')
        self.tree_lotinput_lotID.heading('시간', text='진행시간', anchor='c')
        for col in self.tree_lotinput_lotID["columns"]:
            self.tree_lotinput_lotID.column(col, width=int(380 / len(self.tree_lotinput_lotID["columns"])))
        self.tree_lotinput_lotID.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.tree_lotinput_lotID.bind("< Double-1>",self.tree_item_dclicked)


        self.tree_lotinput_lotID_yscroll = ttk.Scrollbar(self.tree_lotinput_lotID, orient='vertical', command=self.tree_lotinput_lotID.yview)
        self.tree_lotinput_lotID.configure(yscrollcommand=self.tree_lotinput_lotID_yscroll.set)
        self.tree_lotinput_lotID_yscroll.pack(side='right',fill='y')
        

        self.log_menu_imageVerify = tk.Listbox(self.menu_imageVerify, width=54, height=22)
        self.log_menu_imageVerify.grid(row=4, column=0, columnspan=6, padx=5, pady=15, sticky="nsew")

        self.log_menu_imageVerify_scroll = ttk.Scrollbar(self.log_menu_imageVerify, orient='vertical', command=self.log_menu_imageVerify.yview)
        self.log_menu_imageVerify.configure(yscrollcommand=self.log_menu_imageVerify_scroll.set)
        self.log_menu_imageVerify_scroll.pack(side='right',fill='y')

        self.menu_imageVerify.grid_rowconfigure(3, weight=1)
        self.menu_imageVerify.grid_rowconfigure(4, weight=1)
        self.menu_imageVerify.grid_columnconfigure(0, weight=1)
        self.menu_imageVerify.grid_columnconfigure(1, weight=1)
        self.menu_imageVerify.grid_columnconfigure(2, weight=1)
        self.menu_imageVerify.grid_columnconfigure(3, weight=1)
        self.menu_imageVerify.grid_columnconfigure(4, weight=1)

        

        self.mainContainer = ttk.Frame(self.app, width=1280, height=710)
        self.mainContainer.grid(row=0, column=1, padx=5, pady=5)
        self.mainContainer.configure(relief='solid')
        
        self.viewedLot = ''
        self.viewedBarcode = ''
        self.handler_dir = ''
        self.viewedModel = ''
        self.month = 0
        self.day = 0
        self.lot_directLink = ''
        self.drs_requestMSG = ''


        self.app.mainloop()

    def get_lot_info(self):
        if self.combo_lotinput_month.get() == '' or self.combo_lotinput_day.get() == '' or self.combo_lotinput_model.get() == '':
            return
        ''''''
        _year = 2025
        inputMonth = self.combo_lotinput_month.get()
        inputDay = self.combo_lotinput_day.get()

        if inputMonth == '':
            _month = datetime.now().month
        else:
            _month = int(inputMonth)

        if inputDay == '':
            _day = datetime.now().day
        else:
            _day = int(inputDay)
        
        targetPath = []

        _model = self.combo_lotinput_model.get() #모델 정보
        _lotPath = ORIGINAL_IMG_PATH(_month,_day).__getattribute__(_model).__dict__
        for link in _lotPath:
            if os.path.isdir(_lotPath[link]):
                targetPath.append(_lotPath[link])



    
        _lot = []
        _ctime = []
        for child in self.tree_lotinput_lotID.get_children():
            self.tree_lotinput_lotID.delete(child)
        
        for path in targetPath:
            try:
                files = os.listdir(path)
            except FileExistsError:
                return
            except Exception as e:
                return
            

            
            for fname in files:
                if str.find(fname,'.') == -1:
                    file_path = os.path.join(path,fname)
                    creation_time = os.path.getctime(file_path)
                    readable_time = datetime.fromtimestamp(creation_time)
                    _lot.append(fname)
                    _ctime.append(readable_time)
        
        _data = {
            'lot': _lot,
            'ctime':_ctime
        }
        df = pd.DataFrame(_data)
        _sort=df.sort_values('ctime',ascending=False)
        for i,v in _sort.iterrows():
            self.append_lotinputTree(v.loc['lot'],v.loc['ctime'])    
        

    def tree_item_dclicked(self,event):
        self.setOption()

    def append_lotinputTree(self,id,ctime):
        #조회된 Lot리스트를 Tree에 입력(이름과 ctime)
        self.tree_lotinput_lotID.insert('',tk.END,values=(id,ctime))

    def setOption(self):
        itemId = self.tree_lotinput_lotID.selection()[0]
        itemValue = self.tree_lotinput_lotID.item(itemId,'values')
        #self.append_log(itemValue[0])
        self.Images = []
        self.cached_Images = []
        self.viewedLot = itemValue[0]
        self.combo_model.delete(0,tk.END)
        self.combo_model.insert(0,self.combo_lotinput_model.get())
        
        self.entry_Lot.delete(0,tk.END)
        self.entry_Lot.insert(0,self.viewedLot)

        
    


    def getUserData(self,year,month,day,model,lot,barcode):
        # 랏 바코드 판정일 정보로 DRS 루프백 및 판정자 찾기

        hpath = HANDLER(2025,month,day)
        _yesterday = datetime.fromisoformat(f'2025{str.zfill(str(month),2)}{str.zfill(str(day),2)}')-timedelta(1)
        _path = hpath.__dict__[model]
        _path = f'{os.path.dirname(os.path.dirname(_path))}/Dispatcher/{year}{str.zfill(str(month),2)}{str.zfill(str(day),2)}.txt'
        
        MDJ_IP = ''
        targetTime = 0
        
        # REPLY 라인 발견 여부
        hasFOUND = False

        for line in reversed(list(open(_path))):
            try:
                linesplt = str.split(line,',')
                # REPLY 없이 REQUEST 라인만 발견될 경우 그 직전 REPLY 로그를 통하여 IP가져와 사용자 특정
                if hasFOUND and linesplt[1] == 'REPLY': 
                    MDJ_IP = linesplt[2]
                    break

                if linesplt[4] == lot and linesplt[8] == barcode: #바코드/ 랏 일치하는 요청 및 응답라인

                    if linesplt[1] == 'REPLY': #일반적 경우 REPLY 우선 갱신 - 역방향 파싱이므로
                        # 이 경우 판정 시간 기록하여 작업자 특정
                        MDJ_IP = linesplt[2]
                        _h = int(line[1:3])
                        _m = int(line[4:6])
                        _s = int(line[7:9])
                        targetTime = _h*60*60 + _m*60 + _s
                        #hasREPLYFOUND = True
                        pass
                    elif linesplt[1] == 'REQUEST': # REQUEST 요청 라인 발견 시 DRS 루프백 및 hasFOUND 활성화
                        self.drs_requestMSG = '@'+str.split(line,':')[3][1:][:-1]
                        self.send_drs(self.drs_requestMSG)
                        hasFOUND = True
                        
                        break

            except:
                pass
            
        
        # MDJ 판정로그를 찾지 못하였을 시 발생함
        if MDJ_IP == '':
            print('로그를 찾을 수 없습니다.')
            return

        targets = [] # MDJ Process 로그 목록

        _mdjpath = f'//{MDJ_IP}/ros'
        #print(_mdjpath)
        keyword = ''
        match model[0:2]:
            case 'SP':
                keyword = 'SPHINX'
            case 'BA':
                keyword = 'BANFF'
            case 'BE':
                keyword = 'BENTAL'

        # MDJ PC 경로 상의 작업 로그 파일 탐색, 탐색 기준일과 그 전일 두 로그를 찾아 targets 리스트 안에 넣음.
        for root,_,files in os.walk(_mdjpath):
            for file in files:
                if file == f'{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}_Process.txt':
                    if str.upper(root).find(keyword) != -1:
                        targets.append(os.path.join(root,file))
                        targets.append(os.path.join(root,f'{_yesterday.year}-{str.zfill(str(_yesterday.month),2)}-{str.zfill(str(_yesterday.day),2)}_Process.txt'))
        
        # print(targets)

        # 전일 최종 판정자
        _lastOpAtMidnight = ''
        _opChangelog = {}
        for i in range(len(targets)):
            
            # 당일 로그 탐색하여 _opChangelog에 추가
            if i == 0:
                for line in reversed(list(open(targets[i],encoding='EUC-KR'))):
                    if str.find(line,'작업자변경') != -1:
                        timetag = re.match(r'[[]\d\d.\d\d.\d\d.\d\d\d[]]',line).string
                        _h = int(timetag[1:3])
                        _m = int(timetag[4:6])
                        _s = int(timetag[7:9])
                        print(_h)
                        _op = str.split(line,',')[1][:-1]
                        _convertedTime = _h*60*60 + _m*60 + _s
                        _opChangelog[_convertedTime] = _op
                        
            # 전일 로그 탐색하여 최종사용자 _lastOpAtMidnight 추가
            elif i == 1:
                print(targets[i])
                for line in reversed(list(open(targets[i],encoding='EUC-KR'))):
                    if str.find(line,'작업자') != -1:
                        timetag = re.findall(r'[[]\d\d.\d\d.\d\d.\d\d\d[]]',line)[0]
                        # _h = int(timetag[1:3])
                        # _m = int(timetag[4:6])
                        # _s = int(timetag[7:9])
                        _lastOpAtMidnight = re.findall(r'.[-].{5,6}',line)[0]
                        break
                        #_convertedTime = _h*60*60 + _m*60 + _s
        
        result = ''
        isfound = False

        # print(_lastOpAtMidnight)
        # print(_opChangelog)
        # print(targetTime)
        
        for logTime in _opChangelog:
            if targetTime > logTime:
                result = _opChangelog[logTime]
                isfound = True
                break
        
        if isfound == False:
            result = _lastOpAtMidnight
        return result
        

    def send_drs(self,msg:str):
        ip = ('127.0.0.1',8030)

        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        try:
            sock.connect(ip)
            message = bytes(msg,encoding='utf-8')
            sock.sendall(message)
        finally:
            sock.close()
        

        

    def getUserDataTrigger(self):
        try:
            _month = self.combo_lotinput_month.get()
            _day = self.combo_lotinput_day.get()
            _model = self.combo_model.get()
            _lot = str.split(self.entry_Lot.get(),'\n')[0]
            _barcode = str.split(self.entry_barcode.get(),'\n')[0]
            _op = self.getUserData(2025,_month,_day,_model,_lot,_barcode)
            self.entry_operator.configure(state='normal')
            self.entry_operator.delete(0,tk.END)
            self.entry_operator.insert(0,_op)
            self.entry_operator.configure(state='readonly')
        except:
            pass

    def getMachineDataFromLotID(self):
        try:
            _model = ''
            _month = self.combo_lotinput_month.get()
            _day = self.combo_lotinput_day.get()
            _lot = str.split(self.entry_Lot.get(),'\n')[0]

            _orginal_path = ORIGINAL_IMG_PATH(_month,_day)
            for idx in _orginal_path.__dict__:
                for path in _orginal_path.__getattribute__(idx).__dict__:
                    if os.path.isdir(os.path.join(_orginal_path.__getattribute__(idx).__dict__[path],str.upper(_lot))):
                        self.combo_model.set(idx)
                        self.lot_directLink = os.path.join(_orginal_path.__getattribute__(idx).__dict__[path],str.upper(_lot))
        except:
            pass
        
    
    def openDirectLink(self):
        if self.lot_directLink != '':
            os.startfile(os.path.realpath(self.lot_directLink))


    def on_tab_change(self, event): #메인컨테이너 자식요소 세팅
        tab = event.widget.tab('current')['text']
        try:
            for i in self.mainContainer.winfo_children():
                i.destroy()
        except:
            print('can\'t init')
        if tab == '판정자검색': 
            ''''''
            label_lotid = ttk.Label(self.mainContainer,text='MODEL')
            label_lotid.place(x=10,y=10)
            self.combo_model = ttk.Combobox(self.mainContainer,values=self.list_machine)
            self.combo_model.place(x=80,y=10)

            label_lotid = ttk.Label(self.mainContainer,text='LOT ID')
            label_lotid.place(x=10,y=40)
            self.entry_Lot = ttk.Entry(self.mainContainer)
            self.entry_Lot.place(x=80,y=40)

            btn_lotsearch = ttk.Button(self.mainContainer,text='랏검색',command=self.getMachineDataFromLotID,width=8)
            btn_lotsearch.place(x=230,y=38)
            
            btn_openDirectLink = ttk.Button(self.mainContainer,text='원본열기',command=self.openDirectLink,width=8)
            btn_openDirectLink.place(x=300,y=38)

            self.label_barcode = ttk.Label(self.mainContainer,text='BARCODE')
            self.label_barcode.place(x=10,y=100)
            self.entry_barcode = ttk.Entry(self.mainContainer,width=30)
            self.entry_barcode.place(x=80,y=100)

            self.btn_search_operator = ttk.Button(self.mainContainer,text='범인찾기',command=self.getUserDataTrigger)
            self.btn_search_operator.place(x=10,y=130)

            label_operator = ttk.Label(self.mainContainer,text='작업자')
            label_operator.place(x=10,y=160)
            self.entry_operator = ttk.Entry(self.mainContainer)
            self.entry_operator.place(x=80,y=160)
            self.entry_operator.configure(state='readonly')


            
            

if __name__ == "__main__":
    ''''''
    app = App()