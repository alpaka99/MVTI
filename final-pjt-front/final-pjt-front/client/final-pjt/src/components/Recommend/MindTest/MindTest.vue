<template>
  <div>
   
    <!-- <h2>Mind Test</h2> -->
    <Intro v-if="$store.state.test_state === 0"/>
    <Test v-if="$store.state.test_state === 1"/>
    <Bridge v-if='$store.state.test_state === 2'/>
    <Result v-if="$store.state.test_state === 3"/>
    <!-- <h2>mind test end</h2> -->
   
  </div>
</template>

<script>
import Intro from "@/components/Recommend/MindTest/Intro.vue"
import Test from "@/components/Recommend/MindTest/Test.vue"
import Bridge from "@/components/Recommend/MindTest/Bridge.vue"
import Result from "@/components/Recommend/MindTest/Result.vue"
export default {
  name: 'MindTest',
  components: {
    Intro,
    Test,
    Bridge,
    Result
  },
  craeted() {
  }
}
</script>

<style>
ol, ul {
	list-style: none;
}
</style>