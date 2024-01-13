import re
from .utils import json_to_image

class QueryFilters:
    def filter_price_by_minimum(self ,user_data, products_list):
        filtered_product_list = []
        for product in products_list:
            price = re.findall('[.,\d]+' ,str(product['estimated_price']))
            if len(price)>0:
                price = float(price[0])
                if  float(user_data['price_min']) <= price:
                    filtered_product_list.append(product)
        if filtered_product_list is not None:
            return filtered_product_list
        return None

    def filter_price_by_maximum(self , user_data , products_list):
        filtered_product_list = []
        for product in products_list:
            price = re.findall('[.,\d]+' ,str(product['estimated_price']))
            if len(price)>0:
                price = float(price[0])
                if  float(user_data['price_max']) >= price:
                    filtered_product_list.append(product)
        if filtered_product_list is not None:
            return filtered_product_list
        return None

    def filter_brand(self, user_data , products_list):
        filtered_product_list = []
        for product in products_list:
            if user_data['brand'].lower() in product['description'].lower():
                filtered_product_list.append(product)
        if filtered_product_list is not None:
            return filtered_product_list
        return None

    def filter_source(self ,user_data ,  products_list):
        filtered_product_list = []
        for product in products_list:
            if user_data['source'].lower() in product['website'].lower():
                filtered_product_list.append(product)
        if filtered_product_list is not None:
            return filtered_product_list
        return None

def query_filter_client(products_list , user_data):
    query_functions ={
        'price_min' : QueryFilters().filter_price_by_minimum,
        'price_max' : QueryFilters().filter_price_by_maximum,
        'brand' : QueryFilters().filter_brand,
        'source' : QueryFilters().filter_source,
    }
    for query in user_data:
        if user_data[query] and query_functions.get(query):
            products_list = query_functions[query](user_data=user_data , products_list=products_list)
        if len(products_list)==0:
            return f'Can\'t find any product with {query} filter'

    return products_list
