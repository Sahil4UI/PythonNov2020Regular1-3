data = [{"id":101,"Name":"ram","Marks":[90,80,70]},
        {"id":102,"Name":"Shyam","Marks":[45,20,25]},
        {"id":103,"Name":"Geeta","Marks":[38,80,35]},
        {"id":104,"Name":"Seeta","Marks":[10,0,0]},
        {"id":105,"Name":"Mohit","Marks":[90,90,90]}
        ]
"""
101 Ram
102 Shyam
103 Geeta
104 Seeta
105 Mohit
"""
for i in data:
    avg=sum(i['Marks'])//3
    i["Average"]=avg
    print(f"{i['id']},{i['Name']},{avg}")

