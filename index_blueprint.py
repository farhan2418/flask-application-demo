from models.todo import Todo
from flask import Blueprint, request, redirect, render_template
from models import db

index_bp = Blueprint('index_blueprint', __name__, template_folder='templates', static_folder='static', static_url_path='/')

@index_bp.route('/', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        task_content = request.form.get('content')
        new_task = Todo(content = task_content)

        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an error, and we don\'t know what'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks,)
