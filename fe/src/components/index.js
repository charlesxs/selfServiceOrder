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
    const vNodes = []
    // const vm = this

    return (
      <div style="text-align: center; line-height: 50px; vertical-align: center">
        <h1>入口页</h1>
        <Divider />

        {
          routers.forEach(r => {
            vNodes.push(
              <h2 vOn:click={() => {this.$router.push(r.path)}}>
                {r.meta ? r.meta.visible : ''}
              </h2>
            )
          })
        }

        {...vNodes}
      </div>
    )
  }
}
