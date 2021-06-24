<template>
<b-container  style="max-width: 800px;">
  <div>
    <div class="login-title">회원가입</div>
    <div class="login-form ">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="User Name"
          label-for="input-1"
        >
          <b-form-input
            style="min-height: 3rem;"
            id="input-1"
            v-model="credentials.username"
            type="text"
            placeholder="Enter Username"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Password"
          label-for="input-2"

        >
          <b-form-input
            style="min-height: 3rem;"
            id="input-2"
            v-model="credentials.password"
            type="password"
            placeholder="Enter Password"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-3"
          label="Password Confirmation"
          label-for="input-3"

        >
          <b-form-input
            style="min-height: 3rem;"
            id="input-3"
            v-model="credentials.passwordConfirmation"
            type="password"
            placeholder="Enter Password Again"
            required
            @keyup.enter='signup(credentials)'
          ></b-form-input>
        </b-form-group>


        <b-button style="min-height: 2.8rem; width:100%; margin-top:3rem" type="submit" variant="danger" @click='signup(credentials)'>Signup</b-button>
        <!-- <b-button type="reset" variant="danger">Reset</b-button> -->
      </b-form>
<!-- 
      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ credentials }}</pre>
      </b-card> -->
   </div>
  </div>
</b-container>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name: 'Signup',
  data: function() {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: ''
      },
      show: true,
    }
  },
  methods: {
    ...mapActions([
      'signup'
    ]),
     onSubmit(event) {
        event.preventDefault()
        // alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
  }
}
</script>

<style>

</style>