<template>
    <div style="background-color: #f3f3f3; height: 700px">
        <Row class="content">
            <Col span="22" style="font-size: 15px">
                <Row>自助点餐系统收银台</Row>
                <Row style="font-size: 13px; margin-top: 5px">订单编号: {{ order.id }}</Row>
            </Col>
            <Col span="2" style="margin-top: 10px">
                <span style="font-size: 20px; color: #ef2b13; font-weight: bold;">{{ order.amount }}.00</span> 元
            </Col>
        </Row>

        <Card class="container">
            <div>
                <Row style="margin-left: 25%">请扫码支付（元）</Row>
                <Row style="margin-top: 10px">
                    <img src="../../assets/zhifu.png" alt="" style="height: 200px">
                </Row>
            </div>
        </Card>
    </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: "Payment",
    data() {
      return {
      }
    },
    computed: {
      ...mapState([
        'order'
      ])
    },
    mounted() {
      setTimeout(() => {
        this.$router.push({path: '/menu', query: {pay: 'true'}})
      }, 3000)
    }
  }
</script>

<style scoped>
    .content {
        margin: 0 5% 0 5%;
        padding-top: 20px;
    }
    .container {
        margin: 20px 5% 0 5%;
        display: flex;
        justify-content: center;
        height: 300px;
    }
</style>