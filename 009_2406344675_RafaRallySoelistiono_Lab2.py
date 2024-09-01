"""Pada kode ini, Anda hanya perlu mengimplementasikan fungsi-fungsi yang belum diimplementasikan.
Fungsi yang belum diimplementasikan ditandai dengan komentar TODO. Anda dapat menghapus komentar TODO
setelah mengimplementasikan fungsi tersebut. Program utama dengan pilihan menu yang akan dijalankan juga 
sudah diimplementasikan di bagian bawah template ini. Good luck. May the soul of Alan Turing be with you."""

# With love: NZR🥷, YAS️️🧏🏿‍♂️.

# Fungsi untuk mencetak tampilan menu utama. Sudah diimplementasikan.
def main_menu():
    print("="*20 + " Selamat datang di PacilSeeker! " + "="*20 + "\n"
    "(1) Masuk\n"
    "(2) Lihat riwayat CCTV\n"
    "(3) Tinjau kemungkinan tersangka\n"
    "(4) Cetak ringkasan tersangka\n"
    "(5) Keluar")

# Fungsi untuk mengecek apakah pengguna sudah login dan belum diblokir. Sudah diimplementasikan.
def authorized(logged: bool, banned: bool) -> bool:
    if logged == False:
        print("Silakan untuk login terlebih dahulu.\n")
        return False
    if banned == True:
        # HINT: Variable "banned" diubah statusnya pada fungsi yang bertujuan untuk mengecek percobaan login.
        print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
        return False
    return True

# Fungsi untuk meminta data mahasiswa admin. Belum diimplementasikan.
# HINT: Impelementasikan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
def ask_admin():
    student = int(input(f"Masukkan banyaknya mahasiswa admin: "))
    # TODO: Implementasi fungsi untuk meminta input NPM mahasiswa dan menyimpannya di "list_admin".
    list_admin = []
    for i in range(1, student + 1):
        while True:
            #pengecekan npm harus panjangnya 10
            mahasiswa = input(f"NPM mahasiswa admin ke-{i}: ")
            if len(mahasiswa) == 10 and mahasiswa.isdigit():
                list_admin.append(mahasiswa)
                break
            else:
                print("NPM harus terdiri dari 10 digit angka.")
    print()
    return list_admin

# Fungsi untuk meminta data mahasiswa tersangka. Belum diimplementasikan.
# HINT: Impelementasikan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
#pengecekan apakah mahasiswa sebanyak 4
def ask_suspected():
    while True:
        student = int(input("Masukkan banyaknya mahasiswa tersangka: "))
        if student >= 4:
            break
        else:
            print("Jumlah mahasiswa tersangka harus minimal 4.")
    # TODO: Implementasi fungsi untuk meminta input NPM mahasiswa dan menyimpannya di "list_suspected".
    #pengecekan nama karakter mahasiswa tidak boleh lebih dari 10
    list_suspected = []
    for i in range(1, student + 1):
        while True:
            mahasiswa = input(f"Nama mahasiswa tersangka ke-{i}: ")
            if len(mahasiswa) <= 10:
                list_suspected.append(mahasiswa)
                break
            else:
                print("Nama mahasiswa tersangka tidak boleh lebih dari 10 karakter.")
    print()
    return list_suspected

# Fungsi untuk meminta data yang terekam CCTV. Belum diimplementasikan.
# HINT: Impelementasikan input dan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
#validasi data yang dimasukkan cctv tidak boleh lebih dari 99
def ask_case(list_suspected):
    while True:
        case = int(input(f"Masukkan banyaknya data yang terekam CCTV: "))
        if case <= 99:
            break
        else:
            print("Banyaknya data yang terekam CCTV tidak boleh lebih dari 99.")
    # TODO 1: Implementasi fungsi untuk meminta input nama, waktu, dan lantai tempat terdeteksi mahasiswa.
    # TODO 2: Simpan input ke dalam list yang bersesuaian.
    # TODO 3: Gunakan string formatting yang sesuai untuk membuat kode mahasiswa. Kemudian, simpan ke dalam "list_code".
    list_name = []
    list_time = []
    list_level = []
    list_code = []
    for i in range(1, case + 1):
        print(f"========== Kasus ke-{i} ==========")
        nama_mahasiswa = str(input("Nama mahasiswa: "))
        while True:
            #mengecek format waktu dalam input data
            waktu_terdeteksi = input("Waktu terdeteksi (HH:MM): ")
            if ':' in waktu_terdeteksi:
                hh, mm = waktu_terdeteksi.split(':')
                if hh.isdigit() and mm.isdigit():
                    hh = int(hh)
                    mm = int(mm)
                    if 0 <= hh < 24 and 0 <= mm < 60:
                        break
            print("Waktu harus dalam format HH:MM dengan 00 ≤ HH < 24 dan 00 ≤ MM < 60.")
        while True:
            #mengecek apakah lantai tersebut diantara 0-7
            lantai_terdeteksi = int(input("Lantai tempat terdeteksi (0-7): "))
            if 0 <= lantai_terdeteksi <= 7:
                break
            else:
                print("Lantai tempat terdeteksi harus antara 0 sampai 7 inklusif.")
        list_name.append(nama_mahasiswa)
        list_time.append(waktu_terdeteksi)
        list_level.append(lantai_terdeteksi)
        list_code.append(f"{lantai_terdeteksi}{list_suspected.index(nama_mahasiswa):02d}")
    print()
    return list_name, list_time, list_level, list_code

# Fungsi untuk menjalankan menu login pada opsi menu 1. Belum diimplementasikan.
def execute_login(list_admin):
    attempt = 0
    succeed = False
    while attempt < 3 and not succeed:
        npm = input("Masukkan NPM mahasiswa admin yang telah terdaftar:")
        # TODO 1: Implementasi fungsi untuk mengecek apakah NPM yang dimasukkan merupakan NPM mahasiswa admin.
        # HINT: Gunakan variabel succeed dengan mengubah nilainya menjadi True jika NPM ditemukan.
        if npm in list_admin:
            print(f"Selamat datang, mahasiswa dengan NPM {npm}!")
            succeed = True
        else:
            print(f"Maaf, mahasiswa dengan NPM {npm} tidak terdaftar pada sistem.")
            attempt += 1

            # TODO 2: Implementasi fungsi untuk mengecek apakah percobaan login sudah mencapai 3 kali.
            # HINT: Increment variabel attempt jika login gagal. Jika sudah mencapai 3 kali, ubah status variabel yang bersangkutan pada fungsi lainnya.
        if attempt == 3:
            print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.")
    print()
    return attempt # Value yang di-return digunakan pada main untuk menandakan jumlah percobaan login.

# Fungsi untuk menjalankan menu yang menampilkan riwayat CCTV pada menu 2. Belum diimplementasikan.
# HINT: Anda hanya perlu menambahkan argumen yang bersesuaian pada fungsi print() yang sudah diimplementasikan.
def execute_logcheck(list_code, list_name, list_time, list_level):
    # Menggabungkan semua list menjadi satu list tuple
    combined_list = list(zip(list_code, list_name, list_time, list_level))
    # Mengurutkan list berdasarkan waktu
    combined_list.sort(key=lambda x: x[2])
    
    print("{:>4} | {:^10} | {:^7} | {:<15}".format("Kode", "Nama", "Waktu", "Lokasi (lantai)"))
    for item in combined_list:
        print("{:>4} | {:<10} | {:^7} | {:<15}".format(item[0], item[1], item[2], item[3]))
    print()

# Fungsi untuk menghitung persentase kemungkinan tersangka pada menu 3. Belum diimplementasikan.
def execute_suspect(list_code, list_suspected, list_result, list_percentage):
    while True:
        code = input("Masukkan kode mahasiswa tersangka: ")
        # TODO: Implementasi fungsi yang memvalidasi input code.
        # Hint: Gunakan if else statement untuk memvalidasi input code.
        #kode mahasiswa harus sama dengan 3 karakter angka
        #dugaan kejadian dijamin maksimum 999999
        if code in list_code and len(code) == 3 and int(code) <= 999999:
            break
        else:
            print(f"Maaf, mahasiswa dengan kode {code} tidak terdaftar pada sistem.")

    while True:
        time = input("Masukkan dugaan waktu kejadian: ")
        # TODO: Implementasi fungsi yang memvalidasi input time.
        # HINT: Gunakan if else statement serta string slicing untuk memvalidasi input time.
        '''HINT: Input time memiliki panjang 5 karakter, dengan elemen pada 2 index pertama dan 2 terakhir harus berupa angka.
        Anda dapat menggunakan method .isdigit(). Elemen pada 2 index pertama tidak boleh lebih dari 24, serta pada 2 terakhir
        tidak boleh lebih dari 60.'''
        if len(time) == 5 and time[:2].isdigit() and time[3:].isdigit() and time[2] == ":":
            if int(time[:2]) < 24 and int(time[3:]) < 60:
                break
        print("Maaf, format waktu tidak sesuai.")

    while True:
        level = input("Masukkan dugaan lokasi (lantai) kejadian: ")
        # TODO: Implementasi fungsi yang memvalidasi input level.
        # HINT: Gunakan if else statement untuk memvalidasi input level.
        # HINT: Input level harus berupa angka dan tidak boleh lebih dari 7 serta tidak boleh kurang dari 0.
        if level.isdigit() and 0 <= int(level) <= 7:
            break
        print(f"Maaf, lantai {level} tidak ada.")

    num_code = int(code[-2:])
    num_time = int(time[:2]) * 60 + int(time[-2:])
    num_level = int(level)
    if num_code == 3:
        mux_code = 15
    else:
        mux_code = 10

    percentage = max((mux_code + (45 - abs(871 - num_time)) + (40 - abs(2 - num_level) * 5)), 0)
    list_result.append(list_suspected[num_code])
    list_percentage.append(percentage)

    print(f"Berhasil meninjau tersangka pada mahasiswa dengan nama {list_suspected[num_code]} pada pukul {time} di lantai {level}.\n")

# Fungsi untuk mencetak ringkasan tersangka pada menu 4. Belum diimplementasikan.
# HINT: Anda hanya perlu menambahkan argumen yang bersesuaian pada fungsi print() yang sudah diimplementasikan.
def execute_summarize(list_result, list_percentage, logged_student):
    if len(list_percentage) == 0:
        most_suspected = "Tidak ada"
    else:
        print("{:>6} | {:^10} | {:<25}".format("Dugaan", "Nama", "Persentase Menjadi Pelaku"))
        for i in range(len(list_result)):
            print("{:>6} | {:<10} | {:<25}".format(i+1, list_result[i], f"{list_percentage[i]}%"))
        if sum(list_percentage) // len(list_percentage) >= 40:
            index_name = list_percentage.index(max(list_percentage))
            most_suspected = list_result[index_name]
        else:
            most_suspected = logged_student + " (admin)"
    print(f"Nama/NPM mahasiswa tersangka yang paling mungkin: {most_suspected}\n")

# Program utama.
if __name__ == "__main__":
    list_admin = list()
    list_suspected = list()
    list_code = list()
    list_name = list()
    list_time = list()
    list_level = list()
    list_result = list()
    list_percentage = list()
    logged_student = str()

    running = True
    logged = False
    banned = False

    list_admin = ask_admin()
    list_suspected = ask_suspected()
    list_name, list_time, list_level, list_code = ask_case(list_suspected)

    while running:
        main_menu()
        action = int(input("Masukkan pilihan menu: "))
        print("="*72)

        if action == 1:
            if banned == True:
                print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
                continue
            attempt = execute_login(list_admin)

            if attempt == 3:
                logged = True
                banned = True
            else:
                logged = True

        elif action == 2:
            if authorized(logged, banned) == False:
                continue
            execute_logcheck(list_code, list_name, list_time, list_level)

        elif action == 3:
            if authorized(logged, banned) == False:
                continue
            execute_suspect(list_code, list_suspected, list_result, list_percentage)

        elif action == 4:
            if authorized(logged, banned) == False:
                continue
            execute_summarize(list_result, list_percentage, logged_student)

        elif action == 5:
            running = False

        else:
            print("Maaf, pilihan menu Anda tidak diketahui.\n")

    print("Terima kasih karena telah menggunakan PacilSeeker!")