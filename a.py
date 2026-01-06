from flask import Flask, jsonify, request
import subprocess
import os
import sys

app = Flask(__name__, static_folder="static")
# 获取当前文件的绝对路径
file_path = os.path.abspath(__file__)
# 获取当前文件所在的目录
dir_path = os.path.dirname(file_path)


@app.route("/run-script", methods=["POST"])
def run_script():

    # 获取用户输入的账号、密码和语言选项
    username = request.form.get("account")
    password = request.form.get("password")
    lang = request.form.get("lang")

    # 构建完整的脚本路径
    recap_script_path = os.path.join(dir_path, "postcrossingrecap.py")

    # 使用当前 Flask 应用的 Python 解释器
    python_executable = sys.executable
    recap_result = subprocess.run(
        [python_executable, recap_script_path, lang, username, password],
        capture_output=True,
        text=True,
        timeout=300,
    )
    output = recap_result.stderr + recap_result.stdout
    # 返回响应
    return jsonify(success=True, output=output)


@app.route("/list-recap-files", methods=["POST"])
def list_recap_files():
    # 获取用户输入的账号
    username = request.form.get("account")
    recap_folder = os.path.join(app.static_folder, "recap")
    print(recap_folder)
    files = os.listdir(recap_folder)
    # 筛选出以username开头且以.html结尾的文件
    user_html_files = [
        f
        for f in files
        if f.startswith(username) and (f.endswith(".html") or f.endswith(".zip"))
    ]
    return jsonify(user_html_files)


# 定义删除文件的路由


@app.route("/delete-endpoint", methods=["POST"])
def delete_files():
    username = request.form.get("account")
    delete_script_path = os.path.join(dir_path, "delete.py")
    python_executable = sys.executable
    delete_result = subprocess.run(
        [python_executable, delete_script_path, username],
        capture_output=True,
        text=True,
    )
    output = delete_result.stderr + delete_result.stdout
    return jsonify(success=True, output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
