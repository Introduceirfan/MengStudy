<?php
session_start();

// SATPAM: Cek apakah user punya kunci login di session
if (!isset($_SESSION['is_logged_in'])) {
    // Jika belum login, tendang balik ke login.php
    header("Location: login.php");
    exit();
}

$nama_user = $_SESSION['user_login'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Selamat Datang di Dashboard, <?php echo htmlspecialchars($nama_user); ?>!</h1>
    <p>Ini adalah halaman rahasia</p>
    
    <hr>
    <a href="logout.php">LOGOUT KELUAR</a>
</body>
</html>