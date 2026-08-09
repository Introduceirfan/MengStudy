<?php

session_start();

$daftar_menu = [
    'kopi' => 10000,
    'teh' => 5000,
    'nasgor' => 15000
];

if (isset($_POST['menu'])) {
    $menu_dipilih = $_POST['menu'];
    $porsi = $_POST['porsi'];
    $bayar = $_POST['bayar'];

    $harga_satuan = $daftar_menu[$menu_dipilih];
    $total_tagihan = $harga_satuan * $porsi;
    $kembalian = $bayar - $total_tagihan;

    if ($bayar >= $total_tagihan) {
        $_SESSION['hasil'] = "Kamu memesan $menu_dipilih<br>Total tagihan sebesar: $total_tagihan<p style='color: green; font-weight: bold;'>Kamu membayar sebesar $bayar dan sisa kembalianmu adalah $kembalian</p>";
    } else {
        $_SESSION['hasil'] = "<p style='color: red; font-weight: bold'>SORRYY uang kamu kurang segini $total_tagihan</p>";
    } 

    header("Location: cafe.php");
    exit();
} else {
    $_SESSION['hasil'] = "Kamu belum mengklik!";
}

$pesan_hasil = "";
if (isset($_SESSION['hasil'])) {
    $pesan_hasil = $_SESSION['hasil'];

    unset($_SESSION['hasil']);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>AKU Title</title>
</head>
<body>
    <h1>Ini adalah title kasir</h1>
    <form action="" method="POST">
        <div>
            <label>Pilih Menu: </label>
            <select name="menu">
                <option value="" selected disabled hidden>Pilih menu disini!</option>
                <option value="kopi">Kopi Hitam - 10.000</option>
                <option value="teh">Es Teh Manis - 5.000</option>
                <option value="nasgor">Nasi Goreng - 15.000</option>
            </select>
        </div>
        <br>
        <div>
            <label>Porsi</label>
            <input type="number" name="porsi" required>
        </div>
        <br>
        <div>
            <label>Uang kamu?</label>
            <input type="number" name="bayar" required>
        </div>
        <br>
        
        <button type="submit">CEK SINI!</button>
    </form>

    <?php echo $pesan_hasil; ?>
</body>
</html>