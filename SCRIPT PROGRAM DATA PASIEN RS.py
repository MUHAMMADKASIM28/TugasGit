datas = []
inputan = 0

while(inputan != "4"):
   print("## RS. Medika Indonesia ##")
   print("1. Tampilkan Pasien")
   print("2. Tambah Pasien")
   print("3. Hapus Pasien")
   print("4. Keluar")
   print("#################")
   print("Pilih Menu...")
   inputan = input()

   if(inputan == "1"):
       print("Daftar Nama Pasien")
       print(datas)

   if(inputan == "2"):
       print("Tambah Pasien")
       print("Masukkan Nama :")
       nama = input()
       print(datas.append(nama))

   if(inputan == "3"):
       print("Hapus Data Pasien")
       print("Masukkan Nama :")
       nama = input()
       print(datas.remove(nama))

   if(inputan == "4"):
       print("SEMOGA LEKAS SEMBUH :)")

