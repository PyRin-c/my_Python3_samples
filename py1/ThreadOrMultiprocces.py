import threading
import time

def number100(name):
    for i in range(0,500):
        print(name + ":" + str(i))

class MyNumberClass(threading.Thread):
    def __init__(self,n):
        super(MyNumberClass,self).__init__()
        self.n = n

    def run(self):
        for i in range(0, 100):
            print(str(i))

def main():
    # シンプルな処理
    # set thread
    thread1 = threading.Thread(target=number100, args=("t1",),name="Thread 1")
    thread2 = threading.Thread(target=number100, args=("t2",), name="Thread 2")
    # start thread
    thread1.start()
    thread2.start()
    # join
    #thread1.join()
    #thread2.join()

    #classを利用した処理
    thread3 = MyNumberClass("t3")
    thread4 = MyNumberClass("t4")
    # start thread
    thread3.start()
    thread4.start()

    #deamonを使用したスレッド
    thread5 = MyNumberClass("t5")
    thread6 = MyNumberClass("t6")

    thread5.setDaemon(True)
    thread6.setDaemon(True)

    thread5.start()
    thread6.start()
    # スレッド数のカウント
    print("アクティブスレッド数:" + str(threading.active_count()))



if __name__ == "__main__":
    main()