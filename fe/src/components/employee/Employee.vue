<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span style="font-size: 17px;">员工管理</span>
            <span style="width: 300px">
                <Input :search="true" enter-button="搜索" placeholder="请输入员工姓名" id="searchEmployee" />
            </span>
        </div>
        <Divider />

        <Table :columns="tabColumns" :data="tabData"></Table>
    </div>
</template>

<script>
  export default {
    name: "Employee",
    data() {
      return {
        tabColumns: [
          {title: 'ID', key: 'id'},
          {title: '用户名', key: 'username'},
          {title: '姓名', key: 'realName'},
          {title: '性别', key: 'gender'},
          {title: '职位', key: 'type'},
          {title: '手机号', key: 'mobile'},
          {title: '邮箱', key: 'mail', width: 200},
          {
            title: '操作',
            key: 'action',
            width: 200,
            render(h, params) {
              return h('div', [
                h('Button', {
                  props: {type: 'primary', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {console.log('detail', params)}}
                }, '详情'),

                h('Button', {
                  props: {type: 'success', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {console.log('edit', params)}}
                }, '编辑'),

                h('Button', {
                  props: {type: 'error', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {console.log('delete', params)}}
                }, '删除')
              ])
            }
          },
        ],

        tabData: [
          {id: 1, username: 'dachu.wang', realName: '王大厨', gender: '男', type: '厨师', mobile: '173****0136', mail: 'dachu.wang@126.com'},
          {id: 2, username: 'xiaoer.wang', realName: '王小二', gender: '男', type: '服务员', mobile: '173****1135', mail: 'xiaoer.wang@126.com'},
          {id: 3, username: 'die.yu', realName: '于碟', gender: '女', type: '服务员', mobile: '139****3333', mail: 'die.yu@126.com'},
          {id: 4, username: 'shuang.li', realName: '李爽', gender: '女', type: '收银员', mobile: '177****8888', mail: 'shuang.li@126.com'},
          {id: 5, username: 'qiang.li', realName: '李强', gender: '男', type: '经理', mobile: '136****6513', mail: 'qiang.li@126.com'}
        ]
      }
    }
  }
</script>

<style scoped>

</style>