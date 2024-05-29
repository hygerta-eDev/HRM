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
        // Departments fillon ktu---------------


        {
          path: 'Departments',
          name: 'Departments',
          component: () => import('../views/Departments/Departments.vue')
        },
        {
          path: 'Departments/NewDepartment',
          name: 'NewDepartment',
          component: () => import('../views/Departments/NewDepartment.vue')
        },
        {
          path: 'Departments/:id',
          name: 'ViewDepartment',
          component: () => import('../views/Departments/ViewDepartment.vue')
        },
        {
          path: 'Departments/Edit/:id',
          name: 'EditDepartment',
          component: () => import('../views/Departments/EditDepartment.vue')
        },
        // JobPosition fillon ktu---------------


        {
          path: 'JobPositions',
          name: 'JobPositions',
          component: () => import('../views/JobPositions/JobPositions.vue')
        },
        {
          path: 'JobPositions/NewJobPosition',
          name: 'NewJobPosition',
          component: () => import('../views/JobPositions/NewJobPosition.vue')
        },
        {
          path: 'JobPositions/:id',
          name: 'ViewJobPosition',
          component: () => import('../views/JobPositions/ViewJobPosition.vue')
        },
        {
          path: 'JobPositions/Edit/:id',
          name: 'EditJobPosition',
          component: () => import('../views/JobPositions/EditJobPosition.vue')
        },

        // {
        //   path: 'JobPosition',
        //   name: 'JobPosition',
        //   component: () => import('../views/JobPosition/JobPosition.vue')
        // },
        // {
        //   path: 'JobPosition/NewJobPosition',
        //   name: 'NewJobPosition',
        //   component: () => import('../views/JobPosition/NewJobPosition.vue')
        // },
        // {
        //   path: 'JobPosition/:id',
        //   name: 'ViewJobPosition',
        //   component: () => import('../views/JobPosition/ViewJobPosition.vue')
        // },
        // {
        //   path: 'JobPosition/Edit/:id',
        //   name: 'EditJobPosition',
        //   component: () => import('../views/JobPosition/EditJobPosition.vue')
        // },
      ]
    }
  ]
})

export default router
