import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: () => import('../views/layout/Main.vue'),
      children: [
        {
          path: 'Dashboard',
          name: 'dashboard',
          component: () => import('./../views/Dashboard.vue')
        },
        // Employee fillon ktu---------------
        {
          path: 'Employee',
          name: 'Employee',
          component: () => import('../views/Employee/Employee.vue')
        },
        {
          path: 'Employee/NewEmployee',
          name: 'NewEmployee',
          component: () => import('../views/Employee/NewEmployee.vue')
        },
        {
          path: 'Employee/ViewEmployee',
          name: 'ViewEmployee',
          component: () => import('../views/Employee/ViewEmployee.vue')
        },
        {
          path: 'Employee/EditEmployee',
          name: 'EditEmployee',
          component: () => import('../views/Employee/EditEmployee.vue')
        },
        // Companies fillon ktu---------------
        {
          path: 'Companies',
          name: 'Companies',
          component: () => import('../views/Companies/Companies.vue')
        },
        {
          path: 'Companies/NewCompany',
          name: 'NewCompany',
          component: () => import('../views/Companies/NewCompany.vue')
        },
        {
          path: 'Companies/:id',
          name: 'ViewCompany',
          component: () => import('../views/Companies/ViewCompany.vue')
        },
        {
          path: 'Companies/Edit/:id',
          name: 'EditCompany',
          component: () => import('../views/Companies/EditCompany.vue')
        },
      ]
    }
  ]
})

export default router
