<script setup>
import { ref } from "vue";

let clase = ref(null);
const text_predict = ref("");

const text_enviar = ref("Enviar")

const archivoImagen = ref(null);
const imagenPreview = ref('');

const enviar_img = async (e) => {
  e.preventDefault();

  let boton = document.getElementById("btn_enviar"); // Supongamos que el ID del elemento es "archivo"
  text_enviar.value = "Procesando"
  boton.disabled = true;

  let input = document.getElementById("imagen"); // Supongamos que el ID del elemento es "archivo"
  let archivoImagen = input.files[0];
  let formData = new FormData();
  formData.append("imagen", archivoImagen, archivoImagen.name);

  const res = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors",
    body: formData,
    credentials: "same-origin", // include, *same-origin, omit
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  }).then(async (response) => {
    if (response.ok) {
      const a = await response.json(); //first consume it in console.log
      return a; //then consume it again, the error happens
    }
  });

  res == "0" ? (text_predict.value = "Diagnostico: Sano") : (text_predict.value = "Diagnostico: Enfermo");
  clase.value = res;

  text_enviar.value = "Enviar"
  boton.disabled = false;
};



// Manejar el evento de cambio del campo de entrada de archivo
const handleFileChange = (event) => {
  // Obtener el archivo de imagen seleccionado
  archivoImagen.value = event.target.files[0];

  // Crear un objeto FileReader
  const lector = new FileReader();

  // Configurar la función de carga del lector
  lector.onload = (evento) => {
    // Obtener la URL de la imagen cargada
    imagenPreview.value = evento.target.result;
  };

  // Leer el contenido del archivo de imagen como una URL de datos
  lector.readAsDataURL(archivoImagen.value);
};
</script>

<template>
  <div class="container text-center">
    <div class="mt-4 row">
      <p class="fs-1" :class="clase == '0' ? 'text-success' : 'text-danger'">
        {{ text_predict }}
      </p>
    </div>
    <div>
      <img v-show="imagenPreview != ''" :src="imagenPreview" alt="" width="200" height="200" class="my-3" />
    </div>
    <form class="col">
      <input type="file" name="imagen" id="imagen" class="form-control" @change="handleFileChange" />
      <div class="mt-5">
        <button
          type="button"
          class="btn mb-3 w-25 fs-4"
          @click="enviar_img"
          id="btn_enviar"
        >
        {{text_enviar}} 
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
#btn_enviar{
  background: #992B38;
  color: #fff;
}
</style>
