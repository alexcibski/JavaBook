# JavaBook

- Pitch deck, ScreenShot of App, ERD, and Wireframes
https://docs.google.com/presentation/d/19I668nh9xD0B0C1_JiWhTaSTv9IVfFA5NxcylsVHbZA/edit?usp=sharing

- Trello board
https://trello.com/b/HGikWkjX/javabook

- Link to site hosted on Heroku
https://java-book-a57dc0cae3ed.herokuapp.com/

## Technologies Used

- HTML
- CSS
- Python
- Django
- PostgreSQL
- MaterializeCSS
- Adobe Fresco

## Installation Instructions

- Fork and clone to local environment.
- Create https://neon.tech/ account for remote database
- In settings.py match your database connection to your Neon values as shown below.

        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'neondb',
                'USER': '<neon username>',
                'PASSWORD': os.environ['SECRET_KEY'],
                'HOST': '<neon hostname>',
                'PORT': '5432'

        }
        }

- Run command "python3 manage.py migrate" to re-migrate your database to the remote one.
- In .env/activate file, create the env variable
        export SECRET_KEY='<your secret key>'

- To run on localhost:8000
- Run command "source .env/bin/activate" to activate virtual environment.
- Then command "python3 manage.py runserver"

## User Stories

- As a coffee enthusiast, I want a place to save my coffee and coffee makers that I have tried and keep the best ones for future use.

- As a coffee lover, I want to be able to update or delete any entry with brew tips and reviews so that I can have the best coffee all the time.

- I don't want to try to remember how to prepare the different coffees.  I would like to keep a record of brew instructions like a recipe file.


## Unsolved Problems
- Having different background images for different pages of the website.

## Hurdles Overcome
- We wanted to upload a jpeg file for the picture but found that we needed to host on AWS for that functionality.  We ended up using a URL link to populate the picture field of our app.

- We wanted to put a limit on the integer field of the rating field so that the user will be limited to a rating up to five.  We ended up using an answer bank for the user to choose a rating number.

## Next Steps
- Incorporate account creation so that each user can have their own account and data.

- Host our app on AWS so that we can upload photos from our phone since URL's in websites can change.