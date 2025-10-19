<!DOCTYPE html>
<html>
<head>
    <title>Subjects</title>
</head>
<body>
    <h2>Welcome, {{ name }}!</h2>

    <h3>Your Subjects:</h3>
    <ul>
        {% for subject in subjects %}
            <li>{{ subject }}</li>
        {% endfor %}
    </ul>
</body>
</html>
