#coding: utf-8
'''
  تبدیل تاریخ میلادی به خورشید -
  برنامه نویس : داود اکبری -
  1390-1385
 
  .تاریخ هجری خورشیدی در حالت کلی به دوره های بزرگ 2820 ساله تقسیم شده است 
  .که خود این دروره بزرگ به 21 دوره 128 ساله و یک دوره 132 ساله تقسیم شده است
  .دوره 128 ساله شامل یک دوره 29 ساله و 3 دوره 33 ساله 
  .و دروه 132 ساله شامل یک دوره 29 ساله و دو دوره  33 ساله و در آخر یک دوره 37 ساله است
  .دوره 29 ساله دارای یک دوره 5 ساله و 6 دوره 4 ساله است
  .دوره 33 ساله دارای یک دوره 5 ساله و 7 دوره 4 ساله است
  .دوره 37 ساله دارای یک دوره 5 ساله و 8 دوره 4 ساله است
  .سال های آخر دوره های 5  یا 4 ساله کبیسه است
  .ساله های کبیسه 366 روز و سال های عادی 365 روز دارند
  .منظور از عدد تنها 128 یا 132 یا 29 و... دوره های مربوطه است
'''
from DAClassLibrary import DaParsiDateTime, DAexception
from math import *
from datetime import *
from macpath import split

    
#روز اول سال خورشیدی
firstDay = datetime(622, 03, 22)

#سال های در نظر گرفته نشده - آغاز سال هجری خورشیدی
yearsCountblink = 2346
#تعداد سال دوره بزرگ
yearsCountBigAGE = 2820
#تعداد سال دوره 128ساله
yearsCount128 = 128
#تعداد سال دوره 132 ساله
yearsCount132 = 132
#تعداد سال دروه 29 ساله
yearsCount29 = 29
#تعداد سال دروه 33 ساله
yearsCount33 = 33
#تعداد سال دروه 37 ساله
yearsCount37 = 37
#تعداد سال دروه 5 ساله
yearsCount5 = 5
#تعداد سال دروه 4 ساله
yearsCount4 = 4

#تعداد دروه 128 ساله
Count128Circuit = 21
#تعداد دروه 132 ساله
Count132Circuit = 1

#تعداد سال دوره های 128 ساله
yearsCount128AGES = Count128Circuit * yearsCount128
#تعداد سال دوره های 132 ساله
yearsCount132AGES = Count132Circuit * yearsCount132

#تعداد سال گذشته شده تا قبل از زیر دوره 37 ساله
yearsCountBefore37 = yearsCount29 + (2 * yearsCount33)


#تعداد سال کبیسه دوره 128 ساله
anomalyYearsCount128 = 31
#تعداد سال کبیسه دوره 132 ساله
anomalyYearsCount132 = 32
#تعداد سال کبیسه دوره 29 ساله
anomalyYearsCount29 = 7
#تعداد سال کبیسه دوره 33 ساله
anomalyYearsCount33 = 8
#تعداد سال کبیسه دوره 37 ساله
anomalyYearsCount37 = 9
#تعداد سال کبیسه دوره کوچک 4 یا 5 ساله
anomalyYearsCount4OR5 = 1
#تعداد سال کبیسه کل دوره های 128 ساله
anomalyYearsCount128AGES = Count128Circuit * anomalyYearsCount128
#تعداد سال کبیسه کل دوره های 132 ساله
anomalyYearsCount132AGES = Count132Circuit * anomalyYearsCount132
#تعداد سال کبیسه دوره بزرگ
anomalyYearsCountBigAGE = anomalyYearsCount128AGES + anomalyYearsCount132AGES
#تعداد سال کبیسه سال هایی که در نظر گرفته نشده است
anomalyYearsCountBlink = ((yearsCountblink / yearsCount128) * anomalyYearsCount128) + anomalyYearsCount29 + 3#به این دلیل با 3 و 7 جمع شده که 42 سال دارای یک دوره 29 ساله است که دارای 7 سال کبیسه و 13 سال باقی در دوره 33 ساله است که 13 سال داری 3 سال کبیسه است 
#تعداد روز سال عادی
daysCountNormalYear = 365
#تعداد روز سال کبیسه
daysCountAnomalyYear = 366
#تعداد روز سال هایی که در نظر گرفته نشده
daysCountBlinkYear = (yearsCountblink * daysCountNormalYear) + anomalyYearsCountBlink
#تعداد روز دوره بزرگ 2820 ساله
daysCountBigAGE = (yearsCountBigAGE * daysCountNormalYear) + anomalyYearsCountBigAGE
#تعداد روز دوره 128 ساله
daysCount128 = (yearsCount128 * daysCountNormalYear) + anomalyYearsCount128
#تعداد روز دوره 132 ساله
daysCount132 = (yearsCount132 * daysCountNormalYear) + anomalyYearsCount132
#تعداد روز دوره 29 ساله
daysCount29 = (yearsCount29 * daysCountNormalYear) + anomalyYearsCount29
#تعداد روز دوره 33 ساله
daysCount33 = (yearsCount33 * daysCountNormalYear) + anomalyYearsCount33
#تعداد روز دوره 37 ساله
daysCount37 = (yearsCount37 * daysCountNormalYear) + anomalyYearsCount37
#تعداد روز دوره کوچک 5 ساله
daysCount5 = (yearsCount5 * daysCountNormalYear) + anomalyYearsCount4OR5
#تعداد روز دوره کوچک 4 ساله
daysCount4 = (yearsCount4 * daysCountNormalYear) + anomalyYearsCount4OR5


#شماره سال های کبیسه
arrYearNumber = ( 0, 5, 9, 13, 17, 21, 25, 29, 33, 37 )
#نام برج های سال
parsiMonthName = { 1:'فروردین',
                   2:'ارديبهشت', 
                   3:'خرداد', 
                   4:'تير', 
                   5:'امرداد', 
                   6:'شهريور', 
                   7:'مهر', 
                   8:'آبان', 
                   9:'آذر', 
                   10:'دى', 
                   11:'بهمن', 
                   12:'اسفند'}
#روزهای هفته
parsiDayOfWeek = ( "شنبه", 
                   "يكشنبه", 
                   "دوشنبه", 
                   "سه شنبه", 
                   "چهارشنبه", 
                   "پنجشنبه", 
                   "جمعه" )


#تعداد روز ماه های نیمه اول سال
daysCountYearFirstMid = 31
#تعداد روز ماه های نیمه دوم سال
daysCountYearSecMid = 30
#تعداد ماه در هر نیمه سال
monthCountEachYearMid = 6
#تعداد ماه هر سال
monthCountEachYear = monthCountEachYearMid * 2

#تعداد روز هفته
weekDaysCount = 7

#--------
def which2820(ParsiYear):
    '''
      بدست آوردن اینکه سال مورد نظر در کدام دوره بزرگ است
     "ParsiYear"=>سال خورشیدی
     خروجی نشان می دهد که سال مورد نظر در کدام دوره بزرگ است
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    if (ParsiYear <= 0):
        raise DAexception(".سال مورد قبول از یک شروع می شود")

    ParsiYear += yearsCountblink   
    return ceil(ParsiYear / float(yearsCountBigAGE))#ما سقف عدد بدست آمده را می خواهیم زیرا رقم سمت راست به این معنی است که وارد دوره شده است


#---------    
def which2820AtDay(LastDays):
    '''
     بدست آوردن اینکه تعداد روز ورودی در  کدام دوره بزرگ است
     "LastDays"=>تعداد روز گذشته شده از ابتدای تاریخ خورشیدی
     خروجی نشان دهنده کدام دوره بزرگ است
    '''
    return ceil((LastDays + daysCountBlinkYear) / float(daysCountBigAGE))


#----------
def eraBigAGE(ParsiYear):
    '''
     بدست آوردن مبدا دروه ی بزرگ سالی که از ورودی گرفته می شود
     "ParsiYear"=>سال خورشیدی
     مبدا دوره بزرگ سال مورد نظر
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    return ((which2820(ParsiYear) - 1) * yearsCountBigAGE) - yearsCountblink
#-----------


def passedFromEraBigAGE(ParsiYear):
    '''
     سال طی شده از مبدا دوره مورد نظر بزرگ
     "ParsiYear"=>سال خورشیدی
     سال طی شده از مبدا دوره مورد نظر بزرگ
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    return ParsiYear - eraBigAGE(ParsiYear)
#-----------


def which128Or132(ParsiYear):
    '''
     سال مورد نظر در کدام دوره ی 128 یا 132 است
     "ParsiYear"=>سال خورشیدی
     سال مورد نظر در کدام دوره ی 128 یا 132 است
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    #چون دور بزرگ به 21 دوره 128 و یک دوره 132 تقسیم شده
    return ceil(passedFromEraBigAGE(ParsiYear) / float(yearsCount128))
#------------------   
   
   
def which128Or132AtDay(LastDays):
    '''
     سال مورد نظر در کدام دوره ی128 یا 132 قرار دارد 
     "LastDays"=>ورودی برحسب تعداد روز گذشته شده از ابتدای تاریخ خورشیدی
     سال مورد نظر در کدام دوره ی 128 یا 132  قرار دارد  
    '''
    RestDays = (LastDays + daysCountBlinkYear) - ((which2820AtDay(LastDays) - 1) * daysCountBigAGE)
    RestDays /= float(daysCount128)
    return ceil(RestDays)   
#--------------

     
def era128Or132(ParsiYear):
    '''
     بدست آوردن مبدا دوره 128 یا 132 ای که سال مورد نظر در آن قرار دارد
     "ParsiYear"=>سال خورشیدی
     بدست آوردن مبدا دوره 128 یا 132 ای که سال مورد نظر در آن قرار دارد  
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    
    '''
    What = which128Or132(ParsiYear)
    LateYear = 0

    if (What > Count128Circuit):
        LateYear = yearsCount128AGES
    else :
        LateYear = ((What - 1) * yearsCount128)
    
    if (What > Count128Circuit):
        return (((which2820(ParsiYear) * LateYear) + ((which2820(ParsiYear) - 1) * yearsCount132)) - yearsCountblink)
    else :
        return (eraBigAGE(ParsiYear) + LateYear)
#---------------    
    
    
def passedFromEra128Or132(ParsiYear):
    '''
     چند سال از مبدا دوره 128 یا 132 که سال مورد نظر در آن قرار دارد گذشته است
     "ParsiYear"=>سال خورشیدی
     چند سال از مبدا دوره 128 یا 132 که سال مورد نظر در آن قرار دارد گذشته است 
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    
    '''
    return (ParsiYear - era128Or132(ParsiYear))
#--------------------


def whichAge33(LastParsiYear):
    '''
     چندمین دوره 33 ساله
     "LastParsiYear"=>تعداد سال گدشته شده از مبدا دوره 128 یا 132 ساله    
    '''
    return ceil((LastParsiYear - yearsCount29) / float(yearsCount33))
#----------------


def whichAge33FromRestDays(RestDays):
     '''
      "RestDays"=>تعداد روز گدشته شده از مبدا دوره 128 یا 132 ساله
     '''
     return ceil((RestDays - daysCount29) / float(daysCount33))
#------------------------------ 
 

def passedAge33(LastParsiYear):
    '''
     چند سال از ابتدای دوره 33 ساله می گذرد
     "LastParsiYear"=>تعداد سال گدشته شده از مبدا دوره 128 یا 132 ساله
    '''
    return (yearsCount29 + ((whichAge33(LastParsiYear) - 1) * yearsCount33))
#-----------------------


def whatYearOFSubAge(ParsiYear):
    '''
     سال چندم در هر زیر دوره 29 یا 33 یا 37 است
     "ParsiYear"=>سال خورشیدی
    
     سال چندم در هر زیر دوره 29 یا 33 یا 37 است 
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''   
    What = which128Or132(ParsiYear),
    Last = passedFromEra128Or132(ParsiYear)
    if (What > Count128Circuit):
        if ((Last <= yearsCountBefore37) and (Last > yearsCount29)):
            return (Last - passedAge33(Last))
        else :
            if (Last > yearsCountBefore37):
                return (Last - yearsCountBefore37)
            else :
                return Last
    else :
        if (Last > yearsCount29):
            return Last - passedAge33(Last)
        else :
            return Last
 #-----------------------  

def whichSubAge29Or33Or37(ParsiYear):
    '''
     در کدام زیر دوره 29 یا 33 یا 37 است
     "ParsiYear"=>سال خورشیدی
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود   
    '''        
    What = which128Or132(ParsiYear),
    Last = passedFromEra128Or132(ParsiYear)
    
    if (What > Count128Circuit):
        if ((Last <= yearsCountBefore37) and (Last > yearsCount29)):
            return whichAge33(Last)
        else :
            if (Last > yearsCountBefore37):
                return yearsCount37  
            else :
                return yearsCount29    
    else :
        if (Last > yearsCount29):
            return whichAge33(Last)
        else :
            return yearsCount29             
#-------------------------  


def whichSubAge29Or33Or37AtDay(LastDays):
    '''
     در کدام زیر دوره 29 یا 33 یا 37 است
     "LastDays"=>روز گذشته شده از ابتدای دوره 128 یا 132   
    '''
        
    What128Or132 = which128Or132AtDay(LastDays)
    RestDays = (LastDays + daysCountBlinkYear) - ((which2820AtDay(LastDays) - 1) * daysCountBigAGE)
    if (What128Or132 > Count128Circuit):
        RestDays -= (Count128Circuit * daysCount128)
    else :
        RestDays -= ((What128Or132 - 1) * daysCount128)
       
  
    if (What128Or132 > Count128Circuit):
        if ((RestDays > daysCount29) and (RestDays <= (daysCount29 + (2 * daysCount33)))):
            return whichAge33FromRestDays(RestDays)
        else :
            if (RestDays > (daysCount29 + (2 * daysCount33))):
                return yearsCount37
            else :
                return yearsCount29
    else :
          if (RestDays > daysCount29):
              return whichAge33FromRestDays(RestDays)
          else :
              return yearsCount29
#------------------------------------   
 
 
def leapYear(ParsiYear):
    '''
       شناسایی اینکه سال کبیسه است یا نه
       "ParsiYear"=>سال خورشیدی
       اینکه سال کبیسه است یا نه 
       توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    Year = whatYearOFSubAge(ParsiYear)
    return ((Year % yearsCount4 == 1) and  (Year != 1))
#---------------


def parsiMonthDaysCount(ParsiYear, Month):
    '''
     تعداد روز های برج های ایرانی
     "ParsiYear"=>سال خورشیدی
     "Month"=>برج خورشیدی
     اینکه سال کبیسه است یا نه 
     توضیح=>اگر شماره ماه از 1 کوچکتر و از 12 بزرگتر باشد خطا صادر می شود -یا- اگر سال از 1 کمتر باشد     
    '''
        
    if ((Month > 12) or (Month < 1)):
        raise DAexception( ".شماره برح های فارسی از 1 شروع شده و به 12 ختم می شود")
     
    if ((Month >= 1) and (Month <= 6)):
        return 31
    else :
        if (((Month >= 7) and (Month <= 11))):
            return 30 
        else :
            if ((Month == 12) and (leapYear(ParsiYear))):
                return 30
            else :
                return 29
#---------------------------


def multipleLeapYear(ParsiYear):
    '''
     تعداد سال کبسه تا قبل از سال مورد نظر
     "ParsiYear"=>سال خورشیدی
   
     تعداد سال کبسه تا قبل از سال مورد نظر
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
    #دوره 128 ساله ,31 سال و در دوره ی 132 ساله, 32 سال کبيسه وجود دارد و در هر دوره بزرگ 21 دوره 128 ساله و 1 دوره 132 ساله داريم.
    Befor2820Now = (which2820(ParsiYear) - 1) * anomalyYearsCountBigAGE #تعداد سال های کبيسه دوره های 2820 بزرگ قبل از دوره بزرگ سال مورد نظر
    What = which128Or132(ParsiYear)
 
    if (What > Count128Circuit):
        Befor128Or132Now = anomalyYearsCount128AGES
    else :
        Befor128Or132Now = (What - 1) * anomalyYearsCount128

    #تعداد سال کبیسه تا قبل از دور 132 سال مورد نظر موجود- بعد از ؟
    #تعداد سال کبیسه تا قبل از دور 128 سال مورد نظر موجود - بعد از دونقطه
    
    #تعداد سال کبیسه طی شده تا قبل از سال مورد نظر در داخل دوره 128 یا 132
    #تعداد سال دقیق طی شده
    
    if leapYear(ParsiYear):#سال طی شده از ابتدای دوره 128 یا 132 تا سال مورد نظر
        LastFrom128Or132 = (passedFromEra128Or132(ParsiYear) - 1)
    else :
       LastFrom128Or132 = passedFromEra128Or132(ParsiYear)
           
    SubAge = whichSubAge29Or33Or37(ParsiYear)
     
    if (SubAge == yearsCount29):
        LastFrom128Or132 -= 1
    else : 
       if ((SubAge >= 1) and (SubAge <= 3)):
           LastFrom128Or132 -= (1 + SubAge)
       else :
           LastFrom128Or132 -= 4
    
    LastFrom128Or132 /= 4#/تعداد سال کبیسه طی شده از ابتدای 128 یا 132 تا سال مورد نظر
    
    return long(Befor2820Now) + long(Befor128Or132Now) + long(LastFrom128Or132)#تعداد سال کبیسه کل
#--------------------------


def dayToDate(ParsiYear, RestDay):
    '''
     تبدیل روز به تاریخ خورشیدی با گرفتن سال و تعداد روز باقی مانده
     "ParsiYear"=>سال فارسی
     "RestDay"=>روز باقی مانده
    
     تاریخ روز مورد نظر 
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطا صادر می شود
    '''
        
    daysCountFirstMid = monthCountEachYearMid * daysCountYearFirstMid#تعداد روز نیمه اول سال

    RestDay += 1

    IsAYearEndDay = ((RestDay / daysCountAnomalyYear) == 1) and (not leapYear(ParsiYear))#فهمیدن اینکه روز آخر هست و سال کبیسه نیست
    #به منظور ننوشتن دستورات شرطی تو در تو 30 یا 31 را به این صورت می شناسیم
    MonthDaysCount = (daysCountYearSecMid + (2 - ceil(RestDay / daysCountFirstMid)))
    WhatIsAMid = int(RestDay / daysCountFirstMid)#صفر مشخص کننده نیمه اول و یک مشخص کننده نیمه دوم است
    #به این دلیل مقدار را از 2 کم می کنیم جون دو نیم سال دارم و سال دوم باید صفر باشد
    RestDay -= (daysCountFirstMid * WhatIsAMid)
    Month = RestDay / MonthDaysCount
    IsAEndDay = int((RestDay - ((ceil(Month) - 1) * MonthDaysCount)) / MonthDaysCount)#اگز روز آخر ماه باشد 1 وگرنه صفر است
    Month = ceil(Month) + (monthCountEachYearMid * WhatIsAMid)#اگر در ماه دوم باشیم با 6 چمع می شود
    RestDay = int((RestDay % MonthDaysCount) + (IsAEndDay * MonthDaysCount))
    
    if IsAYearEndDay:
        RestDay -= (daysCountYearSecMid - 1)
    
    if IsAYearEndDay:
        Month -= (monthCountEachYear - 1)
   
    if IsAYearEndDay:
        ParsiYear += 1
    
    return  DaParsiDateTime(ParsiYear, Month, RestDay)

#--------------------------


def firstDayYear(ParsiYear):
    '''
     محاسبه روز اول سال مورد نظر
     "ParsiYear"=>سال خورشیدی
    
     محاسبه روز اول سال مورد نظر 
     توضیح=>اگر سال ورودی از 1 کمتر باشد خطاParsiMonthDaysCount صادر می شود   
    '''        
    Days = multipleLeapYear(ParsiYear)
    Days %= weekDaysCount
    Days += (((ParsiYear - 1) % weekDaysCount) + 5)#روز اول سال یک  پنج شنبه بوده و به همین دلیل با 5 جمع می کنیم
    Days %= weekDaysCount
    return Days
#--------------------



def firstDayMonth(ParsiYear, MonthNumber):
    '''
     شماره روز اول برج مورد نظر
     "ParsiYear"=>سال خورشیدی
     "MonthNumber"=>شماه برج
     شماره روز اول برج مورد نظر 
     توضیح=>اگر شماره ماه از 1 کوچکتر و از 12 بزرگتر باشد خطا صادر می شود
    '''
    if ((MonthNumber > 12) or (MonthNumber < 1)):
        raise DAexception( ".شماره برح های فارسی از 1 شروع شده و به 12 ختم می شود")
    First = firstDayYear(ParsiYear)#روز اول سال مورد نظر
    
    if (MonthNumber <= weekDaysCount):
        First += ((MonthNumber - 1) * 3)
    else :
        First += ((MonthNumber + 2) * 2)
    
    First %= weekDaysCount
    return First
#----------------------


def dayOfWeekNumber(parsiDate):
    '''
     شماره روز هفته تاریخ مورد نظر
     "parsiDate"=>تاریخ خورشیدی
    
     شماره روز هفته تاریخ مورد نظر 
    '''
    #روز تاریخ را به این خاطر از یک کم می کنیم تا تعداد روز گذشته شده تا قبل از آن روز را بدست آوریم
    return ((firstDayMonth(parsiDate.Year, parsiDate.Month) + (parsiDate.Day - 1)) % weekDaysCount)
#-------------------------


def dayOfWeekName(parsiDate):
    '''
     نام خورشیدی روز تاریخ مورد نظر
     "parsiDate"=>تاریخ خورشیدی
    
     نام خورشیدی روز تاریخ مورد نظر    
    '''
    return parsiDayOfWeek[dayOfWeekNumber(parsiDate)]
#------------------


def what5Or4(LastDays):
    '''
     محاسبه چندمین زیر دوره کوچک چهار ساله یا پنج ساله
     "LastDays"=>تعداد روز گذشته شده
    
     چندمین زیر دوره کوچک چهار ساله یا پنج ساله 
    '''        
    What = 0
    if (LastDays > daysCount5): #1826تعداد روز دوره کوچک 5 است
        LastDays -= daysCount5
        What = ceil(LastDays / daysCount4)
    
    return  int(What)

#----------------------------

def daysToYear(LastDays, RestDays):
    '''
     تبدیل روز ها ی گذشته شده به سال پارسی
     "LastDays"=>تعداد روز گذشته شده
     "RestDays"=>روز باقی مانده
    
     تبدیل روز ها ی گذشته شده به سال پارسی 
    '''
    What2820 = which2820AtDay(LastDays)#کدام 2820 بزرگ
    Years2820 = (What2820 - 1) * yearsCountBigAGE#سال های 2820
    RestDays = (LastDays + daysCountBlinkYear) - ((What2820 - 1) * daysCountBigAGE)
    
    What128Or132 = which128Or132AtDay(LastDays)
    
    if (What128Or132 > Count128Circuit):
        Years128Or132 = yearsCount128AGES
    else :
        Years128Or132 = (What128Or132 - 1) * yearsCount128
                         
    if (What128Or132 > Count128Circuit):
        RestDays -= (Count128Circuit * daysCount128)
    else :
        RestDays -= ((What128Or132 - 1) * daysCount128)

    Year = Years2820 + Years128Or132

    SubAge29Or33Or37 = whichSubAge29Or33Or37AtDay(LastDays)

    if ((SubAge29Or33Or37 >= 1) and (SubAge29Or33Or37 <= 3)):
        RestDays -= (daysCount29 + ((SubAge29Or33Or37 - 1) * daysCount33))
    else :
        if (SubAge29Or33Or37 == yearsCount37):
            RestDays -= (daysCount29 + (2 * daysCount33))
    
    if ((SubAge29Or33Or37 >= 1) and (SubAge29Or33Or37 <= 3)):
        Year += (yearsCount29 + ((SubAge29Or33Or37 - 1) * yearsCount33))
    else :
        if (SubAge29Or33Or37 == yearsCount37):
            Year += (yearsCount29 + (2 * yearsCount33))            
    
    SubAge5Or4 = what5Or4(RestDays)#تعداد زیر دوره گذشته شده 5 یا 4 #تعداد سال کبیسه
    RestDays -= ((arrYearNumber[SubAge5Or4] * daysCountNormalYear) + SubAge5Or4)
    IN5O4 = (RestDays - 1) / float(daysCountNormalYear)
    Inside5Or4 = floor(IN5O4)#سال چندم زیر دوره 5 یا 4
    RestDays -= (daysCountNormalYear * Inside5Or4)#داخل زیر دوره کوچک 5 یا 4

    if (((Inside5Or4 == yearsCount4) and (arrYearNumber[SubAge5Or4] > 0)) or (Inside5Or4 == yearsCount5)): #چون یک سال کبیسه است و در ضزب محاسبه نمی شود
        RestDays -= 1

    Year = (Year + arrYearNumber[SubAge5Or4] + Inside5Or4 + 1) - yearsCountblink#با یک به خاطر اینکه از سال جدید آغاز شود چمع شد و از 2346 به این دلیل کم شد که سال های نادیده است
    return (Year, RestDays)

#------------------------------

def convertToParsiDate(Date):
    '''
     تبدیل تاریخ میلادی به خورشیدی
     "Date"=>تاریخ میلادی
    
     تاریخ خورشیدی 
     توضیح=>اگر تاریخ ورودی از تاریخ - 0622/03/22 - میلادی کمتر باشد خطا صادر می شود
    '''        
    if (Date < datetime(622, 3, 22)):
        raise DAexception( ".تاریخ 0622/03/22 میلادی برار با روز اول تاریخ خورشیدی است" + "\n .باید تاریخ ورودی برابر یا بزرگتر از این تاریخ باشد")

    RestDays = 0
    LastDays = (Date - firstDay).days #تعداد روز گذشته شده از سال یک تا تاریخ ورودی #1/01/01=622/03/22
    FirstYearsAndLastDays = daysToYear(LastDays, RestDays)#بدست  آوردن سال ابتدای سال تاریخ مورد نظر
    
    #parsiDate = DayToDate(FirstYears, RestDays)
    parsiDate = dayToDate(FirstYearsAndLastDays[0], FirstYearsAndLastDays[1])

    return DaParsiDateTime(parsiDate.Year, parsiDate.Month, parsiDate.Day, Date.hour, Date.minute, Date.second, Date.microsecond)
#---------------------------------------


def parsiDate():
    '''  
     تاریخ خورشیدی
    '''      
    
    return convertToParsiDate(datetime.now())


       
def convertToGregorian(parsiDate):
    '''
      تبدیل تاریخ خورشیدی به میلادی
      "parsiDate"=>تاریخ فارسی
      تبدیل تاریخ خورشیدی به میلادی    
    '''
    MultiplesAnomaly = multipleLeapYear(parsiDate.Year) - anomalyYearsCountBlink#تعداد سال کبیسه کل منهای تعداد سال کبیسه نادیده
    Days = ((parsiDate.Year - 1) * daysCountNormalYear) + MultiplesAnomaly#تعداد کل روز های طی شده تا ابتدای سال مورد نظر
   
    if (parsiDate.Month > monthCountEachYearMid):
        ExtraDays = monthCountEachYearMid
    else :
        ExtraDays = (parsiDate.Month - 1)
            
    OtherDays = ((parsiDate.Month - 1) * daysCountYearSecMid) + ExtraDays#ماه ها تا قبل از ماه مورد نظر ضرب در 30  و با روز اضافی مر بوط به فصل بهار و تابستان جمع شده
    Days += ((OtherDays + parsiDate.Day) - 1)#بدین دلیل از یک  کم می شود چون 1/1/1 یک روز کامل است و در نظر گرفته شده است و می خواهیم از 0/0/0 حساب شود

    date = firstDay + timedelta(days = Days)
        
    return datetime(date.year, date.month, date.day, parsiDate.Hour, parsiDate.Minute, parsiDate.Second, parsiDate.Microsecond)



def strToParsiDate(str):
    '''
    تبدیل رشته به تاریخ خورشیدی
    '''
    try:
       
        dt = str.split(' ')   
        
        splitDate = dt[0].split('/')
        
        splitDate[0] = int(splitDate[0])
        splitDate[1] = int(splitDate[1])
        splitDate[2] = int(splitDate[2])
        
        
        if (len(dt) > 1):
            splitTime = dt[1].split(':')
            
            splitTime[0] = int(splitTime[0])
            splitTime[1] = int(splitTime[1])
            
            if (len(splitTime) > 2):
                splitSM = splitTime[2].split('.')
                
                splitTime[2] = int(splitSM[0]) 
                splitTime3 = 0               
                if (len(splitSM) > 1):
                    splitTime3 = int(splitSM[1])
                
                splitTime = (splitTime[0], splitTime[1], splitTime[2],splitTime3)                    
                    
            else:
                splitTime = (splitTime[0], splitTime[1], 0,0)
                   
        else:
            splitTime = (0,0)
            
        
        return DaParsiDateTime(splitDate[0], splitDate[1], splitDate[2], splitTime[0], splitTime[1], splitTime[2], splitTime[3])
    
    except:
        raise DAexception("Please enter correct date and time!?")
        
     
    
        

        


