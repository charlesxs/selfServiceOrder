// export default {
//   name: 'Index',
//   // eslint-disable-next-line no-unused-vars
//   render(h) {
//     return (
//       <div style="text-align: center; line-height: 50px; vertical-align: center">
//         <h1>入口页</h1>
//         <Divider />
//         <h2 vOn:click={(e) => {
//           this.$router.push('/menu')
//         }}>查看菜单</h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/edit_menu')
//           }
//         }>
//           编辑菜单
//         </h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/order')
//           }
//         }>
//           查看订单
//         </h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/edit_order')
//           }
//         }>
//           修改订单
//         </h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/statistics/cashflow')
//           }
//         }>
//           每月流水统计
//         </h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/statistics/hotfood')
//           }
//         }>
//           热门食物统计
//         </h2>
//
//         <h2 vOn:click={
//           // eslint-disable-next-line no-unused-vars
//           e => {
//             this.$router.push('/employee')
//           }
//         }>
//           员工管理
//         </h2>
//       </div>
//     )
//   }
// };


import routers from '../router';

export default {
  name: 'Index',
  // eslint-disable-next-line no-unused-vars
  render(h) {
    const vNodes = [];

    return (
      <div style="text-align: center; line-height: 50px; vertical-align: center">
        <h1>入口页</h1>
        <Divider />

        {
          routers.map(r => {
            return (
              <h2 vOn:click={() => {this.$router.push(r.path)}}>
                {r.meta ? r.meta.visible : ''}
              </h2>
            );
          })
        }

       {...vNodes}    /** 这段代码没有用, 只是特殊示例. 在vue中这样写不会报错，但是react中不行, 正常也不应该这样写, JSX可以直接渲染 数组形式的component **/
      </div>
    )
  }
}
