# Postcrossing 个人年度回顾生成 - 在线版

[中文README](README_CN.md)  |  [英文README](README.md)

fork from: https://github.com/cnovel/PostCrossingRecap

在线导出网址：[Generate Annual Recap](https://pcrecap.fengsy.cn/static/index.html)
（点击右上角图标切可换语言）

## 声明：

1. 你也可以通过以下方法自行搭建前端的导出方式。
2. 本项目与postcrossing官方无关！且本网站不会存储你的个人账号、密码，只会用于个人数据的生成。如果不再需要，建议生成后删除个人文件。
3. 以下方法选择其中一种即可

## 使用方法（docker）：

1. 运行 `docker run --name pcrecap -p 4567:4567 arthurfsy2/pcrecap:latest`
2. 浏览器打开本地/服务器 IP 地址："http://XXX:4567/static/index.html"，然后根据界面提示操作即可导出数据。
PS：如果是服务器，需要注意`4567`这个端口需要放行，能够正常访问

## 使用方法（后端）：
python版本要求：3.11.X
1. 通过 `pip install -r requirements.txt`安装依赖
2. 通过 `py login.py "youraccount" "yourpassword"`来获取 sent.json/received.json
3. 通过 `py postcrossingrecap.py "language" "account"` 来生成你希望语言版本的回顾（目前 language 可以等于以下值："cn"\"en"）
4. 运行后将会一键生成所有年份的回顾，存放路径：`./recap`，文件名格式为：`{year}_recap_{language}.html`