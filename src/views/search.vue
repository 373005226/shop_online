<template>
    <div>
      <my-header></my-header>
      <search_foot></search_foot>

      <goods style="padding-bottom: 20px;"></goods>


      <my-footer></my-footer>
    </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import search_foot from "../components/search/search_foot";
  import Goods from "../common/Goods";
  export default {
    name: "search",
    components: {Goods, search_foot, MyFooter, MyHeader}
  }
</script>

<style scoped>

</style>
