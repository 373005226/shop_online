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
        name: "Order",
      components: {MyFooter, MyHeader}
    }
</script>

<style scoped>

</style>
