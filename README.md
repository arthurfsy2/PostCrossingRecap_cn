# Postcrossing Recap Generator - Chinese Version

fork from:https://github.com/cnovel/PostCrossingRecap

Instructions:

1. Install dependencies through `pip install -r requirements.txt`
2. Get sent.json/received.json through `py login.py "youraccount" "yourpassword"`
3. Use `py postcrossingrecap.py "language"` to generate a review of the language version you want (currently language can be equal to the following values: "cn"\"en")
4. After running, the review of all years will be generated with one click. The storage path is: `./recap`, and the file name format is: `{year}_recap_{language}.html`

使用方法：

1. 通过`pip install -r requirements.txt`安装依赖
2. 通过`py login.py "youraccount" "yourpassword"`来获取 sent.json/received.json
3. 通过`py postcrossingrecap.py "language" "account"` 来生成你希望语言版本的回顾（目前 language 可以等于以下值："cn"\"en"）
4. 运行后将会一键生成所有年份的回顾，存放路径：`./recap`，文件名格式为：`{year}_recap_{language}.html`
