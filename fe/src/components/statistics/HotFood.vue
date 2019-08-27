<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span style="font-size: 17px;">热门食物统计</span>
            <span>
                选择月份:
                <Select v-model="selectedMonth" style="width:200px">
                    <Option v-for="item in months" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
            </span>
        </div>
        <Divider />

        <Row :gutter=16 style="font-size: 17px">
            <Col span="4">{{ selectedMonth}} 月份热门食物: </Col>
        </Row>
        <Divider />

        <div v-for="(food, i) in foods" :key="i">
            <Row :gutter=6>
                <Col span="7"><img :src="food.imagePath" alt=""></Col>
                <Col span="14" style="font-size: 14px">
                    <Row style="margin-bottom: 10px">菜名: {{ food.name }}</Row>
                    <Row style="margin-bottom: 10px">价格: {{ food.price }} 元</Row>
                    <Row style="margin-bottom: 10px">热度: <Rate :allow-half=true v-model="food.rate"/></Row>
                    <Row style="margin-bottom: 10px">被点次数: {{ food.count }} 次</Row>
                </Col>
            </Row>
            <Divider />
        </div>
    </div>
</template>

<script>
  export default {
    name: "HotFood",
    data() {
      return {
        selectedMonth: 8,
        months: [
          {value: 1, label: '1月份'},
          {value: 2, label: '2月份'},
          {value: 3, label: '3月份'},
          {value: 4, label: '4月份'},
          {value: 5, label: '5月份'},
          {value: 6, label: '6月份'},
          {value: 7, label: '7月份'},
          {value: 8, label: '8月份'},
          {value: 9, label: '9月份'},
          {value: 10, label: '10月份'},
          {value: 11, label: '11月份'},
          {value: 12, label: '12月份'}
        ],
        foods: [
          {
            id: 1,
            imagePath: require('../../assets/yutoupaobing.jpg'),
            name: '鱼头泡饼',
            price: 30,
            rate: 5,
            count: 300
          },
          {
            id: 2,
            imagePath: require('../../assets/malaxiangguo.jpg'),
            name: '麻辣香锅',
            price: 18,
            rate: 4.5,
            count: 230
          },
          {
            id: 3,
            imagePath: require('../../assets/wuhankaoquanyu.jpg'),
            name: '巫山烤全鱼',
            price: 40,
            rate: 4,
            count: 200
          },
          {
            id: 4,
            imagePath: require('../../assets/yutoupaobing.jpg'),
            name: '鱼头泡饼',
            price: 30,
            rate: 3,
            count: 100
          }
        ]
      }
    }
  }
</script>

<style scoped>

</style>