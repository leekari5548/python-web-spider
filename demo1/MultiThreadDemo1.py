import threading
import time


def test(second):
    print(f'Thread {threading.current_thread().name} is running...')
    print(f'Thread {threading.current_thread().name} sleeping {second}s...')
    time.sleep(second)
    print(f'Thread {threading.current_thread().name} slept end...')


if __name__ == '__main__':
    threads = []
    print('MainThread start...')
    # for i in [1, 5]:
    thread1 = threading.Thread(target=test, args=[4])
    thread1.start()
    thread2 = threading.Thread(target=test, args=[5])
    thread2.setDaemon(True)
    thread2.start()
    print('MainThread end...')