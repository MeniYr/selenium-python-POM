import datetime
import os
import time


class Exceptions_logs(object):


    def send(self, e, pic_name="no pic to save"):
        try:
            os.chdir("C:/Python/AutomationProject/Logs")
            self.f = open(f'log_{str(time.strftime("%m-%d-%Y_%H,%M", time.localtime()))}_.txt', 'a')
            if self.f.tell() > (1000 * 1024):
                self.f = open(f'../log_{time.strftime("%m/%d/%Y_%H:%M", time.localtime())}.txt', 'a')
                raise ValueError(f'file is up to 1000kb {self.f.tell()}, open new file')
            else:
                date = datetime.datetime.now()
                self.f.write(f"""
name: Meni Rotblat.
date: {date.now()}. 
description: {e}.
pic:{pic_name}
                     """)
                self.f.flush()
                self.f.close()
        except Exception as e:
            print(e)

