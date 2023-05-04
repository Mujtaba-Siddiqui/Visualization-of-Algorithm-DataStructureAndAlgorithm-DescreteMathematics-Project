

import time
from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Algo Visualizer')
root.geometry('855x550')
root.config(bg='grey')

algo_var = StringVar()
srch = StringVar()
data = []

#_____ Draw data _______#
# hello world assalmualikum kase ho ap sb inshallah sab bhtr hoge lkm

def drdata(data, clr):
    canva.delete('all')
    ch = 380
    cw = 800
    xw = cw / (len(data) + 1)
    ofs = 30
    sp = 10
    n = [i / max(data) for i in data]
    for i, h in enumerate(n):
        x0 = i * xw + ofs + sp
        y0 = ch - h * 320
        x1 = (i + 1) * xw + ofs
        y1 = ch

        canva.create_rectangle(x0, y0, x1, y1, fill=clr[i])
        canva.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


#______ Draw data _______#

#______  Generate  ______#


def gen():
    global data
    minv = int(minen.get())
    maxv = int(maxen.get())
    size = 15
    data = []
    for i in range(15):
        data.append(random.randrange(minv, maxv + 1))
    drdata(data, ['red' for i in range(len(data))])


#______  Generate  ______#

#______ Merge Sort _______#


def mergesort(data, drdata, speed):
    merge_sort(data, 0, len(data) - 1, drdata, speed)


def merge_sort(data, l, r, drdata, speed):
    if l < r:
        mid = (l + r) // 2
        merge_sort(data, l, mid, drdata, speed)
        merge_sort(data, mid + 1, r, drdata, speed)
        merge(data, l, mid, r, drdata, speed)


def merge(data, l, mid, r, drdata, speed):
    drdata(data, clrar(len(data), l, mid, r))
    time.sleep(speed)
    left_data = data[l:mid + 1]
    right_data = data[mid + 1:r + 1]

    li = ri = 0
    for i in range(l, r + 1):
        if li < len(left_data) and ri < len(right_data):
            if left_data[li] <= right_data[ri]:
                data[i] = left_data[li]
                li += 1
            else:
                data[i] = right_data[ri]
                ri += 1
        elif li < len(left_data):
            data[i] = left_data[li]
            li += 1
        else:
            data[i] = right_data[ri]
            ri += 1

    drdata(data, ['green' if l <= c <= r else 'white' for c in range(len(data))])
    time.sleep(speed)


def clrar(n, l, mid, r):
    clr = []
    for i in range(n):
        if l <= i <= r:
            if l <= i <= mid:
                clr.append('yellow')
            else:
                clr.append('blue')
        else:
            clr.append('white')

    return clr


#______ Merge Sort _______#


#______ Linear Search _______#


def linear_search(data, drdata, speed, x):
    for i in range(len(data)):
        if data[i] == int(x):
            drdata(data, ['green' if c == i else 'red' for c in range(len(data))])
            time.sleep(speed)
            break
        else:
            drdata(data, ['yellow' if c == i else 'red' for c in range(len(data))])
            time.sleep(speed)

#______ Linear Search _______#






#______ Binary Search _______#


def clrarr(data, low, mid, high):
    clr = []
    for i in range(len(data)):
        if i == mid:
            clr.append('yellow')
        elif i == low or i == high:
            clr.append('blue')
        else:
            clr.append('red')
    return clr


def bin_srch(data, drdata, speed, x):
    mergesort(data, drdata, speed)
    low = 0
    high = (len(data))-1
    while low <= high:
        mid = (low+high)//2
        drdata(data, clrarr(data, low, mid, high))
        time.sleep(speed)
        if data[mid] == x:
            drdata(data, ['green' if c == mid else 'red' for c in range(len(data))])
            time.sleep(speed)
            break
        elif data[mid] > x:
            high = mid-1
            drdata(data, ['blue' if i == low or i == high else 'red' for i in range(len(data))])
            time.sleep(speed)
        else:
            low = mid+1
            drdata(data, ['blue' if i == low or i == high else 'red' for i in range(len(data))])
            time.sleep(speed)

#______ Binary Search _______#

#______ Start Button _______#


def strt():
    global data

   

    if algo_var.get() == 'Linear Search':
        linear_search(data, drdata, speed, srch.get())

    elif algo_var.get() == 'Binary Search':
        bin_srch(data, drdata, speed, int(srch.get()))

#______ Start Button _______#

#______ GUI _______#


#__ GUI ___#
uif = Frame(root, width=600, height=200, bg='grey')
uif.grid(row=0, column=0, padx=10, pady=5)

canva = Canvas(root, width=830, height=380, bg='light yellow')
canva.grid(row=1, column=0, padx=10, pady=5)

Label(uif, text="Algorithm: ", bg='grey', fg='black', font=('algerian', 12)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
alg = ttk.Combobox(uif, textvariable=algo_var, values=[ 'Linear Search', 'Binary Search'])
alg.grid(row=0, column=1, padx=5, pady=5)
alg.current(0)

speed = 0.3

Label(uif, text='Enter Search Key : ').place(x=275, y=8)
Entry(uif, textvariable=srch).place(x=400,y=8)

Button(uif, text='Start', command=strt, bg='green', fg='white', height=1, width=10).grid(row=0, column=7, padx=30, pady=5)

Label(uif, text="Minimum :", bg='grey', fg='black', font=('algerian', 12)).grid(row=1, column=0, padx=1, pady=1, sticky=E)
Entry(uif, textvariable=minen).place(x=120,y=40)

Label(uif, text="Maximum:", bg='grey', fg='black', font=('algerian', 12)).grid(row=1, column=3, padx=2, pady=1, sticky=E)
Entry(uif, textvariable=maxen).place(x=350,y=40)

Label(uif, text="Size:15 ", bg='grey', fg='black', font=('algerian', 12)).grid(row=2, column=1, padx=1, pady=1, sticky=E)


Button(uif, text='Generate Sample Set', command=gen,bg='green', fg='black', font=('algerian', 10)).grid(row=2, column=4, padx=5, pady=5)

root.mainloop()