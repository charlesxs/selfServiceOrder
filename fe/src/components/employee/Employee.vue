<template>
    <div style="margin-top: 15px">
        <Modal v-model="modal"
               title="编辑员工信息"
               @on-ok="editEmployee"
               @on-cancel="employee = {}">
            <Row class="mm">
                <span style="margin-right: 10px">用户名: </span>
                <Input v-model="employee.username"
                       placeholder="请输入用户名"
                       style="width: 220px; margin-left: 10px" disabled/>
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">姓名: </span>
                <Input v-model="employee.realName"
                       type="textarea"
                       :autosize="{minRows: 2,maxRows: 5}"
                       style="width: 220px; margin-left: 10px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">性别: </span>
                <Input v-model="employee.gender"
                       placeholder="请输入性别"
                       style="width: 220px; margin-left: 10px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">职位: </span>
                <Input v-model="employee.type"
                       placeholder="请输入职位"
                       style="width: 220px; margin-left: 10px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">手机号: </span>
                <Input v-model="employee.mobile"
                       placeholder="请输入手机号"
                       style="width: 220px; margin-left: 10px" />
            </Row>

            <Row class="mm">
                <span style="margin-right: 10px">邮箱: </span>
                <Input v-model="employee.mail"
                       placeholder="请输入邮箱"
                       style="width: 220px; margin-left: 10px" />
            </Row>
        </Modal>

        <Modal v-model="deleteModal"
               title="删除提醒"
               @on-ok="deleteEmployee"
               @on-cancel="employee = {}">
            <p>确定要删除此员工吗？</p>
        </Modal>

        <div class="menu-box">
            <span style="font-size: 17px;">员工管理</span>
            <span style="width: 300px">
                <Input search enter-button="搜索"
                       placeholder="请输入员工姓名"
                       id="searchEmployee"
                       @on-search="searchEmployee"
                />
            </span>
        </div>
        <Divider />

        <Table :columns="tabColumns" :data="tabData"></Table>
    </div>
</template>

<script>
  import _ from 'lodash'
  export default {
    name: "Employee",
    data() {
      let vm = this
      return {
        modal: false,
        deleteModal: false,
        employee: {},
        tabColumns: [
          {title: 'ID', key: 'id', width: 50},
          {title: '用户名', key: 'username'},
          {title: '姓名', key: 'realName'},
          {title: '性别', key: 'gender'},
          {title: '职位', key: 'type'},
          {title: '手机号', key: 'mobile', width: 130},
          {title: '邮箱', key: 'mail', width: 200},
          {
            title: '操作',
            key: 'action',
            width: 200,
            render(h, params) {
              return h('div', [
                // h('Button', {
                //   props: {type: 'primary', size: 'small'},
                //   style: {marginRight: '5px'},
                //   on: {click: () => {console.log('detail', params)}}
                // }, '详情'),

                h('Button', {
                  props: {type: 'success', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {
                    vm.employee = params.row
                    vm.modal = true
                  }}
                }, '编辑'),

                h('Button', {
                  props: {type: 'error', size: 'small'},
                  style: {marginRight: '5px'},
                  on: {click: () => {
                    vm.employee = params.row
                    vm.deleteModal = true
                  }}
                }, '删除')
              ])
            }
          },
        ],
        allData: [
          {id: 1, username: 'dachu.wang', realName: '王大厨', gender: '男', type: '厨师', mobile: '173****0136', mail: 'dachu.wang@126.com'},
          {id: 2, username: 'xiaoer.wang', realName: '王小二', gender: '男', type: '服务员', mobile: '173****1135', mail: 'xiaoer.wang@126.com'},
          {id: 3, username: 'die.yu', realName: '于碟', gender: '女', type: '服务员', mobile: '139****3333', mail: 'die.yu@126.com'},
          {id: 4, username: 'shuang.li', realName: '李爽', gender: '女', type: '收银员', mobile: '177****8888', mail: 'shuang.li@126.com'},
          {id: 5, username: 'qiang.li', realName: '李强', gender: '男', type: '经理', mobile: '136****6513', mail: 'qiang.li@126.com'}
        ],
        tabData: []
      }
    },
    methods: {
      editEmployee() {
      },
      deleteEmployee(){
        this.tabData = _.filter(this.tabData, item => {
          return item.id !== this.employee.id
        })
      },
      searchEmployee(val) {
        if (val === '') {
          this.tabData = this.allData
          return
        }

        let pat = new RegExp(val)
        this.tabData = _.filter(this.tabData, item => {
          return item.realName.match(pat)
        })
      }
    },
    mounted() {
      this.tabData = this.allData
    }
  }
</script>

<style scoped>
    .mm {
        margin: 10px 0 10px 0;
    }

</style>