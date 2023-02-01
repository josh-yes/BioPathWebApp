# BioPath Backend
## General Information
All of the code and relevant information for the backend can be found in this directory with basic initialization commands stored in docker-compose.yaml of the root directory. We are using Django + Django-REST-Framework (DRF) connected to a Postges database. Django manages all of the database interraction for us so, beyond initialization and opening the necessary ports, we don't directly touch Postgres. Note that the Postgres database is mounted to the root directory for data persistence while containers are shutdown, but that this directory is ignored by git as this is for development only and in the deployed environment our Postgres container is unused in favor of a prebuilt AWS Postgres solution. As such we have to keep an eye on the ports, urls, etc as they will need to be configured differently for deployment.

**We have yet to implement any security or research the security capabilities of tools used thus far. This will need to change before deployment.**

## File Structure
This does not contain every file or directory, just the one's that are most critical for you to understand what's going. Django creates a bunch of files and directories that are necessary for everything to work, but aren't necessary for you the developer to mess with or fully understand. These are the files that we have found useful/written code in so far, but please expand this as you inevitably end up modifying or adding other files. Also read [this](https://techvidvan.com/tutorials/django-project-structure-layout/) to better understand the files that Django creates and what they do.

```
Backend
|   Dockerfile $ Dockerfile for backend container. [Dockerfile](https://www.cloudbees.com/blog/what-is-a-dockerfile).  
|---api $ Currently the only app within the project biopath.  
|   |   models.py $ Declares models for api. Django automatically modifies database to match this when migrated.  
|   |   serializers.py $ Uses DRF to serialize models into more basic data types like JSON so that views.py doesn't have to. [Serializers](https://www.django-rest-framework.org/api-guide/serializers/).  
|   |   tests.py $ Don't be like me. Test your code. [Django testing](https://docs.djangoproject.com/en/4.1/topics/testing/overview/) makes it easy.  
|   |   urls.py $ Routes urls to the views in views.py. Using [DRF's routers](https://www.django-rest-framework.org/api-guide/routers/) makes this a breeze and ensures consistency.  
|   |   views.py $ Declares functions that return the json response when a specefic endpoint is reached. DRF's [ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/) make this easy.  
|---biopath $ The Django project that holds our api.  
|   |   settings.py $ Settings for the project (such as how to connect to the database).  
|   |   urls.py $ Routes url routes to views or url prefix patterns to an app's urls.py.  
|   manage.py $ CLI tool for managing the Django project. `python manage.py help`  
|   requirements.txt $ Package requirements to be pip installed on container initialization.  
|   startup.sh $ Startup commands to get Django up and running after container starts.  
```

## API
This is a RESTful API so an understanding of the REST architectural constraints, and especially [CRUD](https://www.codecademy.com/article/what-is-crud) will make understanding and using the interface very easy. We also suggest playing with the [web interface](http://localhost:8000/api) to learn the endpoints and http methods.
So far the available resources are located at...
* /api/enzymes/
* /api/substrates/
* /api/pathway_connections/
* /api/enzyme_substrates/
* /api/users/ *
* /api/groups/ *

\* Currently our webapp doesn't have users and groups but these models are auto-created by Django and necessary for administration. We have not yet researched whether these are adequate for storing and/or sending actual user data.

## Database
### Schema
The database has the following tables...
* Enzymes(*name*, reversible, image)
* Substrates(*name*, image)
* PathwayConnections(*pathway, **enzyme_from**, **enzyme_to***, **substrate**)
* EnzymeSubstrates(***enzyme**, **substrate***, substrate_type, focus)

Note that this list is not complete and not exactly correct. It is useful for understanding how we are conceptually modeling our data, but not an exact representation of the actual DB as Django builds these tables procedurally from the models. As such, in most cases you will likely benefit more from directing your focus to models.py then the actual specefics of how they're stored in the DB.

If you need to know the specefics of how these tables look you're gonna have to exec into the Postgres container and look at it yourself (look at instructions below). One important thing to note is that Django doesn't allow for mulit-field primary keys so they actually have an id field as the primary key and a restriction enforcing uniqueness of the two (or more) fields combined.

### CLI for Postgres from within container
To open a cli for the database...
1. exec into database container (recommend using docker desktop or vscode extension, but a simple `docker exec -it postgres bash` should work)
1. `psql BioPath username`
1. Read [this](https://tomcam.github.io/postgres/#getting-information-about-databases) to see how to submit queries, display tables, etc.

## Django Admin
To create an admin account just startup the containers per usual and then...
1. exec into backend container (recommend using docker desktop or vscode extension, but a simple `docker exec -it backend bash` should work)
1. `python manage.py createsuperuser`
1. Fill in username and password. I've been using root root but y'all can use whatever in dev.
1. Go to [http://localhost:8000/admin](http://localhost:8000/admin)
1. You should be able to login with the user info you supplied. Now you can administer to your hearts content!

## Tests
The philosophy for testing your views is the same as for testing your
models; you need to test anything that you've coded or your design 
specifies, but not the behavior of the underlying framework and other 
third party libraries.

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing