import urllib.request as url
import json
import cgi


form = cgi.FieldStorage()
name = form.getvalue('name')
name = name.replace(' ','%20')
path = "https://cricapi.com/api/playerFinder?apikey=RiPTCn1FNCUNmr3QzfBy03EMIJG2&name="+name
res = url.urlopen(path)
data = json.load(res)
pid = data['data'][0]['pid']

req = url.urlopen(f"https://cricapi.com/api/playerStats?apikey=RiPTCn1FNCUNmr3QzfBy03EMIJG2&pid={pid}")
data=json.load(req)
name = data['fullName']
bat_style = data["battingStyle"]
bowl_style = data["bowlingStyle"]
profile=data['profile']
age=data['currentAge']
role = data['playingRole']
img=data['imageURL']



print("Content-type:text/html\r\n\r\n")
print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h2>PROFILE</h2>
    <p>{profile}</p>
    <img src="{img}">
    <table width="100%" border=2px cellpadding=12px>
       <tr>
            <th>Name</th>
            <th>Batting Style</th>
            <th>Bowling Style</th>
            <th>Age</th>
            <th>Role</th>
       </tr>
        <tr>
            <td>{name}</td>
            <td>{bat_style}</td>
            <td>{bowl_style}</td>
            <td>{age}</td>
            <td>{role}</td>
        </tr>
    </table>
    
</body>
</html>
''')