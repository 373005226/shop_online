<template>
    <div>
      <my-header></my-header>
      <Banner_top></Banner_top>
      <div>
        <integral_mall></integral_mall>
      </div>
      <my-footer></my-footer>
    </div>
</template>

<script>
    import MyHeader from "../common/header/MyHeader";
    import MyFooter from "../common/footer/MyFooter";
    import Banner_top from "../components/Home/banner_top";
    import integral_mall from '../common/integral_goods'
    export default {
        name: "Integral_mall",
      components: {Banner_top, MyFooter, MyHeader,integral_mall}
    }
</script>

<style scoped>

</style>
