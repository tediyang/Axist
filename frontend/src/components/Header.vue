<template>
    <div class="header">
        <FontAwesomeIcon icon="fa-solid fa-bars" @click="toggleNav" class="nav-toggle" />
        <Transition>
            <div class="nav" v-if="showLoginNav || screenWidth > 768">
                <RouterLink to="/home" v-bind:class="{ active: props.active === 'home' }">Home</RouterLink>
                <RouterLink to="/routes" v-bind:class="{ active: props.active === 'routes' }">View Routes</RouterLink>
                <button class="sign-out" @click="signout">
                    Sign out     
                    <FontAwesomeIcon icon="fa-solid fa-right-from-bracket"></FontAwesomeIcon>
                </button>
            </div>
        </Transition>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const showLoginNav = ref(false);
const screenWidth = ref(0);

if (screenWidth.value > 768) {
    console.log("Screen width is greater than 768px");
    // showLoginNav.value = true;
}

const props = defineProps({
    active: {
        type: String,
        required: false,
    }
})

function signout() {
    localStorage.removeItem("user");
    window.location.reload();
}

function toggleNav(event) {
    console.log("Toggling");
    showLoginNav.value = !showLoginNav.value;
    event.target.classList.add("animate");
    setTimeout(() => {
        event.target.classList.remove("animate");
    }, 300);
}

onMounted(() => {
    console.log("Header Component mounted")
    if (!localStorage.getItem("user")) {
        router.push({path: "/"});
    }
    screenWidth.value = window.innerWidth;
    console.log(screenWidth.value);
    window.addEventListener("resize", () => {
        screenWidth.value = window.innerWidth;
        if (screenWidth.value < 768) {
            // showLoginNav.value = false;
        }
    })
    if (screenWidth.value > 768) {
        console.log("Screen width is greater than 768px");
        // showLoginNav.value = true;
    }
    else {
        showLoginNav.value = false;
    }
})

</script>

<style scoped>
@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(180deg);
    }
}

.v-enter-from, .v-leave-to {
    /* opacity: 0; */
    transform: translateX(100%);
}

.v-enter-active, .v-leave-active {
    transition: all 0.4s ease-in;
}

@media screen and (min-width: 768px) {
    .v-enter-from, .v-leave-to {
        /* opacity: 0; */
        transform: translateX(0%);
    }
}

.animate {
    animation: rotate 0.3s ease-in;
}

.sign-out {
    margin-top: 1em;
}

.nav {
    position: fixed;
    /* inset: 8% 0 0 0; */
    inset: 0;
    padding-top: 15%;
    z-index: 100;
    backdrop-filter: blur(1rem);
    display: flex;
    flex-direction: column;
}

.header > svg {
    position: absolute;
    right: 5%;
    top: 3%;
    font-size: 1.5rem;
    cursor: pointer;
    z-index: 10000;
    /* margin-bottom: 2em; */
}

button svg {
    margin-left: 0.5em;
}

.header button {
    color: hsla(160, 100%, 37%, 1);
    transition: 0.4s;
    background: none;
    border: none;
    cursor: pointer;
}

.header a, .header button {
    /* border: 1px solid #ccc; */
    padding: 1em;
    transition: all 0.5s;
    text-align: center;
}

.header a:hover, .header button:hover {
    transform: scale(1.1);
}

@media screen and (min-width: 768px) {
    .header {
        /* display: none; */
        /* border: 1px solid #ccc; */
        margin-bottom: 2em;
    }

    .nav-toggle {
        display: none;
    }

    .nav {
        position: static;
        /* display: block; */
        display: flex;
        flex-direction: row;
        padding: 0;
    }

    .nav a {
        margin: 0 0.2em;
    }

    .nav a, .nav button {
        font-size: 1rem;
    }

    button.sign-out {
        margin-left: auto;
        display: block;
    }
}

@media screen and (min-width: 1024px) {
    .header {
        border-bottom: 1px solid #ccc;
        margin-bottom: 3em;
    }
    .nav a, .nav button {
        /* border: 1px solid #ccc; */
        /* font-size: 1.2rem; */
    }
}
</style>