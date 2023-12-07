# Django Delete Data

To delete data in a Django model, you can use the Django ORM (Object-Relational Mapping) system. Here are the steps to delete data in a Django model:

### Use Django Shell:

1. **Open the Django Shell:**
   Open a terminal or command prompt and navigate to your project directory. Run the following command to open the Django shell:

   ```bash
   python manage.py shell
   ```

2. **Import the Model:**
   Import the model you want to delete data from:

   ```python
   from yourapp.models import YourModel
   ```

   Replace `yourapp` with the actual name of your Django app and `YourModel` with the name of your model.

### Delete Data:

3. **Retrieve the Instance to Delete:**
   Retrieve the instance you want to delete using a query. For example, to delete a book with a specific title:

   ```python
   book_to_delete = YourModel.objects.get(title='Django Advanced')
   ```

   Replace `YourModel` with the name of your model and adjust the query conditions accordingly.

4. **Delete the Instance:**
   Delete the instance from the database using the `delete()` method:

   ```python
   book_to_delete.delete()
   ```

   This removes the corresponding record from the database.

### Example:

Continuing with the previous examples, let's say you want to delete the book with the title 'Django Advanced':

```python
# Assuming your model is defined in models.py in the app 'yourapp'
from yourapp.models import Book

# Retrieve the instance to delete
book_to_delete = Book.objects.get(title='Django Advanced')

# Delete the instance from the database
book_to_delete.delete()
```

After running these commands in the Django shell, the book record with the title 'Django Advanced' will be deleted from the database.

Remember to replace `yourapp` and `YourModel` with the actual names of your Django app and model, and adjust the query conditions accordingly. Also, be cautious when performing delete operations, as they permanently remove data from the database.
