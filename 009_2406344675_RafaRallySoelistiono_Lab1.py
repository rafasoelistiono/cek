
def header(): #fungsi untuk header
    print(">>===========================<<")
    print("||                     	     ||")
    print("||  Welcome to Interrogation ||")
    print("||                     	     ||")
    print(">>===========================<<")

def footer(): #fungsi untuk footer
    print(">>===========================<<")
    print("||                     	    ||")
    print("|| Ending the Interrogation ||")
    print("||                     	    ||")
    print(">>===========================<<")

def cek_angka(npm): #fungsi untuk mengecek npm apakah benar benar angka dan harus berjumlah 10. menghasilkan nilai bool
    if not npm.isdigit():
        return False
    
    jumlah_digit = 0
    for digit in npm:
        jumlah_digit += 1
    
    if jumlah_digit == 10:
        return True
    else:
        return False

while True: #menggunakan loop agar program akan terus berlanjut dan berulang hingga tercapai semua kondisi
    header()
    print()
    while True: # loop untuk mulai interogasi
        start = input("Mulai Interogasi (Y/N)? ")
        if start == "Y":
            print("Mari kita mulai interogasi")
            break
        elif start == "N":
            print("Tidak jadi interogasi")
            print()
            footer()
            break
        else:
            print()
            print("Input tidak valid!")
    
    if start == "N": #conditional agar input N benar benar berhenti
        break
    print()

    while True: #loop untuk memulai input data dari nama,npm,motif, dan alibi
        while True: #loop npm
            nama = input("Siapa namamu? ")
            npm = input("Berapa nomor NPM mu? ")
            if not npm.isdigit():
                print("NPM harus berupa angka!")
                print("------------------------------")
                print()
                continue
            elif not cek_angka(npm):
                print("NPM harus sepanjang 10 digits!")
                print("------------------------------")
                print()
                continue
            else:
                break
    
        while True: #loop motif
            ada_motif = input("Apakah kamu punya motif (Y/N)? ")
            if ada_motif == "Y":
                motif = input("Apa motif kamu tadi? ")
                break
            elif ada_motif == "N":
                motif = None
                break
            else:
                print("Seseorang harus punya motif atau tidak punya motif sama sekali!")
                print("------------------------------")
                print()
                break

        if ada_motif not in ["Y", "N"]: #conditional untuk memastikan input Y/N 
            continue

        while True: #loop alibi
            ada_alibi = input("Apakah kamu punya alibi (Y/N)? ")
            if ada_alibi == 'Y':
                alibi = input("Apa alibi kamu? ")
                break
            elif ada_alibi == 'N':
                alibi = None
                break
            else:
                print("Seseorang harus punya alibi atau tidak punya alibi sama sekali!")
                print("------------------------------")
                print()
                break

        if ada_alibi not in ["Y", "N"]: #conditional untuk memastikan input Y/N
            continue

        print() # daerah result dari output yang diinput diatas
        print(f"{nama} dengan NPM {npm}", end=" ") 
        if motif:
            print(f"memiliki {motif}", end=" ")
        else:
            print("tidak memiliki motif", end=" ")

        if alibi:
            print(f"dan tidak memiliki alibi {alibi}")
        else:
            print("dan tidak memiliki alibi")

        if (motif and not alibi): #ini conditional untuk menentukan apakah user termasuk kedalam beberapa kriteria dilihat dari penyertaan motif atau alibi
            print(f"{nama} mencurigakan nih >:(")
        elif (motif and alibi) or (not motif and not alibi):
            print(f"{nama} lumayan mencurigakan nih...")
        else:
            print(f"{nama} tidak terlalu mencurigakan sih")
        
        print("------------------------------")

        print()

        while True: #loop terakhir untuk memastikan apakah program ingin dilanjutkan atau tidak
            lanjutkan_interogasi = input("Lanjut interogasi (Y/N)? ")
            if lanjutkan_interogasi in ['Y', 'N']:
                break
            else:
                print()
                print("Input tidak valid")
            
        if lanjutkan_interogasi == 'N': #conditional untuk memastikan input N agar benar benar end
            print("Interogasi telah selesai")
            print()
            footer()
            break
        else:
            print("------------------------------")
            print()

    break