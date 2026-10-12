from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('auth','0012_alter_user_first_name_max_length')]
    operations = [
        migrations.CreateModel(name='Product',fields=[
            ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
            ('name',models.CharField(max_length=160)),('category',models.CharField(default='General',max_length=80)),
            ('description',models.TextField()),('price',models.DecimalField(decimal_places=2,max_digits=10)),
            ('image_url',models.URLField(blank=True)),('stock',models.PositiveIntegerField(default=10)),
            ('created_at',models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='Order',fields=[
            ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
            ('full_name',models.CharField(max_length=120)),('email',models.EmailField(max_length=254)),
            ('phone',models.CharField(max_length=20)),('address',models.TextField()),('city',models.CharField(max_length=80)),
            ('pincode',models.CharField(max_length=10)),('total',models.DecimalField(decimal_places=2,max_digits=10)),
            ('status',models.CharField(choices=[('PLACED','Placed'),('PROCESSING','Processing'),('SHIPPED','Shipped'),('DELIVERED','Delivered')],default='PLACED',max_length=20)),
            ('created_at',models.DateTimeField(auto_now_add=True)),
            ('user',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='orders',to='auth.user'))]),
        migrations.CreateModel(name='OrderItem',fields=[
            ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
            ('quantity',models.PositiveIntegerField()),('price',models.DecimalField(decimal_places=2,max_digits=10)),
            ('order',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='items',to='shop.order')),
            ('product',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,to='shop.product'))]),
    ]
