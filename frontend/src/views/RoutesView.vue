<template>
    <div class="routes">
        <Header active="routes" />
        <p>You routes history goes here</p>
    </div>
  </template>
  
<script setup>
import { ref } from "vue";
import Header from "../components/Header.vue"

const show = ref(true);
</script>

<style scoped>

.routes {
    margin-top: 2em;
}

@media (min-width: 1024px) {


}
</style>
  