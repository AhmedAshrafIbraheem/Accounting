
EPS = 1e-2

gray = "gray"
green = "green"
red = "red"
black = "black"
white = "white"

password = "كلمة السر"
newPassword = "كلمة السر الجديدة"
passwordSymbol = "*"

ok = "OK"
back = "العودة"
enterKey = "<Return>"

mainGroup = 'المجموعة الرئيسية'
subGroup = 'المجموعة الفرعية'
kind = 'الصنف'
supplier = 'المورد'
customer = 'العميل'
date = 'التاريخ'
unit = 'الوحدة'

chooseMainGroup = 'اختر المجموعة الرئيسية'
chooseSubGroup = 'اختر المجموعة الفرعية'
chooseKind = 'اختر الصنف'
chooseSupplier = 'اختر المورد'
chooseCustomer = 'اختر العميل'
chooseUnit = 'اختر الوحدة'

area = "المساحة"
paid = "المبلغ المدفوع"
price = "السعر الكلي"

action = "العملية"
chooseAction = "اختر العملية"
money = "المبلغ"

advancePayment = "السلفة"
chooseAdvancePayment = "اختر السلفة"

rowHeight = 50


def isNumber(number):
    try:
        if float(number) >= 0:
            return True
        else:
            return False
    except Exception:
        return False
