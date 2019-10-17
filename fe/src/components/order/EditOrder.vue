<template>
    <div style="margin-top: 15px">
        <h2>修改订单</h2>
        <Divider />

        <Collapse v-model="defaultCollapse">
            <Panel v-for="(order, i) in orders" :key="i">
                <span style="margin-right: 15px">客户姓名: {{ order.username }}</span>
                <span style="margin-right: 15px">订单ID: {{ order.id }}</span>
                <span style="margin-right: 15px">创建时间: {{ order.createTime }}</span>
                <div slot="content">
                    <Row class="mm"
                         :gutter="10"
                         style="font-size: 14px">
                        <Col span="2">订单ID: </Col>
                        <Col span="17">{{ order.id }}</Col>

                        <Col span="5">
                            <Button size="small" type="success" @click="editOrder(order)">确认修改</Button>
                        </Col>
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
                        <Col>
                            <Input v-model="order.amount" style="width: 50px; margin-top: -3px" /> 元
                        </Col>
                    </Row>
                    <Row class="mm"
                         :gutter="10"
                         style="font-size: 14px">
                        <Col span="2">支付状态: </Col>
                        <Col>
                            <Select v-model="order.payment" size="small" style="width:100px" :style="{color: payStateColor(order.payment)}">
                                <Option v-for="item in payState" :value="item" :key="item">{{ item }}</Option>
                            </Select>
                        </Col>
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
                                <Col span="10" style="font-size: 14px;">
                                    <Row style="margin-bottom: 10px">菜名: {{ food.name }}</Row>
                                    <Row style="margin-bottom: 10px">介绍: {{ food.intro }}</Row>
                                    <Row style="margin-bottom: 10px">价格: {{ food.price }}</Row>
                                </Col>

                                <Col span="3" style="font-size: 20px; cursor: pointer">
                                    <Icon style="color: red" type="ios-trash-outline" @click="deleteFood(order, food)" />
                                </Col>
                                <Divider />
                            </Row>
                        </Col>
                    </Row>
                </div>
            </Panel>
        </Collapse>
    </div>

</template>

<script>
  import axios from 'axios'
  import _ from 'lodash'

  export default {
    name: "EditOrder",
    data() {
      return {
        defaultCollapse: '0',
        payState: ['未支付', '已支付'],
        orders: [
          // {
          //   username: '张三',
          //   id: '97b015b8-c08e-42bd-932f-9e147e53aa8d',
          //   amount: 88,
          //   payment: '未支付',
          //   createTime: '2019-08-25 12:03:00',
          //   detail: [
          //     {
          //       id: 1,
          //       imagePath: require('../../assets/yutoupaobing.jpg'),
          //       name: '鱼头泡饼',
          //       intro: '俺家鱼头泡饼很好吃',
          //       price: 30,
          //       added: false
          //     },
          //     {
          //       id: 2,
          //       imagePath: require('../../assets/malaxiangguo.jpg'),
          //       name: '麻辣香锅',
          //       intro: '麻辣香锅很辣',
          //       price: 18,
          //       added: false
          //     },
          //     {
          //       id: 3,
          //       imagePath: require('../../assets/wuhankaoquanyu.jpg'),
          //       name: '巫山烤全鱼',
          //       intro: '巫山烤全鱼',
          //       price: 40,
          //       added: false
          //     }
          //   ]
          // },
          // {
          //   username: '李四',
          //   id: '88c015b8-c08e-42bd-932f-9e147e53aa2d',
          //   amount: 88,
          //   payment: '已支付',
          //   createTime: '2019-08-25 11:30:00',
          //   detail: [
          //     {
          //       id: 1,
          //       imagePath: require('../../assets/yutoupaobing.jpg'),
          //       name: '鱼头泡饼',
          //       intro: '俺家鱼头泡饼很好吃',
          //       price: 30,
          //       added: false
          //     },
          //     {
          //       id: 2,
          //       imagePath: require('../../assets/malaxiangguo.jpg'),
          //       name: '麻辣香锅',
          //       intro: '麻辣香锅很辣',
          //       price: 18,
          //       added: false
          //     },
          //     {
          //       id: 3,
          //       imagePath: require('../../assets/wuhankaoquanyu.jpg'),
          //       name: '巫山烤全鱼',
          //       intro: '巫山烤全鱼',
          //       price: 40,
          //       added: false
          //     }
          //   ]
          // }
        ]
      }
    },
    methods: {
      payStateColor(payment) {
        if (payment === '已支付') {
          return 'green'
        }
        return 'red'
      },
      editOrder(order) {
        axios.post('/edit_order',
          {'data': order})
          .then(resp => {
            this.$Message.success('订单修改成功')
          })
          .catch(err => {
            this.$Message.error(`订单修改失败: ${err}`)
          })
      },
      deleteFood(order, food) {
        order.detail = _.filter(order.detail, item => {
          return item.id !== food.id
        })

        order.amount = _.sumBy(order.detail, item => {
          return item.price
        })
      }
    },
    mounted() {
        axios.get('/list_orders')
          .then(resp => {
            this.orders = resp.data.data
          })
          .catch(err => {
            this.$Message.error(`get orders error: ${err}`)
          })
    }
  }
</script>

<style scoped>
    .mm {
        margin: 10px 0 10px 0;
    }
</style>