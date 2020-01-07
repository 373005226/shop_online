<template>
    <div>
      <banner_top></banner_top>
      <MainNav></MainNav>
    </div>
</template>

<script>
  import banner_top from "./Home/banner_top";
  import MainNav from "./Home/MainNav";
    export default {
      name: "MainPage",
      components: {
        banner_top,
        MainNav,
      },
    }
</script>

<style scoped>

</style>
