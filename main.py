pengeluaran = {}

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
            print("4.Keluar")
            pilihan = input("Masukkan Pilihan Anda: ").lower()
            if pilihan not in [
                "1", "tambah pengeluaran", "1.tambah pengeluaran",
                "2", "lihat pengeluaran", "2.lihat pengeluaran",
                "3", "total pengeluaran", "3.total pengeluaran",
                "4", "keluar", "4.keluar"
            ]:
                print("Pilihan Tidak Valid, Harap Memasukkan Pilihan Yang Valid")
                continue
            else:
                if pilihan in ["4", "keluar", "4.keluar"]:
                    print("Jangan Lupa Catat Pengeluaranmu Ya:D")
                    break
                elif pilihan in ["1", "tambah pengeluaran", "1.tambah pengeluaran"]:
                    tambah_pengeluaran(pengeluaran)
                elif pilihan in ["2", "lihat pengeluaran", "2.lihat pengeluaran"]:
                    lihat_pengeluaran(pengeluaran)
                elif pilihan in ["3", "total pengeluaran", "3.total pengeluaran"]:
                    total_pengeluaran(pengeluaran)


"""PROSES SYSTEM"""
main_menu_process()