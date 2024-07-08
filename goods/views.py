from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
        "title": "Каталог товаров",
        
        "catalog_items": [
        {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
         },

         {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
         },

         {'image': 'deps/images/goods/double bed.jpg',
         },

         {'image': 'deps/images/goods/kitchen table.jpg',
         'name': '',
         'description': '',
         'price': 365.00},

         {'image': 'deps/images/goods/kitchen table 2.jpg',
         'name': '',
         'description': '',
         'price': 430.00},

         {'image': 'deps/images/goods/corner sofa.jpg',
         'name': '',
         'description': '',
         'price': 610.00},

         {'image': 'deps/images/goods/bedside table.jpg',
         'name': '',
         'description': '',
         'price': 55.00},

         {'image': 'deps/images/goods/sofa.jpg',
         'name': '',
         'description': '',
         'price': 190.00},

         {'image': 'deps/images/goods/office chair.jpg',
         'name': '',
         'description': '',
         'price': 30.00},

         {'image': 'deps/images/goods/plants.jpg',
         'name': '',
         'description': '',
         'price': 10.00},

         {'image': 'deps/images/goods/flower.jpg',
         'name': '',
         'description': '',
         'price': 15.00},

         {'image': 'deps/images/goods/strange table.jpg',
         'name': '',
         'description': '',
         'price': 25.00},
        ]
    }
    return render(request, "goods/catalog.html", context )


def product(request):

    return render(request, "goods/product.html")