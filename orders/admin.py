from django.contrib import admin
from .models import Order, OrderDetails
import csv
import datetime
from django.http import HttpResponse


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    # raw_id_fields = ['product']
    list_editable = []



@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'quantity', 'returned_quantity', 'version']
    list_editable = ['quantity', 'returned_quantity']






def export_to_csv(modeladmin, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(context_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [fields for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'




class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cash', 'card', 'returned', 'username']
    list_editable = ['cash', 'card', 'returned']
    list_filter = ['created']
    inlines = [OrderDetailsInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)