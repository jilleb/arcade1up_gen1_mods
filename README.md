# Mods, tools and info for Aracade1Up Generation 1 PCBs

## Disclaimer
This repository is meant to be a one-stop-shop for info, howto's and tools for modding Arcade1Up Generation 1 cabinets. Most of the knowledge is very spread out, hidden in long Reddit threads or just in the heads of some people.  I know that most people throw out the original hardware, and only use the screen and case of the Arcade1Up together with a RetroPie. In my opinion this is wasteful, and my goal is to get the most out of the original hard- and software. Please do not abuse, misuse or sell the stuff I'm sharing here. Make sure to keep backups of everything you intend to change. Everything you do, is at your own risk. This repository is not meant for piracy, sharing illegal files or to harm Arcade1Up hardware or the Arcade1Up company in any way.

Make sure to have fun, because that's what this all about.

## Info
I will fill a wiki with all things I find out and gather online about the Gen1 machines. 



## Tools

Requirements:
- Python 3 with PIL installed. (run ```pip install image``` from your cmd or terminal)
- Some basic knowledge about computer usage.

### 565_to_png.py
![image](https://user-images.githubusercontent.com/8352494/170453744-176c0a92-fb42-45cb-bdae-8f6735fa2515.png)

Tool to convert all .565 and .load files from a certain folder to .png files for easy editing.

Usage: ```python 565_to_png.py <path to .565 files> <output folder>```

For example:
```python 565_to_png.py c:\temp\565\ c:\temp\565\converted\```

### png_to_565.py
Tool to convert all .png files from a certain folder back to .565 or .load files for use in your Arcade1Up device.

Usage: ```python png_to_565.py <path to .png files> <output folder>```

For example:
```python png_to_565.py c:\temp\565\converted\ c:\temp\565\converted\new_565\```





[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jille)
