import { useState } from 'react'

function App() {
  const [stok, setStok] = useState(10)

  // 1. Amankan logika if-else lo di dalam fungsi mandiri di sini!
  const tanganiKurangStok = () => {
    if (stok > 0) {
      setStok(stok - 1)
    } else {
      alert("Waduh bos, stok udah abis! Gak bisa minus!")
    }
  }

  return (
    <div style={{ padding: '50px', fontFamily: 'sans-serif' }}>
      <h1>Toko Sembako Masbro 🏪</h1>
      <p>Stok Beras Saat Ini: <strong>{stok}</strong> Kg</p>
      
      <button onClick={() => setStok(stok + 1)} style={{ padding: '10px 20px', cursor: 'pointer' }}>
        Tambah Stok Beras
      </button>

      {/* 2. Di tombol tinggal panggil nama fungsinya doang, bersih banget! */}
      <button onClick={tanganiKurangStok} style={{ padding: '10px 20px', cursor: 'pointer', marginLeft: '10px' }}>
        Kurangi Stok Beras
      </button>
    </div>
  )
}

function Barang(props) {
  return (
    <div style={{border: '2px solid #ccc', padding: '20px', borderRadius: '10px', marginBottom: '15px', width: '300px' }}>
      <h3></h3>
    </div>
  )
}
export default App