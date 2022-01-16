#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install schedule
import schedule
from time import sleep
from datetime import datetime
import time


# 01 定期実行する関数を準備
def task():
    now = datetime.now()
    print("タスク実行中 : " + now.strftime('%H:%M:%S.%f'))


def schedule01():
    start_time = datetime.now()
    print("start : " + start_time.strftime('%H:%M:%S.%f'))
    # 02 スケジュール登録
    # 1秒毎のjob実行を登録
    schedule.every(1).seconds.do(task)
    # # 1分毎のjob実行を登録
    # schedule.every(1).seconds.do(task)
    # # 1時間毎のjob実行を登録
    # schedule.every(1).hours.do(task)
    # # AM11:00のjob実行を登録
    # schedule.every().day.at("11:00").do(task)
    # # 日曜日のjob実行を登録
    # schedule.every().sunday.do(task)
    # # 水曜日13:15のjob実行を登録
    # schedule.every().wednesday.at("13:15").do(task)

    # 03 イベント実行
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    schedule01()


if __name__ == '__main__':
    main()
