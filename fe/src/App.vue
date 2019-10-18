<template>
  <div id="app" class="container">

    <div class="header">
      欢迎使用自助点餐系统

      <Dropdown style="float: right; margin: 0 -40px 0 0; color: #2b85e4; cursor: pointer;"
                @on-click="onClick"
                v-if="!isLogin"
                >
          <Icon type="md-person" size="20"/>
        <DropdownMenu slot="list">
          <DropdownItem name="order">我的订单</DropdownItem>
          <DropdownItem name="logout">退出登录</DropdownItem>
        </DropdownMenu>
      </Dropdown>

    </div>

    <div id="body">
      <router-view></router-view>
    </div>

    <div id="footer"></div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'app',
  data() {
    return {
      isLogin: false
    }
  },
  methods: {
    onClick (name) {
      if (name === 'logout') {
        axios
            .get('/logout')
            .then(r => {
              if (r.data.message !== 'success'){
                this.$Message.info(`${r.data.message}`)
              } else {
                this.$Message.success('已退出登录')
              }
            })
        return
      }

      this.$router.push({path: '/' + name, query: {type: 'myOrder'}})
    }
  },
  mounted() {
    let path = this.$route.path
    this.isLogin = path.match(/(login|^\/$)/);
  },
  watch: {
    '$route'()  {
      let path = this.$route.path
      this.isLogin = path.match(/(login|^\/$)/);
    }
  },
  // 导航守卫没生效
  // beforeRouteUpdate(to, from, next) {
  //   console.log(to, from)
  //   if (to.path.match(/login/) && to.path !== from.path) {
  //     this.isLogin = true
  //   } else {
  //     this.isLogin = false
  //   }
  //   next()
  // }
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
