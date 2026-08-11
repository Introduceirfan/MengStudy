<?php
session_start();

if (isset($_SESSION['is_logged_in'])) {
    header("Location: dashboard.php");
    exit();
}

$error_message = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (empty($_POST['username']) || empty($_POST['password'])) {
        $error_message = "Username dan Password wajib diisi!";
    } else {
        $username = $_POST['username'];
        $password = $_POST['password'];
        if ($username === 'admin' && $password === '12345') {
            $_SESSION['is_logged_in'] = true;
            $_SESSION['user_login']   = $username;

            header("Location: dashboard.php");
            exit();
        } else {
            $error_message = "Username atau Password salah!";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login System</title>
</head>
<body>
    <h2>Form Login</h2>

    <?php if (!empty($error_message)): ?>
        <p style="color: red; font-weight: bold;"><?php echo htmlspecialchars($error_message); ?></p>
    <?php endif; ?>

    <form action="" method="POST">
        <div>
            <label>Username:</label>
            <input type="text" name="username">
        </div>
        <br>
        <div>
            <label>Password:</label>
            <input type="password" name="password">
        </div>
        <br>
        <button type="submit">LOGIN</button>
    </form>
</body>
</html>