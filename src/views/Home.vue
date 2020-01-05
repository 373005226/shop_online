<template>
  <div class="home">
    <Headers></Headers>
    <Search_nav></Search_nav>
  </div>
</template>

<script>
// @ is an alias to /src
import Headers from "../common/headers"
import Search_nav from "../components/search_nav";

export default {
  name: 'home',
  components: {
    Search_nav,
    Headers
  }
}
</script>
