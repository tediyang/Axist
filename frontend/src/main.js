import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// import the fontawesome core
import { library } from "@fortawesome/fontawesome-svg-core";

// import the fontawesome icon component
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"

// specific icons for the project
import { faBars, faArrowLeftLong, faLocationDot, faArrowRight, faRightFromBracket } from "@fortawesome/free-solid-svg-icons";

// add icons to library
library.add(faArrowLeftLong)
library.add(faBars)
library.add(faLocationDot)
library.add(faArrowRight)
library.add(faRightFromBracket)

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.component('FontAwesomeIcon', FontAwesomeIcon)

app.mount('#app')
