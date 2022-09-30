from email.policy import default
from django.contrib.auth.models import Group
from django.contrib import admin



from .models import Category, Product, Product_history


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    list_filter = [ 'status']
    list_editable = ['status']



    
class Product_historyInline(admin.TabularInline):
    model = Product_history
    raw_name_fields = ['product']


@admin.register(Product_history)
class Product_historyAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'version', 'price']
    list_per_page = 20



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category', 'status', 'version']
    list_filter = ['category', 'status']
    list_editable = ['status']
    inlines = [Product_historyInline]




class GroupsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # list_editable = ['name']



admin.site.unregister(Group)
admin.site.register(Group, GroupsAdmin)





# class UserModel(AbstractUser):
#     list_display = ('id', 'is_staff', 'is_active')
#     list_filter = ['is_staff']
#     list_editable = ['is_staff', 'is_active']





# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)



        





