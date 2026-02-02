window.onDeleteProduk = (url, csrf_token) => {
  if (confirm("Apakah kamu yakin untuk menghapus ?")) {
        fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrf_token,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert("Gagal menghapus!");
            }
        });
  }
}

window.onUpdateProduk = (url, csrf_token,data) => {
    console.log(url)
  if (confirm(`Apakah kamu yakin untuk mengubah ${data.nama_produk} ?`)) {
        fetch(url, {
            method: 'PUT',
            headers: {
                'X-CSRFToken': csrf_token,
                'Content-Type': 'application/json'
            },
          body : JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert("Gagal menghapus!");
            }
        });
  }
}
