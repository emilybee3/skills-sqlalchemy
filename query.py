"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without thes
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# # Get the brand with the **id** of 8.
# >>> eight = Brand.query.filter(Brand.id==8).one()
# >>> eight.name
# u'Austin'

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# >>> corv = Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()
# >>> corv
# [<Car id=5 Car Year=1953 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=6 Car Year=1954 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=8 Car Year=1955 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=10 Car Year=1956 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=11 Car Year=1957 Brand Name=Chevrolet Car Name=Corvette>,   
# <Car id=13 Car Year=1958 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=17 Car Year=1959 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=20 Car Year=1960 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=26 Car Year=1961 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=28 Car Year=1962 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=38 Car Year=1963 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=39 Car Year=1964 Brand Name=Chevrolet Car Name=Corvette>]

# # Get all models that are older than 1960.
# >>> old = Model.query.filter(Model.year < 1960).all()
# >>> old
# [<Car id=1 Car Year=1909 Brand Name=Ford Car Name=Model T>, 
# <Car id=2 Car Year=1926 Brand Name=Chrysler Car Name=Imperial>

# # Get all brands that were founded after 1920.
# >>> new = Brand.query.filter(Brand.founded > 1920).all()
# >>> new
# [<Brand id=2  Founded=1925 Headquarters=Auburn Hills, Michigan Discontinued=None>, 
# <Brand id=9  Founded=1954 Headquarters=Chalfont St Peter, Buckinghamshire Discontinued=1976>, 
# <Brand id=11  Founded=1926 Headquarters=Detroit, MI Discontinued=2010>, 
# <Brand id=14  Founded=1928 Headquarters=Auburn Hills, Michigan Discontinued=2001>, 
# <Brand id=15  Founded=2003 Headquarters=Palo Alto, CA Discontinued=None>]


# # Get all models with names that begin with "Cor".
# >>> corvette = Model.query.filter(Model.name.like('Cor%')).all()
# >>> corvette
# [<Car id=5 Car Year=1953 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=6 Car Year=1954 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=8 Car Year=1955 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=10 Car Year=1956 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=11 Car Year=1957 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=13 Car Year=1958 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=17 Car Year=1959 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=19 Car Year=1960 Brand Name=Chevrolet Car Name=Corvair>, 
# <Car id=20 Car Year=1960 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=26 Car Year=1961 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=28 Car Year=1962 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=37 Car Year=1963 Brand Name=Chevrolet Car Name=Corvair 500>, 
# <Car id=38 Car Year=1963 Brand Name=Chevrolet Car Name=Corvette>, 
# <Car id=39 Car Year=1964 Brand Name=Chevrolet Car Name=Corvette>]


# # Get all brands with that were founded in 1903 and that are not yet discontinued.
# >>> around = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == 'Null').all()
# >>> around
# []

# # Get all brands with that are either discontinued or founded before 1950.
# >>> cars = Brand.query.filter(db.or_(Brand.founded<1950, Brand.discontinued.isnot(None))).all()
# [<Brand id=1  Founded=1903 Headquarters=Dearborn, MI Discontinued=None>, 
# <Brand id=2  Founded=1925 Headquarters=Auburn Hills, Michigan Discontinued=None>, 
# <Brand id=3  Founded=1919 Headquarters=Saint-Ouen, France Discontinued=None>, 
# <Brand id=4  Founded=1907 Headquarters=Ryton-on-Dunsmore, England Discontinued=1981>, 
# <Brand id=5  Founded=1911 Headquarters=Detroit, Michigan Discontinued=None>, 
# <Brand id=6  Founded=1902 Headquarters=New York City, NY Discontinued=None>, 
# <Brand id=7  Founded=1916 Headquarters=Munich, Bavaria, Germany Discontinued=None>, 
# <Brand id=8  Founded=1905 Headquarters=Longbridge, England Discontinued=1987>, 
# <Brand id=9  Founded=1954 Headquarters=Chalfont St Peter, Buckinghamshire Discontinued=1976>, 
# <Brand id=10  Founded=1852 Headquarters=South Bend, Indiana Discontinued=1967>, 
# <Brand id=11  Founded=1926 Headquarters=Detroit, MI Discontinued=2010>, 
# <Brand id=12  Founded=1903 Headquarters=Detroit, MI Discontinued=None>, 
# <Brand id=13  Founded=1901 Headquarters=Kenosha, Washington Discontinued=1969>, 
# <Brand id=14  Founded=1928 Headquarters=Auburn Hills, Michigan Discontinued=2001>,
# <Brand id=15  Founded=2003 Headquarters=Palo Alto, CA Discontinued=None>]


# # Get any model whose brand_name is not Chevrolet.
# >>> models = Model.query.filter(Model.brand_name.isnot('Chevrolet')).all()
# >>> models
# [<Car id=1 Car Year=1909 Brand Name=Ford Car Name=Model T>, 
# <Car id=2 Car Year=1926 Brand Name=Chrysler Car Name=Imperial>,

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year == year).join(Brand).all()

    for Model.name, Model.brand_name, Brand.headquarters in model_info:
        print ("Model name:", Model.name, "Brand:", Model.brand_name, 
               "Headquarters:", Brand.headquarters)


def get_brands_summary(brand):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary = db.session.query(Brand.name, Model.name).filter(Brand.name == brand).join(Model).all()
    for Brand.name, Model.name in brand_summary:
        print ("Brand:", Brand.name, "Model:", Model.name)

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The returned value is the object containing the information about the brand name
# Ford. The datatype is a class instance from the Brand class. 


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table manages two one to many relationships with two different tables.