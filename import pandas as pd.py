import pandas as pd
student_data = pd.DataFrame({"name":['Alice','Bob','Charlie','David','Eva'],
                             "Age":[20,22,19,21,20],
                             "Grade":['A','B','A','C','B'],
                             "Marks":[85,78,92,65,74]})
print(student_data.head(3))
print(student_data[["name","Marks"]])
print(student_data["Grade"]=='A')