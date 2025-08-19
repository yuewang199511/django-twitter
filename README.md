# twitter stream backend with django

This is a lightweight twitter back end project with mysql as the database and Django as the REST-API framework.
This project follows a typical MVC template and then introduces **Redis** and **Memcached** to accelerate the caching and retrieving process.

This project mainly serves as a sample of implementing a MVC oriented coding style and certain backend solutions.

# About project setup

You can always follow the official guide of any backend frameworks to setup your backend service, just gather the following materials:

1. environment setup for **program language** and **your framework**(full suite **Django**, light weight **flask**)
2. seup database (if it is a stateful service)
3. setting up router and database connection if necessary
4. read the guide of how to start make a simple API sample and test it
5. Write shell script and requirement.txt to make the above setup process automatic and repeatable
6. Write a **Dockerfile** if for deployment

# Project structure
## Models

The folders named with plurals like accounts, comments, tweets are all models. They represent specific objects in the database.

Their structures are quite the same and most API frameworks provide samples to create them. They are usually composed by the following things

### basics

1. model definition in the database. Some frameworks can define objects in Mysql through code, please keep an eye on official guides on how to maintain them.
2. view/API
3. serializer/deserializer

with those basic ingridients, you should be able to have at least one running API and retreiveable data

### extra
those are the things always good to have if you are considering certain optimizations, but remember they somtimes require trade offs

1. pagination, always good to have if you have a long list of data to retrieve but only want a small portion visible
2. cache, cahes are good to have but you need to have a cache intermediate and have a good coding template to put initilization and cache clean up in your models
3. hepler functions/services, it is a good habbit to have a script for each model to store specific bussiness logics
4. tests, always good to have tests for each model and each MVC layers are working
5. listeners, you may need to have listeners to do extra work before construction and after destruction of a data, like manipulating caches

## project manager folder

For this repository it is twitter.

Usually a full suite of web backend has its own manager folder to store things like settings and meta info. Just look for official documents about how to setup.

TODO: It is reasonable to have secrets in development branches, but if the project should be visible to multiple users and needs deployment, better to use infra frameworks like **K8s**

## utils
Always only stores helper functions that can be used globally here and your client of intermediate components might get here. Such as a **Redis** client

For this project is it a comprehensive tool box your can refer to if you want certain funcitons in your project.

### decorators
You can always try to find useful decorators online, lots of good samples on github

For this project it is a decorator to check if parameters/data from request have the same keys as defined. Having this decrator can save some time writing same logic in serializer

### json_decoder

The json decoder in Django used to lose some percision at that time so this class overwrites it. You can always consider overwrite the original class in python

### listener

The common listener used in this project is to clear caches when object got changed or deleted

### memchaed helper

An simple cache helper quite useful if you only have a key:value cache needed

### paginations

always good to havea pagination helper class. You can also check for other paginations samples from other SDK or projects. I recommend [Supervisely](https://github.com/supervisely/supervisely) if you are looking for one for HTTP based client

### ratelimit

Django can set are customized ratelimit function globally. You can check for official documents about how to set them

### redis client/helper/serializer

Redis to good to cache list or numeric data

You can find some sample code online. In this project a redis toolbox is combines by the follwing parts
1. client: the code the setup and stop client is needed. Usually you just need a global client class for the whole program
2. helper: You still need to write your own functions or wrap them if you want to load, clean list or manipulate numbers
3. serializer: finally if you are working with database, you will need to serialize/deserialize them with models
