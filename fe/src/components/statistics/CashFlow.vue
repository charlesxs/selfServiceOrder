<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span style="font-size: 17px;">每月流水统计</span>
            <span>
                选择月份:
                <Select v-model="selectedMonth" style="width:200px">
                    <Option v-for="item in months" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
            </span>
        </div>
        <Divider />

        <Row :gutter=6 style="font-size: 17px">
            <Col span="3">{{ selectedMonth}} 月份总收入: </Col>
            <Col span="3">{{ amount }} 元 </Col>

            <Col span="2">总订单量: </Col>
            <Col span="3">{{ 3000 }}个 </Col>
        </Row>
        <Divider />

        <Row style="font-size: 14px">
            {{ selectedMonth }}月份订单列表:
        </Row>

        <Table :columns="tabColumns" :data="tabData"></Table>
    </div>
</template>

<script>
  export default {
    name: "CashFlow",
    data() {
      return {
        selectedMonth: 8,
        amount: 23000,
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

        tabColumns: [
          {title: '客户姓名', key: 'username', width: 100},
          {title: '订单ID', key: 'oid', width: 300},
          {title: '创建时间', key: 'createTime', width: 200},
          {title: '订单金额', key: 'amount'},
          {title: '订单状态', key: 'state'},
          {
            title: '操作',
            key: 'action',
            width: 150,
            render(h, params) {
              return h('div', [
                h('Button', {
                  props: {type: 'primary', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {this.show(params.index)}}
                }, '查看订单详情')
              ])
            }
          },
        ],
        tabData: [
          {username: '张三', oid: '97b015b8-c08e-42bd-932f-9e147e53aa8d', createTime: '2019-08-25 12:03:00', amount: 88, state: '已支付'},
          {username: '王磊', oid: '72159392-6512-493b-a769-2ab582e7135a', createTime: '2019-08-25 12:30:20', amount: 188, state: '已支付'},
          {username: '李四', oid: '0e42f864-0eac-4347-9f46-2b9c5b204485', createTime: '2019-08-25 13:01:22', amount: 99, state: '已支付'},
          {username: '王峰', oid: '02e43c87-78bd-404c-bdcf-0b16e44aa79b', createTime: '2019-08-25 11:13:00', amount: 399, state: '已支付'},
          {username: '明磊', oid: '14b58d53-3027-4b0f-a4da-1b1c2482f2bf', createTime: '2019-08-25 12:01:00', amount: 838, state: '已支付'},
          {username: '张强', oid: '24d6be55-6fe8-46d2-9af8-8cdfa01f252a', createTime: '2019-08-25 12:02:00', amount: 100, state: '已支付'},
          {username: '王哲', oid: 'b7e7b9e4-1c84-4e5d-8722-730888299304', createTime: '2019-08-25 12:10:00', amount: 60, state: '已支付'},
          {username: '李峰', oid: '0b9f16a3-848f-46e9-a2a0-bdd0a0252592', createTime: '2019-08-25 12:23:00', amount: 30, state: '已支付'},
          {username: '李强', oid: '500c35e3-b678-4e8c-95d6-be9dbe5241e8', createTime: '2019-08-25 12:43:00', amount: 199, state: '已支付'},
          {username: '黎明', oid: '2b7d7134-0a21-4050-babe-6c952fedc991', createTime: '2019-08-25 12:43:00', amount: 299, state: '已支付'},
          {username: '王宝强', oid: '2d92679c-6563-43f8-9d4c-15999fba7637', createTime: '2019-08-25 12:33:00', amount: 399, state: '已支付'},
          {username: '古天乐', oid: '4f61ca18-7495-40fe-bdf4-4c8d912617e0', createTime: '2019-08-25 12:03:00', amount: 298, state: '已支付'},
          {username: '刘德华', oid: '90c9c5ed-a5fd-45c4-9f76-baa8af14c75a', createTime: '2019-08-25 12:03:00', amount: 188, state: '已支付'},
          {username: '任达华', oid: '11a7914a-28df-44fc-8bbe-084c32962683', createTime: '2019-08-25 12:03:00', amount: 858, state: '已支付'}
        ]
      }
    }
  }
</script>

<style scoped>
    .menu-box {
        display: flex;
        padding: 0 5px 0 5px;

        justify-content: space-between;
    }
</style>