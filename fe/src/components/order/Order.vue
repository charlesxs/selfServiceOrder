<template>
    <div style="margin-top: 15px">
        <h2>我的订单</h2>
        <Divider />

        <Row class="mm"
            :gutter="10"
            style="font-size: 14px">
            <Col span="2">订单ID: </Col>
            <Col>{{ order.id }}</Col>
        </Row>

        <Row class="mm"
             :gutter="10"
             style="font-size: 14px">
            <Col span="2">下单时间: </Col>
            <Col>{{ order.createTime }}</Col>
        </Row>

        <Row class="mm"
            :gutter="10"
            style="font-size: 14px">
            <Col span="2">订单金额: </Col>
            <Col>{{ order.amount }} 元</Col>
        </Row>
        <Row class="mm"
            :gutter="10"
            style="font-size: 14px">
            <Col span="2">支付状态: </Col>
            <Col :style="{color: payStateColor}">{{ order.payment }}</Col>
        </Row>

        <Divider />
        <Row
            :gutter="10"
            style="font-size: 14px">
            <Col span="2">订单详情: </Col>
            <Col span="22">
                <Row :gutter=16
                     v-for="food in order.detail"
                     :key="food.id">
                    <Col span="7"><img :src="food.imagePath" alt=""></Col>
                    <Col span="14" style="font-size: 14px;">
                        <Row style="margin-bottom: 10px">菜名: {{ food.name }}</Row>
                        <Row style="margin-bottom: 10px">介绍: {{ food.intro }}</Row>
                        <Row style="margin-bottom: 10px">价格: {{ food.price }}</Row>
                    </Col>
                    <Divider />
                </Row>
            </Col>
        </Row>
    </div>

</template>

<script>
  export default {
    name: "Order",
    data() {
      return {
        order: {
          id: '97b015b8-c08e-42bd-932f-9e147e53aa8d',
          amount: 88,
          payment: '未支付',
          createTime: '2019-08-25 12:03:00',
          detail: [
            {
              id: 1,
              imagePath: require('../../assets/yutoupaobing.jpg'),
              name: '鱼头泡饼',
              intro: '俺家鱼头泡饼很好吃',
              price: 30,
              added: false
            },
            {
              id: 2,
              imagePath: require('../../assets/malaxiangguo.jpg'),
              name: '麻辣香锅',
              intro: '麻辣香锅很辣',
              price: 18,
              added: false
            },
            {
              id: 3,
              imagePath: require('../../assets/wuhankaoquanyu.jpg'),
              name: '巫山烤全鱼',
              intro: '巫山烤全鱼',
              price: 40,
              added: false
            }
          ]
        }
      }
    },
    computed: {
      payStateColor() {
        if (this.order.payment === '已支付') {
          return 'green'
        }
        return 'red'
      }
    }
  }
</script>

<style scoped>
    .mm {
        margin: 10px 0 10px 0;
    }
</style>