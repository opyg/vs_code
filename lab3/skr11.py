
students={
    "121191":{
        "name":'Jan',
        "lastname":'Kowalski',
        "grades":[4.0,4,5,4.5,3.5,3]
    },
    "120673":{
        "name":'Huan',
        "lastname":'Cortes',
        "grades":[2.0,3,3.5,3.5,2,3]
    }
}
for index, student_info in students.items(): 
    name = student_info["name"] 
    last_name = student_info["lastname"] 
    grades = student_info["grades"] 
    avg = sum(grades) / len(grades) if grades else 0.0 
    print(f"Index: {index}") 
    print(f"Name: {name}") 
    print(f"Last name: {last_name}") 
    print(f"AVG: {avg:.2f}\n") 

