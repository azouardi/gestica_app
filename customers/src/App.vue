<template>
  <div id="wrapper">
    <nav class = "navbar is-dark">
      <div class = "navbar-brand">
        <router-link to="/" class = "navbar-item">Home</router-link>
      </div>
      <div class="navbar-menu">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
            <div class="navbar-item">
              <div class="buttons">
            <router-link to="/dashboard/my-account" class="button is-light">My Account</router-link>
          </div>
        </div>
          </template>
          <template v-else>
            <router-link to="/" class="navbar-item">Home</router-link>
            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/log-in" class="button is-success">Login</router-link>
                <router-link to="/sign-up" class="button is-light">Sign-up</router-link>
              </div>
            </div>
          </template>

        </div>
      </div>
    </nav>
    <section class="section">
      <div class="container">
        <router-view/>
      </div>
    </section>

    <footer class="footer">
      <div class="container">
        <div class="content has-text-centered">
          <p>
            <strong>Ad Associés</strong> by <a href="https://ma.linkedin.com/in/ouardiazzeddine/en">Azzeddine OUARDI</a>.
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name :'App',
    beforeCreate() {
      this.$store.commit('initialiseStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token" + token
      } else {
        axios.defaults.headers.common['Authorization'] = null
      }
    }
  }


</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
