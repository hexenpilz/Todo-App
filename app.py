from flask import Flask, render_template, request, redirect, jsonify
from models import db, Todo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# -------------------------
# HTML ROUTES
# -------------------------

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return redirect("/")


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


# -------------------------
# API ROUTES (JSON)
# -------------------------

@app.route("/api/todos")
def api_get_todos():
    todos = Todo.query.all()
    data = [
        {"id": t.id, "title": t.title, "done": t.done}
        for t in todos
    ]
    return jsonify(data)


@app.route("/api/todos", methods=["POST"])
def api_add_todo():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    todo = Todo(title=data["title"])
    db.session.add(todo)
    db.session.commit()

    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "done": todo.done
    }), 201


@app.route("/api/todos/<int:todo_id>", methods=["PATCH"])
def api_update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.json

    if not data or "done" not in data:
        return jsonify({"error": "done field is required"}), 400

    todo.done = data["done"]
    db.session.commit()

    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "done": todo.done
    })


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def api_delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()

    return jsonify({
        "message": "deleted",
        "id": todo.id,
        "title": todo.title
    }), 200


if __name__ == "__main__":
    app.run(debug=True)