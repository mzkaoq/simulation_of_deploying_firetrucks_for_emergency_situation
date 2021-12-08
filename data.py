

with open('osp-coord.csv') as file:
    content = file.readlines()
rows = content[:]
fire_departments = []
for element in rows:
    x = element.split(",")
    x[1] = float(x[1])
    x[2] = float(x[2][:8])
    fire_departments.append(x)
#print(fire_departments)
