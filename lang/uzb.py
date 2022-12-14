# LANG: HINDI [UZBEKISTAN ðºð¿] LANG CODE: HND                       >>  copyright Â©ï¸ 2021 nabilanavab  <<                                         fileName : lang/uzb.py
#                                              Thank: nabilanavab                                           E-mail: nabilanavab@gmail.com

from configs.config import settings

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : """Salom [{}](tg://user?id={})..!!
Ushbu bot sizga PDFar bilan ko'p narsalarni qilishda yordam beradi ð¥³

Asosiy xususiyatlardan ba'zilari:\nâ `Rasmlarni PDFga aylantirish`
â `PDFni rasmlarga o'tkazish`\nâ `Ofis fayllarini PDFga aylantirish`""",
    "HomeACB" : {
        "âï¸ SOZLAMALAR âï¸" : "Home|B", "â ï¸ YORDAM â ï¸" : "Home|C",
        "ð¢ KANAL ð¢" : f"{str(settings.OWNED_CHANNEL)}",
        "ð Rate ð" : f"{str(settings.SOURCE_CODE)}",
        "ð¶ YOPISH ð¶" : "close|mee"
    },
    "HomeAdminCB" : {
        "âï¸ SOZLAMALAR âï¸" : "Home|B", "â ï¸ YORDAM â ï¸" : "Home|C",
        "ð¢ KANAL ð¢" : f"{str(settings.OWNED_CHANNEL)}",
        "ð Rate ð" : f"{str(settings.SOURCE_CODE)}",
        "ð½ STATUSI ð½" : f"status|home", "ð¶ YOPISH ð¶" : "close|mee"
    },
    "HomeB" : """SOZLAMALAR âï¸\n\nFOYDALANUVCHI NOMI   : {}
FOYDALANUVCHI ID           : {}\nUSERNAME    : {}\nQO'SHILGAN SANASI      : {}\n
LANGUAGE    : {}\nAPI                    : {}
ESKIZ            : {}\nMAXSUS NOM         : {}\nFAYL NOMI      : {}""",
    "HomeBCB" : {
        "ð TIL ð" : "set|lang", "ð ESKIZ ð" : "set|thumb",
        "ð NOMI ð" : "set|fname", "ð© API ð©" : "set|api",
        "ð MAXSUS NOM ð" : "set|capt", "Â« BOSH SAHIFA Â«" : "Home|B2A"
    },
    "HomeC" : """ðª **Yordam XABAR** ðª:
```
Asosiy xususiyatlardan ba'zilari:
 â Tasvirlarni PDF ga oÊ»zgartiring\n â PDF qoÊ»llanmalari\n â KoÊ»plab mashhur kodeklarni pdf ga aylantiring
 
Pdf faylini o'zgartirish:
 â PDFâ¥TASIRLAR [barcha, diapazon, sahifalar]\n â xujjatlardan PDFgacha [png, jpg, jpeg]\n â TASVIRLARâ¥PDF\n â PDF METAMAÊ¼LOV\n â PDFâ¥TEXT\n â MATNâ¥PDF\n â Pdf faylni siqish
 â PDF NI BOÊ»LASH [diapazon, sahifalar]\n â PDF-NI BIRGA OLISH\n â SHTAMP QOÊ»SHING\n â PDF NOMNI OÊ»zgartiring\n â PDF-NI AYLANTIRISH\n â PDF FORMATTERI \n â PDFâ¥FIJSON/TXT
 â PDFâ¥HTML [veb koÊ»rinishi]\n â URLâ¥PDF\n â PDFâ¥ZIP/TAR/RAR [barcha, diapazon, sahifalar]\nVa yana koÊ»p.. ```""",
    "HomeCCB" : {"Â« BOSH SAHIFA Â«" : "Home|A", "â ï¸ QO'LLANMA â ï¸" : "Home|D"},
    "HomeD" : """`Bu bepul xizmat bo'lgani uchun men bu xizmatni qancha vaqt saqlab turishimga kafolat bera olmayman..`ð
 
â ï¸ Ko'rsatmalar â ï¸:
ð __Iltimos, bot adminlarini suiiste'mol qilishga urinmang__ ð
ð __Bu yerda spam yubormang, doimiy ravishda taqiqlanishi mumkin ð²__.
ð __ Porno kontent ham sizga DOIMIY BAN beradi ð¯__

**Boshlash uchun istalgan rasmni yuboring:** ð""",
    "HomeDCB" : {"â ï¸ YORDAM â ï¸" : "Home|C", "Â» BOSH SAHIFA Â»" : "Home|A"}  
}

SETTINGS = {
    "default" : ["STANDART â", "MAXSUS â"], "chgLang" : {"SOZLAMALAR âï¸ Â» TILNI O'ZGARTIRISH ð" : "nabilanavab"},
    "error" : "MaÊ¼lumotlar bazasidan maÊ¼lumotlarni olishda nimadir xato ketdi", "lang" : "Endi, xohlagan tilni tanlang...",
    "ask" : ["Endi, Menga yuboring..", "Endi, Menga yuboring... ð\n\nTez.! Matnni ko'rib chiqishga vaqtim yo'q.. ð\n\n/bekor qilish: bekor qilish"],
     "askApi" : "\n\nQuyidagi havolani oching va menga maxfiy kodni yuboring:", "waitApi" : {"Havolani ochish â" : "https://www.convertapi.com/a/signin"},
    "wait" : {"Kutilmoqda.. ð¥±" : "nabilanavab"}, "back" : {"Â« BOSH SAHIFA Â«" : "Home|B2S"}, "errorCB" : {"Â« BOSH SAHIFA Â«" : "Home|B2A"},
    "result" : ["Sozlamalarni yangilab bo'lmadi â", "Sozlamalar muvaffaqqiyatli yangilandi â"], "cant" : "Ushbu funksiyadan foydalanib bo'lmaydi â",
    "feedback" : "Sizga oÊ»xshagan Ajoyib mijozlar sharhlari boshqalarga yordam beradi.\n@azik_developer"
                 "\n\nXatolikni xabar berish {} til:\n`â¢ Maxsus til\nâ¢ Xato xabar\nâ¢ Yangi xabar`",
    "feedbtn" : {"Til xatosi haqida xabar berish" : settings.REPORT},
    "thumb" : [
        {"SOZLAMA âï¸ Â» ESKIZ ð·" : "nabilanavab", "â» QO'SHISH â»" : "set|thumb+", "Â« BOSH SAHIFA Â«" : "Home|B"},
        {"SOZLAMA âï¸ Â» ESKIZ ð·" : "nabilanavab", "â» ALMASHTIRISH â»" : "set|thumb+", "ð O'CHIRISH ð" : "set|thumb-", "Â« BOSH SAHIFA Â«" : "Home|B2S"}
    ],
    "fname" : [
        {"SOZLAMA âï¸ Â» FNAME ð·" : "nabilanavab", "â» QO'SHISH â»" : "set|fname+", "Â« BOSH SAHIFA Â«" : "Home|B2S"},
        {"SOZLAMA âï¸ Â» FNAME ð·" : "nabilanavab", "â» ALMASHTIRISH â»" : "set|fname+", "ð O'CHIRISH ð" : "set|fname-", "Â« BOSH SAHIFA Â«" : "Home|B2S"}
    ],
    "api" : [
        {"SOZLAMA âï¸ Â» API ð·" : "nabilanavab", "â» QO'SHISH â»" : "set|api+", "Â« BOSH SAHIFA Â«" : "Home|B2S"},
        {"SOZLAMA âï¸ Â» API ð·" : "nabilanavab", "â» ALMASHTIRISH â»" : "set|api+", "ð O'CHIRISH ð" : "set|api-", "Â« BOSH SAHIFA Â«" : "Home|B2S"}
    ],
    "capt" : [
        {"SOZLAMA âï¸ Â» MAXSUS NOM ð·" : "nabilanavab", "â» QO'SHISH â»" : "set|capt+", "Â« BOSH SAHIFA Â«" : "Home|B2S"},
        {"SOZLAMA âï¸ Â» MAXSUS NOM ð·" : "nabilanavab", "â» ALMASHTIRISH â»" : "set|capt+", "ð O'CHIRISH ð" : "set|capt-", "Â« BOSH SAHIFA Â«" : "Home|B2S"}
    ]
}

BOT_COMMAND = {"start" : "Xush kelibsiz xabari..", "txt2pdf" : "Matndan PDF yaratish"}

HELP_CMD = {
    "userHELP" : """[FOYDALANUVCHI BUYRUQLARI XABARI]:\n
/start: Botni ishga tushirish\n/cancel: joriy ishni bekor qilish
/delete: PDF qilayotga\n/txt2pdf: Matndan PDF yaratish""",
    "adminHelp" : """\n\n\n[ADMIN BUYRUQLARI XABARI]:\n
/send: foydalanuvchiga shaxsiy xabar yuborish uchun""",
    "footerHelp" : f"""\n\n\nManba-kodi: [I2pdf]({str(settings.SOURCE_CODE)})
Bot: @azik_pdfbot ð\n[Qo'llab quvvatlash]({settings.OWNED_CHANNEL})""",
    "CB" : {"â ï¸ YOPISH â ï¸" : "close|all"}
}

STATUS_MSG = {
    "HOME" : "`Endi hozirgi holatni olish uchun pastdan istalgan variantni tanlang ð±.. `",
    "_HOME" : {
        "ð â SERVER â ð" : "nabilanavab", "ð¶ XOTIRA ð¶" : "status|server",
        "ð¥¥ MA'LUMOTLAR BAZASI ð¥¥" : "status|db", "ð â VRO'YXATNI OLISH â ð": "nabilanavab",
        "ð ADMIN ð" : "status|admin", "ð¤ FOYDALANUVCHILAR ð¤" : "status|users",
        "Â« ORQAGA Â«" : "Home|A"
    },
    "DB" : """ð MA'LUMOTLAR BAZASI :\n\n**â Ma'lumotlar bazasi foydalanuvchilari :** `{}`ta ð\n**â Ma'lumotlar bazasi guruhlari :** `{}`ta ð""",
    "SERVER" : """**â Umumiy xotira     :** `{}`
**â Foydalanilgan xotira     :** `{}({}%)`\n**â Bo'sh xotira      :** `{}`
**â CPU foydalanishi      :** `{}`%\n**â RAM foydalanishi     :** `{}`%
**â Hozirgi ishlar  :** `{}`ta\n**â Xabar IDsi     :** `{}`""",
    "BACK" : {"Â« ORQAGA Â«" : "status|home"}, "ADMIN" : "**Total ADMIN:** __{}__\n",
    "USERS" : "MaÊ¼lumotlar bazasida saqlangan foydalanuvchilar:\n\n", "NO_DB" : "Hozircha maÊ¼lumotlar bazasi oÊ»rnatilmagan ð©"
}

feedbackMsg = f"[Taklif va shikoyat yozish ð]({settings.FEEDBACK})"

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : """Salom guruhdagilar.! ðï¸\nMen bu yerda yangiman {message.chat.title}\n
O'zimni tanishtirishga ijozat bering..\nMening ismim iLovePDF, men sizga ko'p narsalarni qilishga yordam bera olaman
@Telegram PDF fayllaridagi narsalar\n\nUshbu ajoyib bot uchun @azik_developer ga rahmat ð""",
    "HomeACB" : {
        "ð¤  BOT YARATUVCHISI ð¤ ": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "ð¡ï¸ YANGILANISH KANALI ð¡": f"{settings.OWNED_CHANNEL}", "ð Rate ð": f"{settings.SOURCE_CODE}"
    }
}

# BANNED USER UI
BAN = {
    "cbNotU" : "Xabar siz uchun emas.. ð",
    "banCB" : {
        "O'z botingizni yarating": f"{settings.SOURCE_CODE}", "Qo'llanma": f"{settings.SOURCE_CODE}",
        "Yangilanish kanali": "https://telegram.dog/azik_projectss"
    },
    "UCantUse" : """Hey {}\n\nBA'ZI SABABLARGA KO'RA SIZ BU BOTDAN FOYDALANA OLMAYSIZ :(""",
    "UCantUseDB" : """Hey {}\n\nBA'ZI SABABLARGA KO'RA SIZ BU BOTDAN FOYDALANA OLMAYSIZ :(\n\nSABABI: {}""",
    "GroupCantUse" : """{} HECH QACHON MENDAN YAXSHI JAVOB KUTMANG\n
ADMINLAR BU YERDA ISHLASHIMNI CHEKLASHDI.. ð¤­""",
    "GroupCantUseDB" : """{} HECH QACHON MENDAN YAXSHI JAVOB KUTMANG\n
ADMINLAR BU YERDA ISHLASHIMNI CHEKLASHDI.. ð¤­\n\nSABABI: {}""",
    "Force" : """Kuting [{}](tg://user?id={})..!!\n
Katta yuk tufayli bu botdan faqat kanal a'zolari foydalanishi mumkin ð¶\n
Bu Mendan foydalanish uchun quyida ko'rsatilgan kanalga qo'shilishingiz kerakligini bildiradi!\n
Qoâshilgandan soâng ââ»ï¸ Qayta urinishâ»ï¸â tugmasini bosing.. ð""",
    "ForceCB" : {"ð KANALGA ULANISH ð" : "{}", "â»ï¸ Qayta urinish â»ï¸" : "refresh"},
    "Fool" : "Chiroqni olmangà´àµ.. ð¤­"
}

checkPdf = {
    "pg" : "`Sahifalar soni: â¢{}â¢`ta ð",
    "pdf" : """`Ushbu faylni nima qilmoqchisiz.?`\n\nFayl Nomi : `{}`\nFayl Hajmi : `{}`""",
    "pdfCB" : {
        "â­ METADATA â­" : "metaData", "ð³ï¸ KO'RIB CHIQISH ð³ï¸" : "preview",
        "ð¼ï¸ RASMGA O'TKAZISH ð¼ï¸" : "pdf|img", "âï¸ MATNGA O'TKAZISH âï¸" : "pdf|txt",
        "ð SHIFRLAR ð" : "work|encrypt", "ð SHIFRDAN OCHISH ð" : "work|decrypt",
        "ðï¸ SIQISH ðï¸" : "work|compress", "ð¤¸ AYLANTIRISH ð¤¸" : "pdf|rotate",
        "âï¸ KESISH âï¸" : "pdf|split", "ð§¬ BIRLASHTIRISH ð§¬" : "merge", "â¢ï¸ STAMP â¢ï¸" : "pdf|stp",
        "âï¸ QAYTA NOMLASH âï¸" : "work|rename", "ð OCR ð" : "work|ocr",
         "ð¥· A4 FORMATGA O'TKAZISH ð¥·" : "work|format", "ð« YOPISH ð«" : "close|all"
    },
    "error" : """__Men bu fayl bilan hech narsa qilmayman__ ð\n\nð  `KODEK XATOLIGI`  ð""",
    "errorCB" : {"â KODEKDA XATOLIK â" : "error", "ð¸ YOPISH ð¸" : "close|all"},
    "encrypt" : """`FAYL SHIFRLANGAN` ð\n\nFayl Nomi: `{}`\nFayl Hajmi: `{}`""",
    "encryptCB" : {"ð SHIFRDAN OCHISH ð" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """**\nTugalllandi â : **{0}/{1}\n**Tezligi ð:** {2}/s\n**Qolgan vaqt â³:** {3}""",
    "dlImage" : "`Rasmingiz yuklab olinmoqda..â³`", "upFile" : "`Sizga yuborilmoqda..`ð¤",
    "dlFile" : "`Faylingiz yuklab olinmoqda..` ð¥", "upFileCB" : {"ð¤ .. YUBORILMOQDA.. ð¤" : "nabilanavab"},
    "workInP" : "ISHLAB CHIQILMOQDA.. ð", "refresh" : {"â»ï¸ Qayta urinish â»ï¸" : "{}"},
    "takeTime" : """```âï¸ Ish davom etmoqda..`\n`Bu biroz vaqt olishi mumkin..```ð""",
    "cbPRO_D" : ["ð¤ Yuklab olinmoqda: {:.2f}% ð¤", "ð¯ BEKOR QILISH ð¯"], "cbPRO_U" : ["ð¤ YUKLANDI: {:.2f}% ð¤", "ð¯ BEKOR QILISH ð¯"]
}

GENERATE = {
    "deleteQueue" : "`Navbat muvaffaqqiyatli o'chirildi..`ð¤§", "noQueue" : "`Navbat topilmadi..`ð²",
    "noImages" : "Rasm topilmadi.!! ð", "getFileNm" : "Endi menga fayl nomini yuboring ð: ",
    "geting" : "Fayl Nomi: `{}`\nSahifalar: `{}`ta", "getingCB" : {"ð PDF YARATILMOQDA.." : "nabilanavab"},
    "currDL" : "Yuklab olingan {} rasm ð¥±"
}

document = {
    "refresh" : PROGRESS['refresh'], "inWork" : PROGRESS['workInP'], "reply" : checkPdf['pdf'],
    "replyCB" : checkPdf['pdfCB'], "download" : PROGRESS['dlFile'], "process" : "âï¸ Qayta ishlanmoqda..",
    "takeTime" : PROGRESS['takeTime'], "upFile" : PROGRESS['upFile'], "dlImage" : PROGRESS['dlImage'],
    "big" : """Haddan tashqari yuk tufayli, admin pdf fayllar uchun {}mb ni cheklaydi ð
\n`Iltimos, menga {}mb hajmidan kichikroq fayl yuboring` ð""",
    "bigCB" : {"ð 2 Gb qo'llab-quvvatlash botini yarating ð" : "https://t.me/i2pdfbotchannel"},
    "imageAdded" : """`Qo'shildi {} sahifa sizning PDFingizga..`ð¤\n\nFaylNomi: `{}.pdf`""",
    "setHdImg" : """Endi PDF formatiga tasvir HD rejimida ð""",
    "setDefault" : {"Â« Standart sifatga qaytish Â«" : "close|hd"},
    "error" : """NIMADIR XATO KETDI.. ð\n\nXATOLIK: `{}`""",
    "noAPI" : "`Iltimos, aylantirish API'sini qo'shing.. ð©\n\nboshlash Â» sozlamalar Â» api Â» qo'shish/o'zgartirish`",
    "useDOCKER" : "`Fayl qo'llab-quvvatlanmaydi, docker yordamida botni o'rnating`",
    "fromFile" : "`Konvertatsiya qilindi: {} dan {}`ga", "unsupport" : "`Qo'llab quvvatlanmaydigan fayl..ð`",
    "generateRN" : {"YARATISH ð" : "generate", "NOM O'ZGARTIRIB YARATISH âï¸" : "generateREN"},
    "generate" : {"YARATISH ð" : "generate"}, "cancelCB" : {"â¨ Bekor qilish â©" : "close|me"}
}

noHelp = f"`hech kim sizga yordam bermaydi` ð"

split = {
    "inWork" : PROGRESS['workInP'], "cancelCB" : document['cancelCB'],
    "download" : PROGRESS['dlFile'], "exit" : "`Jarayon bekor qilindi..` ð",
    "button" : {
        "âï¸ PDF Â» KESISH â" : "nabilanavab", "Sahifalar soni bilan ð¦" : "split|R",
        "Yakka sahifalar ð" : "split|S", "Â« ORQAGA Â«" : "pdf"
    },
    "work" : ["Range", "Single"], "over" : "`5 marta urinish.. Jarayon bekor qilindi..`ð",
    "pyromodASK_1" : """__Pdf kesish Â» Oraliqda\nEndi, oraliqni kiriting (boshlanish:oxiri) :__
\n/exit __bekor qilish uchun__""",
    "completed" : "`Downloading Completed..` â",
    "error_1" : "`Syntaksis Xatolik: FaqatBoshlangichvaoxirgisahifa `ð¶",
    "error_2" : "`Syntaksis Xatolik: oxirgiRaqamtogrikiritng `ð¶",
    "error_3" : "`Syntaksis Xatolik: birinchiraqamtogrikiriting `ð¶",
    "error_4" : "`Syntaksis Xatolik: sahifasoniraqambolishikerak` ð§ ",
    "error_5" : "`Syntaksis Xatolik: tushashRaqamiYoq yoki Sonmas` ð¶",
    "error_6" : "`Hech qanday raqam topib bo'lmadi..`ð",
    "error_7" : "`Nimadir xato ketdi..`ð", "error_8" : "`Ushbu {} sondan kichik raqamlar kiriting..`ð",
    "error_9" : "`Birinchi sahifalar sonini tekshiring` ð", "upload" : "âï¸ `Sizga yuborilmoqda..` ð¤"
}

pdf2IMG = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "uploadfile" : split["upload"],
    "toImage" : {
        "âï¸ PDF Â» RASMGA O'TKAZISH â" : "nabilanavab", "ð¼ RASM SHAKLDA ð¼" : "pdf|img|img",
        "ð FAYL SHAKLDA ð" : "pdf|img|doc", "ð¤ ZIP SHAKLDA ð¤" : "pdf|img|zip",
        "ð¯ TAR SHAKLDA ð¯" : "pdf|img|tar","Â« ORQAGA Â«" : "pdf" 
    },
    "imgRange" : {
        "âï¸ PDF Â» RASMGA O'TKAZISH Â» {} â" : "nabilanavab", "ð HAMMASINI ð" : "p2img|{}A",
        "ð¤§ ORALIQ BILAN ð¤§" : "p2img|{}R", "ð SAHIFALAR BILAN ð" : "p2img|{}S", "Â« ORQAGA Â«" : "pdf|img"
    },
    "over" : "`5 marta urinish.. Jarayon bekor qilindi..`ð",
    "pyromodASK_1" : """__Pdf - RasmâºFayl sifatida Â» Sahifalar:\nEndi, oraliqni kiriting (boshlanish:oxiri) :__
\n/exit __bekor qilish uchun__""",
    "pyromodASK_2" : """__Pdf - RasmâºFayl sifatida Â» Pages:\nEndi, sonlarni vergul bilan kiriting (1,3,5) :__
\n/exit __bekor qilish uchun__""",
    "exit" : "`Process Canceled..` ð",
    "error_1" : "`Syntaksis Xatolik: FaqatBoshlangichvaoxirgisahifa `ð¶",
    "error_2" : "`Syntaksis Xatolik: oxirgiRaqamtogrikiritng `ð¶",
    "error_3" : "`Syntaksis Xatolik: birinchiraqamtogrikiriting `ð¶",
    "error_4" : "`Syntaksis Xatolik: sahifasoniraqambolishikerak` ð§ ",
    "error_5" : "`Syntaksis Xatolik: tushashRaqamiYoq yoki Sonmas` ð¶",
    "error_6" : "`Hech qanday raqam topilmadi..`ð", "error_7" : "`Nimadir xato ketdi..`ð",
    "error_8" : "`PDF da faqatgina {} sahifa mavjud` ð©", "error_9" : "`birinchi sahifalar sonini tekshiring` ð",
    "error_10" : "__Ba'zi cheklovlar tufayli Bot faqat 50 sahifani ZIP sifatida yuboradi..__ð",
    "total" : "`Umumiy sahifalar: {}..â³`", "upload" : "`Yuborilmoqda: {}/{} sahifalar.. ð¬`",
    "current" : "`Tugallandi: {}/{} sahifalar.. ð¤`", "complete" : "`Yuborish tugallandi.. `ðï¸",
    "canceledAT" : "`Bekor qilindi {}/{} sahifalarda..` ð", "cbAns" : "âï¸ Okey, Bekor qilinmoqda.. ",
    "cancelCB" : {"ð¤ BEKOR QILISH ð¤" : "close|P2I"},     # EDITABLE: â
    "canceledCB" : {"ð BEKOR QILINDI ð" : "close|P2IDONE"},
    "completed" : {"ð TUGALLANDI ð" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "upload" : PROGRESS['upFile'],
    "load" : "__Haddan tashqari yuklanish tufayli siz bir vaqtning o'zida faqat 5 ta pdf faylni birlashtira olasiz__",
    "sizeLoad" : "`Haddan tashqari yuk tufayli Bot Faqat %sMb pdf fayllarni qo'llab-quvvatlaydi..", # removing %s show error
    "pyromodASK" : """__BIRLASHITIRISH pdflarni Â» Umuumiy navbatdagi pdflar: {}__

/exit __bekor qilish uchun__
/merge __birlashitirsh uchun__""",
    "exit" : "`Jarayon bekor qilindi..` ð", "total" : "`Umumiy PDFlar : {} ð¡",
    "current" : "__PDFni yuklab olish boshlanmoqda : {} ð¥__", "cancel" : "`birlashtirish jarayoni tugallandi.. ð`",
    "started" : "__Birlshtirish boshlandi.. __ ðª", "caption" : "`Birlashtirigan pdf ð`",
    "error" : "`balki PDF himoyalangan..`\n\nSababi: {}"
}

metaData = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "download" : PROGRESS['dlFile'],   # [â]
    "read" : "Ilitmos ushbu xabarni qayta o'qing.. ð¥´"
}

preview = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "error" : document['error'],
    "download" : PROGRESS['dlFile'], "_" : "PDFda atigi {} sahifa mavjud ð¤\n\n",
    "__" : "PDF safifalar: {}\n\n", "total" : "`Umumiy sahifalar: {}..` ð¤",
    "album" : "`Albom tayyorlanmoqda..` ð¤¹", "upload" : f"`Yuborilmqoda: oldindan ko;rish rasmlari.. ð¬`"
}

stamp = {
    "stamp" : {
        "âï¸ PDF Â» PECHAT â" : "nabilanavab",
        "Not For Public Release ð¤§" : "pdf|stp|10",
        "For Public Release ð¥±" : "pdf|stp|8",
        "Confidential ð¤«" : "pdf|stp|2", "Departmental ð¤" : "pdf|stp|3",
        "Experimental ð¬" : "pdf|stp|4", "Expired ð" : "pdf|stp|5",
        "Final ð§" : "pdf|stp|6", "For Comment ð¯ï¸" : "pdf|stp|7",
        "Not Approved ð" : "pdf|stp|9", "Approved ð¥³" : "pdf|stp|0",
        "Sold â" : "pdf|stp|11", "Top Secret ð·" : "pdf|stp|12",
        "Draft ð" : "pdf|stp|13", "AsIs ð¤" : "pdf|stp|1",
        "Â« ORQAGA Â«" : "pdf"
    },
    "stampA" : {
        "âï¸ PDF Â» PECHAT Â» RANGI â" : "nabilanavab",
        "Qizil â¤ï¸" : "spP|{}|r", "Ko'k ð" : "spP|{}|b",
        "Yashil ð" : "spP|{}|g", "Sariq ð" : "spP|{}|c1",
        "Pushti ð" : "spP|{}|c2", "Havorang ð" : "spP|{}|c3",
        "Oq ð¤" : "spP|{}|c4", "Qora ð¤" : "spP|{}|c5",
        "Â« Orqaga Â«" : "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "upload" : PROGRESS['upFile'],
    "stamping" : "`Pechatlash boshlanmoqda..` ð ", "caption" : """Pechatlangan pdf\nrangi : `{}`\nannot : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'], "button" : document['cancelCB'],
    "rot360" : "Sizda katta muammo bor..ð", "ocrError" : "Admin cheklagan ðð¤",
    "largeNo" : "menga 5 sahifadan kam pdf yuboring.. ð",
    "pyromodASK_1" : """__PDF {} Â»\nEndi, ilimtos parolni kiriting :__\n\n/exit __bekor qilish uchun__""",
    "pyromodASK_2" : """__Qayta nomlash PDF Â»\nEndi, Iltimos yangi nomni  kiriting:__\n\n/exit __bekor qilish uchun__""",
    "exit" : "`Jarayon bekor qilindi.. `ð", "ren_caption" : "__Yangi nomi:__ `{}`", 
    "notENCRYPTED" : "`Fayl himoyalanmagan..` ð",
    "compress" : "âï¸ `Siqish boshlanmoqda.. ð¡ï¸\nBu biroz vaqt olishi mumkin..`ð",
    "decrypt" : "âï¸ `Paroldan ochish boshlanmoqda.. ð\nBu biroz vaqt olishi mumkin..`ð",
    "encrypt" : "âï¸ `Shifrlash boshlanmoqda.. ð\nBu biroz vaqt olishi mumkin..`ð",
    "ocr" : "âï¸ `OCr qatlam qo'shilmoqda.. âï¸\nBu biroz vaqt olishi mumkin..`ð",
    "format" : "âï¸ `Formatlash boshlandi.. ð¤\nBu biroz vaqt olishi mumkin..`ð",
    "rename" : "âï¸ `Qayta nomlash boshlanmoqda.. âï¸\nBu biroz vaqt olishi mumkin..`ð",
    "rot" : "âï¸ `Aylantirish boshlanmoqda.. ð¤¸\nBu biroz vaqt olishi mumkin..`ð",
    "pdfTxt" : "âï¸ `Matn chiqarib olinmoqda.. ð¾\nBu biroz vaqt olishi mumkin..`ð",
    "fileNm" : "Eski fayl nomi: {}\nYangi fayl nomi: {}",
    "rotate" : {
        "âï¸ PDF Â» AYLANTIRISH â" : "nabilanavab", "90Â°" : "work|rot90", "180Â°" : "work|rot180",
        "270Â°" : "work|rot270", "360Â°" : "work|rot360", "Â« ORQAGA Â«" : "pdf"
    },
    "txt" : {
        "âï¸ PDF Â» MATN QILISH â" : "nabilanavab", "ð XABAR ð" : "work|M", "ð§¾ TXT FAYL ð§¾" : "work|T",
        "ð HTML ð" : "work|H", "ð JSON ð" : "work|J", "Â« ORQAGA Â«" : "pdf"
    }
}

PROCESS = {
    "ocr" : "OCR QOSHILDI  ", "decryptError" : "__Faylni ushbu parol bilan himoyalab bo'lmadi__ `{}` ð¸ï¸",
    "decrypted" : "__Himoyalangan fayl__", "encrypted" : "__Sahida raqami__: {}\n__Parol__ ð: ||{}||",
    "compressed" : """`Haqiqiy hajmi : {}\nSiqilgan hajmi : {}\n\nNisbati : {:.2f} %`""",
    "cantCompress" : "Faylni bundab ortiq siqib bo'lmaydi..ð¤",
    "pgNoError" : """__Bazi sabablarga kora A4 FORMATLASH 5 sahifadan kam bo'lgan pdf fayllarni qo'llab-quvvatlaydi__\n\nJami sahifalar: {} â­""",
    "ocrError" : "`Allaqachon matn qatlami mavjud.. `ð",
    "90" : "__90Â° aylantirilgan__", "180" : "__180Â° aylantirilgan__", "270" : "__270Â° aylantirilgan__",
    "formatted" : "A4 Formatlangan fayl", "M" : "â» Chiqarili {} sahifalar â»",
    "H" : "HTML Fayl", "T" : "TXT Fayl", "J" : "JSON Fayl"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"], "exit" : split['exit'], "nothing" : "Yaratishga hech nima yoq.. ð",
    "TEXT" : "`Matndan PDF yaratish Â»`", "start" : "txt faylini Pdf ga aylantirish boshlandi..ð",
    "font_btn" : {
        "TXT@PDF Â» SHRIFTNI TANLASH" : "nabilanavab", "Times" : "pdf|font|t", "Courier" : "pdf|font|c", "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s", "Zapfdingbats" : "pdf|font|z", "ð« YOPISH ð«" : "close|me"
    },
    "size_btn" : { "TXT@PDF Â» {} Â» jOYLASHISH TANLANG" : "nabilanavab", "To'gri" : "t2p|{}|p", "O'nggag burilgan" : "t2p|{}|l", "Â« Orqaga Â«": "pdf|T2P"},
    "askT" : "__MATNNI PDF QILISH Â» Endi, iltimos sarlavha kiritng:__\n\n/exit __bekor qilish uchun__\n/skip __o'tkazib yuborish__",
    "askC" : "__MATNNI PDF QILISH Â» Now, Iltimos, paragrafni kiriting {}:__\n\n/exit __bekor qilish uchunl__\n/create __yaratish uchun__"
}

URL = {
     "get" : {"ð§­ PDF faylni oling ð§­" : "getFile"}, "close" : HELP_CMD['CB'], "notPDF" : "`PDF fayl emas",
     "error" : "ð Nimadir xato ketdi ð\n\nXATO: `{}`\n\nNB: Guruhlarda botlar faqat guruhga qoÊ»shilgandan keyin yuboriladigan hujjatlarni olishi mumkin =)",
     "done" : "```Deyarli tugadi.. â\nEndi, Yuklash boshlandi.. ð¤```", "_error_" : "menga istalgan url yoki bevosita telegram pdf havolalarini yuboring",
     "openCB" : {"Brauzerda ochish" : "{}"}, "_error" : "`Biror narsa noto'g'ri ketdi =(`\n\n`{}`",
     "_get" : "[Chatni ochish]({})\n\n**CHAT HAQIDA â**\nChat turi: {}\nChat nomi: {}\nChat Usr: @{}\n"
              "Chat ID : {}\nSana : {}\n\n**MEDIYA HAQIDA â**\nMedia: {}\nFayl nomi: {}\nFayl hajmi: {}\n\nFayl turi: {}"
}

getFILE = {
    "inWork" : PROGRESS['workInP'], "big" : "pdf urlni {}mb dan kamroq yuborish", "wait" : "Kutib turing.. Menga ruxsat bering.. ð",
    "dl" : {"ð¥ ..YUKLASH.. ð¥" : "nabilanavab"}, "up" : {"ð¤ ..YUKLASH.. ð¤" : "nabilanavab"},
    "complete" : {"ð COMPLETED ð" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "Bu xususiyat ishlab chiqilmoqda â·ï¸", "Annenn paranjille xatosi.. keyin nima.. ð",
    "Jarayon bekor qilindi.. ð", "Fayl shifrlanmagan.. ð", "Bu haqda hech qanday rasmiy narsa yo'q.. ð", "ð Bajarildi.. ð"
]

inline_query = {
    "TOP" : { "Endi tilni Tanlang" : "nabilanavab" }, "capt" : "TILI SOZLASH âï¸", "des" : "By: @ta_ja199 â¤"
}
