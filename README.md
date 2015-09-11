### Run it locally
```python manage.py runserver```. Now go to ```localhost:8000``` to view the site!

## Contributing

When installing new packages, always make sure to update the requirements file.
```
pip freeze > requirements.txt
```
In general, whenever you pull code, you should probably run ```python manage.py migrate``` in case someone has committed new database migrations to the repository.

You should also periodically run ```pip install -r requirements.txt``` in case someone has installed new packages. 

