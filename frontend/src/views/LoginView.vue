<template>
    <div class="login">
        <RouterLink to="/">
            <FontAwesomeIcon icon="fa-solid fa-arrow-left-long" />
        </RouterLink>
        <h2>Login to your account</h2>
        <div class="form-inputs">
            <span class="error" v-if="error">Please fill in all your details to continue.</span>
            <span class="auth-error" v-if="authError">Something went wrong! Please check your details and try again :(</span>
            <input type="email" placeholder="Enter email" v-model="email" @keydown="error=false">
            <input type="password" placeholder="Enter password" v-model="password" @keydown.enter="login">
            <button @click="login">Login</button>
            </div>
        <p>
            Don't have an account?
            <RouterLink to="/signup">Sign up now</RouterLink>
        </p>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            email: "",
            password: "",
            error: false,
            authError: false
        }
    },
    methods: {
        login() {
            if (this.email === "" || this.password === "") {
                this.error = true;
                return;
            }

            console.log(this.email, this.password);

            if (this.email == "olotonjoshua@gmail.com" && this.password == "next23rd") {
                // Login successfull
                this.authError = false;
                // set localstorage
                localStorage.setItem("user", this.email);
                this.$router.push({path: "/home"});
            }
            else {
                this.authError = true;
            
                // Reset form fields
                this.email = "";
                this.password = "";
            }
        }
    }
}
</script>

<style scoped>

.login h2 {
    margin-top: 1em;
}
.form-inputs {
    margin-top: 2em;
    display: flex;
    flex-direction: column;
    gap: 1em;
}

input {
    background: var(--vt-c-black-soft);
    padding: 1em;
    border-radius: 6px;
    color: #fff;
    outline: 1px solid rgb(3, 96, 65);
    border: none;
}

button {
    margin: 1em 0em;
    background: rgb(3, 96, 65);
    color: #fff;
    flex-grow: 1;
    text-align: center;
    padding: 1em;
    border-radius: 5px;
    transition: all 0.5s;
    border: none;
}

svg {
    font-size: 1.2rem;
}

.auth-error {
    color: red;
    font-size: 0.7rem;
}
</style>