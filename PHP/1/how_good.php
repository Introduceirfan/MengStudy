<?php
if (isset($_POST['nama'])) {
    $nama_user = $_POST['nama'];
    $ipk_user = $_POST['ipk'];
    $toelf_user = $_POST['toefl'];

    if ($ipk_user >= 3.25 && $toelf_user >= 450) {
        
        echo "<p style='color: green; font-weight: bold;'>Selamat <b>$nama_user!</b> Anda dinyatakan LOLOS seleksi awal dengan IPK $ipk_user dan TOEFL $toelf_user.</p>";
    } else {
        
        echo "<p style='color: red; font-weight: bold;'>Mohon maaf <b>$nama_user</b>, Anda BELUM LOLOS seleksi awal. Tetap semangat!</p>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Cek beasiswa</title>
</head>
<body>
    <h2>Apakah kamu lolos beasiswa?</h2>

    <form action="" method="POST">
        <div>
            <label>Nama:</label><br>
            <input type="text" name="nama" required>
        </div>
        <br>
        <div>
            <label>IPK:</label><br>
            <input type="number" step="0.01" name="ipk" required>
        </div>

        <div>
            <label>toefl:</label><br>
            <input type="number" name="toefl" required>
        </div>
        <br>
        <button type="submit">CEK DISINI!</button>
    </form>
</body>
</html>