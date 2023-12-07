# Django Update Data 

To update data in a Django model, you can use the Django ORM (Object-Relational Mapping) system. Here are the steps to update data in a Django model:

### Use Django Shell:

1. **Open the Django Shell:**
   Open a terminal or command prompt and navigate to your project directory. Run the following command to open the Django shell:

   ```bash
   python manage.py shell
   ```

2. **Import the Model:**
   Import the model you want to update data for:

   ```python
   from yourapp.models import YourModel
   ```

   Replace `yourapp` with the actual name of your Django app and `YourModel` with the name of your model.

### Update Data:

3. **Retrieve the Instance to Update:**
   Retrieve the instance you want to update using a query. For example, to update a book with a specific title:

   ```python
   book_to_update = YourModel.objects.get(title='Django Basics')
   ```

   Replace `YourModel` with the name of your model and adjust the query conditions accordingly.

4. **Modify the Fields:**
   Modify the fields you want to update:

   ```python
   book_to_update.title = 'Django Advanced'
   book_to_update.published_date = date(2023, 3, 1)
   ```

   Adjust the field names and new values accordingly.

5. **Save the Instance:**
   Save the modified instance to the database using the `save()` method:

   ```python
   book_to_update.save()
   ```

   This updates the corresponding record in the database.

### Example:

Continuing with the previous example, let's say you want to update the title and publication date of the book with the title 'Django Basics':

```python
# Assuming your model is defined in models.py in the app 'yourapp'
from yourapp.models import Book
from datetime import date

# Retrieve the instance to update
book_to_update = Book.objects.get(title='Django Basics')

# Modify the fields
book_to_update.title = 'Django Advanced'
book_to_update.published_date = date(2023, 3, 1)

# Save the updated instance to the database
book_to_update.save()
```

After running these commands in the Django shell, the book record with the title 'Django Basics' will be updated with the new title 'Django Advanced' and the new publication date.

Remember to replace `yourapp` and `YourModel` with the actual names of your Django app and model, and adjust the query conditions, field names, and values accordingly.
