import turtle as t
import random

def initialize_turtle(tersangka_list):
    # Mengatur ukuran layar dan kecepatan turtle
    t.setup(800, 600)
    t.speed(0)
    t.hideturtle()
    t.penup()
    
    # Menggambar sumbu x dan y
    t.goto(-150, 0)
    t.pendown()
    t.goto(150, 0)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.goto(0, 150)
    t.penup()
    
    # Menandai sumbu x
    for i in range(-5, 6):
        t.goto(i * 30, -5)
        t.pendown()
        t.goto(i * 30, 5)
        t.penup()
        if i != 0:
            t.goto(i * 30, -20)
            t.write(i, align="center")
    
    # Menandai sumbu y
    for i in range(-5, 6):
        t.goto(-5, i * 30)
        t.pendown()
        t.goto(5, i * 30)
        t.penup()
        if i != 0:
            t.goto(-20, i * 30)
            t.write(i, align="center")
    
    # Memberi label pada sumbu
    t.goto(200, -20)
    t.write("Tingkat Motif", align="center")
    t.goto(20, 170)
    t.write("Tingkat Alibi", align="center")
    
    # Menentukan tersangka dengan index pelaku tertinggi
    if tersangka_list:
        tersangka_tertinggi = max(tersangka_list, key=count_index)
        index_tertinggi = count_index(tersangka_tertinggi)
        t.goto(0, -250)
        t.write(f"tersangka dengan index pelaku tertinggi bernilai {index_tertinggi} adalah {tersangka_tertinggi['nama']} ", align="center")
    else:
        t.goto(0, -250)
        t.write("Belum ada data tersangka", align="center")


def plot_point(tersangka):
    # TODO: Lengkapi fungsi untuk menggambar objek tersangka
    color = (random.random(), random.random(), random.random())
    tersangka_motif = tersangka['motif']
    tersangka_alibi = tersangka['alibi']
    tersangka_nama = tersangka['nama']
    
    t.goto(tersangka_motif * 30, tersangka_alibi * 30)
    
    if tersangka_motif >= 0 and tersangka_alibi >= 0:
        draw_square(color)
    elif tersangka_motif < 0 and tersangka_alibi >= 0:
        draw_diamond(color)
    elif tersangka_motif < 0 and tersangka_alibi < 0:
        draw_triangle(color)
    elif tersangka_motif > 0 and tersangka_alibi < 0:
        draw_circle(color)
    
    t.goto(tersangka_motif * 30 + 10, tersangka_alibi * 30 - 10)
    t.write(f"{tersangka_nama} ({int(tersangka_motif)},{int(tersangka_alibi)})", align="left")

def count_index(tersangka):
    # TODO: Lengkapi fungsi untuk menghitung indeks pelaku
    tersangka_motif = tersangka['motif']
    tersangka_alibi = tersangka['alibi']
    indeks_pelaku = (tersangka_motif / 2) - (tersangka_alibi / 2)
    return indeks_pelaku

def draw_square(color):
    # TODO: Lengkapi fungsi untuk menggambar persegi
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_triangle(color):
    # TODO: Lengkapi fungsi untuk menggambar segitiga
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(10)
        t.left(120)
    t.end_fill()
    t.penup()
    
def draw_diamond(color):
    # TODO: Lengkapi fungsi untuk menggambar belah ketupat
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.left(45)
        t.forward(10)
        t.left(135)
        t.forward(10)
    t.end_fill()
    t.penup()

def draw_circle(color):
    # TODO: Lengkapi fungsi untuk menggambar lingkaran
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()

tersangka_list = []

# Main program
print("Welcome to DekPenol Graphing")
while True:
    # TODO: Tampilan menu utama program
    print('''
---------------------------------------
Pilihan:
1) Tambah Tersangka
2) Cetak Grafik Tersangka
3) Exit
---------------------------------------''')
    choice = str(input("Pilihan:"))
    print()

    if choice == "1":
        # TODO: Lengkapi opsi 1
        tersangka_berapa = int(input("Masukkan jumlah tersangka: "))
        for i in range(1, tersangka_berapa+1):
            print()
            tersangka_nama = str(input(f"Masukkan nama tersangka ke-{i}: "))
            
            while True:
                tersangka_motif = int(input("Masukkan tingkat motif (antara -5 sampai 5): "))
                tersangka_alibi = int(input("Masukkan tingkat alibi (antara -5 sampai 5): "))
                if -5 <= tersangka_motif <= 5 and -5 <= tersangka_alibi <= 5:
                    duplicate = False
                    for tersangka in tersangka_list:
                        if tersangka['motif'] == tersangka_motif and tersangka['alibi'] == tersangka_alibi:
                            duplicate = True
                            break
                    if not duplicate:
                        break
                    else:
                        print("Kombinasi motif dan alibi ini sudah dimasukkan sebelumnya!")
                else:
                    print("Nilai tingkat motif dan alibi harus di antara -5 sampai 5!")

            tersangka = {'nama': tersangka_nama, 'motif': tersangka_motif, 'alibi': tersangka_alibi}
            tersangka_list.append(tersangka)

    elif choice == "2":
        # TODO: Lengkapi opsi 2
        if tersangka_list:
            # Bagian bawah ini jangan diubah, hanya untuk memastikan screen turtle dapat ditutup dan digunakan kembali
            try:
                initialize_turtle(tersangka_list)
            except t.Terminator:
                initialize_turtle(tersangka_list)

            for tersangka in tersangka_list:
                plot_point(tersangka)
            
        else:
            print("Belum ada data tersangka. Silakan tambahkan tersangka terlebih dahulu.")
            

    elif choice == "3":
        # TODO: Lengkapi fungsi opsi 3
        print("Terimakasih telah menggunakan DekPenol Graphing.")
        break

    else:
        print("input tidak valid")