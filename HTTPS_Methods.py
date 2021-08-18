#!/usr/bin/env python
# coding: utf-8




#HTTP REQUESTS

# import requests

#GET : Retrieve an existing resource

url="https://www.geeksforgeeks.org/"
dict1={'key1':'value1'}
get_method=requests.get(url, params=dict1)
print(get_method)
print(get_method.status_code)
print(get_method.url)

#POST : Create a new resource

post_method=requests.post('https://httpbin.org/post', data=dict1)
print(post_method)
print(post_method.json())

#PUT : Update an existing resource else create a new resource if existing ones is not present

put_method=requests.put('https://httpbin.org/put', data={'k1':'v1'})
print(put_method.status_code)
print(put_method.json())
print(put_method.content)

#DELETE: It vanishes the specified resource

delete_method=requests.delete('https://httpbin.org/delete', data=dict1)
print(delete_method)
print(delete_method.json())
print(delete_method.content)

#HEAD : Retrieve meta-information in response headers

head_method=requests.head('https://httpbin.org/', data=dict1)
print(head_method)
print(head_method.headers)
print(head_method.content)

#PATCH : Partially update an existing resource

patch_method=requests.patch('https://httpbin.org/patch', data=dict1)
print(patch_method)
print(patch_method.content)




