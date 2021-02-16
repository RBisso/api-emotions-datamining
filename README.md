# api-emotions-dataminig

## pulling from docker hub repository
```shell
# docker pull bissorm/api-emotions-datamining
```
## executing the docker image
```shell
# docker run -p 8000:8000 bissorm/api-emotions-datamining
```

## project structure
The structure of a Django project works by separating the project parts into applications. Normally, the first application receives the name of the project, when it is built. I changed the name to ```config```, as it is responsible for the project settings. For this project, I created two more apps, ```api``` and ```frontend```.
### api/
App responsible for handling the calls to classify a phrase/text.

#### api/\_\_init\_\_.py
Called when the application starts. Contains a class ``` Classifier ``` responsible for the training and classification of the phrases.

#### api/urls.py
Contais the routs for the ``` api ``` app.
#### api/views.py

#### api/words_db.py
Contains the database for training and testing the data mining model.
### config/

#### config/settings.py
#### config/urls.py

### frontend/

#### frontend/urls.py
#### frontend/views.py
#### frontend/static/
#### frontend/staticfiles/

### nltk_data/
Folder that contains the nltk data for the training model. This was needed because nltk normally uses a UI for downloading the data, so a manual installation were needed.
### Procfile
File used to build the [heroku app](https://protected-earth-88770.herokuapp.com/)
### Dockerfile
File used to build the [docker image](https://hub.docker.com/r/bissorm/api-emotions-datamining)
