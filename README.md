# Material
**1.** About\
**2.** [Quick Start](#QuickStart)

## About
A library to help you create programs with the selection of colors from wallpapers. Windows only! (Yet)
> An example of using Material: Creating a GUI.


<img src="https://i.postimg.cc/0yxzxt47/image.png" width="700">


## Quick Start <a name="QuickStart"></a>
##### How to get the most popular color from image? 
```
import material

color = material.get_popular_color(path)
print(color)

# ---> (r, g, b)
```

##### How to get the most popular color from windows wallpaper? 
```
import material

color = material.get_popular_color(material.get_wallpaper_path())
print(color)

# ---> (r, g, b)
```

##### How to get the several popular colors from windows wallpaper? 
```
import material

color = material.get_popular_colors(material.get_wallpaper_path(), amount = 5)
print(color)

# ---> [[r, g, b], [r, g, b], [r, g, b]]
```
