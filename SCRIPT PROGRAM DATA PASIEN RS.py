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