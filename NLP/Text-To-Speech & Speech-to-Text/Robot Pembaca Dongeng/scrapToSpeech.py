import xlwings as xw
from gtts import gTTS
import os
from datetime import datetime

workbook = xw.Book('hasil.xlsx')
sheet = workbook.sheets[0]

def kosonginSheet():
    sheet.clear_contents() #Ngosongin Sheet
    sheet.range("A1").value = ['Keyword', 'Judul', 'Penulis', 'Waktu Postingan', 'Cerita']

def prosesDongeng(keyword,dongeng):
    judul, penulis, waktu, cerita = dongeng

    cerita.pop()
    cerita = " ".join(cerita)

    sheet.range("A2").value = [keyword, judul, penulis, waktu, cerita]
    workbook.save()

def bacaDongeng():
    # Reference : https://www.youtube.com/watch?v=_Q8wtPCyMdo
    a = str('Keyword yang dicari adalah ') + sheet.range("A2").value + '. '  # Keyword
    b = str('Judul dongeng kali ini yaitu ') + sheet.range("B2").value + '. '  # Judul
    c = sheet.range("C2").value + str(' adalah nama penulis artikel ini. ') # Penulis

    y = sheet.range("D2").value.strftime("%d %B, %Y")

    d = str('Beliau membuat artikel ini pada tanggal ') + y + str('. ')     # Tanggal
    e = str('Baiklah. Mari kita mulai membaca dongengnya. ') + sheet.range("E2").value[:300]    # Dongeng

    # Bisa ampe 2 menit nunggu nya
    # e = str('Mari kita mulai membaca dongeng. ') + sheet.range("E2").value

    x = a + b + c + d + e
    
    language = 'id' # di cmd gtts-cli --all
    output = gTTS(text=x,lang=language)

    output.save('belajar.mp3')
    os.system("start belajar.mp3")


# Error
# language = 'id-ID-Standard-B' # di cmd gtts-cli --all
# wb.sheets[0].range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row