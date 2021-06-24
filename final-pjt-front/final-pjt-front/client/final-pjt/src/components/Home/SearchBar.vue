<template>
<div>
  <input type="text" :value="inputText" 
  v-model="keyword"
  @keyup.enter="inputEntered">
  <button @click="inputEntered">검색</button>
</div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: {
    keyword: ''
  },
  methods: {
    inputeEntered(){
      
    }
  }
}
</script>

<style>

</style>