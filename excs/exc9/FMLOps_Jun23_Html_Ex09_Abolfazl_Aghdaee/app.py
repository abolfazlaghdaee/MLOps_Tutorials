from flask import Flask
from flask import render_template, request,redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

std_dict = {
    1: {'id': 1, 'name': 'ahmad hosseini', 'age': 20, 'email': 'kobra@example.com'},
    2: {'id': 2, 'name': 'arash pourmand', 'age': 22, 'email': 'arash@aga'}
} 
@app.route("/profile")
def profile():

    return render_template('profile.html', std_dict=std_dict)



list_course = {
       1: {'id': 1, 'name': "math", 'description': "Learn the basics of mathematics.", 'teacher': "Sirous Hosseini"},
       2:{'id': 2, 'name': "cs", 'description': "Dive deep into cs.", 'teacher': "Hossein Alavi"},
       3: {'id': 3, 'name': "physics", 'description': "An introduction to Physics.", 'teacher': "Kamran tafti"},

    }
@app.route("/courses")
def courses():


    return render_template('courses.html', list_course = list_course)




@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    list_course = {
       1: {'id': 1, 'name': "math", 'description': "Learn the basics of mathematics.", 'teacher': "Sirous Hosseini"},
       2:{'id': 2, 'name': "cs", 'description': "Dive deep into cs.", 'teacher': "Hossein Alavi"},
       3: {'id': 3, 'name': "physics", 'description': "An introduction to Physics.", 'teacher': "Kamran tafti"},

    }

    list_course = list_course.get(course_id, None)
    
    # if course is None:
    #     return "Course not found", 404
    
    return render_template('course_detail.html', course=list_course)

@app.template_filter()
def custom_filter(desc):
    return desc[:10]


@app.route('/profile/<int:student_id>', methods=['GET', 'POST'])
def profile_id(student_id):
    student = std_dict.get(student_id)
    
    if student is None:
        return "Student not found", 404

    if request.method == 'POST':
        student['name'] = request.form.get('name')
        student['age'] = request.form.get('age')
        student['email'] = request.form.get('email')

        std_dict[student_id] = student
        
        return redirect(url_for('profile', student_id=student_id))
    
    return render_template('profile_id.html', student=student)




    
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        teacher = request.form['teacher']

        id = len(list_course) + 1

        list_course[id] = {
            'id': id,
            'name': title,
            'description': description,
            'teacher': teacher
        }
        


        if not title or not description or not teacher:
            return "All fields are required!"

        # Redirect to the course list
        return redirect(url_for('courses'))

    return render_template('add_course.html')
    
    
   











if __name__ == "__main__":
    app.run(port=5000, debug=True)

