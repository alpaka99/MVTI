<template>
<b-container style="max-width: 800px;">
  <div>
    <div class='login-title'>로그인</div>
    <div class="login-form">
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
            @keyup.enter='login(credentials)'
          ></b-form-input>
        </b-form-group>


        <b-button style="min-height: 2.8rem; width:100%; margin-top: 3rem" type="submit" variant="danger" @click='login(credentials)'>Login</b-button>
        <!-- <b-button type="reset" variant="danger">Reset</b-button> -->
      </b-form>

      <!-- <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ credentials }}</pre>
      </b-card> -->
   </div>
  </div>
</b-container>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'Login',
  data: function(){
    return {
      credentials: {
        username: '',
        password: ''
      },
       show: true
    }
  },
  methods: {
    ...mapActions([
      'login'
    ]),
     onSubmit(event) {
        event.preventDefault()
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.credentials.username = ''
        this.credentials.password = ''
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
.login-title {
  text-align: left;
  color: whitesmoke;
  font-family: Noto Sans KR, serif;
  font-size: 3rem;
  font-weight: 500;
  margin: 0 0 0.5rem 0.5rem;
}
.login-form {
  text-align: left;
  color: whitesmoke;
  margin-left: 0.5rem;
}
</style>