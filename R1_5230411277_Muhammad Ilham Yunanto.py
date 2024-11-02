class Transaksi:
    def __init__(self, no, detail):
        self.no = no
        self.detail = detail

class Produk:
    def __init__(self, kode, nama, jenis):
        self._kode = kode
        self.nama = nama
        self.jenis = jenis

class Snack(Produk):
    def __init__(self, kode, nama, jenis, harga):
        super().__init__(kode, nama, jenis)
        self.harga = harga

class Makanan(Produk):
    def __init__(self, kode, nama, jenis, harga):
        super().__init__(kode, nama, jenis)
        self.harga = harga

class Minuman(Produk):
    def __init__(self, kode, nama, jenis, harga):
        super().__init__(kode, nama, jenis)
        self.harga = harga

class Pegawai:
    def __init__(self, nik, nama, alamat):
        self._nik = nik
        self.nama = nama
        self.alamat = alamat

class Struk:
    def __init__(self, noTransaksi, namaPegawai, namaProduk, jumlahProduk, totalHarga):
        self.noTransaksi = noTransaksi
        self.namaPegawai = namaPegawai
        self.namaProduk = namaProduk
        self.jumlahProduk = jumlahProduk
        self.totalHarga = totalHarga


def kelola_snack():
    snacks = []
    while True:
        print("======Menu Kelola Snack======")
        print("1. Tambah Snack")
        print("2. Tampilkan Snack")
        print("0. Kembali")
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            kode = input("Masukkan Kode Snack: ")
            nama = input("Masukkan Nama Snack: ")
            jenis = input("Masukkan Jenis Snack: ")
            harga = float(input("Masukkan Harga Snack: "))
            snacks.append(Snack(kode, nama, jenis, harga))
            print("Snack berhasil ditambahkan!")
        elif pilih == "2":
            print("Daftar Snack:")
            for snack in snacks:
                print(f"Kode: {snack._kode}, Nama: {snack.nama}, Jenis: {snack.jenis}, Harga: {snack.harga}")
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu untuk mengelola makanan
def kelola_makanan():
    makanan = []
    while True:
        print("======Menu Kelola Makanan======")
        print("1. Tambah Makanan")
        print("2. Tampilkan Makanan")
        print("0. Kembali")
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            kode = input("Masukkan Kode Makanan: ")
            nama = input("Masukkan Nama Makanan: ")
            jenis = input("Masukkan Jenis Makanan: ")
            harga = float(input("Masukkan Harga Makanan: "))
            makanan.append(Makanan(kode, nama, jenis, harga))
            print("Makanan berhasil ditambahkan!")
        elif pilih == "2":
            print("Daftar Makanan:")
            for item in makanan:
                print(f"Kode: {item._kode}, Nama: {item.nama}, Jenis: {item.jenis}, Harga: {item.harga}")
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu untuk mengelola minuman
def kelola_minuman():
    minuman = []
    while True:
        print("======Menu Kelola Minuman======")
        print("1. Tambah Minuman")
        print("2. Tampilkan Minuman")
        print("0. Kembali")
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            kode = input("Masukkan Kode Minuman: ")
            nama = input("Masukkan Nama Minuman: ")
            jenis = input("Masukkan Jenis Minuman: ")
            harga = float(input("Masukkan Harga Minuman: "))
            minuman.append(Minuman(kode, nama, jenis, harga))
            print("Minuman berhasil ditambahkan!")
        elif pilih == "2":
            print("Daftar Minuman:")
            for item in minuman:
                print(f"Kode: {item._kode}, Nama: {item.nama}, Jenis: {item.jenis}, Harga: {item.harga}")
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def kelola_pegawai():
    pegawai = []
    while True:
        print("======Menu Kelola Pegawai======")
        print("1. Tambah Pegawai")
        print("2. Tampilkan Pegawai")
        print("0. Kembali")
        pilih = input("Pilih Menu: ")

        if pilih == "1":
            nik = input("Masukkan NIK Pegawai: ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai.append(Pegawai(nik, nama, alamat))
            print("Pegawai berhasil ditambahkan!")
        elif pilih == "2":
            print("Daftar Pegawai:")
            for p in pegawai:
                print(f"NIK: {p._nik}, Nama: {p.nama}, Alamat: {p.alamat}")
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu utama
def Menu():
    while True:
        print("======Menu Utama======")
        print("1. Menu Kelola Produk")
        print("2. Menu Pegawai")
        print("3. Menu Pembelian")
        print("0. Keluar")
        pilih = input("Pilih Menu di atas: ")

        if pilih == "1":
            while True:
                print("======Menu Kelola Produk======")
                print("1. Menu Kelola Snack")
                print("2. Menu Kelola Makanan")
                print("3. Menu Kelola Minuman")
                print("0. Kembali")
                sub_pilih = input("Pilih Menu: ")

                if sub_pilih == "1":
                    kelola_snack()
                elif sub_pilih == "2":
                    kelola_makanan()
                elif sub_pilih == "3":
                    kelola_minuman()
                elif sub_pilih == "0":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    
        elif pilih == "2":
            kelola_pegawai()

        elif pilih == "3":
            print("")

        elif pilih == "0":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


Menu()
