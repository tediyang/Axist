<script setup>
defineProps({
    msg: {
        type: String,
        required: true,
    }
})
</script>

<template>
    <h2>{{ msg }}</h2>
</template>

<style></style>