<template>
    <div style="margin-top: 15px">
        <div class="menu-box">
            <span class="menu">编辑菜单</span>
            <span>
                <Button type="success"
                        size="small"
                        style="margin-right: 30px"
                        @click="openAdd"
                >添加菜品</Button>
            </span>
        </div>
        <Divider />

        <Modal v-model="modal"
               :title="modalInfo.title"
               @on-ok="modalInfo.onOk">
            <Row class="mm" style="margin-bottom: 30px">
                <Col span="2">图片: </Col>
                <Col span="22">
                    <div class="demo-upload-list" v-for="item in uploadList">
                        <template v-if="item.status === 'finished'">
                            <img :src="item.url">
                            <div class="demo-upload-list-cover">
                                <Icon type="ios-eye-outline" @click.native="handleView(item)"></Icon>
                                <Icon type="ios-trash-outline" @click.native="handleRemove(item)"></Icon>
                            </div>
                        </template>
                        <template v-else>
                            <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                        </template>
                    </div>

                    <Upload
                            ref="upload"
                            :default-file-list="defaultList"
                            :show-upload-list="false"
                            :on-success="handleSuccess"
                            :format="['jpg','jpeg','png']"
                            type="drag"
                            multiple
                            action="/upload_image"
                            style="display: inline-block; width:58px;">
                        <div style="width: 58px;height:58px;line-height: 58px; display: inline">
                            <Icon type="ios-camera" size="20"></Icon>
                        </div>
                    </Upload>
                    <Modal title="查看图片" v-model="viewImage">
                        <img :src="currentImage.url" v-if="viewImage" style="width: 100%">
                    </Modal>
                </Col>
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
                       type="number"
                       style="width: 220px" />
            </Row>
        </Modal>

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
        <!--这里套一个div, 是为了解决 v-for 不渲染的问题, 具体参考: https://blog.csdn.net/tearsknow/article/details/78412227 -->
        <div>
            <div v-for="food in foods" :key="food.id">
                <Row :gutter=6>
                    <Col span="7"><img :src="food.imagePath" alt="" style="width: 220px; height: 125px"></Col>
                    <Col span="14" style="font-size: 14px">
                        <Row style="margin-bottom: 10px">菜名: {{ food.name }}</Row>
                        <Row style="margin-bottom: 10px">介绍: {{ food.intro }}</Row>
                        <Row style="margin-bottom: 10px">价格: {{ food.price }}</Row>
                        <Row>
                            <Button type="primary" disabled>
                                添加购物车
                            </Button>
                        </Row>

                    </Col>
                    <Col span="3" style="font-size: 20px; cursor: pointer">
                        <Icon @click.native="openEdit(food)" type="ios-create-outline" />
                        <Icon @click.native="openDelete(food)" style="color: red" type="ios-trash-outline" />
                    </Col>
                </Row>
                <Divider />
            </div>
        </div>

        <Modal
                v-model="deleteModal"
                title="删除提醒"
                @on-ok="deleteMenu">
            <p>确定要删除此菜品吗？</p>
        </Modal>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "EditMenu",
    data() {
      return {
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
        foods: [
          // {
          //   id: 1,
          //   imagePath: require('../../assets/yutoupaobing.jpg'),
          //   name: '鱼头泡饼',
          //   intro: '俺家鱼头泡饼很好吃',
          //   price: 30,
          //   added: false
          // },
          // {
          //   id: 2,
          //   imagePath: require('../../assets/malaxiangguo.jpg'),
          //   name: '麻辣香锅',
          //   intro: '麻辣香锅很辣',
          //   price: 18,
          //   added: false
          // },
          // {
          //   id: 3,
          //   imagePath: require('../../assets/wuhankaoquanyu.jpg'),
          //   name: '巫山烤全鱼',
          //   intro: '巫山烤全鱼',
          //   price: 40,
          //   added: false
          // }
        ],

        deleteModal: false,
        uploadList: [],
        viewImage: false,
        currentImage: '',
        modalInfo: {
          title: '',
          onOk: () => 'OK'
        },
        currentFood: {},
        modal: false,
        defaultList: []
      }
    },
    methods: {
      handleRemove(file) {
        const fileList = this.$refs.upload.fileList;
        this.$refs.upload.fileList.splice(fileList.indexOf(file), 1);

        // 删除服务器上图片
        let payload = {
          'data': {
            'filename': file.name
          }
        }
        axios.post('/delete_image', payload)
          .catch(e => {
            this.$Message.error(`图片删除失败: ${e}`)
          })
      },

      handleView (item) {
        this.currentImage = item;
        this.viewImage = true;
      },

      handleSuccess(response, file) {
        file.url = response.data.filename
        file.name = response.data.filename.split('/').slice(-1)[0]

        this.currentFood.imagePath = response.data.filename
      },

      selectCategory(category) {
        /* eslint-disable */
        category.active = true
        this.selectedCategory.push(category.content)
      },

      openAdd() {
        // 清空 file list
        const fileList = this.$refs.upload.fileList;
        this.$refs.upload.fileList.splice(0, fileList.length);

        this.modal = true
        this.currentFood = {}
        this.modalInfo.title = '添加食物'
        this.modalInfo.onOk = this.addMenu
      },

      openEdit(food) {
        // 动态赋值 defaultList
        this.defaultList = [{
          name: food.imagePath.split('/').slice(-1)[0],
          url: food.imagePath
        }]

        // 解决 default-file-list 动态赋值不显示的问题
        this.$nextTick(()=> { //赋值后马上更新
          this.uploadList = this.$refs.upload.fileList;
        });

        this.modal = true
        this.currentFood = food
        this.modalInfo.title = '编辑食物'
        this.modalInfo.onOk = this.editMenu
      },

      openDelete(food) {
        this.deleteModal = true
        this.currentFood = food
      },

      editMenu() {
        this.modal = false;

        let payload = {
          data: [{
            action: 'update',
            ...this.currentFood
          }]
        }
        axios.post('/edit_menu', payload)
          .then(r => {
            this.$Message.success('菜单编辑成功')
          })
          .catch(e => {
            this.$Message.error(`菜单编辑失败: ${e}`)
          })
      },

      deleteMenu() {
        this.deleteModal = false;

        let payload = {
          data: [{
            action: 'delete',
            ...this.currentFood
          }]
        }
        axios.post('/edit_menu', payload)
          .then(r => {
            this.$Message.success('删除成功')

            this.foods = _.filter(this.foods, item => {
              return item.id !== this.currentFood.id
            })
          })
          .catch(e => {
            this.$Message.error(`删除失败: ${e}`)
          })
      },
      addMenu() {
        this.modal = false

        let payload = {
          data: [{
            action: 'add',
            ...this.currentFood
          }]
        }

        axios.post('/edit_menu', payload)
          .then(r => {
            this.$Message.success('菜单添加成功')
            this.foods.push(this.currentFood)
          })
          .catch(e => {
            this.$Message.error(`菜单添加失败: ${e}`)
          })
      }
    },
    mounted() {
      this.uploadList = this.$refs.upload.fileList

      axios.get('/menu')
        .then(resp => {
          this.foods = _.orderBy(resp.data.data, ['id'], ['asc'])
        })
        .catch(err => {
          this.$Message.error(`菜单加载失败: ${err}`)
        })
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

    .demo-upload-list{
        display: inline-block;
        width: 60px;
        height: 60px;
        text-align: center;
        line-height: 60px;
        border: 1px solid transparent;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        position: relative;
        box-shadow: 0 1px 1px rgba(0,0,0,.2);
        margin-right: 4px;
    }
    .demo-upload-list img{
        width: 100%;
        height: 100%;
    }
    .demo-upload-list-cover{
        display: none;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0,0,0,.6);
    }
    .demo-upload-list:hover .demo-upload-list-cover{
        display: block;
    }
    .demo-upload-list-cover i{
        color: #fff;
        font-size: 20px;
        cursor: pointer;
        margin: 0 2px;
    }

</style>