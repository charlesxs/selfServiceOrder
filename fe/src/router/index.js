// router

import Index from '@/components/index.js';
import Menu from '@/components/menu';
import { EditMenu } from '@/components/menu';
import { Order, EditOrder } from '@/components/order';
import { CashFlow, HotFood } from '@/components/statistics';
import Employee from "@/components/employee";

const routers = [
  {
    // 通配符匹配，* 会匹配所有路径, order-* 会匹配以order开头的路由
    path: '*',
    component: Index
  },
  {
    path: '/menu',
    component: Menu,
    meta: {
      visible: '查看菜单'
    }
  },
  {
    path: '/edit_menu',
    component: EditMenu,
    meta: {
      visible: '编辑菜单'
    }
  },
  {
    path: '/order',
    component: Order,
    meta: {
      visible: '查看订单'
    }
  },
  {
    path: '/edit_order',
    component: EditOrder,
    meta: {
      visible: '修改订单'
    }
  },
  {
    path: '/statistics/cashflow',
    component: CashFlow,
    meta: {
      visible: '每月流水'
    }
  },
  {
    path: '/statistics/hotfood',
    component: HotFood,
    meta: {
      visible: '热门食物'
    }
  },
  {
    path: '/employee',
    component: Employee,
    meta: {
      visible: '员工管理'
    }
  }
];


export default routers;