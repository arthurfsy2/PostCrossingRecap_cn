# Postcrossing Recap Generator - Chinese Version

fork from:https://github.com/cnovel/PostCrossingRecap

How to use (backend):

1. Install dependencies through `pip install -r requirements.txt`
2. Get sent.json/received.json through `py login.py "youraccount" "yourpassword"`
3. Use `py postcrossingrecap.py "language" "account"` to generate a review of the language version you want (currently language can be equal to the following values: "cn"\"en")
4. After running, the review of all years will be generated with one click. The storage path is: `./recap`, and the file name format is: `{year}_recap_{language}.html`

How to use (front-end):

1. Install dependencies through `pip install -r requirements.txt`
2. Execute the front-end program through `py a.py`. If everything goes well, you can see "Running on http://XXX:4567" on the command line.
3. Open the local IP address: "http://XXX:4567/static/index.html" in the browser, and then follow the interface prompts to export the data.

How to use (front-end):

1. Install dependencies through `pip install -r requirements.txt`
2. Execute the front-end program through `py a.py`. If everything goes well, you can see "Running on http://XXX:4567" on the command line.
3. Open the local IP address: "http://XXX:4567/static/index.html" in the browser, and then follow the interface prompts to export the data.
   使用方法（后端）：

4. 通过`pip install -r requirements.txt`安装依赖
5. 通过`py login.py "youraccount" "yourpassword"`来获取 sent.json/received.json
6. 通过`py postcrossingrecap.py "language" "account"` 来生成你希望语言版本的回顾（目前 language 可以等于以下值："cn"\"en"）
7. 运行后将会一键生成所有年份的回顾，存放路径：`./recap`，文件名格式为：`{year}_recap_{language}.html`

使用方法（前端）：

1. 通过`pip install -r requirements.txt`安装依赖
2. 通过`py a.py`执行前端程序，如果顺利的话，命令行可以看到“Running on http://XXX:4567”
3. 浏览器打开本地 IP 地址："http://XXX:4567/static/index.html"，然后根据界面提示操作即可导出数据。
