<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span class="menu">编辑菜单</span>
            <span>
                <Button type="success" size="small" style="margin-right: 30px">添加菜品</Button>
                <Button type="info" size="small">编辑分类</Button>
            </span>
        </div>
        <Divider />

        <!-- 分类-->
        <div style="font-size: 14px; cursor: pointer;">
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
                <Col span="7"><img :src="food.imagePath" alt=""></Col>
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
                <Col span="3" style="font-size: 20px; cursor: pointer">
                    <Icon @click.native="openEditModal(food)" type="ios-create-outline" />
                    <Icon style="color: red" type="ios-trash-outline" />
                </Col>
            </Row>
            <Divider />
        </div>

        <Modal
            v-model="modal"
            title="编辑食物"
            @on-ok="editMenu">
            <Row class="mm" style="margin-bottom: 30px">
                <span style="margin-right: 10px">图片: </span>
                <img :src="currentFood.imagePath" alt="">
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">菜名: </span>
                <Input v-model="currentFood.name"
                       placeholder="请输入菜名"
                       style="width: 220px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">介绍: </span>
                <Input v-model="currentFood.intro"
                       type="textarea"
                       :autosize="{minRows: 2,maxRows: 5}"
                       placeholder="菜品介绍"
                       style="width: 220px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">价格: </span>
                <Input v-model="currentFood.price"
                       placeholder="请输入价格"
                       style="width: 220px" />
            </Row>
        </Modal>
    </div>
</template>

<script>
  export default {
    name: "EditMenu",
    data() {
      return {
        modal: false,
        cartNum: 0,
        drawer: false,
        currentFood: {},
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
        foods: [
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
          },
          {
            id: 4,
            imagePath: require('../../assets/yutoupaobing.jpg'),
            name: '鱼头泡饼',
            intro: '鱼头泡饼很好吃，哈哈哈',
            price: 30,
            added: false
          }
        ],
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
      processOrder() {
        // 处理订单
      },
      openEditModal(food) {
        this.modal = true
        this.currentFood = food
      },
      editMenu() {
        this.modal = false
      }
    }
  }
</script>

<style scoped>
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
        background-color: #13D1BE;
        border-radius: 100px;
        color: #fff!important;
    }

    a {
        color: #666!important;
    }

    .mm {
        margin: 10px 0 10px 0;
    }

</style>