async function generateModalUpdate(url,url_form,id) {
    const modal = document.getElementById('modalProduk-update');
    const form = document.getElementById('formProduk-update');
    const title = modal.querySelector('h3');


    title.innerText = "Memuat Data...";
    modal.style.display = "block";

    try {
      const response = await fetch(url,{method : "GET"});
        console.log(response) 
        if (!response.ok) throw new Error("Gagal mengambil data");
        
        const data = await response.json();

        form.reset();

        Object.keys(data).forEach(key => {
            const input = form.querySelector(`[name="${key}"]`);
            
            if (input) {
                input.value = data[key];
            }
        });

        title.innerText = "Update Produk: " + (data.nama || "Data");
        
      form.action = url_form
    } catch (error) {
        console.error("Error:", error);
        alert("Terjadi kesalahan saat mengambil data produk.");
        closeModal();
    }
}

function getFormDataAsJson(e,formId) {
  e.preventDefault()
  const form = document.getElementById(formId);
  const formData = {};
  console.log("form",form,formId)

  // Mengambil semua element child yang merupakan input, select, atau textarea
  const elements = form.querySelectorAll("input, select, textarea");

  elements.forEach(element => {
    const { name, value, type, checked } = element;

    // Pastikan element punya atribut 'name' agar bisa jadi key di JSON
    if (name) {
      if (type === "checkbox") {
        formData[name] = checked; // Simpan boolean untuk checkbox
      } else if (type === "radio") {
        if (checked) formData[name] = value; // Hanya ambil yang dipilih
      } else {
        formData[name] = value;
      }
    }
  });
  console.log(formData)

  return formData;
}

function closeModal(cls) {
    document.getElementById(cls).style.display = "none";
}


function openModal(cls) {
  document.getElementById(cls).style.display = "block";
}

// Menutup modal jika user klik di luar kotak modal
window.onclick = function(event) {
  let modal = document.getElementById("modalProduk");
  if (event.target == modal) {
    closeModal();
  }
}
