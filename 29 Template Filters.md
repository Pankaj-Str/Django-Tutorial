# Template Filters

Template filters in Django allow you to modify the output of template variables or tags before they are displayed. Django provides several built-in filters, and you can also create custom filters to suit your specific needs. Here's how you can use both built-in and custom template filters in Django:

### Using Built-in Template Filters:

1. **Upper and Lowercase Filters:**
   - `upper`: Converts a string to uppercase.
   - `lower`: Converts a string to lowercase.

   ```html
   {{ variable|upper }}
   {{ variable|lower }}
   ```

2. **Capitalize Filter:**
   - `capitalize`: Capitalizes the first character of a string.

   ```html
   {{ variable|capitalize }}
   ```

3. **Date Formatting Filters:**
   - `date`: Formats a date according to a given format string.
   - `time`: Formats a time according to a given format string.
   - `datetime`: Formats a datetime according to a given format string.

   ```html
   {{ date_value|date:"Y-m-d" }}
   {{ time_value|time:"H:i:s" }}
   {{ datetime_value|datetime:"Y-m-d H:i:s" }}
   ```

4. **Length Filter:**
   - `length`: Returns the length of a string or list.

   ```html
   {{ variable|length }}
   ```

5. **Default Filter:**
   - `default`: Sets a default value if the variable is undefined or empty.

   ```html
   {{ variable|default:"Default Value" }}
   ```

6. **Join Filter:**
   - `join`: Joins the elements of a list with a specified delimiter.

   ```html
   {{ list|join:", " }}
   ```

### Creating Custom Template Filters:

1. **Create a Python Module for Filters:**
   Create a Python module within your app's `templatetags` directory. This module will contain your custom template filters.

   ```python
   # myapp/templatetags/custom_filters.py

   from django import template

   register = template.Library()

   @register.filter(name='add_prefix')
   def add_prefix(value, prefix):
       return f"{prefix}{value}"
   ```

2. **Use the `@register.filter` Decorator:**
   Define your custom filter function and decorate it with `@register.filter`. Optionally, you can specify the filter name using the `name` parameter.

3. **Load and Use Custom Filters in Templates:**
   Load your custom filter module in your template, and then you can use your custom filter as you would use any built-in filter.

   ```html
   {% load custom_filters %}

   {{ variable|add_prefix:"Prefix-" }}
   ```

   In this example, the `add_prefix` filter adds a specified prefix to a string.

By using both built-in and custom template filters, you can manipulate and format data in your Django templates to suit your application's requirements.