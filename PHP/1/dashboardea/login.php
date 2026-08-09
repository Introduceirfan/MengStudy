<?php
session_start()

if (isset($_SESSION['is_logged_in'])) {
    header("Location: dashboard.php");
    exit();
}

$error_message = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (empty($_POST['username']) || empty($_POST['password'])) {
        $error_message = "Username dan password wajib banget diisi!";
    } else {
        $username = $_POST['username']
        $password = $_POST['password']
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login Page</title>
</head>
<body>
    <h1>Login ke dashboard!</h1>
    <form action="" method="POST">
        <div>
            <label>Username: </label>
            <input type="text" name="username" required>
        </div>
        <br>
        <div>
            <label>Password: </label>
            <input type="text" name="password" required>
        </div>
        <br>
        <button type="submit">Loginkan!</button>
    </form>
</body>
</html>