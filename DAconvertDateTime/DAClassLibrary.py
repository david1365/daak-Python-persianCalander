#coding: utf-8

import DAConvertDate
from datetime import *


class DAexception(BaseException):
    pass



class DaParsiDateTime(object):
    '''
     نوع داده تاریخ خورشیدی
     برنامه نویس : داود اکبری 
     1390-1385
    '''    
     
    def __init__(self, year = 1, month = 1, day = 1, hour = 0, minute = 0, second = 0, microsecond = 0):
        '''
        Constructor
        متدی که داده را با توجه به پارامتر ورودی می سازد
        "year"=>سال خورشیدی بین - 1 و 9223372036854775807 است
        "month"=>برج خورشیدی - بین 1 و 12 است
        "day"=>روز خورشیدی - بین 1 و حداکثر تعداد روز ماه مورد نظر
        "hour"=>ساعت - بین 0 و 23 است
        "minute"=>دقیقه - بین 0 و 59 است
        "second"=>ثانیه - بین 0 و 59 است
        "microsecond"=>میلی ثانیه - بین 0 و 999999 است
        "توضیح"=> سال کمتر از 1 و بیشتر از9223372036854775807 یا برج کمتر از 1 و بیشتر از 12 یا روز کمتر از 1 و بیشتر از تعداد روزش در هر سال یا ساعت کمتر از 0 و بیشتز از 23 یا دقیقه کمتر از 0 و بیشتر از 59 یا ثانیه کمتر از 0 و بیشتر از 59 و میلی ثانیه کمتر از صفر و بیشتر از 999 
        '''      
                                
        if ((year <= 0) or (year > 9223372036854775807)):
                raise DAexception(".سال مورد قبول بین یک و 9223372036854775807 است")
        elif ((month > 12) or (month < 1)) :
                raise DAexception(".برج های سال خورشیدی بین 1 و 12 است")
        elif ((day < 1) or (day > DAConvertDate.parsiMonthDaysCount(year, month))):
                raise DAexception("روز برج" + " " + DAConvertDate.parsiMonthName[month] + " سال " + str(year) + " بین عدد 1 و  " + DAConvertDate.parsiMonthDaysCount(year, month) + " است ")
        elif ((hour < 0) or (hour > 23)):
                raise DAexception("ساعت بین 0 و 23 است")        
        elif ((minute < 0) or (minute > 59)):
                raise DAexception("دقیقه بین 0 و 59 است")
        elif ((second < 0) or (second > 59)):
                raise DAexception("ثانیه بین 0 و 59 است")
        elif ((microsecond < 0) or (microsecond > 999999)):
                raise DAexception("میلی ثانیه بین 0 و 999999 است")

        
        self.__year = long(year)
        self.__month = int(month)
        self.__day = int(day)
        self.__hour = int(hour)
        self.__minute = int(minute)
        self.__second = int(second)
        self.__microsecond = int(microsecond)


    
    
    
    def __addZero(self, str):
        if len(str) < 2 :
            str = '0' + str
        return str
    
    #رشته تاریخ
    def __str__(self):
        return str(int(self.__year)) + '-' + self.__addZero(str(int(self.__month))) + '-' + self.__addZero(str(int(self.__day))) + ' ' + self.__addZero(str(int(self.__hour))) + ':' + self.__addZero(str(self.__minute)) + ':' + self.__addZero(str(self.__second)) + '.' + self.__addZero(str(self.__microsecond))
        
    #رشته ی تاریخ پارسی
    def parsiStrDateTime(self):
        return str(int(self.__year)) + '/' + self.__addZero(str(int(self.__month))) + '/' + self.__addZero(str(int(self.__day))) + ' ' + self.__addZero(str(int(self.__hour))) + ':' + self.__addZero(str(self.__minute)) + ':' + self.__addZero(str(self.__second)) + '.' + self.__addZero(str(self.__microsecond))
        
    
    #حداکثر تاریخ خورشیدی
    def __getMaxValue(self):
        return  DaParsiDateTime(9223372036854775807, 12, 29, 23, 59, 59, 999999)    
    MaxValue = property(__getMaxValue, None, None, 'حداکثر تاریخ خورشیدی')
    

    #حداقل تاریخ خورشیدی
    def __getMinValue(self):
        return DaParsiDateTime()        
    MinValue = property(__getMinValue, None, None, 'حداقل تاریخ خورشید')


    #نام خورشیدی برج مورد نظر
    def __getMonthName(self):
        return DAConvertDate.parsiMonthName[self.__month]
    MonthName = property(__getMonthName, None, None, 'نام خورشیدی برج مورد نظر')
    

    #شماره روز هفته تاریخ مورد نظر
    def __getDayOfWeekNumber(self):
        return DAConvertDate.dayOfWeekNumber(self)
    DayOfWeekNumber = property(__getDayOfWeekNumber, None, None, 'شماره روز هفته تاریخ مورد نظر')
    

    #نام روز هفته تاریخ مورد نظر
    def __getDayOfWeekName(self):
        return DAConvertDate.dayOfWeekName(self)
    DayOfWeekName = property(__getDayOfWeekName, None, None, 'نام روز هفته تاریخ مورد نظر')


    #میلی ثانیه
    def __getMicrosecond(self):
        return self.__microsecond 
    Microsecond = property(__getMicrosecond, None, None, 'میلی ثانیه')
    

    #ثانیه
    def __getSecond(self):
        return self.__second
    Second = property(__getSecond, None, None, 'ثانیه')
    

    #دقیقه
    def __getMinute(self):
        return self.__minute 
    Minute = property(__getMinute, None, None, 'دقیقه')
    

    #ساعت
    def __getHour(self):
        return self.__hour 
    Hour = property(__getHour, None, None, 'ساعت')
    
   
    #روز
    def __getDay(self):
        return self.__day
    Day = property(__getDay, None, None, 'روز')
    

    #برج
    def __getMonth(self):
        return self.__month 
    Month = property(__getMonth, None, None, 'برج')
    

    #سال
    def __getYear(self):
        return self.__year 
    Year = property(__getYear, None, None, 'سال')
    
    
    #تاریخ و زمان حالا
    def __getNow(self):
        return DAConvertDate.parsiDate() 
    Now = property(__getNow, None, None, 'تاریخ و زمان حالا')
        
    
    def addYears(self, Years):
        '''
         اضافه کردن به سال
         "Years"=>تعداد سال
        '''
        
        return  DaParsiDateTime(self.Year + Years, self.Month, self.Day, self.Hour, self.Minute, self.Second, self.Microsecond)
    
    '''
    این تابع مشکلی ندارد ولی تابع بهینه شده در کد های زبان پی اچ پی موجود است
    ''' 
    def addMonths(self, months):
        '''
         اضافه کردن به برج
        "months"=>تعداد برج
    
        '''
        if (months != 0):
            #در زیر تعداد سال یا ماهی که قرار است کم یا زیاد شود بدست می آید
            tempYear = abs(months) / 12
            tempMonth = abs(months) % 12
         
            #در زیر اگر ورودی صفر باشد هیچ عملی انجام نمی شود ولی اگر منفی یا مثبت باشد با توجه به آن ماه و سال بدست می آید
            if (months > 0):
                tempMonth = self.Month + tempMonth
                if (tempMonth > 12):
                    tempYear += (tempMonth / 12)#حداکثر یکسال اضافه می شود
                    tempMonth = (tempMonth % 12)                                  
            else :
                tempMonth = self.Month - tempMonth
                if (tempMonth <= 0):
                    tempMonth = 12 + tempMonth#با این دلیل با 12 جمع می شود زیرا عدد منقی است و خروجی عددی مثبت و ماه مورد نظر است
                    tempYear += 1#در زیر .سال با تابع مربوط به خود کم یا زیاد می شود و جمع با ۱ یعنی یکسال دیگر برای کم شدن اضافه می شود                    
                tempYear = -tempYear#در اینجا منفی می شود زیرا می خواهیم اگر با تابع حساب شد کم کند 
            
            return DaParsiDateTime(self.addYears(tempYear).Year, tempMonth, self.Day, self.Hour, self.Minute, self.Second, self.Microsecond)
        
        return self
    
    
    def addDays(self, days):
        '''
         اضافه کردن به روز
        "days"=>تعداد روز
        '''
        return DAConvertDate.convertToParsiDate(DAConvertDate.convertToGregorian(self) + timedelta(days = days))
           
    
    def addHours(self, hours):
        '''
         اضافه کردن به ساعت
        "hours"=>تعداد ساعت
        '''
        return DAConvertDate.convertToParsiDate(DAConvertDate.convertToGregorian(self) + timedelta(hours = hours))
    
    
    def addMinutes(self, minutes):
        '''
         اضافه کردن به دقیقه
        "minutes"=>تعداد دقیقه
        '''
        return DAConvertDate.convertToParsiDate(DAConvertDate.convertToGregorian(self) + timedelta(minutes = minutes))
    
    
    def addSeconds(self, seconds):
        '''
         اضافه کردن به ثانیه
        "seconds"=>تعداد ثانیه
        '''
        return DAConvertDate.convertToParsiDate(DAConvertDate.convertToGregorian(self) + timedelta(seconds = seconds))
    
    
    def addMicroseconds(self, microseconds):
        '''
         اضافه کردن به میکرو ثانیه
        "microseconds"=>تعداد میکرو ثانیه
        '''
        return DAConvertDate.convertToParsiDate(DAConvertDate.convertToGregorian(self) + timedelta(microseconds = microseconds))

