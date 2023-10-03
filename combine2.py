def my_name_is():
    print("My name is Sayma Akther")


def i_have_enrolled_course(course_name):
     print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"



courses = [
    {
        "course": "Python and Web",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"Python"

    },
    {
        "course": "Java and  Spring Boot",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"Java"

    },
    {
        "course": "PHP & Laravel",
        "frontend": "HTML,CSS,JavaScripts",
        "backend":"PHP , Artisan CLI"

    }
]


for item in courses:
    # print(item)
    course_name =  item["course"]
    backend = item["backend"] 
    frontend = item["frontend"]
    
    my_name_is()  
    i_have_enrolled_course(course_name)
    result =  i_have_learning(backend, frontend)
    print(result)
    print()
# Update the code according your name, and different types of course listed in Bangla Fighter Website: https://banglafighter.com/crs
