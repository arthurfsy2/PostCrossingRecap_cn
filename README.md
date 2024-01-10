# Postcrossing Recap Generator - Chinese Version

fork from:https://github.com/cnovel/PostCrossingRecap

Instructions:
1. Get sent.json/received.json through `py login.py "youraccount" "yourpassword"`
2. Use `py postcrossingrecap.py "language"` to generate a review of the language version you want (currently language can be equal to the following values: "cn"\"en")
3. After running, the review of all years will be generated with one click. The storage path is: `./recap`, and the file name format is: `{year}_recap_{language}.html`

使用方法：
1、通过`py login.py "youraccount" "yourpassword"`来获取sent.json/received.json
2、通过`py postcrossingrecap.py "language"` 来生成你希望语言版本的回顾（目前language可以等于以下值："cn"\"en"）
3、运行后将会一键生成所有年份的回顾，存放路径：`./recap`，文件名格式为：`{year}_recap_{language}.html`