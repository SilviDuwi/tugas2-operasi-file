class Book:
    def init(self):
        pass

    def baca_file(self, nama_file):
        try:
            with open(nama_file,'r') as file:
                isi_file = file.read()
                print(isi_file)
        except FileNotFoundError:
            print(f"file {nama_file} tidak ada.")
        except Exception as e:
            print(f"Terjadi Kesalahan saat membaca: {e}")

    def tulis_file(self, nama_file, mode):
        try:
            nama_buku = input("Judul buku: ")
            teks = f"\n{nama_buku}"
            with open(nama_file, mode) as file:
                file.write(teks)
                print(f"Teks sudah ditulis & disimpan dalam {nama_file}")
        except Exception as e:
            print(f"Gagal menulis: {e}")