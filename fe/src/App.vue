<template>
  <div id="app" class="container">

    <div class="header">
      欢迎使用自助点餐系统
    </div>

    <div id="body">
      <router-view></router-view>
    </div>

    <div id="footer"></div>
  </div>
</template>

<script>

export default {
  name: 'app'
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  .header {
    background-color: #f8f8f9;
    text-align: center;
    font-size: large;
    vertical-align: middle;
    line-height: 50px;

    margin-bottom: 10px;
  }

  .container {
    margin: 0 10% 0 10%;
  }

  .ivu-layout-header {
  }
</style>
