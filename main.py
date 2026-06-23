
import time

"""LOAD DATA"""
def load_data():
    pengeluaran = {}
    try:
        with open("data_tracker.txt", "r") as file:
            for line in file:
                nama, jumlah = line.strip().split(":")
                pengeluaran[nama] = int(jumlah)
    except FileNotFoundError:
        pass
    return pengeluaran

"""SIMPAN DATA"""
def save_data(pengeluaran):
    with open("data_tracker.txt", "w") as file:
        for nama, jumlah in pengeluaran.items():
            file.write(f"{nama}:{jumlah}\n")

pengeluaran = load_data()

"""FUNCTION EDIT NAMA PENGELUARAN"""
def edit_nama_pengeluaran(pengeluaran):
    while True:
        print("=" * 98)
        print("Harap Masukkan Nama/Judul Yang Ada Di Riwayat Pengeluaranmu Ya, Agar Tidak Error Saat Diedit:)")
        print("=" * 98)
        nama_lama_yang_mau_diedit = input("Masukkan Nama/Judul Pengeluaran Lama Yang Anda Ingin Edit: ")
        if nama_lama_yang_mau_diedit in pengeluaran:
            jumlah_pengeluaran = pengeluaran[nama_lama_yang_mau_diedit]
            nama_baru = input("Masukkan Nama/Judul Baru Untuk Diganti Nama: ")
            pengeluaran[nama_baru] = jumlah_pengeluaran
            pengeluaran.pop(nama_lama_yang_mau_diedit)
            save_data(pengeluaran)
            print("YEY! Berhasil Mengedit Nama Baru:)")
            time.sleep(1)
            break
        else:
            print("Tidak Ada Nama/Judul Pengeluaran Seperti Itu Di Riwayat Pengeluaranmu:(")
            time.sleep(1.5)
            break



"""FUNCTION EDIT JUMLAH PENGELUARAN"""
def edit_jumlah_pengeluaran(pengeluaran):
    while True:
        print("=" * 98)
        print("Harap Masukkan Nama/Judul Yang Ada Di Riwayat Pengeluaranmu Ya, Agar Tidak Error Saat Diedit:)")
        print("=" * 98)
        masukkan_nama_pengeluaran = input("Masukkan Nama Pengeluaran: ")
        if masukkan_nama_pengeluaran in pengeluaran:
            try:
                masukkan_jumlah_pengeluaran_edit = int(input("Masukkan Jumlah/Nominal Yang Ingin Anda Edit: "))
                pengeluaran.update({masukkan_nama_pengeluaran:masukkan_jumlah_pengeluaran_edit})
                save_data(pengeluaran)
                time.sleep(2)
                print(f"YEY:) Berhasil Mengedit Jumlah Pengeluaran Pada {masukkan_nama_pengeluaran}")
                time.sleep(1.5)
                break
            except ValueError:
                print("Harap Masukkan Angka Yah:)")
                continue
        else:
            print("Tidak Ada Nama/Judul Pengeluaran Seperti Itu Di Riwayat Pengeluaranmu:(")
            time.sleep(1.5)
            break


"""MENU EDIT PENGELUARAN"""
def editpengeluaran(pengeluaran):
    while True:
        if pengeluaran == {}:
            print("Tidak Ada Pengeluaran Yang Ingin Di Edit:(")
            break
        else:
            print("=" * 25, "EDIT PENGELUARAN", "=" * 25)
            print("1.Edit Jumlah Pengeluaran")
            print("2.Liat Pengeluaran")
            print("3.Edit Nama Pengeluaran")
            print("4.Keluar Menu Edit")
            pilihan_edit = input("Masukkan Pilihan Anda: ").lower()
            if pilihan_edit not in [
                "1", "edit jumlah", "edit jumlah pengeluaran",
                "2", "lihat pengeluaran", "liat",
                "3", "edit nama", "edit nama pengeluaran",
                "4", "keluar", "keluar menu edit", "keluar menu edit"
            ]:
                print("Harap Masukkan Pilihan Yang Benar Yah:)")
            else:
                if pilihan_edit in ["4", "keluar", "keluar menu edit", "keluar menu edit"]:
                    print("Kembali Menu Utama..")
                    time.sleep(2)
                    break
                elif pilihan_edit in ["1", "edit jumlah", "edit jumlah pengeluaran"]:
                    edit_jumlah_pengeluaran(pengeluaran)
                elif pilihan_edit in ["2", "lihat pengeluaran", "liat"]:
                    lihat_pengeluaran(pengeluaran)
                elif pilihan_edit in ["3", "edit nama", "edit nama pengeluaran"]:
                    edit_nama_pengeluaran(pengeluaran)


"""HAPUS PENGELUARAN"""
def hapuspengeluaran(pengeluaran):
    if pengeluaran == {}:
        print("Tidak Ada Pengeluaran Yang Ingin Dihapus:(")
    else:
        hapus_pengeluaran= input("Masukkan Nama/Judul Pengeluaran Untuk Dihapus:")
        if hapus_pengeluaran in pengeluaran:
            pengeluaran.pop(hapus_pengeluaran)
            save_data(pengeluaran)
            print("Berhasil Menghapus Pengeluaran:)")
        else:
            print("Tidak Ada Nama/Judul Pengeluaran Seperti Itu Di Riwayat Pengeluaranmu:(")

"""TOTAL PENGELUARAN"""
def total_pengeluaran(pengeluaran):
    total = 0
    if pengeluaran == {}:
        print("ERROR:Gagal Menjumlahkan Total, Tidak Ada Riwayat Pengeluaran:(")
    else:
        for jumlah_pengeluaran in pengeluaran.values():
            total += jumlah_pengeluaran
        print(f"Total Pengeluaran Anda: {total:,}")



"""LIHAT PENGELUARAN"""
def lihat_pengeluaran(pengeluaran):
    if pengeluaran == {}:
        print("Belum Ada Pengeluaran Yang Tercatat:(")
    else:
        nomor = 1
        for nama_pengeluaran, jumlah_pengeluaran in pengeluaran.items():
            print(f"{nomor}. {nama_pengeluaran}        : {jumlah_pengeluaran:,}")
            nomor += 1
            time.sleep(1.5)

"""INPUT DAN MENAMBAHKAN PENGELUARAN"""
def tambah_pengeluaran(pengeluaran):
    try:
        nama_pengeluaran = input("Masukkan Nama Pengeluaran: ")
        jumlah_pengeluaran = int(input("Masukkan Jumlah Pengeluaran: "))
        pengeluaran[nama_pengeluaran] = jumlah_pengeluaran
        save_data(pengeluaran)
        print("YEYY Berhasil Menambahkan Dan Mencatat Pengeluaran Anda:D")
        time.sleep(1.5)
    except ValueError:
        print("Harap Masukkan Angka!")

"""RAPIHIN MENU"""
def header_dan_isi_menu_rapih():
    print("\n" + "=" * 50)
    print("          PERSONAL EXPENSE TRACKER")
    print("=" * 50)
    print("1.Tambah Pengeluaran")
    print("2.Lihat Pengeluaran")
    print("3.Total Pengeluaran")
    print("4.Hapus Pengeluaran")
    print("5.Edit Pengeluaran")
    print("6.Keluar")
    print("=" * 50)


"""FUNCTION SYSTEM"""
def main_menu_process():
    while True:
            header_dan_isi_menu_rapih()
            pilihan = input("Masukkan Pilihan Anda(1-6): ")
            if pilihan not in ["1", "2", "3", "4", "5", "6"]:
                print("Pilihan Tidak Valid, Harap Memasukkan Pilihan Yang Valid")
                continue
            else:
                if pilihan in ["6"]:
                    print("Jangan Lupa Catat Pengeluaranmu Ya:D")
                    break
                elif pilihan in ["1"]:
                    tambah_pengeluaran(pengeluaran)
                elif pilihan in ["2"]:
                    lihat_pengeluaran(pengeluaran)
                elif pilihan in ["3"]:
                    total_pengeluaran(pengeluaran)
                elif pilihan in ["4"]:
                    hapuspengeluaran(pengeluaran)
                elif pilihan in ["5"]:
                    editpengeluaran(pengeluaran)


"""PROSES SYSTEM"""
main_menu_process()