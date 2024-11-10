import csv
import os
import pandas as pd
import time


file_names_turkish=["TARIH","ISLEM KODU","ORTAK SOZLESME NO","UYE ISLEM NO","ALIS_SATIS","ISLEM ADEDI","ISLEM FIYATI","ISLEM HACMI","HESAP TIPI","HESAP NO","ACENTE/FON KODU (AFK)","REFERANS NO","EMIR NO","EMIR NO NUMERIK","TEMSILCI","ISLEM ZAMANI","ACIGA SATIS ISARETI","NORMAL ISLEM_ISLEM RAPORLAMA","SEANS","ISLEM DURUMU","TAKAS TARIHI","AKTIF_PASIF","TAKAS TARAFI ISLEM NO","TAKAS TARAFI ORTAK ANLASMA NO","TEMSILCI IMZASI"]

timestr = time.strftime("%Y%m%d")
name=f"Q:/_HiSenetl/İŞLEM DEFTERLERİ VE TESCİL/İŞLEM DEFTERLERİ/UID_"+timestr+".IYM"
with open(name, "r") as dosya:
    csv_reader = csv.DictReader(dosya, delimiter=";")

    with open("bank_account.csv", "w" , newline="") as new_file:
        csv_writer= csv.DictWriter(new_file, fieldnames=file_names_turkish, delimiter=";")
        all_count=0
        bank_count=0
        csv_writer.writeheader()
        for line in csv_reader:
            all_count+=1
            if(line["HESAP TIPI"]=="M") and (".HE" in line["ISLEM KODU"]) and ("1-00" in line["REFERANS NO"]):
                line["ISLEM FIYATI"] = str(line["ISLEM FIYATI"]).replace(".", ",")
                line["ISLEM HACMI"] = str(line["ISLEM HACMI"]).replace(".", ",")
                csv_writer.writerow(line)
                bank_count+=1
print("\n\nişlem tamamlanmıştır\n\n")

    



