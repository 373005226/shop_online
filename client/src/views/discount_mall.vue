<template>
  <div>
    <my-header></my-header>
    <Banner_top></Banner_top>

    <my-footer></my-footer>
  </div>
</template>

<script>
    import MyHeader from "../common/header/MyHeader";
    import Banner_top from "../components/Home/banner_top";
    import MyFooter from "../common/footer/MyFooter";
    export default {
        name: "discount_mall",
      components: {MyFooter, Banner_top, MyHeader}
    }
</script>

<style scoped>

</style>
