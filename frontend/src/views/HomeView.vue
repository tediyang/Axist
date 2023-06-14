<script setup>
import { onMounted, ref } from "vue";
import Header from "../components/Header.vue"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'


const name = ref(localStorage.getItem("user"));
const country = ref("");
const region = ref("");
const directions = ref("");
const pageLoading = ref(true);

onMounted(() => {
    console.log("Component mounted")

    const url = "https://geo.ipify.org/api/v2/country?apiKey=at_wnQ5o0HXVdV1UL4q7gUe6ldlU0TIH&ipAddress";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            pageLoading.value = false;
            console.log(data);
            country.value = data.location.country;
            region.value = data.location.region;
        })
        .then(error => {
            console.log(error);
        });
})
</script>

<template>
    <Transition name="page">
        <div class="home" v-if="!pageLoading">
            <Header active="home" />
            <div class="location">
                <FontAwesomeIcon icon="fa-solid fa-location-dot" />
                <p>{{ region }}, {{ country }}</p>
            </div>
            <h3 class="welcome">Welcome, {{ name }}</h3>

            <div class="direction-input">
                <input type="text" v-model="directions" placeholder="Where would you like to go..">
            <button>
                <FontAwesomeIcon icon="fa-solid fa-arrow-right"></FontAwesomeIcon>
            </button>
            </div>
        </div>
        <div class="loading" v-else>
            <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
        </div>
    </Transition>
</template>

<style scoped>
.page-enter-from, .page-leave-to {
    /* opacity: 0; */
    /* transform: translateX(10px); */
}

.page-enter-active, .page-leave-active {
    /* transition: all 0.2s ease-in-out; */
}

.home {
    margin-top: 2em;
}
.loading {
    margin-top: 2em;
    text-align: center;
    /* display: flex;
    justify-content: center; */
}
.location {
    display: flex;
    /* justify-content: end; */
    align-items: center;
    /* border: 1px solid #ccc; */
    /* margin-bottom: 2em; */
    font-size: 1.1rem;
}

.location p {
    margin-left: 1em;
}

.welcome {
    margin: 1.5em 0;
}

.direction-input {
    display: flex;
    align-items: center;
    outline: 1px solid rgb(3, 96, 65);
    border-radius: 6px;
    background: var(--vt-c-black-soft);
}

input {
    width: 100%;
    background: none;
    padding: 1em;
    color: #fff;
    border: none;
    outline: none;
}

button {
    /* margin: 1em 0em; */
    /* background: rgb(3, 96, 65); */
    color: #fff;
    flex-grow: 1;
    text-align: center;
    padding: 1em;
    border-radius: 5px;
    transition: all 0.5s ease-out;
    border: none;
    background: none;
}

button:hover {
    background: rgb(3, 96, 65);
}

@media screen and (min-width: 768px) {
    .home {
        margin: 0;
    }
}

@media screen and (min-width: 1024px) {
    .home {
        width: 100%;
    }
}
</style>