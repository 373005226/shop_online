<template>
  <div>
    <my-header></my-header>
    <goods></goods>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import Goods from "../common/Goods";
  export default {
    name: "catelogy",
    components: {Goods, MyFooter, MyHeader}
  }
</script>

<style scoped>

</style>
