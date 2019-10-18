<template>
    <div class="login">
        <Row class="login-box">
            <Col span="10" offset="7">
                <Card :bordered="false">
                    <p style="font-size: 20px" slot="title">登录</p>
                    <Row style="margin-top: 20px">
                        <Col span="4">
                            <label for="username">用户名: </label>
                        </Col>
                        <Col span="18">
                            <Input id="username" placeholder="请输入用户名" v-model="username"/>
                        </Col>
                    </Row>

                    <Row style="margin-top: 30px">
                        <Col span="4">
                            <label for="password">密码: </label>
                        </Col>
                        <Col span="18">
                            <Input id="password"
                                   type="password"
                                   placeholder="请输入密码"
                                   v-model="password"
                                   @keydown.enter.native="login"
                            />
                        </Col>
                    </Row>

                    <Button type="primary"
                            style="width: 250px; margin-top: 30px; margin-left: 60px"
                            @click="login"
                    >
                        登录
                    </Button>
                </Card>
            </Col>
        </Row>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "LogIn",
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        if (!this.username || !this.password) {
          this.$Message.warning('缺少用户名或密码')
          return
        }

        axios.post('/login', {
          username: this.username,
          password: this.password
        })
          .then(r => {
            if (r.data.message !== 'success') {
              this.$Message.error(`登录失败: ${r.data.message}`)
            } else {
              this.$router.push({path: '/menu'})
            }
          })
          .catch(e => {
            this.$Message.error(`登录失败: ${e}`)
          })
      }
    }
  }
</script>

<style scoped>
    .login {
        background-image: url("../assets/login-bg.jpg");
        height: 800px;
        opacity: 0.9;
    }

    .login-box{
        padding-top: 200px;
    }
</style>