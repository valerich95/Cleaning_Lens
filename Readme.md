<!-- @format -->

# Install

- install python\_

- create and activate virtual env\_

## Requirements

```
	 pip install -r requirements.txt
```

- Copy Train models to the ./trained_model

  ```
  [+] root
  	...(rest of folders)
  	[+] trained_model
  		-	ext.pth
  		-	simModel.pth

  ```

# Usage

in project directory open terminal and run this commands

```
	python manage.py makemigrations
	python manage.py migrate

```

## runserver using

```
	python manage.py runserver
```

### and use it with [Open home page](http://127.0.0.1:8000/)

---

## You can also see the api refrences in post man.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/25523392-a2bf4123-03df-4b4f-83f0-1c9a460c1f92?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25523392-a2bf4123-03df-4b4f-83f0-1c9a460c1f92%26entityType%3Dcollection%26workspaceId%3D2d00ee0a-9ff9-4553-98ee-4627dddf8f10)

## create super user to log in django admin panel

```
	python manage.py createsuperuser
```

use your credential to log in [django admin](https://127.0.0.1:8000/admin)
