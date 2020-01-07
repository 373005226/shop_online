<template>
    <div>
      <banner_top></banner_top>
      <MainNav></MainNav>
    </div>
</template>

<script>
  import banner_top from "./Home/banner_top";
  import MainNav from "./Home/MainNav";
  import MainCarousel from "./Home/MainCarousel";
    export default {
      name: "MainPage",
      components: {
        banner_top,
        MainNav,
        MainCarousel
      },
    }
</script>

<style scoped>

</style>
