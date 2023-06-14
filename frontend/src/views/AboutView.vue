<template>
  <div class="about">
    <button @click="show=!show">Toggle</button>
    <Transition>
      <h1 v-if="show">This is an about page</h1>
    </Transition>
  </div>
</template>

<script setup>
import { ref } from "vue";

const show = ref(true);
</script>

<style>
.v-enter-from, .v-leave-to {
  /* opacity: 0; */
  transform: translateX(100%);
}
.v-enter-active, .v-leave-active {
  transition: all 0.5s ease-in;
}

@media (min-width: 1024px) {
  .about {
    /* min-height: 100vh;
    display: flex;
    align-items: center; */
  }
}
</style>
