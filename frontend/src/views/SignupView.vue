<template>
    <div class="signup">
        <RouterLink to="/">
            <FontAwesomeIcon icon="fa-solid fa-arrow-left-long" />
        </RouterLink>
        <h2>Create an account</h2>
        <p>Ensure you provide the correct details</p>
        <div class="form-inputs">
            <span class="error" v-if="error">Please fill in all your details to continue.</span>
            <input type="text" placeholder="Enter first name" v-model="firstName" @keydown="error=false">
            <input type="text" placeholder="Enter surname" v-model="lastName" @keydown="error=false">
            <input type="email" placeholder="Enter email" v-model="email" @keydown="error=false">
            <input type="password" placeholder="Enter password" v-model="password" @keydown="error=false">
            <button @click.prevent="signup">Create account</button>
        </div>
        <p>
            Already have an account?
            <RouterLink to="/login">Login</RouterLink>
        </p>
    </div>
</template>

<script>
export default {
    name: 'SignUp',
    data() {
        return {
            firstName: "",
            lastName: "",
            email: "",
            password: "",
            error: ""
        }
    },
    methods: {
        signup() {
            if (this.firstName == "" || this.lastName == "" || this.email == "" || this.password == "") {
                this.error = true;
                
                return;
            }

            console.log(this.email, this.password, this.firstName, this.lastName);
            
            this.firstName = "";
            this.lastName = "";
            this.email = "";
            this.password = "";
        }
    }
}
</script>

<style scoped>

/* .v-enter-from, .v-leave-to {
    opacity: 0;
}

.v-enter-active, .v-leave-active {
    transition: all 0.5s ease-in-out;
} */


.signup {
    transition: all 0.5s ease-in-out;
}

.signup h2 {
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
</style>