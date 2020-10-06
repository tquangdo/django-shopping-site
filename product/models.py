from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Loại Sản phẩm"


class ProductModel(models.Model):
    title = models.CharField(
        max_length=255, default='', verbose_name='Tiêu đề')
    description = models.TextField(default='', verbose_name='Mô tả')
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, verbose_name='Loại sản phẩm')
    product_img = models.ImageField(
        upload_to='products/', verbose_name='Ảnh sản phẩm', blank=True)
    price = models.IntegerField(default=0, verbose_name='giá tiền')
    active = models.BooleanField(default=True, verbose_name='trạng thái')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sản phẩm"


class VariationModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, verbose_name='sản phẩm')
    title = models.CharField(
        max_length=255, default='', verbose_name='Tiêu đề')
    price = models.IntegerField(default=0, verbose_name='Giá tiền')
    sale_price = models.IntegerField(default=0, verbose_name='Giá sale')
    inventory = models.IntegerField(default=0, verbose_name='Tồn kho')
    active = models.BooleanField(default=True, verbose_name='Trạng thái')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sản phẩm change"
