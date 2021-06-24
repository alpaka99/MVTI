import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import vuetify from '@/plugins/vuetify' // path to vuetify export
// import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'

import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

Vue.config.productionTip = false
Vue.use(VueGlide)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
