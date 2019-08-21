import sys
import pymysql
from functools import partial
from Ui_project import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget, QTableWidgetItem, QAbstractScrollArea, QHeaderView
from PyQt5 import QtGui
from Ui_select_dialog import Ui_Dialog as select_ui
from Ui_where_dialog import Ui_Dialog as where_ui
from Ui_delete_dialog import Ui_Dialog as delete_ui
from Ui_insert_dialog import Ui_Dialog as insert_ui
from Ui_update_dialog import Ui_Dialog as update_ui
from Ui_count_dialog import Ui_Dialog as count_ui
from Ui_sum_dialog import Ui_Dialog as sum_ui
from Ui_min_dialog import Ui_Dialog as min_ui
from Ui_max_dialog import Ui_Dialog as max_ui
from Ui_avg_dialog import Ui_Dialog as avg_ui
#from Ui__dialog import Ui_Dialog as _ui
class MainWindow(QMainWindow, Ui_MainWindow):
    sql = ""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    def onBindingUI(self):
        self.exe_btn.clicked.connect(self.exe)
        self.clear_btn.clicked.connect(self.clear)
        self.select_btn.clicked.connect(self.select_dialog)
        self.where_btn.clicked.connect(self.where_dialog)
        self.delete_btn.clicked.connect(self.delete_dialog)
        self.insert_btn.clicked.connect(self.insert_dialog)
        self.update_btn.clicked.connect(self.update_dialog)
        self.in_btn.clicked.connect(self.in_dialog)
        self.not_in_btn.clicked.connect(self.not_in_dialog)
        self.exists_btn.clicked.connect(self.exists_dialog)
        self.not_exists_btn.clicked.connect(self.not_exists_dialog)
        self.count_btn.clicked.connect(self.count_dialog)
        self.sum_btn.clicked.connect(self.sum_dialog)
        self.min_btn.clicked.connect(self.min_dialog)
        self.max_btn.clicked.connect(self.max_dialog)
        self.avg_btn.clicked.connect(self.avg_dialog)
        self.having_btn.clicked.connect(self.having_dialog)
        
    def in_dialog(self):
        self.input.append('in')
    def not_in_dialog(self):
        self.input.append('not in')
    def exists_dialog(self):
        self.input.append('where exists')
    def not_exists_dialog(self):
        self.input.append('where not exists')
    def having_dialog(self):
        self.input.append('having')   
    def clear(self):
        self.input.setText('')

    def get_table(self):
        target = self.sql[self.sql.find('update:')]
        target = self.sql[self.sql.find('from'):]
        if target.find('arena') != -1:
            table_name = 'arena'
        elif target.find('player') != -1:
            table_name = 'player'
        elif target.find('game') != -1:
            table_name = 'game'
        elif target.find('team') != -1:
            table_name = 'team'
        elif target.find('champ') != -1:
            table_name = 'champ'
        return table_name

    def  get_field(self):
        table_name = self.get_table()
        db = pymysql.connect("localhost","root","pwd","nba" )
        cursor = db.cursor() 
        cursor.execute("SHOW columns FROM "+table_name)
        field_info = cursor.fetchall()
        field_name_list = []
        for row in field_info:
            field_name_list.append(row[0])
        cursor.close()
        db.close()
        return field_name_list

    def get_col(self): 
        field_name_list = self.get_field()  
        col_name_list = []
        for field in field_name_list:
            if self.sql.find(field) != -1:
                col_name_list.append(field)
        if self.sql.find('*') == -1:
            return col_name_list
        else:
            return field_name_list

    def set_col(self):
        col_name_list = self.get_col()
        self.output.setColumnCount(len(col_name_list))
        self.output.setHorizontalHeaderLabels(col_name_list)
        
    def show_data(self,data):
        self.output.clear()
        i=0
        self.set_col()
        self.output.setRowCount(len(data))
        for row in data:
            for item in row:
                item = str(item)
                self.output.setItem(0,i,QTableWidgetItem(item))
                i = i+1

    def exe(self):
        db = pymysql.connect("localhost","root","1123","nba" )
        cursor = db.cursor() 
        self.sql = ''
        self.sql = self.input.toPlainText().lower()
        try:
            cursor.execute(self.sql)
            data = cursor.fetchall()
            db.commit()
        except:
            db.rollback()
        if self.sql.find('select') != -1:
            self.show_data(data)
        cursor.close()
        db.close()
        
    def select_dialog(self):
        Dialog = QDialog()
        ui = select_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select "+field+"\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def where_dialog(self):
        Dialog = QDialog()
        ui = where_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            condition = ui.condition_edt.toPlainText()
            sql = "where "+condition
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def delete_dialog(self):
        self.clear()
        Dialog = QDialog()
        ui = delete_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            condition = ui.condition_edt.toPlainText()
            sql = "delete from "+table+ "\nwhere "+condition
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def insert_dialog(self):
        self.clear()
        Dialog = QDialog()
        ui = insert_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            value = ui.value_edt.toPlainText()
            sql = "insert into "+table+ " ("+field+")\nvalues ("+value+")"
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def update_dialog(self):
        self.clear()
        Dialog = QDialog()
        ui = update_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            condition = ui.condition_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            value = ui.value_edt.toPlainText()
            sql = "update "+table+ "\nset "+field+" = "+value+"\nwhere "+condition
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def count_dialog(self):
        Dialog = QDialog()
        ui = count_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select count("+field+")\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def sum_dialog(self):
        Dialog = QDialog()
        ui = sum_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select sum("+field+")\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()
    
    def min_dialog(self):
        Dialog = QDialog()
        ui = min_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select min("+field+")\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()
    
    def max_dialog(self):
        Dialog = QDialog()
        ui = max_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select max("+field+")\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()

    def avg_dialog(self):
        Dialog = QDialog()
        ui = avg_ui()
        ui.setupUi(Dialog)
        def cancel(self):
            Dialog.close()
        def set_text(i):
            table = ui.table_edt.toPlainText()
            field = ui.field_edt.toPlainText()
            sql = "select avg("+field+")\nfrom "+table
            i.append(sql)
            Dialog.close()
        ok = partial(set_text,self.input)    
        ui.cancel_btn.clicked.connect(cancel)
        ui.ok_btn.clicked.connect(ok)
        Dialog.show()
        Dialog.exec_()
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
