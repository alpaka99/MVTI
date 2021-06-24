<template>
  <b-container class="max-width: 800px">
    <div class="login-title" style="text-align:center; padding-top:8rem; ">Are you sure?</div>
    <b-button style="min-height: 2.8rem; width:18%; margin-top: 3rem; color: whitesmoke;" variant="danger" @click='logout'>Logout</b-button>
  </b-container>
</template>

<script>
export default {
  name: 'Logout',
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>

</style>