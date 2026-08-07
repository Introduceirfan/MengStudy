<?php
// 1
// $daftar_harga = [15000, 45000, 120000, 8000, 250000];

// foreach ($daftar_harga as $harga) {
//     if ($harga >= 100000) {
//         echo "Barang Mahal: Rp $harga - Dapet Gratis Ong!\n"; 
//     } else {
//         echo "Barang Reguler: Rp $harga\n"; 
//     }
// }

//2
// $laptop = [
//     "merk" => "ASUS",
//     "ram" => "16GB",
//     "harga" => 12000000
// ];

// foreach ($laptop as $key => $value) {
//     if ($key == "harga") {
//       echo "$key : Rp $value\n";  
//     } else {
//         echo "$key : $value\n";
//     }    
// }

//3
// $keranjang = [
//     ["produk" => "Indomie", "harga" => 3500, "jumlah" => 5],
//     ["produk" => "Susu UHT", "harga" => 12000, "jumlah" => 2],
//     ["produk" => "Roti Tawar", "harga" => 15000, "jumlah" => 1]
// ];
// $total_belanja = 0;

// foreach ($keranjang as $value) {
//     $subtotal = $value["harga"] * $value["jumlah"];
//     echo "Produk: {$value["produk"]} | Total: Rp $subtotal\n";
//     $total_belanja += $subtotal;
// }

// echo "Total Bayar: Rp $total_belanja\n"

//4
// function format_user($nama, $role) {
//     if ($role == "admin") {
//         echo "ADMIN - {$nama}\n";
//     } else {
//         echo "{$role} - {$nama}\n";
//     }
// }
// format_user("Budi", "admin");
// format_user("Siti", "user");

// mini boss i guess
// function hitung_subtotal($daftar_pesanan) {
//     $subt = 0;
//     foreach ($daftar_pesanan as $value) {
//         $subt += $value["harga"] * $value["jumlah"];
//     }
//     return $subt;
// }

// function hitung_pajak($nominal) {
//     $tax = $nominal * 0.10;
//     return $tax;
// }

// $pesanan = [
//     ["nama" => "Nasi Goreng", "harga" => 25000, "jumlah" => 2],
//     ["nama" => "Es Teh Manis", "harga" => 5000, "jumlah" => 3],
//     ["nama" => "Ayam Bakar", "harga" => 30000, "jumlah" => 1]
// ];

// $subtotal = hitung_subtotal($pesanan);
// $pajak = hitung_pajak($subtotal);
// $grand_total = $subtotal + $pajak;

// echo "--- STRUK RESTORAN ---\n";
// echo "Subtotal : Rp {$subtotal}\n";
// echo "Pajak 10%: Rp {$pajak}\n";
// echo "----------------------\n";
// echo "Total    : Rp {$grand_total}";

?>
<!-- this is for the adaptation with my own language magic? -->