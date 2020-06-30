## Built By [Ian Mdawida](https://github.com/ian1017/)

## Description
The app is a Picture Gallery used to display images from different locations and categories. Users can view details of picture by clicking on the info icon.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I can:
* View different photos that interest them.
* Click on a single photo to expand it and also view the details of the photo. 
* View the most recent posts.
* Search for different categories of photos. (ie. Travel, Food).
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Landing page | **On page load** | Site description and gallery pictures |
| Display picture information | **Click info icon on picture** | Opens a modal that shows a large version of the picture and its details |
| Display different picture categories | **Enter search term on the search bar** | Display search results if search term meets database categories |
| Display pictures from different categories |**Click 'Location/Globe' Icon on the navigation bar**|Displays a select field that allows users to search for pictures from a specific country/location|

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* postgres database
* virtualenv
* django

### Cloning
* In your terminal:
        
        $ git clone https://github.com/ian1017/gallery.git
        $ cd sokkyyy-the-gallery

## Running the Application
* Creating the virtual environment:

        $ pip install virtualen
        $ virtualenv virtual
        $ source virtual/bin/activate

* Installing Django and other Modules:

        $ pip install -r requirements.txt


* To run the application, in your terminal:


        $ python3.6 manage.py runserver



## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test photos

## Technologies Used
* Python3.8
* Django
* MDbootstrap
* Google Fonts
* FontAwesome
* Postgres SQL

## License
[Ian Mdawida](https://github.com/ian1017/)