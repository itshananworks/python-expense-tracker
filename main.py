pengeluaran = {}

import time

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


"""EDIT PENGELUARAN"""
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
        try:
            hapus_pengeluaran = input("Masukkan Nama/Judul Pengeluaran Untuk Dihapus: ")
            pengeluaran.pop(hapus_pengeluaran)
            print("Berhasil Menghapus Pengeluaran:)")
        except KeyError:
            print("Tidak Ada Nama/Judul Pengeluaran Seperti Itu Di Riwayat Pengeluaranmu:(")




"""TOTAL PENGELUARAN"""
def total_pengeluaran(pengeluaran):
    total = 0
    if pengeluaran == {}:
        print("ERROR:Gagal Menjumlahkan Total, Tidak Ada Riwayat Pengeluaran:(")
    else:
        for jumlah_pengeluaran in pengeluaran.values():
            total += jumlah_pengeluaran
        print("Total pengeluaran Anda:", total)



"""LIHAT PENGELUARAN"""
def lihat_pengeluaran(pengeluaran):
    if pengeluaran == {}:
        print("Belum Ada Pengeluaran Yang Tercatat:(")
    else:
        nomor = 1
        for nama_pengeluaran, jumlah_pengeluaran in pengeluaran.items():
            print(nomor,".",nama_pengeluaran, "=", jumlah_pengeluaran)
            nomor += 1

"""INPUT DAN MENAMBAHKAN PENGELUARAN"""
def tambah_pengeluaran(pengeluaran):
    try:
        nama_pengeluaran = input("Masukkan Nama Pengeluaran: ")
        jumlah_pengeluaran = int(input("Masukkan Jumlah Pengeluaran: "))
        pengeluaran[nama_pengeluaran] = jumlah_pengeluaran
        print("YEYY Berhasil Menambahkan Dan Mencatat Pengeluaran Anda:D")
    except ValueError:
        print("Harap Masukkan Angka!")




"""FUNCTION SYSTEM"""
def main_menu_process():
    while True:
            print("=" * 25, "PERSONAL EXPENSE TRACKER", "=" * 25)
            print("1.Tambah Pengeluaran")
            print("2.Lihat Pengeluaran")
            print("3.Total Pengeluaran")
            print("4.Hapus Pengeluaran")
            print("5.Edit Pengeluaran")
            print("6.Keluar")
            pilihan = input("Masukkan Pilihan Anda: ").lower()
            if pilihan not in [
                "1", "tambah pengeluaran", "1.tambah pengeluaran",
                "2", "lihat pengeluaran", "2.lihat pengeluaran",
                "3", "total pengeluaran", "3.total pengeluaran",
                "4", "hapus pengeluaran", "4.hapus pengeluaran",
                "5", "edit pengeluaran", "5.edit pengeluaran",
                "6", "keluar", "6.keluar"
            ]:
                print("Pilihan Tidak Valid, Harap Memasukkan Pilihan Yang Valid")
                continue
            else:
                if pilihan in ["6", "keluar", "6.keluar"]:
                    print("Jangan Lupa Catat Pengeluaranmu Ya:D")
                    break
                elif pilihan in ["1", "tambah pengeluaran", "1.tambah pengeluaran"]:
                    tambah_pengeluaran(pengeluaran)
                elif pilihan in ["2", "lihat pengeluaran", "2.lihat pengeluaran"]:
                    lihat_pengeluaran(pengeluaran)
                elif pilihan in ["3", "total pengeluaran", "3.total pengeluaran"]:
                    total_pengeluaran(pengeluaran)
                elif pilihan in ["4", "hapus pengeluaran", "4.hapus pengeluaran"]:
                    hapuspengeluaran(pengeluaran)
                elif pilihan in ["5", "edit pengeluaran", "5.edit pengeluaran"]:
                    editpengeluaran(pengeluaran)




"""PROSES SYSTEM"""
main_menu_process()