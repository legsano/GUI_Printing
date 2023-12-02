import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import filedialog
from tkdocviewer import *
import os
#-------------------------------------------------------

#Setting window-----------------------------------------
def Ubah():
    secondWindow = tk.Tk()
    secondWindow.title("Printer Options")
    secondWindow.configure(background='#E7F6F2')
    secondWindow.resizable(0, 0)
    secondWindow.geometry("260x165")

    #value jenis kertas
    A = ["A4", "A3", "B2", "B3"]

    #value jenis tinta
    B = ["Hitam Putih", "Warna"]

    # value jenis tinta
    C = ["Canon Pixma MG2570S", "HP Color Laser", "Panasonic KX-MB2275", "Epson L360", "Fuji Xerox DocuPrint", "Brother DCP-T300"]

    # SECONDWINDOW--------------------------------------

    # label printer
    label3 = tk.Label(secondWindow, text="Printer", font="Arial 10",bg="#E7F6F2")
    label3.grid(row=0, column=0, sticky=W)

    # label Jenis kertas
    label = tk.Label(secondWindow, text="Jenis Kertas", font="Arial 10",bg="#E7F6F2")
    label.grid(row=1, column=0, sticky=W)

    #label tinta
    label1 = tk.Label(secondWindow, text="Jenis Tinta", font="Arial 10",bg="#E7F6F2")
    label1.grid(row=2, column=0, sticky=W)

    #label Jumlah Kertas
    label2 = tk.Label(secondWindow, text="Sisa Kertas", font="Arial 10",bg="#E7F6F2")
    label2.grid(row=3, column=0, sticky=W)

    # label Copy
    label2 = tk.Label(secondWindow, text="Copy", font="Arial 10",bg="#E7F6F2")
    label2.grid(row=4, column=0, sticky=W)

    #value Printer
    jenisPrinterDrop = ttk.Combobox(secondWindow, font="Arial 10", value=C,width=21)
    jenisPrinterDrop.grid(row=0, column=1, pady=2)
    setPD = jenisPrinter.get()
    jenisPrinterDrop.insert(0, setPD)
    jenisPrinterDrop.config(state="readonly")

    #velue Jenis Kertas
    jenisKertasDrop = ttk.Combobox(secondWindow, font="Arial 10", value=A, width=21)
    jenisKertasDrop.grid(row=1,column=1)
    setKD = jenisKertas.get()
    jenisKertasDrop.insert(0, setKD)
    jenisKertasDrop.config(state="readonly")

    #value tinta
    jenisTintaDrop = ttk.Combobox(secondWindow, font="Arial 10", value=B, width=21)
    jenisTintaDrop.grid(row=2, pady=2, column=1)
    setTD = jenisTinta.get()
    jenisTintaDrop.insert(0, setTD)
    jenisTintaDrop.config(state="readonly")

    #value jumlah Kertas
    jumlahKertasDrop = ttk.Entry(secondWindow, font="Arial 10")
    jumlahKertasDrop.grid(row=3,pady=2, column=1, sticky= tk.W+tk.E)
    setJK = jumlahKrts.get()
    jumlahKertasDrop.insert(0, setJK)

    #value jumlah copy
    jumlahCpyDrop = ttk.Entry(secondWindow, font="Arial 10")
    jumlahCpyDrop.grid(row=4, column=1, sticky= tk.W+tk.E)
    setJC = jumlahCopy.get()
    jumlahCpyDrop.insert(0, setJC)


    #pemanggilan setting
    def Setting():
        # manggil printer
        nilaiPrinter = jenisPrinterDrop.get()
        jenisPrinter.config(state="normal")
        jenisPrinter.delete(0, 'end')
        jenisPrinter.insert(0, nilaiPrinter)
        jenisPrinter.config(state="readonly")

        #manggil Jenis kertas
        nilaiJKertas = jenisKertasDrop.get()
        jenisKertas.config(state="normal")
        jenisKertas.delete(0, 'end')
        jenisKertas.insert(0, nilaiJKertas)
        jenisKertas.config(state="readonly")

        #manggil tinta
        nilaiTinta = jenisTintaDrop.get()
        jenisTinta.config(state="normal")
        jenisTinta.delete(0, 'end')
        jenisTinta.insert(0, nilaiTinta)
        jenisTinta.config(state="readonly")

        # manggil Keras
        nilaiKertas = jumlahKertasDrop.get()
        jumlahKrts.config(state="normal")
        jumlahKrts.delete(0, 'end')
        jumlahKrts.insert(0, nilaiKertas)
        jumlahKrts.config(state="readonly")

        #manggil copy
        nilaiCopy = jumlahCpyDrop.get()
        jumlahCopy.config(state="normal")
        jumlahCopy.delete(0, 'end')
        jumlahCopy.insert(0, nilaiCopy)
        jumlahCopy.config(state="readonly")

        secondWindow.destroy()
    #tombol save
    tombol = tk.Button(secondWindow, text="Save", command=Setting)
    tombol.grid(row=5, column=1,pady=3 ,padx= 3,sticky=E)



# WINDOW UTAMA
window = tk.Tk()
window.title("Desktop Printer")
window.geometry("1060x662")
window.configure(background='#E7F6F2')
window.resizable(0, 0)

#LABEL

tk.Label(window, text="        Monitoring        ", font="Arial 10", pady=2,relief="raised").grid(row=0,column=0,padx= 5,pady=5,columnspan=3, sticky=S+N+W+E)
tk.Label(window, text="Printer", font="Arial 10",bg="#E7F6F2").grid(row=1, column=0, sticky=W, padx=2)
tk.Label(window, text="Kertas", font="Arial 10",bg="#E7F6F2").grid(row=2, column=0, sticky=tk.W, padx=2)
tk.Label(window, text="Tinta", font="Arial 10",bg="#E7F6F2").grid(row=3, column=0, sticky=tk.W, padx=2)
tk.Label(window, text="JK", font="Arial 10",bg="#E7F6F2").grid(row=4, column=0, sticky=tk.W, padx=2)
tk.Label(window, text="Copy", font="Arial 10",bg="#E7F6F2").grid(row=5, column=0, sticky=tk.W, padx=2)
tk.Label(window, text="Tercetak", font="Arial 10",bg="#E7F6F2").grid(row=10, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=12, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=13, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=14, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=15, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=16, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=17, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=18, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=19, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=20, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=21, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=22, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=23, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=24, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=25, column=0, sticky=tk.W, padx=2)
tk.Label(window, text=" ", font="Arial 10",bg="#E7F6F2").grid(row=26, column=0, sticky=tk.W, padx=2)


#monitoring ENTRY
jenisPrinter = ttk.Entry(window)
jenisPrinter.grid(row=1,padx=5 ,pady= 5,column=1,columnspan=2, sticky=W+E)
settinganP = ["Canon Pixma MG2570S", "HP Color Laser", "Panasonic KX-MB2275", "Epson L360", "Fuji Xerox DocuPrint", "Brother DCP-T300"]
setprint = settinganP[0]
jenisPrinter.insert(0, setprint)
jenisPrinter.config(state="readonly")

jenisKertas = ttk.Entry(window)
jenisKertas.grid(row=2,padx=5 ,column=1,columnspan=2, sticky=W+E)
settinganJK = ["A4", "A3", "B2", "B3"]
setkertas = settinganJK[0]
jenisKertas.insert(0, setkertas)
jenisKertas.config(state="readonly")

jenisTinta = ttk.Entry(window)
jenisTinta.grid(row=3,padx=5, column=1, pady=5,columnspan=2, sticky=W+E)
settinganT = ["Hitam Putih", "Warna"]
setTinta = settinganT[0]
jenisTinta.insert(0, setTinta)
jenisTinta.config(state="readonly")

SisaKertas = StringVar()
jumlahKrts = ttk.Entry(window, justify=CENTER, width=13,textvariable=SisaKertas)
jumlahKrts.grid(row=4,padx=5, column=1, sticky=W+E)
jumlahKrts.insert(0, 0)
jumlahKrts.config(state="readonly")

sisacopy = StringVar()
jumlahCopy = ttk.Entry(window, justify=CENTER,width=13, textvariable=sisacopy)
jumlahCopy.grid(row=5,padx=5, pady=5 ,column=1, sticky=W+E)
jumlahCopy.insert(0, 0)
jumlahCopy.config(state="readonly")

jumlahTercetak = ttk.Entry(window,justify=CENTER, width=13)
jumlahTercetak.grid(row=10,padx=5, pady=5,column=1, sticky=W+E)
jumlahTercetak.insert(0, 0)
jumlahTercetak.config(state="readonly")

#IMG LIB
gambar = Image.open('gear-option.png')
gambar = gambar.resize((23,23))
gmbr = ImageTk.PhotoImage(gambar)

Pic = Image.open('printer.png')
Pic= Pic.resize((35,35))
Pict = ImageTk.PhotoImage(Pic)

logo = PhotoImage(file="printer1.png")
window.iconphoto(True, logo)
TM = 0
#------------------------------------------------------

def update_progress_label():
    return f"Persentase Tinta : {pb['value']}%"



pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=13
)
pb.grid(column=1, row=6, columnspan=2, padx=5, sticky= W+E)

pb['value'] = 100

def fungsiTinta():
    global TM
    temp1 = int(sisacopy.get())
    temp2 = int(SisaKertas.get())
    TZ = temp2 - temp1

    while temp2 > TZ:
        window.update()
        time.sleep(1)


        print(temp1)
        temp1 -= 1
        CD1 = temp1

        print(temp2)
        temp2 -= 1
        CD3 = temp2

        print(TM)
        TM += 1
        CD2 = TM


        if temp2 < 0:
            messagebox.showerror("ERORR", "Kertas Habis Segera Isi Ulang")
            break
        else:
            jumlahCopy.config(state='normal')
            jumlahCopy.delete(0, 'end')
            jumlahCopy.insert(0, CD1)
            jumlahCopy.config(state="readonly")
            jumlahKrts.config(state='normal')
            jumlahKrts.delete(0, 'end')
            jumlahKrts.insert(0, CD3)
            jumlahKrts.config(state="readonly")
            jumlahTercetak.config(state='normal')
            jumlahTercetak.delete(0, 'end')
            jumlahTercetak.insert(0, CD2)
            jumlahTercetak.config(state="readonly")
            tk.Label(window, text=f"Telah Selesai : {CD2} ", font="Arial 10",relief="sunken").grid(row=27, column=4,columnspan=5,
                                                                                                                  padx=5,pady=5,sticky=W+E)

        ingfotinta = 0.5
        nilaibar = pb['value']
        pb['value'] = nilaibar - ingfotinta
        sisaTinta['text'] = update_progress_label()
        print(ingfotinta)

    if temp1 == 0:
        messagebox.showinfo("INPO", "Print Telah Selesai 👌👌")


sisaTinta = tk.Label(window, text=update_progress_label(), padx=5, pady=5,bg="#E7F6F2")
sisaTinta.grid(row=8, column=1,columnspan=2,sticky=W)

#------------------------------------------------------

def openfile():
    file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                      title="pilih file",
                                      filetypes=(("PDF", "*.pdf"),
                                                 ("DOC", "*.docx"),
                                                 ("all files", "*.*")))
    X = str(file)
    V = DocViewer(window,scrollbars='both')
    V.grid(row=1, column= 4,padx=5,rowspan=26,columnspan=5,sticky=W+E+N+S)
    V.display_file(X)

#------------------------------------------------------

#Tombol Opt
Setting_button = tk.Button(window, image=gmbr ,pady=10,padx=10,command=Ubah)
Setting_button.grid(row=0, column=5,sticky=E+W+S+N,pady=5,padx=5)

Print_button = tk.Button(window,text="Print", command=fungsiTinta,image=Pict, pady=1,padx=1,compound=TOP)
Print_button.grid(row=10, column=2,padx=5,pady=5,sticky=E)

Buka_file = tk.Button(window, text="Open File",font= "arial 10",command=openfile,width=99,)
Buka_file.grid(row=0, column=4,padx=5,pady=5)

# Run the application
window.mainloop()
