<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" placeholder="Username" name="username">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" placeholder="Password" name="password">
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
                            <button class="button is-success">Log In</button>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <router-link to="/sign-up">Don't have an account?</router-link>
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
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            axios.defaults.headers.common['Authorization'] = null

            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password
            }

            axios
                .post("/api/v1/token/login", formData)

                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = "Token " + token

                    localStorage.setItem('token', token)

                    this.$router.push('/dashboard')
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