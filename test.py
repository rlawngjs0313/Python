import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from selenium import webdriver
 
form_class = uic.loadUiType('TicketingMacro.ui')[0] 
 
 
class MyWindow(QtWidgets.QMainWindow, form_class):
    is_data_disabled = False  # 정보 입력창 비활성화 여부
    time = None  # 스레드로부터 받아오는 현재 시간
 
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.user_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.seats_number_spinbox.setValue(1)
        self.date_edit.setDate(QtCore.QDate.currentDate())
        self.time_edit.setTime(QtCore.QTime.currentTime())
        self.disableElements(self.time_edit, self.label_auto_start)
 
        self.apply_btn.clicked.connect(self.initData)  # 확인 버튼 클릭
        self.login_btn.clicked.connect(self.startLogin)  # 로그인 버튼 클릭
        self.start_ticketing_btn.clicked.connect(self.startTicketing)  # 시작 버튼 클릭
        self.seats_number_spinbox.valueChanged.connect(self.checkSeatsNumber)  # 좌석 개수 변경
        self.use_auto_start.stateChanged.connect(self.useAutoStart)  # 자동 시작 여부 변경
 
    def initData(self):
        if not self.is_data_disabled:  # 정보 입력창 활성화 시
            self.user_id = self.user_id_input.text()  # 아이디
            self.user_password = self.user_password_input.text()  # 비밀번호
            self.product_code = self.product_code_input.text()  # 공연 코드
            self.seats_number = self.seats_number_spinbox.value()  # 좌석 개수
            self.use_random_seat = self.use_seat_select.isChecked()  # 중간(랜덤) 선택 여부
            self.is_canceled_ticketing = self.canceled_ticket_mode.isChecked()  # 취켓팅 여부
            if self.use_auto_start.isChecked():  # 자동 시작 시 시간 24시간 방식 -> 12시간 방식 변경
                self.time = self.time_edit.time()
                self.time = str(self.time.toPyTime())[:6] + '00'
                if int(self.time[0:2]) > 12:
                    self.new_time_h = int(self.time[0:2]) - 12
                    self.time = str(self.new_time_h) + self.time[2:]
                    if self.new_time_h < 10:
                        self.time = '0' + self.time
                elif self.time[0:2] == '00':
                    self.time = '12' + self.time[2:]
            self.date = self.date_edit.date()  # 날짜
            self.date = self.date.toPyDate()
            self.date = str(self.date).replace('-', '')
            self.disableElements(self.user_id_input, self.user_password_input, self.product_code_input, self.date_edit,
                                 self.seats_number_spinbox, self.use_seat_select, self.use_auto_start, self.time_edit, self.canceled_ticket_mode)  # 요소 비활성화
            self.is_data_disabled = True
            self.apply_btn.setText('수정')
            QtWidgets.QMessageBox.information(self, '완료', '정보 입력이 완료되었습니다.')
        else:
            self.is_data_disabled = False
            self.apply_btn.setText('확인')
            self.enableElements(self.user_id_input, self.user_password_input, self.product_code_input, self.date_edit,
                                self.seats_number_spinbox, self.use_seat_select, self.use_auto_start, self.time_edit, self.canceled_ticket_mode)  # 요소 활성화
 
    # 좌석 개수 변경
    def checkSeatsNumber(self):
        if self.seats_number_spinbox.value() > 4:
            self.seats_number_spinbox.setValue(4)
            QtWidgets.QMessageBox.critical(self, '오류', '최대 좌석 개수는 4개입니다.')
        if self.seats_number_spinbox.value() < 1:
            self.seats_number_spinbox.setValue(1)
            QtWidgets.QMessageBox.critical(self, '오류', '최소 좌석 개수는 1개입니다.')
 
    # 요소들 입력받아 한꺼번에 활성화
    def enableElements(self, *elements):
        for element in elements:
            element.setEnabled(True)
 
    # 요소들 입력받아 한꺼번에 비활성화
    def disableElements(self, *elements):
        for element in elements:
            element.setEnabled(False)
 
    # 자동시작 시
    def useAutoStart(self):
        if self.use_auto_start.isChecked():
            self.enableElements(self.time_edit, self.label_auto_start)
        else:
            self.time = None
            self.disableElements(self.time_edit, self.label_auto_start)
 
    # 로그인
    def startLogin(self):
        self.time_th = TimeThread()
        if self.apply_btn.text() == '확인':  # 확인 버튼을 누르지 않았을 때
            QtWidgets.QMessageBox.critical(self, '오류', '좌석 정보를 입력하세요.')
        else:
            # Dictionary 형식으로 정보 전달
            ticketing_data_to_send = {
                'user_id': self.user_id,  # 아이디
                'user_pw': self.user_password,  # 비밀번호
                'product_code': self.product_code,  # 공연 번호
                'date': self.date,  # 공연 날짜
                'time': self.time,  # 자동시작 시간
                'seats_number': self.seats_number,  # 좌석 개수
                'use_random_seat': self.use_random_seat,  # 랜덤 선택 여부
                'time_signal': self.time_th.time_signal,  # 시간 스레드
                'is_canceled': self.is_canceled_ticketing  # 취켓팅 여부
            }
            self.apply_btn.setEnabled(False)  # 확인(수정) 버튼 비활성화
            self.login_btn.setEnabled(False)  # 로그인 버튼 비활성화
            # 시간/티켓팅 스레드 시작
            self.time_th.start()
            self.time_th.time_signal.connect(self.changeTime)
            self.ticketing_th = TicketingThread(ticketing_data=ticketing_data_to_send)
            self.ticketing_th.start()
 
    # 티켓팅 시작
    def startTicketing(self):
        self.ticketing_th.start_ticketing = True
 
    # 타이머 시작
    def startTimer(self):
        self.time_th = TimeThread()
        self.time_th.start()
        self.time_th.time_signal.connect(self.changeTime)
 
    @QtCore.pyqtSlot(str)
    def changeTime(self, time):
        if time == 'error':  # 웹드라이버(시계) 종료시 알림
            QtWidgets.QMessageBox.critical(self, '오류', '타이머를 끄지 마십시오.')
        else:
            self.now_time.setText(time)
 
 
class TimeThread(QtCore.QThread):
    time_signal = QtCore.pyqtSignal(str)
 
    def run(self):
        while True:
            self.driver = webdriver.Chrome('chromedriver.exe')
            #네이버 시계 접속
            self.driver.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%9C%EA%B3%84&oquery=%EC%8B%9C%EA%B3%84&tqi=UEMiLdprvTossFQzFhCssssssKG-165498')
            while True:
                try:
                    text = self.driver.find_element_by_css_selector('#_cs_domestic_clock > div._timeLayer.time_bx > div > div').text  # 네이버 시계 text
                    text = text.replace('\n', '').replace(' ', '')[0:8]
                except:
                    self.time_signal.emit('error')  # 웹드라이버(시계) 종료 시 error emit
                    break
                self.time_signal.emit(''.join(text))
 
 
class TicketingThread(QtCore.QThread):
    def __init__(self, ticketing_data, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.user_id = ticketing_data['user_id']
        self.user_password = ticketing_data['user_pw']
        self.product_code = ticketing_data['product_code']
        self.date = ticketing_data['date']
        self.set_time = ticketing_data['time']
        self.seats_number = ticketing_data['seats_number']
        self.use_random_seat = ticketing_data['use_random_seat']
        self.time_signal = ticketing_data['time_signal']
        self.is_canceled_ticketing = ticketing_data['is_canceled']
        self.driver = self.driver = webdriver.Chrome('chromedriver.exe')
        self.time_signal.connect(self.checkTime)  # 시간 스레드와 연결(자동시작)
        self.is_logined = False  # 로그인 여부 False
        self.start_ticketing = False  # 시작 여부 False
 
    # 요소는 반드시 CSS 셀렉터로만(ID 우선)
 
    # 로그인
    def login(self):
        self.driver.get('https://ticket.interpark.com/Gate/TPLogin.asp')
        iframes = self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(iframes[0])
        self.driver.find_element_by_id('userId').send_keys(self.user_id)
        self.driver.find_element_by_id('userPwd').send_keys(self.user_password)
        self.driver.find_element_by_id('btn_login').click()
        self.driver.get('https://ticket.interpark.com/')  # 인터파크 메인 페이지로 강제 접속
 
    def selectSeat(self):
        self.failed_to_get_ticket = False  # 취켓팅용-기본적으로 성공으로 표시
        # 직링 생성
        self.url = 'http://poticket.interpark.com/Book/BookSession.asp?GroupCode={}&Tiki=N&Point=N&PlayDate={}&PlaySeq=001&BizCode=&BizMemberCode='.format(self.product_code, self.date)
        self.driver.get(self.url)
 
        # 요소를 찾을 때까지 무한 루프(찾지 못하면 예외)
        while True:
            try:
                first_iframe = self.driver.find_element_by_id('ifrmSeat')  # 첫번째 아이프레임
            except:
                continue
            else:
                break
        self.driver.switch_to.frame(first_iframe)
        while True:
            try:
                next_iframe = self.driver.find_element_by_id('ifrmSeatDetail')  # 두번째 좌석선택 아이프레임
            except:
                continue
            else:
                break
        self.driver.switch_to.frame(next_iframe)
 
        self.loop_time = 0  #취켓팅용
        while True:
            try:
                elements = self.driver.find_elements_by_class_name('stySeat')
                self.loop_time += 1
                # 취켓팅하면서 루프를 100번 돌면 루프 탈출
                if self.is_canceled_ticketing and (self.loop_time > 100):
                    self.failed_to_get_ticket = True  # 잔여 좌석 인식 실패(개수 0)
                    break
            except:
                continue
            else:
                if len(elements) == 0:  # 예외는 나지 않았지만 좌석이 인식되지 못한 경우
                    continue
                else:
                    break
 
        while len(elements) > 0:
            # 첫번째부터 1개 선택
            if (not self.use_random_seat) and (self.seats_number == 1):
                self.driver.find_element_by_css_selector('#TmgsTable > tbody > tr > td > img:nth-child(3)').click()  # 바로 첫번째 요소 선택
 
            # 여러개 선택
            elif not self.use_random_seat:
                seat_count = 0
                for element in elements:
                    if seat_count < self.seats_number:
                        element.click()
                        seat_count += 1
 
            # 랜덤/여러개 선택
            elif self.use_random_seat:
                start_seat = random.randint(
                    int(len(elements) / 2), len(elements) - self.seats_number)
                for i in range(start_seat, start_seat + self.seats_number):
                    if start_seat < self.seats_number + start_seat:
                        elements[i].click()
            try:
                self.driver.switch_to.default_content()  # 제일 바깥으로 아이프레임 벗어남
                self.driver.switch_to.frame(first_iframe)  # 첫번째 아이프레임으로 다시 변경
                self.driver.find_element_by_id('NextStepImage').click()  # 다음 버튼 클릭
                self.driver.find_element_by_class_name('title')  # 임의의 요소 찾아서 크롬 종료 방어
            except:
                continue
            else:
                break
 
    @QtCore.pyqtSlot(str)
    def checkTime(self, data):
        self.time = data
 
    def run(self):
        # 로그인되지 않았다면 로그인
        if not self.is_logined:
            self.login()
            self.is_logined = True
        while True:
            if str(self.set_time) == str(self.time):  # 입력한 시간하고 일치한다면
                self.start_ticketing = True
            if self.start_ticketing:
                self.selectSeat()  # 티켓팅 시작
                if not self.is_canceled_ticketing:  # 취켓팅이 아니고 끝난 경우는 성공으로 처리
                    self.start_ticketing = False
                if not self.failed_to_get_ticket:  # 취켓팅인데 성공한 경우
                    self.start_ticketing = False
                if self.is_canceled_ticketing and self.failed_to_get_ticket:  # 취켓팅인데 실패한 경우
                    pass
 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()