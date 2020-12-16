import cgi
formdata = cgi.FieldStorage()

a = int(formdata.getvalue('fnum'))
b = int(formdata.getvalue('snum'))

c=a+b
d=a-b
e=a*b
f=a%b


print("Content-type:text/html\r\n\r\n")
print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h2>sum of {a} and {b} is {c}</2>
    <h2>difference of {a} and {b} is {d}</2>
    <h2>Multiplication of {a} and {b} is {e}</2>
    <h2>Division of {a} and {b} is {f}</2>
</body>
</html>
''')