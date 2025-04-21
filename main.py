import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import threading
import os
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import math
import shutil
import time

from asset.handler import HANDLER
from asset.original_img import ORIGINAL_IMG_PATH
from asset.review_img import REVIEW_IMG_PATH


class App:
    def __init__(self):
        self.DEBUGMODE = False
        self.app = tk.Tk()
        self.app.geometry('1720x720')
        self.app.title('랏검증기 v1.0.02')
        self.app.resizable(0, 0)

        self.leftContainer = ttk.Frame(self.app, width=400, height=710)
        self.leftContainer.grid(row=0, column=0, rowspan=10, padx=5, pady=5, sticky="ns")
        self.leftContainer.configure(relief='solid')

        self.searchTab = ttk.Notebook(self.leftContainer, width=400, height=700)
        self.searchTab.pack(fill='both', expand=True)

        self.menu_imageVerify = ttk.Frame(self.searchTab, width=400, height=600)
        self.searchTab.add(self.menu_imageVerify, text='원본이미지 조회')

        self.menu_lotAnalitics = ttk.Frame(self.searchTab, width=400, height=600)
        self.searchTab.add(self.menu_lotAnalitics, text='로트 통계')

        self.searchTab.bind('<<NotebookTabChanged>>', self.on_tab_change)

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

        if self.DEBUGMODE:
            self.btn_lotinput_search.configure(command=self.debug_lot_info)
        else:
            self.btn_lotinput_search.configure(command=self.get_lot_info)
            
        self.tree_lotinput_lotID = ttk.Treeview(self.menu_imageVerify, columns=['Lot ID', '시간'], show='headings')
        self.tree_lotinput_lotID.heading('Lot ID', text='Lot Id', anchor='c')
        self.tree_lotinput_lotID.heading('시간', text='진행시간', anchor='c')
        for col in self.tree_lotinput_lotID["columns"]:
            self.tree_lotinput_lotID.column(col, width=int(380 / len(self.tree_lotinput_lotID["columns"])))
        self.tree_lotinput_lotID.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.tree_lotinput_lotID.bind("<Double-1>",self.tree_item_dclicked)


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
        
        self.Images = []
        self.baseImgSize = 650
        self.baseImg_XOfsset = 0
        self.baseImg_YOfsset = 0
        self.cached_Images = []
        self.cachePath = ''
        self.viewedLot = ''
        self.viewedBarcode = ''
        self._img_show_idx = 0
        self.original_img_root = ''
        self.AUTOVIEW = False
        self.num_nowshoing_rev = 0
        self.isreviewimgCached = False
        self.handler_dir = ''

        self.app.bind('<Left>', self.on_key)
        self.app.bind('<Right>', self.on_key)
        self.app.bind('<space>',self.on_key)
        self.app.bind('<Return>',self.on_key)

        self.app.mainloop()
        
    def on_key(self,event):
        if event.keysym == 'Right' or event.keysym == 'space':
            self.next_image()
        elif event.keysym == 'Left':
            self.previous_image()
        elif event.keysym == 'Return':
            self.toggle_autoview()
    
    def copy_file(self,src,dst):
        try:
            shutil.copy2(src,dst)
        except Exception as e:
            self.append_log('이미지를 불러오는데 실패했습니다.')
            self.append_log(e)

    def excute_auto_view(self):
        #오토뷰 실행함수. 다른코드에서 에러 발생 시 동작하지 않음.
        if self.AUTOVIEW:
            self.next_image()
            self.app.after(150,self.excute_auto_view)

    def create_precache(self,src,dst):
        #이미지 프리캐싱
        threading.Thread(target=self.copy_file, args=(src,dst), daemon=True).start()
        

    def show_image(self,index):
        #이미지를 띄우는 함수.
        if len(self.Images) == 0:
            self.append_log('보여줄 이미지가 없거나 검색조건에 부합하는 이미지가 없습니다.')
            return
            
        filepath = self.Images[self._img_show_idx]
        
        try:
            for i in range (1,9):
                if self.cached_Images[self._img_show_idx + i]:
                    pass
                else:
                    self.cached_Images[self._img_show_idx + i] = True
                    self.create_precache(self.Images[self._img_show_idx + i],self.cachePath)
        except:
            pass


        if self.cached_Images[self._img_show_idx] == True:
            img= Image.open(f'./cachedData/{self.viewedLot}/{os.path.basename(self.Images[self._img_show_idx])}')
        else:
            img = Image.open(filepath)
        isize = img.size
        mvalue = max(img.size)
        ratio = self.baseImgSize/mvalue
        wishsize = (math.floor(isize[0]*ratio),math.floor(isize[1]*ratio))
        img.thumbnail(wishsize)
        tkimg = ImageTk.PhotoImage(img)
        self.label_lotinput_image.configure(image=tkimg)
        self.label_lotinput_image.place(x=0+self.baseImg_XOfsset,y=-25+self.baseImg_YOfsset)
        self.label_lotinput_image.img = tkimg
        self.modify_imgnum(f'{self._img_show_idx+1} / {len(self.cached_Images)}')
        self.viewedBarcode = str.split(os.path.splitext(os.path.basename(filepath))[0],'_')[3]
        self.entry_showing_Barcode.delete(0,tk.END)
        self.entry_showing_LotID.delete(0,tk.END)
        self.entry_showing_LotID.insert(0,self.viewedLot)
        self.entry_showing_Barcode.insert(0,self.viewedBarcode)

        try:
            _module_handler_data = self.findreviewed().values[0]
        except Exception as e:
            self.append_log('Handler을 불러오는 과정에 오류가 발생했습니다.')
            return
    
                
        for item in self.tree_showed.get_children():
            self.tree_showed.delete(item)

        for i in range(len(_module_handler_data)):
            self.tree_showed.insert("",i,values=list(_module_handler_data))

        if self.isreviewimgCached == True:
            
            self.init_rev()
            _revpath = './review'
            revlist = os.listdir(_revpath)
            newlist = []
            try:
                for element in revlist:
                    splt = str.split(element,'_')
                    if splt[3] == self.viewedBarcode:
                        i = os.path.abspath(os.path.join(_revpath,element))
                        newlist.append(i)
                if len(newlist) > 0:
                    self.add_element_rev(newlist)
                else:
                    pass
            except:
                pass
            

        

        
        _judgement = _module_handler_data[14]
        _defectcode = _module_handler_data[15]
        if not pd.isna(_defectcode):
            if _judgement =='G':
                self.frame_image_container.configure(bg='green')
                self.label_lotinput_image.configure(bg='green')
                self.canvas_reviewViewer.configure(bg='green')
            elif _judgement =='N':
                self.frame_image_container.configure(bg='yellow')
                self.label_lotinput_image.configure(bg='yellow')
                self.canvas_reviewViewer.configure(bg='yellow')
            elif _judgement =='R':
                self.frame_image_container.configure(bg='red')
                self.label_lotinput_image.configure(bg='red')
                self.canvas_reviewViewer.configure(bg='red')
        else:
            self.frame_image_container.configure(bg='gray')
            self.label_lotinput_image.configure(bg='gray')
            self.canvas_reviewViewer.configure(bg='gray')

        
            



    def next_image(self):
        if self._img_show_idx < len(self.Images) - 1 :
            self._img_show_idx += 1
            self.show_image(self._img_show_idx)
    
    def previous_image(self):
        if self._img_show_idx > 0:
            self._img_show_idx -= 1
            self.show_image(self._img_show_idx)
    
    def toggle_autoview(self):
        if self.AUTOVIEW:
            self.AUTOVIEW = False
            self.btn_toggle_autoview.configure(text='자동넘기기 켜기')
        else:
            self.AUTOVIEW = True
            self.btn_toggle_autoview.configure(text='자동넘기기 끄기')
            self.excute_auto_view()

    def autoview_thread(self,sec):
        if self.AUTOVIEW:
            time.sleep(sec)
            self.next_image()
        

    def tree_item_dclicked(self,event):
        self.search()

    def search(self):
        itemId = self.tree_lotinput_lotID.selection()[0]
        itemValue = self.tree_lotinput_lotID.item(itemId,'values')
        #self.append_log(itemValue[0])

        # 이미지 로드에 필요한 필드 및 리스트 초기화
        self.Images = []
        self.cached_Images = []
        self.viewedLot = itemValue[0]
        self.cachePath = f'./cachedData/{itemValue[0]}'
        self.viewedLot = itemValue[0]
        self._img_show_idx = 0
        self.isreviewimgCached = False
        self.lotinput_lotverify_request(itemValue[0])
        self.append_log(f'Lot 조회: {itemValue[0]}')
        self.copy_review(itemValue[0])
        self.init_rev()

    def modify_imgnum(self,string):
        #몇 번 째 이미지를 보여주고 있는지를 표시하는 인덱스 수정
        self.label_currentImgNum.configure(text = string)
        self.label_currentImgNum.update()

    def append_log(self,msg):
        self.now = str(datetime.now())[0:-7]
        self.log_menu_imageVerify.insert(tk.END, "[{}] {}".format(self.now,msg))
        self.log_menu_imageVerify.update()
        self.log_menu_imageVerify.see(tk.END)
    
    def append_lotinputTree(self,id,ctime):
        #조회된 Lot리스트를 Tree에 입력(이름과 ctime)
        self.tree_lotinput_lotID.insert('',tk.END,values=(id,ctime))

    def open_imagedir(self):
        #탐색중인 랏의 원본 이미지 폴더를 여는 함수
        os.startfile(os.path.abspath(self.original_img_root))

    def open_revdir(self):
        #탐색중인 랏의 리뷰 이미지 폴더를 여는 함수
        #self.copy_review(self.viewedLot)
        os.startfile(os.path.abspath('./review/'))

    def copy_review(self,lot):
        if not self.isreviewimgCached:
            #탐색중인 랏의 리뷰이미지를 로컬로 복사해오는 함수
            #
            _model = self.combo_lotinput_model.get()
            _month = self.combo_lotinput_month.get()
            _day = self.combo_lotinput_day.get()

            _lot = lot

            _revdir = REVIEW_IMG_PATH(_month,_day)
            _namefield = ['v1','v2','v3','v4']
            _list_revdir = _revdir.__getattribute__(_model)
            if os.path.isdir('./review'):
                shutil.rmtree('./review')
                os.mkdir('./review')
            else:
                os.mkdir('./review')

            for name in _namefield:
                _url = os.path.join(_list_revdir.__getattribute__(name),_lot)
                if not os.path.isdir(_url):
                    pass
                else:
                    for root,_,files in os.walk(_url):
                        for file in files:
                            splt = str.split(file,'_')
                            if os.path.splitext(file)[1] =='.jpg' and splt[4] == 'rev':
                                '''_path = os.path.join(_)'''
                                _path = os.path.join(root,file)
                                shutil.copy2(src=_path,dst=os.path.abspath('./review/'))
            
            self.isreviewimgCached = True
            
            _localrevlist = os.listdir('./review')
            wish_mkdirlist = ['./judgement/GOOD','./judgement/REPAIR','./judgement/TIMEOUT','./judgement/NG']
            for path in wish_mkdirlist:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    os.mkdir(path)
                else:
                    os.mkdir(path)

            goodList = []
            repairList = []
            ngList = []
            timeoutList = []

            _demensionPath = f'//10.114.237.156/ros/Dimension/2024/{_month}/{_day}/{_lot}'

            _demensionList = [] #디멘션에 들어있는 바코드 리스트

            ###디멘션 경로로부터 바코드 가져오기###
            for root,_,files in os.walk(_demensionPath):
                for file in files:
                    splt = str.split(file,'_')
                    if os.path.splitext(file)[1] =='.jpg' and splt[4] == 'rev':
                        if _demensionList.count(splt[3]) == 0:
                            _demensionList.append(splt[3])


            _handlerPath = HANDLER(2024,_month,_day).__dict__[_model]
            
            _handler_good = f'{_handlerPath}/{_lot}_Good.csv'
            _handler_repair = f'{_handlerPath}/{_lot}_N1.csv'
            _handler_NG = f'{_handlerPath}/{_lot}_N2.csv'
            
            if os.path.isfile(_handler_good):
                _csv = pd.read_csv(_handler_good)
                for item in _csv[_csv['DefectCode'].notna()]['Barcode'].values:
                    goodList.append(item)

            if os.path.isfile(_handler_repair):
                _csv = pd.read_csv(_handler_repair)
                tempreapirList = _csv['Barcode'].values
                for barcode in tempreapirList:
                    if _demensionList.count(barcode) == 0:
                        timeoutList.append(barcode)
                    else:
                        repairList.append(barcode)

            if os.path.isfile(_handler_NG):
                _csv = pd.read_csv(_handler_NG)
                for item in _csv['Barcode'].values:
                    ngList.append(item)

            
            
            for imgname in _localrevlist:
                splt = str.split(imgname,'_')
                if goodList.count(splt[3]) != 0:
                    shutil.copy2(src=f'./review/{imgname}',dst='./judgement/GOOD')
                if repairList.count(splt[3]) != 0:
                    shutil.copy2(src=f'./review/{imgname}',dst='./judgement/REPAIR')
                if timeoutList.count(splt[3]) != 0:
                    shutil.copy2(src=f'./review/{imgname}',dst='./judgement/TIMEOUT')
                if ngList.count(splt[3]) != 0:
                    shutil.copy2(src=f'./review/{imgname}',dst='./judgement/NG')
            
            self.append_log('---------------------------------')
            self.append_log(f'[{_lot} 조회결과]')
            self.append_log(f'Good: {len(goodList)}개')
            self.append_log(f'Repair: {len(repairList)}개')
            self.append_log(f'Time: {len(timeoutList)}개')
            self.append_log(f'Ng: {len(ngList)}개')
            self.append_log('---------------------------------')
            

        else:
            self.append_log('이미 리뷰이미지가 로드되었습니다.')

         
    def debug_lot_info(self):
        ''''''
        if self.combo_lotinput_month.get() == '' or self.combo_lotinput_day.get() == '' or self.combo_lotinput_model.get() == '':
            self.append_log('진행날짜 혹은 호기값중 빈 값이 있습니다.')
            return
        
        for item in self.tree_lotinput_lotID.get_children():
            self.tree_lotinput_lotID.delete(item)
        path = './debugPath/'
        try:
            files = os.listdir(path)
        except FileExistsError:
            self.append_log('파일 내 경로 확인 불가.')
            return
        except Exception as e:
            self.append_log(f'오류 발생: {e}')
            return
        
        for child in self.tree_lotinput_lotID.get_children():
            self.tree_lotinput_lotID.delete(child)

        for fname in files:
            file_path = os.path.join(path,fname)
            creation_time = os.path.getctime(file_path)
            readable_time = datetime.fromtimestamp(creation_time)
            self.append_lotinputTree(fname,readable_time)
        
        self.append_log(f'{self.combo_lotinput_month.get()}월 {self.combo_lotinput_day.get()}일 {self.combo_lotinput_model.get()}호기 검색')
    
    def get_lot_info(self):
        if self.combo_lotinput_month.get() == '' or self.combo_lotinput_day.get() == '' or self.combo_lotinput_model.get() == '':
            self.append_log('진행날짜 혹은 호기값중 빈 값이 있습니다.')
            return
        ''''''
        _year = 2024
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

        if len(targetPath)>0:
            for path in targetPath:
                self.append_log(f'경로탐색: {path}')
        else:
            self.append_log(f'경로 확인불가.')
            return

    
        _lot = []
        _ctime = []
        for child in self.tree_lotinput_lotID.get_children():
            self.tree_lotinput_lotID.delete(child)
        
        for path in targetPath:
            try:
                files = os.listdir(path)
            except FileExistsError:
                self.append_log('파일 내 경로 확인 불가.')
                return
            except Exception as e:
                self.append_log(f'오류 발생: {e}')
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
            
        
        self.append_log(f'{self.combo_lotinput_month.get()}월 {self.combo_lotinput_day.get()}일 {self.combo_lotinput_model.get()}호기 검색')
    
    def findreviewed(self):
        #이미지가 리뷰된 적 있는지 handler 탐색

        ##
        ## Known Bugs
        ## LOT 진행 중 일자 변경 시 HANDLER 현재 모듈 진행에 맞게 경로 변경됨
        ##
        ##
        _year = 2024
        _month = self.combo_lotinput_month.get()
        _day = self.combo_lotinput_day.get()
        _machine = self.combo_lotinput_model.get()
        
        hadress = HANDLER(2024,_month,_day)
        radress = REVIEW_IMG_PATH(_month,_day)
        
        _path = hadress.__dict__[_machine]

        targetcsv = []
        for file in os.listdir(_path):
            _filename, _ext = os.path.splitext(file)
            if _ext == '.csv':
                try:
                    _lotOnFilename, _judgement = str.split(_filename,'_')

                    if _lotOnFilename == self.viewedLot:
                        targetcsv.append(file)
                        
                except Exception as e:
                    print(e)
        
        for csv in targetcsv:
            csvdata = pd.read_csv(os.path.join(_path,csv))
            target_on_csvdata = csvdata[csvdata['Barcode'] == self.viewedBarcode]
            
            if len(target_on_csvdata) > 0:
                return target_on_csvdata
            else:
                continue



    def lotinput_lotverify_request(self,target): #이미지 프리캐싱 함수. 캐싱 속도 문제 리팩토링 필요
        ''''''
        _year = 2024
        _month = self.combo_lotinput_month.get()
        _day = self.combo_lotinput_day.get()
        _machine = self.combo_lotinput_model.get()
        oadress = ORIGINAL_IMG_PATH(_month,_day)
        _opath = ''
        

        for i in oadress.__getattribute__(_machine).__dict__:
            link = oadress.__getattribute__(_machine).__dict__[i]
            if os.path.isdir(link):
                for file in os.listdir(link):
                    if file == target:
                        _opath = os.path.join(link,file)
                        break

        self.original_img_root = _opath
        resultImgs = []
        self.Images = []

        filters = []
        filter1 = self.combo_filter1_lotinput_image.get()
        filter2 = self.combo_filter2_lotinput_image.get()
        filter3 = self.filter3_entry.get()
        if filter1 != '':
            filters.append(filter1)
        if filter2 != '':
            filters.append(filter2)
        if filter3 != '':
            filters.append(filter3)
            

        if not os.path.isdir(self.cachePath):
            os.mkdir(self.cachePath)
        else:
            for file in os.listdir(self.cachePath):
                os.remove(os.path.join(self.cachePath,file))
        '''
        def findfunc(targ,filt):
            for root,_,files in os.walk(targ):
                for file in files:
                    if re.findall(filt,file) != []:
                        filepath = os.path.join(root,file)
                        self.Images.append(filepath)
                        self.cached_Images.append(False)'''
        # try:
        #     for root,_,files in os.walk(_opath):
        #         for file in files:
        #             if os.path.splitext(file)[1] == '.jpg':
        #                 #필터 알고리즘
        #                 #필터가 빈 칸이 아니면 적용해야함
        #                 #find 해서 1이상일때 필터가 빈칸일경우 0 아닐경우 찾으면 1이상 아니면 -1
        #                 splt = str.split(file,'_')

        #                 if (splt[1] == filter1 or filter1 == '') and (splt[2] == filter2 or filter2 == '') and str.find(file,filter3) != -1:
        #                     filepath = os.path.join(root,file)
        #                     self.Images.append(filepath)
        #                     self.cached_Images.append(False)
        #                 else:
        #                     pass
        # except Exception as e:
        #     self.append_log(e)
        trays = []

        for dir in os.listdir(_opath):
            _dirpath = os.path.join(_opath,dir)
            if os.path.isdir(_dirpath):
                trays.append(os.path.join(_dirpath,'RawImage'))
        

        for tray in trays:
            for file in os.listdir(tray):
                filesplit = str.split(file,'+')[0]
                if all(filter_word in filesplit for filter_word in filters):
                    self.Images.append(os.path.join(tray,file))
                    self.cached_Images.append(False)
                    #self.append_log(file)


        
        self.show_image(self._img_show_idx)

    def autofill(self,target:str):
        if target =='cnt':
            self.combo_filter1_lotinput_image.delete(0,tk.END)
            self.combo_filter1_lotinput_image.insert(0,'T5')
            self.combo_filter2_lotinput_image.delete(0,tk.END)
            self.combo_filter2_lotinput_image.insert(0,'Image03')
        elif target == 'liner1':
            self.combo_filter1_lotinput_image.delete(0,tk.END)
            self.combo_filter1_lotinput_image.insert(0,'B2')
            self.combo_filter2_lotinput_image.delete(0,tk.END)
            self.combo_filter2_lotinput_image.insert(0,'Image12')
        elif target == 'liner2':
            pass
            
    def autofillfn_cnt(self):
        self.autofill('cnt')
    
    def autofillfn_liner1(self):
        self.autofill('liner1')

    def add_element_rev(self,images:list):
        '''
        리뷰이미지 로드할 컨테이너 추가 메서드
        '''
        for i in range(len(images)):
            self.num_nowshoing_rev += 1
            img = Image.open(images[i])
            isize = img.size
            ratio = 110/isize[1]
            wishsize = (math.floor(isize[0]*ratio),math.floor(isize[1]*ratio))
            img.thumbnail(wishsize)
            tkimg = ImageTk.PhotoImage(img)
            
            try:
                lbl = tk.Label(self.canvas_reviewViewer.winfo_children()[i],image=tkimg)
                lbl.img = tkimg
                lbl.pack(side='left',padx=5)
            except:
                pass

    def add_HDLlog(self):
        #추가하려는 데이터
        wishdata = self.tree_showed.get_children()[0]
        wishValue = self.tree_showed.item(wishdata,'values')
        
        #책갈피
        treelen = len(self.tree_handlerviewer.get_children())
        canAdd = True
        if treelen > 0:
            for item in self.tree_handlerviewer.get_children():
                verify_data = self.tree_handlerviewer.item(item,'values')
                if verify_data[2] == wishValue[2]:
                    canAdd = False
                    self.append_log('이미 존재하는 항목을 추가하려 하였습니다.')
                    return
                else:
                    pass
        if canAdd:
            self.tree_handlerviewer.insert('',tk.END,values=wishValue)


    def remove_HDLlog_selected(self):
        try:
            selected_log = self.tree_handlerviewer.selection()[0]
            self.tree_handlerviewer.delete(selected_log)
        except:
            self.append_log('선택된 책갈피 항목이 없습니다.')

    def remove_HDLlog_all(self):
        try:
            for item in self.tree_handlerviewer.get_children():
                self.tree_handlerviewer.delete(item)
            self.append_log('전체 책갈피 삭제완료.')
        except:
            self.append('전체 항목 삭제에 실패했습니다.')

    def add2clipboard_HDL_all(self):
        clipboard_data = []
        row_data = []
        row_data.append('Count\tPosition\tBarcode\tLoadPort\tLoadTray\tLoadPos\tLoadPicker\tLoadBuffer\tLoadIndex\tMainIndex\tTransIndex\tTransBuffer\tTransPicker\tGoodPicker\tJudge\tDefectCode')
        for item in self.tree_handlerviewer.get_children():
            row = self.tree_handlerviewer.item(item,'values') #줄 데이터(튜플)
            row_data.append('\t'.join(row))
            clipboard_data = '\n'.join(row_data)
        self.tree_handlerviewer.clipboard_clear()
        self.tree_handlerviewer.clipboard_append(clipboard_data)

    def init_rev(self):
        
        for element in self.canvas_reviewViewer.winfo_children():
            element.destroy()
        
        self.frame_rev1 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev1.place(x=5,y=5,width=110,height=110)

        self.frame_rev2 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev2.place(x=125,y=5,width=110,height=110)
        
        self.frame_rev3 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev3.place(x=245,y=5,width=110,height=110)
        
        self.frame_rev4 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev4.place(x=365,y=5,width=110,height=110)
        
        self.frame_rev5 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev5.place(x=485,y=5,width=110,height=110)
        
        self.frame_rev6 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev6.place(x=5,y=125,width=110,height=110)

        self.frame_rev7 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev7.place(x=125,y=125,width=110,height=110)
        
        self.frame_rev8 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev8.place(x=245,y=125,width=110,height=110)
        
        self.frame_rev9 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev9.place(x=365,y=125,width=110,height=110)
        
        self.frame_rev10 = tk.Frame(self.canvas_reviewViewer,border=1,relief='solid')
        self.frame_rev10.place(x=485,y=125,width=110,height=110)

        
    def insert_event(self,event): #로그 입력 - 키입력 바인딩용 함수
        self.add_HDLlog()

    def save_logged_img(self):
        ''''''
        try:
            shutil.rmtree('./loggedImages')
            os.mkdir('./loggedImages')
        except:
            os.mkdir('./loggedImages')

        dst = os.path.abspath('./loggedImages/')
        targets = []
        for item in self.tree_handlerviewer.get_children():
            row_data = self.tree_handlerviewer.item(item,'values')
            targets.append(row_data[2])

        filter_1 = self.combo_filter1_lotinput_image.get()
        filter_2 = self.combo_filter2_lotinput_image.get()

        for target in targets:
            for path in self.Images:
                sptxt = str.split(os.path.basename(path),'_')
                if sptxt[1] == filter_1 and sptxt[2] == filter_2 and sptxt[3] == target + '.jpg':
                    shutil.copy2(src=path,dst=dst)

        os.startfile(dst)

            
    def rmcachedata(self): #캐시 데이터 삭제
        directories = ['./cachedData','./review','./loggedImages','./judgement']
        for dir in directories:
            if os.path.isdir(dir):
                shutil.rmtree(dir)
                os.mkdir(dir)
            else:
                os.mkdir(dir)
        self.append_log('캐시 삭제 성공')


    def openjudgementData(self):
        ''''''
        os.startfile(os.path.abspath('./judgement/'))

        #print(tempList) #모든 의뢰된 적 있는 바코드 리스트

    def getUserData(self,year,month,day,model,lot,barcode):
        hpath = HANDLER(2024,month,day)
        _yesterday = datetime.fromisoformat(f'2024{str.zfill(str(month),2)}{str.zfill(str(day),2)}')-timedelta(1)
        _path = hpath.__dict__[model]
        _path = f'{os.path.dirname(os.path.dirname(_path))}/Dispatcher/{year}{str.zfill(str(month),2)}{str.zfill(str(day),2)}.txt'
        #print(_path)
        
        MDJ_IP = ''
        targetTime = 0
        hasFOUND = False

        for line in reversed(list(open(_path))):
            try:
                linesplt = str.split(line,',')
                if hasFOUND and linesplt[1] == 'REPLY':
                    MDJ_IP = linesplt[2]
                    #print('성공')
                    break

                if linesplt[4] == lot and linesplt[8] == barcode:
                    if linesplt[1] == 'REPLY':
                        MDJ_IP = linesplt[2]
                        _h = int(line[1:3])
                        _m = int(line[4:6])
                        _s = int(line[7:9])
                        targetTime = _h*60*60 + _m*60 + _s
                        
                        break
                    elif linesplt[1] == 'REQUEST':
                        hasFOUND = True
                        pass

            except:
                pass


        if MDJ_IP == '':
            self.append_log('로그를 찾을 수 없습니다.')
            return

        targets = [] # MDJ Process 로그 목록

        _mdjpath = f'//{MDJ_IP}/ros'
        #print(_mdjpath)

        for root,_,files in os.walk(_mdjpath):
            for file in files:
                if file == f'{year}-{str.zfill(str(month),2)}-{str.zfill(str(day),2)}_Process.txt':
                    targets.append(os.path.join(root,file))
                    targets.append(os.path.join(root,f'{_yesterday.year}-{str.zfill(str(_yesterday.month),2)}-{str.zfill(str(_yesterday.day),2)}_Process.txt'))
        
        
        _lastOpAtMidnight = ''
        _opChangelog = []
        for i in range(len(targets)):
            #print(targets[i])
            if i == 0:
                for line in reversed(list(open(targets[i],encoding='EUC-KR'))):
                    if str.find(line,'작업자변경') != -1:
                        #print(line)
                        _h = int(line[1:3])
                        _m = int(line[4:6])
                        _s = int(line[7:9])
                        _op = str.split(line,',')[1][:-1]
                        _convertedTime = _h*60*60 + _m*60 + _s
                        _opChangelog.append(f'{_convertedTime}/{_op}')
                        
                        
            elif i == 1:
                for line in reversed(list(open(targets[i],encoding='EUC-KR'))):
                    if str.find(line,'작업자변경') != -1:
                        # _h = int(line[1:3])
                        # _m = int(line[4:6])
                        # _s = int(line[7:9])
                        _lastOpAtMidnight = str.split(line,',')[1][:-1]
                        break
                        #_convertedTime = _h*60*60 + _m*60 + _s
        result = ''
        #print(targetTime)
        #print(_lastOpAtMidnight)
        isfound = False
        for log in _opChangelog:
            if targetTime > int(log[0:5]):
                result = str.split(log,'/')[1]
                isfound = True
                break
        
        if isfound == False:
            result = _lastOpAtMidnight
        return result
    
    
    def getUserDataTrigger(self):
        _op = self.getUserData(2024,self.combo_lotinput_month.get(),self.combo_lotinput_day.get(),self.combo_lotinput_model.get(),self.viewedLot,self.viewedBarcode)
        self.append_log(_op)
        

        
        


    def on_tab_change(self, event): #메인컨테이너 자식요소 세팅
        tab = event.widget.tab('current')['text']
        try:
            for i in self.mainContainer.winfo_children():
                i.destroy()
        except:
            print('can\'t init')
        if tab == '원본이미지 조회': 
            ''''''
            self.frame_image_container = tk.Frame(self.mainContainer,borderwidth=2,width=655,height=595,bg='gray')
            self.frame_image_container.place(x=5,y=55)
            self.label_lotinput_image = tk.Label(self.frame_image_container,bd=2,bg='gray',width=650,height=650)
            
            

            self.label_lotinput_image.place(x=0,y=-25)
            self.label_lotinput_image.update_idletasks()

            self.filter1_combo_list = ['T1','T2','T3','T4','T5','B1','B2','A1','A2']
            self.combo_filter1_lotinput_image = ttk.Combobox(self.mainContainer,values=self.filter1_combo_list)
            self.combo_filter1_lotinput_image.place(x=5,y=5)
            self.combo_filter1_lotinput_image.configure(width=4)

            self.filter2_combo_list = ['Image01','Image02','Image03','Image04','Image05','Image06','Image07','Image08','Image09','Image10','Image11','Image12','Image13','Image14','Image15','Image16']
            self.combo_filter2_lotinput_image = ttk.Combobox(self.mainContainer,values=self.filter2_combo_list)
            self.combo_filter2_lotinput_image.place(x=60,y=5)
            self.combo_filter2_lotinput_image.configure(width=8)

            self.filter3_entry = ttk.Entry(self.mainContainer)
            self.filter3_entry.place(x=145,y=5)

            self.search_btn = ttk.Button(self.mainContainer, command=self.search, text='검색', width=10)
            self.search_btn.place(x=300,y=3)

            self.autoFill_cnt = ttk.Button(self.mainContainer,text='커넥터',width=7,command=self.autofillfn_cnt)
            self.autoFill_cnt.place(x=5,y=30)
            
            self.autoFill_Liner1 = ttk.Button(self.mainContainer,text='라이너1',width = 7,command=self.autofillfn_liner1)
            self.autoFill_Liner1.place(x=65,y=30)


            self.label_currentImgNum = ttk.Label(self.mainContainer,text='0/0')
            self.label_currentImgNum.place(x=320,y=650)

            self.entry_showing_LotID = ttk.Entry(self.mainContainer)
            self.entry_showing_LotID.place(x=15,y=653)
            self.entry_showing_LotID.configure(width=16)

            self.entry_showing_Barcode = ttk.Entry(self.mainContainer)
            self.entry_showing_Barcode.place(x=15,y=678)
            self.entry_showing_Barcode.configure(width=28)

            self.btn_toggle_autoview = ttk.Button(self.mainContainer,text='자동넘기기 켜기',command=self.toggle_autoview,width=13)
            self.btn_toggle_autoview.place(x=470,y=650)

            self.btn_openorgfolder = ttk.Button(self.mainContainer,text='원본 폴더 열기',command=self.open_imagedir)
            self.btn_openorgfolder.place(x=570,y=650)

            self.btn_openrevfolder = ttk.Button(self.mainContainer,text='리뷰 폴더 열기',command=self.open_revdir)
            self.btn_openrevfolder.place(x=570,y=675)
            
            self.btn_rmcache = ttk.Button(self.mainContainer,text='캐시 삭제',command=self.rmcachedata,width=13)
            self.btn_rmcache.place(x=470,y=675)


            
            #리뷰이미지 뷰어 캔버스
            self.canvas_reviewViewer = tk.Canvas(self.mainContainer)
            self.canvas_reviewViewer.configure(border=1,relief='sunken')
            self.canvas_reviewViewer.place(x=665,y=5,width=600,height=240)
            self.canvas_reviewViewer.configure(bg='gray')

            
            
            #핸들러 요소
            handlercolumns = ['Count','Position','Barcode','LoadPort','LoadTray','LoadPos','LoadPicker','LoadBuffer','LoadIndex','MainIndex','TransIndex','TransBuffer','TransPicker','GoodPicker','Judge','DefectCode']
            self.tree_showed = ttk.Treeview(self.mainContainer,columns=handlercolumns,show='headings')
            self.tree_showed.place(x=665,y=305,width=600,height=48)
            
            for num in range(len(handlercolumns)):
                self.tree_showed.heading(column=str(num),text=handlercolumns[num],anchor='c')
            for col in self.tree_showed["columns"]:
                self.tree_showed.column(col, width = int(600/len(self.tree_showed["columns"])))
            
            self.init_rev()

            #lot 기록 Treeview요소

            self.btn_addtoTreeview = ttk.Button(self.mainContainer)

            self.tree_handlerviewer = ttk.Treeview(self.mainContainer,columns=handlercolumns,show="headings")
            self.tree_handlerviewer.place(x=665,y=400,width=600,height=300)

            self.tree_handlerviewer_yscroll = ttk.Scrollbar(self.tree_handlerviewer,orient='vertical',command=self.tree_handlerviewer.yview)
            self.tree_handlerviewer.configure(yscrollcommand=self.tree_handlerviewer_yscroll.set)
            self.tree_handlerviewer_yscroll.pack(side='right',fill='y')

            for num in range(len(handlercolumns)):
                self.tree_handlerviewer.heading(column=str(num),text=handlercolumns[num])
            for col in self.tree_handlerviewer["columns"]:
                self.tree_handlerviewer.column(col,width = int(500/len(self.tree_handlerviewer["columns"])))

            self.app.bind('<Insert>',self.insert_event)


            #로그 선택 삭제버튼
            self.btn_log_rmselected = ttk.Button(self.mainContainer,text= '선택 삭제',command=self.remove_HDLlog_selected)
            self.btn_log_rmselected.place(x=900,y=370)

            #로그 전체 삭제버튼
            self.btn_log_rmselected = ttk.Button(self.mainContainer,text= '전체 삭제',command=self.remove_HDLlog_all)
            self.btn_log_rmselected.place(x=990,y=370)


            #로그로 저장버튼
            self.btn_handler2log = ttk.Button(self.mainContainer,text='책갈피로',command=self.add_HDLlog)
            self.btn_handler2log.place(x=1080,y=370)


            #로그 클립보드로 복사버튼
            self.btn_log2clipboard = ttk.Button(self.mainContainer,text='복사',command=self.add2clipboard_HDL_all)
            self.btn_log2clipboard.place(x=1170,y=370)

            #로그 기록 이미지 저장버튼
            self.btn_log2saveimg = ttk.Button(self.mainContainer,text='이미지 저장',command=self.save_logged_img)
            self.btn_log2saveimg.place(x=665,y=370)

            
            #todo - 양품/리페어/NG/타임 이미지보기
            self.btn_openDetailJudge = ttk.Button(self.mainContainer,text='판정상세보기',command=self.openjudgementData)
            self.btn_openDetailJudge.place(x=380,y=675)

            self.testbtn = ttk.Button(self.mainContainer,text='작업자정보',command=self.getUserDataTrigger)
            self.testbtn.place(x=380,y=650)
            

if __name__ == "__main__":
    ''''''
    app = App()