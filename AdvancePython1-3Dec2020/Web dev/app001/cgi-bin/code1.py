a = 12
b = 50
c = a+b

print("Content-type:text/html\r\n\r\n")
print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<!--    heading tag -  h1,h2,h3,h4,h5,h6-->
    <h1>Sum of {a} and {b} is {c} </h1>
</body>
</html>
''')