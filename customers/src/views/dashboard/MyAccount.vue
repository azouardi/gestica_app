<template>
    <div class="page-my-account">
    <h1 class="title">My Account</h1>
    
    <button class="button is-danger" @click="logout()">Log out</button>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios
                .post("/api/v1/token/logout/")
                .then(response => {
                    axios.defaults.headers.common['Authorization']=null

                    localStorage.removeItem('token')

                    this.$store.commit('removeToken')

                    this.$router.push('/')
                })
                .catch(
                    error => {
                        if (error.response) {
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