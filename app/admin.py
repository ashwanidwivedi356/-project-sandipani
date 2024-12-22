from django.contrib import admin
# from . models import user

# from .models import ContactMessage


# Register your models here.
from django.contrib import admin
from . models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand',
    'product_image']



@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','product','quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','customer','product','quantity','ordered_date','status']
    

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'category', 'subject', 'created_at')
#     search_fields = ('first_name', 'last_name', 'email', 'subject')
#     list_filter = ('category', 'created_at')




# # Register your models here.
