<template>
    <div>
      <my-header></my-header>
      <search_foot></search_foot>

      <searchgoods style="padding-bottom: 20px;"></searchgoods>

      <my-footer></my-footer>
    </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import search_foot from "../components/search/search_foot";
  import searchgoods from "../common/searchgoods";
  export default {
    name: "search",
    components: {searchgoods, search_foot, MyFooter, MyHeader}
  }
</script>

<style scoped>

</style>
