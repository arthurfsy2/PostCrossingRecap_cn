# Postcrossing Personal Recap Generator - Online Version

[中文README](README_CN.md)  |  [英文README](README.md)

fork from:https://github.com/cnovel/PostCrossingRecap

Online export URL: [Generate Annual Recap](https://pcrecap.fengsy.cn/static/index.html)
(Click the icon in the upper right corner to switch languages)

## statement:

1. You can also build the front-end export method by yourself through the following methods.
2. This project has nothing to do with postcrossing officially! And this website will not store your personal account number and password, it will only be used to generate personal data. It is recommended to delete personal files after generation if they are no longer needed.
3. Just choose one of the following methods

## How to use (docker):

1. Run `docker run --name pcrecap -p 4567:4567 arthurfsy2/pcrecap:latest`
2. Open the local/server IP address in the browser: "http://XXX:4567/static/index.html", and then follow the prompts on the interface to export the data.
PS: If it is a server, you need to pay attention to the need to open the `4567` port to be able to access normally

How to use (front-end):
1. Install dependencies through `pip install -r requirements.txt`
2. Execute the front-end program through `py a.py`. If everything goes well, you can see "Running on http://XXX:4567" on the command line.
3. Open the local IP address: "http://XXX:4567/static/index.html" in the browser, and then follow the interface prompts to export the data.

## How to use (backend):
Python version required: 3.11.X
1. Install dependencies through `pip install -r requirements.txt`
2. Get sent.json/received.json through `py login.py "youraccount" "yourpassword"`
3. Use `py postcrossingrecap.py "language" "account"` to generate a review of the language version you want (currently language can be equal to the following values: "cn"\"en")
4. After running, the review of all years will be generated with one click. The storage path is: `./recap`, and the file name format is: `{year}_recap_{language}.html`
