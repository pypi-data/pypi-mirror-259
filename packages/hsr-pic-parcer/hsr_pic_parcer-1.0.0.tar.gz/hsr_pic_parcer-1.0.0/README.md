# hsr_pic_parser

## Introduction

This is a Python library for getting pictures of characters, cones and relics with names from [starrail.mana](https://starrail.mana.wiki/).


## Installation

pip install hsr_pic_parser


##Functions, which can be used

```python
get_char_pic(name) # returns bynary picture of the character and full name of the character
get_char_icon_pic(name)) # returns bynary icon picture of the character and full name of the character
get_cone_pic(number) # returns bynary icon picture of the cone and full name of cone
get_cone_icon_pic(number) # returns bynary icon picture of the cone and full name of cone
get_relic_icon_pic(number) # returns bynary icon picture of the relic and full name
```

## Example

You can get picture of character using the following code:

```python
from hsr_pic_parser import get_char_pic

picture, name = get_char_pic('argenti')
```
The name of the character should be identical to the one used in [starrail.mana](https://starrail.mana.wiki/).

You can get picture and the name of the light cone:

```python
from hsr_pic_parser import get_cone_pic

picture, name = get_cone_pic(20000)
```
The code of the light cone should be equivalent to the one used in [starrail.mana](https://starrail.mana.wiki/).

## Another example
```python
from hsr_pic_parser import get_relic_icon_pic

pic, name = get_relic_icon_pic(101) #here we are using function

def save_image_as_png(image_data, output_file_path):
    with open(output_file_path, "wb") as png_file:
        png_file.write(image_data) #here is saving function 

save_image_as_png(pic, argenty) #here we are saving the icon of relic
```


