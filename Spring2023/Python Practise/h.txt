grades_dict = {}
with open('studentData.txt', 'r') as f:
    for line in f:
        strings = line.strip()
        strings_to_list=strings.split()
        student_name=strings_to_list[0]
        grades = list(map(int, strings_to_list[1:]))
        grades_dict[student_name] = grades

threshold=int(input("Please Enter a threshold Value: "))
for name, grades in grades_dict.items():
    exam_numbers=grades
    count=0

    for score in exam_numbers:
        if score>threshold:
            count+=1
           
    print(f"{name} got {count} over {threshold}")