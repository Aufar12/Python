import pandas as pd
import string

def scrapToExcel(namaAkun, scrapLikes, scrapRetweets):

    count = 0
    tempDict = {'Target': [], 'SourceAkun': []}
    like_df = pd.DataFrame(tempDict)

    for i in scrapLikes:
        listLike = []
        listTarget = []
        for j in i:
            listLike+=j
        
        listTarget = [namaAkun[count]] * len(listLike)

        tempDict = {'Target': listTarget, 'SourceAkun': listLike}
        df = pd.DataFrame(tempDict)
        df = df.drop_duplicates(subset='SourceAkun', keep="last").reset_index(drop=True)
        like_df = pd.concat([like_df, df])
        count+=1

    print(like_df)

    count = 0
    tempDict = {'Target': [], 'SourceAkun': []}
    retweet_df = pd.DataFrame(tempDict)

    for i in scrapRetweets:
        listRetweet = []
        listTarget = []
        for j in i:
            listRetweet+=j
        
        listTarget = [namaAkun[count]] * len(listRetweet)

        tempDict = {'Target': listTarget, 'SourceAkun': listRetweet}
        df = pd.DataFrame(tempDict)
        df = df.drop_duplicates(subset='SourceAkun', keep="first").reset_index(drop=True)
        retweet_df = pd.concat([retweet_df, df])
        count+=1


    with pd.ExcelWriter('result\\thread_twitter.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
        like_df.to_excel(writer, sheet_name='Likes', index=False)
        retweet_df.to_excel(writer, sheet_name='Retweets', index=False)


def repliesToExcel(namaAkun,scrapAkun, scrapText):

    count = 0
    tempDict = {'Target': [], 'SourceAkun': [], 'Text': []}
    reply_df = pd.DataFrame(tempDict)

    for i in range(0, len(scrapAkun)):
        listAkun = []
        listText = []

        for j in range(0, len(scrapAkun[i])):
            for k in range(0, len(scrapAkun[i][j])):
                tempText = scrapText[i][j][k].replace('\n', '').rstrip(string.digits)

                if tempText != '':
                    listAkun.append(scrapAkun[i][j][k])
                    listText.append(tempText)
        
        listTarget = [namaAkun[count]] * len(listAkun)
        tempDict = {'Target': listTarget, 'SourceAkun': listAkun, 'Text': listText}
        df = pd.DataFrame(tempDict)
        df = df.drop_duplicates(subset=['SourceAkun', 'Text'], keep="first").reset_index(drop=True)
        reply_df = pd.concat([reply_df, df])
        count+=1

    with pd.ExcelWriter('result\\replies_twitter.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
        reply_df.to_excel(writer, sheet_name='Reply', index=False)

def formatReply(reply):
    tempReply = reply.replace('\n', '')
    # print(reply)

    if 'Pelajari lebih lanjut' in reply or '@' == tempReply[0] and 'Retweet' in tempReply and 'Suka' in tempReply:
        return '', ''
    else:
        reply = reply.split('\n')

        if '@' not in reply[1]:
            return '', ''

        akun = reply[1]
    
        while True:
            try:
                reply[-1] = int(reply[-1])
                del reply[-1]
            except:
                break
        
        text = ' '.join(reply[4:])
    
    return akun, text

# x = [[['Membalas \n@convomfs\nIni masih ada wkwk\nMuhammad Yusril Ihza Kurzah\n@yusril_kurzah\n · 30 Jul 2020\nGilang yg ini malah maksa minta pap jempol kaki wkwk\nTampilkan utas ini\n1', 'Membalas \n@convomfs\nBntar ini ap\n1', 'Kalo ga salah pernah heboh tuh tahun kemaren soal fetish yang orang dibungkus kek di kafanin gitu, alasannya buat tugas penelitian kuliah padahal mah buat kesenangannya dia sendiri\n1', 'Membalas \n@convomfs\nini dah lama kan ya, thread nya masih ada gasi?\n4\n54', 'Nitip dong penasaran\n1\n2', 'Membalas \n@convomfs\nKok diingetin lagi sih kasusnya gilang bungkus\n2\n295', 'ini apaansi\n1\n19', 'Membalas \n@convomfs\neh ini apa? kaya lemper\n4\n42', 'Membalas \n@convomfs\nIni apaa? Baru liat, ada threadnya gaa?\n1', 'Kasus Gilang bungkus kalo gak salah pas 2021/2020\n2'], ['Membalas \n@convomfs\nIni masih ada wkwk\nMuhammad Yusril Ihza Kurzah\n@yusril_kurzah\n · 30 Jul 2020\nGilang yg ini malah maksa minta pap jempol kaki wkwk\nTampilkan utas ini\n1', 'Membalas \n@convomfs\nBntar ini ap\n1', 'Kalo ga salah pernah heboh tuh tahun kemaren soal fetish yang orang dibungkus kek di kafanin gitu, alasannya buat tugas penelitian kuliah padahal mah buat kesenangannya dia sendiri\n1', 'Membalas \n@convomfs\nini dah lama kan ya, thread nya masih ada gasi?\n4\n54', 'Nitip dong penasaran\n1\n2', 'Membalas \n@convomfs\nKok diingetin lagi sih kasusnya gilang bungkus\n2\n295', 'ini apaansi\n1\n19', 'Membalas \n@convomfs\neh ini apa? kaya lemper\n4\n42', 'Membalas \n@convomfs\nIni apaa? Baru liat, ada threadnya gaa?\n1', 'Kasus Gilang bungkus kalo gak salah pas 2021/2020\n2']], [['Membalas \n@WidyoLita\n2) Dr kronologi panjang yg diceritakan @m_fikris, Gilang (G) melakukan eksploitasi pd orang lain dengan motif tertentu utk tujuan pribadi.  Senioritas dipakai untuk mempengaruhi mhsw pemula dgn mengatasnamakan riset ilmiah.\n2\n85\n652', '3). G cukup tricky menempatkan posisinya sbg senior utk mendirect korban, bahkan pd ranah yg sebenarnya hak korban sbg pribadi. \nSelain itu G banyak excuse shg korban iba & kurang nyaman utk bersikap asertif. \nSy bersyukur jk ternyata byk jg calon korban yg sdh menolak sjk awal.\n2\n53\n509', '4). Stiap riset ilmiah, terlebih yg melibatkan manusia sbg partisipan dgn menggunakan perlakukan tertentu yg menimbulkan risiko fisik/psikis WAJIB lolos prosedur ethical clearance dr tim etik institusi.\nDr sini dinilai apkh sbuah riset berikut prosesnya layak/tdk diselenggarakan.\n5\n519\n1.141', '5). Jk sdh lolos ethical clearance, masih dituntut adanya informed consent yg mesti diisi & ditandatangani oleh partisipan sbg tanda persetujuan resmi. Di sini selain nama peneliti juga tercantum nama penanggung jawab/profesional jk terjadi hal2 di luar kendali.\n3\n290\n671', '6). Jk 1 saat kita diminta mjd partisipan sbuah riset yg memakai perlakuan tertentu, mintalah informed consent, plajari baik2 & baru diteken. \nJk ragu, tolak! \nRiset ilmiah SANGAT hormati otonomi partisipan utk membuat keputusan. Bahkan undur diri di tengah proses pun dibolehkan.\n3\n623\n1.361'], []], [['Membalas \n@yusril_kurzah\nLanjutannya (1)\n281\n671\n2.936', 'Membalas \n@yusril_kurzah\nLanjutannya (2)\n149\n392\n2.349', 'Membalas \n@yusril_kurzah\nLanjutannya (3)\n245\n478\n2.049', 'Membalas \n@yusril_kurzah\nyg terakhir, setelh ini nda dibls wkwk jadi kasian ga dpt pap jempol kaki:(\n553\n1.107\n4.826', 'Membalas \n@yusril_kurzah\nBapak lo nonton lang\n11\n269\n896', 'Membalas \n@yusril_kurzah\nOrang normal kalo berantem di WA yg di bahas : telat, bohong, Utang, pacar, selingkuh, putus\n\nBiseksual yg lagi vertigo kalo berantem di WA yg di bahas:\nPap jempol kaki \n36\n442\n3.615'], ['Membalas \n@yusril_kurzah\nyg terakhir, setelh ini nda dibls wkwk jadi kasian ga dpt pap jempol kaki:(\n553\n1.107\n4.826', 'Membalas \n@yusril_kurzah\nBapak lo nonton lang\n11\n269\n896', 'Membalas \n@yusril_kurzah\nOrang normal kalo berantem di WA yg di bahas : telat, bohong, Utang, pacar, selingkuh, putus\n\nBiseksual yg lagi vertigo kalo berantem di WA yg di bahas:\nPap jempol kaki \n36\n442\n3.615']], [['Membalas \n@remukanbakwan__\n@SaveVidBot\n1', 'Membalas \n@remukanbakwan__\nBelum dibungkus udah tumpah weh\n1\n2', 'Nasib bekata lain\n1\n2'], ['Membalas \n@remukanbakwan__\n@SaveVidBot\n1', 'Membalas \n@remukanbakwan__\nBelum dibungkus udah tumpah weh\n1\n2', 'Nasib bekata lain\n1\n2']], [['Membalas \n@nksthi\nmas aik atrah gong ngerasakne dibungkus langsung karo gilang\n1', 'Wkwkw ', 'Membalas \n@nksthi\nKebalik ra sih?\n1\n2', 'Nggak laaah\n1', 'Membalas \n@nksthi\nCiyeeee curhaat ciyeeeee', 'Membalas \n@nksthi\nBahahahajingan \n@SiELLL666\n1', 'Aku vertigo loh dek. Ntar kalo kmabuh trus aku bunuh diri anak ayam tetangga kamu mau jawab tanggung? \n1\n1', 'Membalas \n@nksthi\n"maaf baru bales"\n\n\'chat ndek isuk lagek di bales\'\n\n"Iya maaf tadi diajak keluar gilang, dia temenku dari sma jadi udah deket banget"\n\n\'Halah asu bajingan omongmu cuman temen\'\n1\n1\n8', '1', 'Membalas \n@nksthi\nThreadnya creepy kenapa disini jadi malah bikin ketawa-ketawa. \n1\n1', 'iyaa. aku juga mikir mau mau nya di repotin. dan se innocent itu dia. dan temennya ngikut lagi.\n1\n1'], ['Membalas \n@nksthi\nmas aik atrah gong ngerasakne dibungkus langsung karo gilang\n1', 'Wkwkw ', 'Membalas \n@nksthi\nKebalik ra sih?\n1\n2', 'Nggak laaah\n1', 'Membalas \n@nksthi\nCiyeeee curhaat ciyeeeee', 'Membalas \n@nksthi\nBahahahajingan \n@SiELLL666\n1', 'Aku vertigo loh dek. Ntar kalo kmabuh trus aku bunuh diri anak ayam tetangga kamu mau jawab tanggung? \n1\n1', 'Membalas \n@nksthi\n"maaf baru bales"\n\n\'chat ndek isuk lagek di bales\'\n\n"Iya maaf tadi diajak keluar gilang, dia temenku dari sma jadi udah deket banget"\n\n\'Halah asu bajingan omongmu cuman temen\'\n1\n1\n8', '1', 'Membalas \n@nksthi\nThreadnya creepy kenapa disini jadi malah bikin ketawa-ketawa. \n1\n1', 'iyaa. aku juga mikir mau mau nya di repotin. dan se innocent itu dia. dan temennya ngikut lagi.\n1\n1']], [['Membalas \n@panjidorky13\nmysecacc\n@mysecacc6\n · 22 Apr 2020\n[KUMPULAN THREAD KASUS KEJAHATAN SEKSUAL YANG SEDANG VIRAL]\n\nHERE WE GO \nTampilkan utas ini\n9', 'Membalas \n@panjidorky13\nYa Allah males banget \n1\n1', 'y bgtulah ~\n1', 'Membalas \n@panjidorky13\nCuma tau gilang doang xixi\n1\n1', 'oalah in ~\n1', 'Membalas \n@panjidorky13\nSama* pake kacamata\n1\n2', 'tulls in ~', 'Membalas \n@panjidorky13\nfik\n@penjurukanan\n · 31 Jul 2020\nUdah berapa kali kalian membaca tulisan "kurban perasaan" hari ini?\n1\n3', 'oalah in ~', 'Membalas \n@panjidorky13\nDari sini gw tau, ternyata cowok berkacamata, berkumis itu bahaya :v\n1\n15'], ['Membalas \n@panjidorky13\nmysecacc\n@mysecacc6\n · 22 Apr 2020\n[KUMPULAN THREAD KASUS KEJAHATAN SEKSUAL YANG SEDANG VIRAL]\n\nHERE WE GO \nTampilkan utas ini\n9', 'Membalas \n@panjidorky13\nYa Allah males banget \n1\n1', 'y bgtulah ~\n1', 'Membalas \n@panjidorky13\nCuma tau gilang doang xixi\n1\n1', 'oalah in ~\n1', 'Membalas \n@panjidorky13\nSama* pake kacamata\n1\n2', 'tulls in ~', 'Membalas \n@panjidorky13\nfik\n@penjurukanan\n · 31 Jul 2020\nUdah berapa kali kalian membaca tulisan "kurban perasaan" hari ini?\n1\n3', 'oalah in ~', 'Membalas \n@panjidorky13\nDari sini gw tau, ternyata cowok berkacamata, berkumis itu bahaya :v\n1\n15']], [['Membalas \n@Felizersyhy\nbahasanya yaampun "AKU GA BISA DISANGGAH" HAHAHAHA\n47\n38\n85', 'Membalas \n@Felizersyhy\ntumben yaya paham, biasanya gapaham sampe harus diceritain detail baru paham wkwkwk\ntuh kan ya gaada salahnya kita tau masalah sexual gitu, biar gajadi korbannn\n1\n2', 'ini td di ceritain PxL dulu teh(:'], ['Membalas \n@Felizersyhy\nbahasanya yaampun "AKU GA BISA DISANGGAH" HAHAHAHA\n47\n38\n85', 'Membalas \n@Felizersyhy\ntumben yaya paham, biasanya gapaham sampe harus diceritain detail baru paham wkwkwk\ntuh kan ya gaada salahnya kita tau masalah sexual gitu, biar gajadi korbannn\n1\n2', 'ini td di ceritain PxL dulu teh(:']], [['Membalas \n@kholidpurnomoaj\n1\n7\n58', '3\n8\n61', '1\n3\n37', '1\n3\n40', '3\n2\n33', '3\n2\n25', '2\n2\n33'], ['3\n2\n33', '3\n2\n25', '2\n2\n33']]]
# y = [[['@dimsum2000', '@buvnnyi', '@rancting', '@jeonlouse', '@beutymochi', '@agirlinthefz', '@pjswibu', '@sweetiemorre', '@numberwanprince', '@tonelemonade'], ['@dimsum2000', '@buvnnyi', '@rancting', '@jeonlouse', '@beutymochi', '@agirlinthefz', '@pjswibu', '@sweetiemorre', '@numberwanprince', '@tonelemonade']], [['@WidyoLita', '@WidyoLita', '@WidyoLita', '@WidyoLita', '@WidyoLita'], []], [['@yusril_kurzah', '@yusril_kurzah', '@yusril_kurzah', '@yusril_kurzah', '@sabanaayyy', '@_van_nistelRoy'], ['@yusril_kurzah', '@sabanaayyy', '@_van_nistelRoy']], [['@abdulmajid1202', '@Patriciagrayw', '@remukanbakwan__'], ['@abdulmajid1202', '@Patriciagrayw', '@remukanbakwan__']], [['@urjmhngxx', '@nksthi', '@diankurniaa7', '@nksthi', '@Nyimazzz', '@taufiqulirfana', '@SiELLL666', '@rereisnotaloser', '@AidaKsw', '@blueberryonlips', '@rezawiraisyi'], ['@urjmhngxx', '@nksthi', '@diankurniaa7', '@nksthi', '@Nyimazzz', '@taufiqulirfana', '@SiELLL666', '@rereisnotaloser', '@AidaKsw', '@blueberryonlips', '@rezawiraisyi']], [['@panjidorky13', '@Nurulhaayati', '@panjidorky13', '@saoirseneema', '@panjidorky13', '@prakon_r', '@panjidorky13', '@penjurukanan', '@panjidorky13', '@itsssme_'], ['@panjidorky13', '@Nurulhaayati', '@panjidorky13', '@saoirseneema', '@panjidorky13', '@prakon_r', '@panjidorky13', '@penjurukanan', '@panjidorky13', '@itsssme_']], [['@Felizersyhy', '@uwisiitem', '@Felizersyhy'], ['@Felizersyhy', '@uwisiitem', '@Felizersyhy']], [['@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj'], ['@kholidpurnomoaj', '@kholidpurnomoaj', '@kholidpurnomoaj']]]
# z = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h']

# repliesToExcel(z,y, x)
# print(len(x))

'	libragurl@dimsum2000·16 FebMembalas @convomfsIni masih ada wkwkMuhammad Yusril Ihza Kurzah@yusril_kurzah · 30 Jul 2020Gilang yg ini malah maksa minta pap jempol kaki wkwkTampilkan utas ini1'