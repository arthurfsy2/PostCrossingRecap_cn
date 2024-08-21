# 使用 Ubuntu 22.04 作为基础镜像
FROM ubuntu:22.04

# 设置环境变量以避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 更新包列表并安装 Python 3 和 pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# 将 requirements.txt 复制到容器中
COPY requirements.txt /app/requirements.txt

# 设置工作目录
WORKDIR /app

# 安装依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 将 Flask 应用程序的代码复制到容器中
COPY . /app

# 设置环境变量以指定 Flask 应用程序
ENV FLASK_APP=a.py

# 暴露 Flask 默认端口
EXPOSE 4567

# 启动 Flask 应用程序
CMD ["flask", "run", "--host=0.0.0.0"]
