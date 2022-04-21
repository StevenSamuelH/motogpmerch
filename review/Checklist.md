## Checklist

1. [X] Create new app by running `django-admin startapp review` in root directory (`motogpmerch`).

2. [X] Register `review/` path in `motogpmerch/urls.py` file, so that you can access the app by accessing [http://localhost:8000/review](http://localhost:8000/review)

3. [X] Add `review` into `INSTALLED_APPS` in `motogpmerch/settings.py` file.

4. Create `ReviewProduk` model:

   1. [X] In this Motogpmerch, you will create `ReviewProduk` model that contains `nama`, `kondisi`, `rating`, `tanggal_penjualan`, `review`, `gambar`
    + **gambar**.
      You can use this code as a template:

      ```python
          from django.db import models

          class ReviewProduk(models.Model):
              nama = models.CharField(max_length=100)
              kondisi = models.CharField(max_length=100)
              rating = models.FloatField()
              tanggal_penjualan = models.DateField()
              review = models.TextField()
              gambar = models.ImageField(upload_to='motogpmerch-images')
      ```

   2. [X] Register your model on `review/admin.py` so you can access your database from Django Admin. Don't forget to run migration.
   3. [X] Add `ReviewProduk` information via Django Admin (see: <https://docs.djangoproject.com/en/3.2/intro/tutorial02/>).

5. Show page to list created `ReviewProduk` with table format:

   1. [X] Create `index` method in `review/views.py` that render HTML for our response. Implement it just like you implement `index` method in [lab_5/views.py](../../lab_5/views.py).
   2. [X] Create a template named `review_produk.html` in `review/templates` folder that contains a table as a template for our `ReviewProduk` model. You can use [lab5.html](../../lab_5/templates/lab5.html) as an example and modify it into `review_produk.html` file.
   3. [X] Customize HTML and CSS in `review_produk.html` template with your own imagination and style.
   4. [X] Create file `review/urls.py` with route `''` for `index` path so that you can access the result by accessing [http://localhost:8000/review](http://localhost:8000/review).

6. [X] Access all the endpoint that you have built in this lab using Web Browser.