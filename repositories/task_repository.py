from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    # @staticmethod
    # def update_task(name, description):
    #     task = task.query.filter_by(name=name, description=description).first()
    #     task = Task(name=name, description=description)
    #     db.session.commit()
    #     return task
    

#     @app.route("/update", methods=["POST"])
# def update():
#     newtitle = request.form.get("newtitle")
#     oldtitle = request.form.get("oldtitle")
#     book = Book.query.filter_by(title=oldtitle).first()
#     book.title = newtitle
#     db.session.commit()
#     return redirect("/")