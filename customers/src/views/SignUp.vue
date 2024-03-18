<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" placeholder="Username" name="username">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email" placeholder="Email" name="email" >
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" placeholder="Password" name="password">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Confirm Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="confirmPassword" placeholder="Confirm Password" name="confirm_password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p
                            v-for="error in errors"
                            v-bind:key="error"
                        >
                        {{ error }}
                    </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Sign Up</button>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <router-link to="/log-in">Already have an account?</router-link>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                username: this.username,
                email: this.email,
                password: this.password
            }
            
            if (this.password !== this.confirmPassword) {
                this.errors.push("Passwords do not match");
                return; // Stop form submission
            }

            axios
                .post("/api/v1/users/", formData)
                .then(response => {
                    console.log(response)

                    this.$router.push('/log-in')
                })
                .catch(
                    error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            console.log(JSON.stringify(error.message))
                        } else {
                            console.log(JSON.stringify(error))
                        }
                    }
                )
        }
    }
}
</script>

