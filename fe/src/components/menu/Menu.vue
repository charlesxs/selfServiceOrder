<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span class="menu">菜单</span>
            <Badge :count=cartNum @click.native="drawer = true" style="cursor: pointer">
                <img src="../../assets/shopping.png" alt="" class="image">
            </Badge>

            <Drawer title="购物车详情" :closable="false" v-model="drawer">
                <ul style="margin-left: 20px; font-size: 13px">
                    <li v-for="f in shoppingCart" :key="f.id">
                        {{ f.name }} ￥{{ f.price }}
                    </li>
                </ul>

                <Row
                    style="margin-top: 30px">总计: {{ amount }}</Row>
                <Button
                    style="margin-top: 10px"
                    type="primary"
                    @click="goMyOrder">
                    下订单
                </Button>
            </Drawer>
        </div>

        <Modal
                v-model="modal1"
                title="订单提醒">
            <p>您的订单已经生成，请耐心等待片刻，精致美味马上就好。</p>
        </Modal>
        <Divider />

        <!-- 分类-->
        <div style="font-size: 14px; cursor: pointer">
            <Row v-for="(cs, idx) in categorys" :key="idx" style="margin-top: 5px;">
                <Col span="5" v-if="idx === 0"> {{cs[0]}} </Col>
                <Col span="5" v-else>&nbsp</Col>

                <Col span="3" v-for="(c, i) in cs.slice(1)"
                     :key="i"
                     :class="{suggest: c.active}"
                     @click.native="selectCategory(c)">
                    <a href="#/menu">{{ c.content }} </a>
                </Col>
            </Row>
        </div>
        <Divider />

        <!--菜品详情-->
        <div v-for="(food, i) in foods" :key="i">
            <Row :gutter=6>
                <Col span="7"><img :src="food.imagePath" alt="" style="width: 220px; height: 125px"></Col>
                <Col span="14" style="font-size: 14px">
                    <Row style="margin-bottom: 10px">菜名: {{ food.name }}</Row>
                    <Row style="margin-bottom: 10px">介绍: {{ food.intro }}</Row>
                    <Row style="margin-bottom: 10px">价格: {{ food.price }}</Row>
                    <Row>
                        <Button
                            type="primary"
                            @click="addCart(food)"
                            v-if="!food.added">
                            添加购物车
                        </Button>
                        <Button
                            style="background-color: #9c9c9c; color: #f8f8f9;"
                            v-else
                            @click="delCart(food)">
                            已添加购物车
                        </Button>
                    </Row>
                </Col>
            </Row>
            <Divider />
        </div>
    </div>
</template>

<script>
  import uuidv4 from 'uuid/v4'
  import axios from 'axios'
  import _ from 'lodash'

  export default {
    name: "Menu",
    data() {
      return {
        cartNum: 0,
        drawer: false,
        modal1: !!this.$route.query.pay,
        categorys: [
          ['分类',
            {content: '蛋糕', active: false},
            {content: '火锅', active: false},
            {content: '自助餐', active: false},
            {content: '小吃快餐', active: false},
            {content: '日韩料理', active: false},
            {content: '汤/粥/炖菜', active: false}],
          ['',
            {content: '西餐', active: false},
            {content: '东北菜', active: false},
            {content: '川湘菜', active: false},
            {content: '聚餐宴请', active: false},
            {content: '烧烤烤肉', active: false},
            {content: '江浙菜', active: false}],
          ['',
            {content: '粤菜', active: false},
            {content: '海鲜', active: false},
            {content: '素食', active: false},
            {content: '中式烤吧', active: false},
            {content: '西北菜', active: false},
            {content: '新疆菜', active: false}]
        ],
        selectedCategory: [],
        shoppingCart: [],
        foods: [],
        amount: 0
      }
    },
    methods: {
      selectCategory(category) {
        /* eslint-disable */
         category.active = true
         this.selectedCategory.push(category.content)
      },
      addCart(food) {
        this.shoppingCart.push(food)
        this.cartNum++
        food.added = true
        this.amount += food.price
      },
      delCart(food) {
        this.shoppingCart = this.shoppingCart.filter(v => {
          return v.id !== food.id;
        })

        this.cartNum--
        food.added = false
        this.amount -= food.price
      },
      goMyOrder() {
        let order = {
          id: uuidv4(),
          amount: this.amount,
          payment: '未支付',
          createTime: (new Date().toISOString()).replace('T', ' ').replace(/\.[0-9]+Z$/, ''),
          detail: this.shoppingCart,
          username: 'xiaoshuang'
        }

        this.$store.commit('pushOrder', order)
        this.$router.push({path: '/order'})
      }
    },
    mounted() {
      axios.get('/menu')
        .then(resp => {
          let foods = _.orderBy(resp.data.data, ['id'], ['asc'])
          this.foods.push(...foods)
        })
        .catch(err => {
          this.$Message.error(`菜单加载失败: ${err}`)
        })
    }
  }
</script>

<style>
  .image {
      width: 25px;
      height: 25px;
  }

  .menu-box {
      display: flex;
      padding: 0 5px 0 5px;

      justify-content: space-between;
  }
  .menu {
      font-size: 17px;
  }

  .suggest {
      background-color: #13D1BE;
      border-radius: 100px;
      color: #fff!important;
  }

  a:hover {
      color: #2b85e4 !important;
  }

    a {
        color: #666!important;
    }

    h2:hover {
        color: #2b85e4 !important;
    }

    h2 {
        color: #666!important;
        cursor: pointer;
    }

</style>