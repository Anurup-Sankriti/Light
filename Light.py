import threading
import time
import tkinter as tk

lock = threading.Lock()
count = 0
lights = "on"
def a():
  global count
  global lights
  while(1):
    lock.acquire()
    try:
      count += 1
      if count%2 == 0 :
        #print("off")
        lights = "off"
        print(lights)

      else:
        #print("on")
        lights = "on"
        print(lights)




    finally:
      time.sleep(1)
      lock.release()


t = threading.Thread(name='a', target=a)
t.start()


r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()

r.mainloop()