def my_name_is():
    print("My name is Bangla Fighter Engineering")


def i_have_enrolled_course(course):
    # for course in courses:
     print(f"I have enrolled in a course named {course['course_name']}")


def i_have_learning(course):
    return f"Learning {course['backend']}, {course['frontend']}"



courses = [
    {
        "course_name": "Python and Web",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"Python"

    },
    {
        "course_name": "Java and  Spring Boot",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"Java"

    },
    {
        "course_name": "PHP & Laravel",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"PHP , Artisan CLI"

    }
]

for course in courses:
    my_name_is()
    i_have_enrolled_course(course)
    result = i_have_learning(course)
    print(result)
    print()

# Update the code according your name, and different types of course listed in Bangla Fighter Website: https://banglafighter.com/crs
