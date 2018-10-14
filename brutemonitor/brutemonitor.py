import threading
import time

import screenprinter
from color import colors

class SmartSleep(threading.Thread):
    def __init__(self, interval=0.25):
        super().__init__()
        self.interval = interval


    def run(self):
        time.sleep(self.interval)

class Brutemonitor(list):
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        self.__scrprntr = screenprinter.ScreenPrinter(None, 500, 1)
        self.__scrprntr.commit()

    def __getitem__(self, item):


        text = []

        alku = list.__getitem__(list(map(str, self)), slice(0, item))
        if len(alku):
            text.append(' '.join(alku))
            text.append(" ")

        text.append(f"{colors.green}{list.__getitem__(self, item)}{colors.white} ")
        text.append(' '.join(list.__getitem__(list(map(str, self)), slice(item + 1, len(self)))))
        text = ''.join(text)


        self.__scrprntr.blankScreen()
        self.__scrprntr.putText(0, 0, text)
        self.__scrprntr.commit()

        time.sleep(0.25)



        return list.__getitem__(self, item)

    def __setitem__(self, key, value):
        text = []
        list.__setitem__(self, key, value)

        alku = list.__getitem__(list(map(str, self)), slice(0, key))
        if len(alku):
            text.append(' '.join(alku))
            text.append(" ")

        text.append(f"{colors.blue}{list.__getitem__(self, key)}{colors.white} ")
        text.append(' '.join(list.__getitem__(list(map(str, self)), slice(key + 1, len(self)))))
        text = ''.join(text)

        self.__scrprntr.blankScreen()
        self.__scrprntr.putText(0, 0, text)
        self.__scrprntr.commit()

        time.sleep(0.5)


    def __str__(self):
        return ' '.join(map(str, self))

    # def __iter__(self):
    #     return (self.__getitem__(i) for i in range(len(self)))




a = Brutemonitor(list(range(100)))
for i in range(len(a)):
    a[i] = a[i] ** 2

a[0]