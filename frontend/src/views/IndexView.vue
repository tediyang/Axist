<script setup>
import { onMounted } from 'vue';
import {useRouter} from 'vue-router';
import TheWelcome from '../components/TheWelcome.vue'

const router = useRouter();
onMounted(() => {
  if (localStorage.getItem("user")) {
    router.push({path: "/home"});
  }
})
</script>

<template>
  <div class="index">
    <img src="/AXIST1-1.png" alt="" srcset="">
    <div class="intro">
      <div class="intro__text">
        <h1>
          GET THERE
          <FontAwesomeIcon icon="fa-solid fa-location-dot" v-bind:style="{ color: 'hsla(160, 88%, 49%, 0.635)' }"></FontAwesomeIcon>
        </h1>
        <h2 v-bind:style="{ color: 'red' }">EASIER</h2>
        <h2 v-bind:style="{ color: 'yellow' }">QUICKER</h2>
        <h2 v-bind:style="{ color: 'green' }">FASTER</h2>
      </div>
      <div class="nav">
        <!-- <RouterLink to="/">Home</RouterLink> -->
        <RouterLink to="/signup">Sign up</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.index::before {
  content: "";
    position: absolute;
    inset: 0;
    background-image: url(/AXIST2.png);
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    z-index: -100;
    opacity: 0.2;
}

.intro {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;

  width: 70%;
  margin: 0 auto;
  background: var(--color-background);
  opacity: 0.8;
  padding: 3em 0;
  box-shadow: 0 0 2px 0px #ccc;
}

img {
  margin: 2em auto;
  width: 45%;
  max-width: 150px;
  display: block;
  object-fit: cover;
}

.nav {
  display: flex;
  flex-direction: column;
  gap: 0.8em;
  width: 70%;
  max-width: 350px;
  margin: 1em auto 0 auto;
}

.nav a {
  background: rgb(3, 96, 65);
  color: #fff;
  flex-grow: 1;
  text-align: center;
  padding: .4em 1em;
  border-radius: 5px;
  transition: all 0.5s;
}

.nav a:hover {
  background: rgba(3, 96, 65, 0.7);
}

@media screen and (min-width: 768px) {
  .nav a {
    padding: .6em 1em;
  }
}

@media screen and (min-width: 1024px) {

  img {
    margin: 0 auto;
    width: 28%;
  }
  .intro {
    width: 55%;
    margin: 1rem auto;
    background: var(--color-background);
    opacity: 0.8;
    padding: 3em 0;
    box-shadow: 0 0 2px 0px #ccc;
  }

  .intro__text {
    position: static;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 3em;
    transform: translate(0, 0);
    box-shadow: none;
  }

  .intro h1 {
    font-size: 2.1rem;
  }

  .intro h2 {
    font-size: 1.4rem;
  }
  .index::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image: url(/AXIST2.png);
    background-position: center;
    background-size: cover;
    z-index: -100;
    opacity: 0.3;
  }

  .nav {
    position: static;
    bottom: 6%;
    left: 0;
    right: 0;
    display: flex;
    flex-direction: column;
    gap: 1.6em;
    width: 30%;
    margin: 0 auto;
  }
}
</style>
