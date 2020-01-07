<template>
  <div class="home">
    <Headers></Headers>
    <search></search>
    <main-page></main-page>
  </div>
</template>

<script>
// @ is an alias to /src
import Headers from "../common/headers"
import search from "../common/search"
import MainPage from "../components/MainPage";
export default {
  name: 'home',
  components: {
    Headers,
    search,
    MainPage
  }
}
</script>
