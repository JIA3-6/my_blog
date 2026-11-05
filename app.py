from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# 模擬資料庫：儲存文章列表
posts = [
    {
        "title": "我的第一篇 Flask 文章",
        "author": "管理者",
        "content": "歡迎來到我的簡易部落格！這是使用 Python Flask 建立的。",
    }
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        if title and author and content:
            posts.append(
                {"title": title, "author": author, "content": content}
            )
            return redirect(url_for("index"))

    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)