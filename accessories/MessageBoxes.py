import tkinter.messagebox as tkm


def confirmation(): return tkm.askokcancel("تأكيد", "هل أنت متأكد مما ادخلته؟")


def showInfo(message): tkm.showinfo(message=message)


def showNewMoney(money): showInfo(str(money) + " :" + "المبلغ الموجود بالخزينة")


def showNewPassword(password): showInfo(password + " :" + "كلمة السر الجديدة")


def showWarning(message): tkm.showwarning(message=message)


def mainGroupNotChosen(): showWarning('لم يتم اختيار المجموعة الرئيسية بعد')


def subGroupNotChosen(): showWarning('لم يتم اختيار المجموعة الفرعية بعد')


def kindNotChosen(): showWarning('لم يتم اختيار الصنف بعد')


def supplierNotChosen(): showWarning('لم يتم اختيار المورد بعد')


def customerNotChosen(): showWarning('لم يتم اختيار العميل بعد')


def nonNumberArea(): showWarning("المساحة التي ادخلتها ليست رقما")


def nonNumberPaid(): showWarning("المبلغ الذي ادخلته ليس رقما")


def nonNumberPrice(): showWarning("السعر الكلي الذي ادخلته ليس رقما")


def paidGreaterThanPrice(): showWarning("المبلغ المدفوع اكثر من السعر الكلي")


def paidGreaterThanRest(): showWarning("المبلغ المدفوع اكثر من المبلغ المتبقي")


def notEnoughMoney(): showWarning("المبلغ المدفوع اكثر مما في الخزينة")


def notEnoughArea(): showWarning("المساحة المطلوبة أكثر مما في المخزن")


def wrongPassword(): showWarning("كلمة سر خاطئة")


def futureDate(): showWarning("التاريخ الذي ادخلته في المستقبل")


def timeNotChoosen(): showWarning("تاريخ العملية لم يتم اختياره")


def emptyEntry(): showWarning("لم يكتب شيئا بعد")


def repeatedNames(): showWarning("هناك اخر له نفس الاسم")


def actionNotChoosen(): showWarning('العملية لم تختر بعد')


def advancePaymentNotChosen(): showWarning('لم يتم اختيار السلفة بعد')


def nothingFound(): showWarning('لا يوجد')
