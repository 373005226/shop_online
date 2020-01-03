<template>
  <div class="home">
    <Header></Header>
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '../components/HelloWorld.vue'
import Header from "../common/header";

export default {
  name: 'home',
  components: {
    HelloWorld,
    Header
  }
}
</script>
