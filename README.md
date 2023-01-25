# Tools4Insta

Contribution of tools for Instagram.

My Photography Insta 📸: https://www.instagram.com/cagy_pics/ (click the like button 💖 if you're cool~)

❗❗❗: don't steal my photographs PLEASE

1. [toInsta](./toInsta.py): Convert images to 1:1 size depending on the bigger side (height/width) via [PIL](https://pillow.readthedocs.io/en/stable/index.html#) lib
   - install PIL (make sure you have Python 3 installed):
        ```
        python -m pip install --upgrade pip
        python -m pip install --upgrade Pillow
        ```
   - add your images to `./origins` folder
     - If you need to rotate your images, modify the third argument of `process()` function. The default is 0, my example case is 90 degrees.
   - run the command: `python toInsta.py`
   - check your images in `./tarts` folder

