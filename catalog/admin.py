from django.contrib import admin
from catalog.models import Book, bookInstance,Author,Genre, language
from django.utils import dateformat
import datetime
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(language)



@admin.register(bookInstance)
class instanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','borrower','issued','returned')
    list_filter = ('issued','returned','issued_at','return_date')
    fields = ('borrower','book',('issued','returned'), 'quantity','issued_at', 'return_date')
 
  

    # def days_remaining(self,obj):
    #     if obj.issued:
    #         d_1 = datetime.now().date()
    #         d_2 = obj.return_date.date()
    #         if d_2 < d_1:
    #             delta = d_1 - d_2
    #             return f"{delta.days}"




        # if obj.issued:    
        #     if obj.returned:
        #         return 'returned'
        #     elif obj.return_date:
        #         y,m,d = str(timezone.now()).split('-')
        #         today = datetime.date(int(y),int(m),int(d))
        #         y2,m2,d2 = str(obj.return_date()).split('-')
        #         lastdate = datetime.date(int(y2),int(m2),int(d2))
        #         if lastdate>today:
        #             return f"{(lastdate-today).days} Not Returned Yet!!"
        #         return f"{(today-lastdate).days} days passed"
        #     return "not issued"
        # return "not issued"
 
