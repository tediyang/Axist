<script setup>
import { RouterView } from 'vue-router'
</script>

<template>

  <RouterView v-slot="{ Component }">
    <Transition name="route" mode="out-in">
      <component :is="Component"></component>
    </Transition>
  </RouterView>

</template>

<style scoped>
  /* ROUTE TRANSITION CLASSES */
  .route-enter-active, .route-leave-active {
    transition: opacity 0.2s ease-in-out;
  }

  .route-enter-from, .route-leave-to {
    opacity: 0;
  }

  /* .route-enter-to, .route-leave-from {
    opacity: 1;
  } */
</style>