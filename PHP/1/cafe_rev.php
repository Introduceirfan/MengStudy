<?php

session_start();

$daftar_menu = [
    'kopi'   => 10000,
    'teh'    => 5000,
    'nasgor' => 15000
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (empty($_POST['menu'])) {
        $_SESSION['hasil'] = "<p style='color: red;'>SORRY kamu belum memilih menu ini</p>";
    } else {
        $menu_dipilih  = $_POST['menu'];
        $porsi         = $_POST['porsi'];
        $bayar         = $_POST['bayar'];

        $harga_satuan  = $daftar_menu[$menu_dipilih];
        $total_tagihan = $harga_satuan * $porsi;
        $kembalian     = $bayar - $total_tagihan;

        // Sanitasi teks & format rupiah
        $menu_clean      = htmlspecialchars($menu_dipilih);
        $total_formatted = number_format($total_tagihan, 0, ',', '.');

        if ($bayar >= $total_tagihan) {
            $kembalian_formatted = number_format($kembalian, 0, ',', '.');
            $bayar_formatted     = number_format($bayar, 0, ',', '.');

            $_SESSION['hasil'] = "Kamu memesan <strong>$menu_clean</strong><br>Total tagihan sebesar: Rp $total_formatted<p style='color: green; font-weight: bold;'>Kamu membayar sebesar Rp $bayar_formatted dan sisa kembalianmu adalah Rp $kembalian_formatted</p>";
        } else {
            $kurang = $total_tagihan - $bayar;
            $kurang_formatted = number_format($kurang, 0, ',', '.');

            $_SESSION['hasil'] = "<p style='color: red; font-weight: bold;'>SORRYY uang kamu kurang segini Rp $kurang_formatted</p>";
        } 
    }

    header("Location: cafe.php");
    exit(); 
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
            <select name="menu" required>
                <option value="" selected disabled hidden>Pilih menu disini!</option>
                <option value="kopi">Kopi Hitam - 10.000</option>
                <option value="teh">Es Teh Manis - 5.000</option>
                <option value="nasgor">Nasi Goreng - 15.000</option>
            </select>
        </div>
        <br>
        <div>
            <label>Porsi</label>
            <input type="number" name="porsi" min="1" required>
        </div>
        <br>
        <div>
            <label>Uang kamu?</label>
            <input type="number" name="bayar" min="0" required>
        </div>
        <br>
        
        <button type="submit">CEK SINI!</button>
    </form>

    <?php echo $pesan_hasil; ?>
</body>
</html>