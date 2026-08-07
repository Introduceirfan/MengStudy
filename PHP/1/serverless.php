<?php

if (isset($_POST['email'])) {
    $email_user = $_POST['email'];
    
    echo "<h3>Login Berhasil untuk email: $email_user</h3>";
    echo "<hr>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>POST PHP Dummy</title>
</head>
<body>
    <h2>This is login</h2>
    
    <form action="" method="POST">
        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>
        
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        
        <button type="submit">Submit Login</button>
    </form>
</body>
</html>