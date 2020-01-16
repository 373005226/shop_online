<template>
  <div>
    <my-header></my-header>

    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
    export default {
      name: "detail",
      components:{
        MyHeader,
        MyFooter
      }
    }
</script>

<style scoped>

</style>
