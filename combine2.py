def my_name_is():
    print("My name is Bangla Fighter Engineering")


# def i_have_enrolled_course(course_name):
#      print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"



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

def course_data(backend,frontend, courses):
   for item in courses:
       backend_value = item.get(backend, None)
       frontend_value = item.get(frontend, None)
       result = i_have_learning(backend_value, frontend_value)
       print(result)


    #    name_value = item.get(course_name, None)
    #    i_have_enrolled_course(course_name)
    #    print(name_result)

       
    # my_name_is()
# course_data("course_name", courses)
course_data("backend","frontend",courses)
    # print(result)
    # print()

# Update the code according your name, and different types of course listed in Bangla Fighter Website: https://banglafighter.com/crs
