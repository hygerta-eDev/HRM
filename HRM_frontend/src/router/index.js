// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// Define your routes
const routes = [
  {
    path: '/',
    name: 'main',
    component: () => import('../views/layout/Main.vue'),
    children: [
      {
        path: 'Dashboard',
        name: 'dashboard',
        component: () => import('./../views/Dashboard.vue'),
        meta: { requiresAuth: true }
      },
      // Employee routes
      {
        path: 'Employee',
        name: 'Employee',
        component: () => import('../views/Employee/Employee.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Employee/NewEmployee',
        name: 'NewEmployee',
        component: () => import('../views/Employee/NewEmployee.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Employee/ViewEmployee/:id',
        name: 'ViewEmployee',
        component: () => import('../views/Employee/ViewEmployee.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Employee/EditEmployee/:id',
        name: 'EditEmployee',
        component: () => import('../views/Employee/EditEmployee.vue'),
        meta: { requiresAuth: true }
      },
      // Companies routes
      {
        path: 'Companies',
        name: 'Companies',
        component: () => import('../views/Companies/Companies.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Companies/NewCompany',
        name: 'NewCompany',
        component: () => import('../views/Companies/NewCompany.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Companies/:id',
        name: 'ViewCompany',
        component: () => import('../views/Companies/ViewCompany.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Companies/Edit/:id',
        name: 'EditCompany',
        component: () => import('../views/Companies/EditCompany.vue'),
        meta: { requiresAuth: true }
      },
      // Departments routes
      {
        path: 'Departments',
        name: 'Departments',
        component: () => import('../views/Departments/Departments.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Departments/NewDepartment',
        name: 'NewDepartment',
        component: () => import('../views/Departments/NewDepartment.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Departments/:id',
        name: 'ViewDepartment',
        component: () => import('../views/Departments/ViewDepartment.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Departments/Edit/:id',
        name: 'EditDepartment',
        component: () => import('../views/Departments/EditDepartment.vue'),
        meta: { requiresAuth: true }
      },
      // JobPositions routes
      {
        path: 'JobPositions',
        name: 'JobPositions',
        component: () => import('../views/JobPositions/JobPositions.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'JobPositions/NewJobPosition',
        name: 'NewJobPosition',
        component: () => import('../views/JobPositions/NewJobPosition.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'JobPositions/:id',
        name: 'ViewJobPosition',
        component: () => import('../views/JobPositions/ViewJobPosition.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'JobPositions/Edit/:id',
        name: 'EditJobPosition',
        component: () => import('../views/JobPositions/EditJobPosition.vue'),
        meta: { requiresAuth: true }
      },
      // Qualifications routes
      {
        path: 'Qualifications',
        name: 'Qualifications',
        component: () => import('../views/Qualifications/Qualifications.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Qualifications/NewQualifications',
        name: 'NewQualifications',
        component: () => import('../views/Qualifications/NewQualifications.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Qualifications/:id',
        name: 'ViewQualifications',
        component: () => import('../views/Qualifications/ViewQualifications.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Qualifications/Edit/:id',
        name: 'EditQualifications',
        component: () => import('../views/Qualifications/EditQualifications.vue'),
        meta: { requiresAuth: true }
      },
      // Ethnicities routes
      {
        path: 'Ethnicities',
        name: 'Ethnicities',
        component: () => import('../views/Ethnicities/Ethnicities.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Ethnicities/NewEthnicity',
        name: 'NewEthnicity',
        component: () => import('../views/Ethnicities/NewEthnicity.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Ethnicities/:id',
        name: 'ViewEthnicity',
        component: () => import('../views/Ethnicities/ViewEthnicity.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'Ethnicities/Edit/:id',
        name: 'EditEthnicity',
        component: () => import('../views/Ethnicities/EditEthnicity.vue'),
        meta: { requiresAuth: true }
      },
      // LeaveTypes routes
      {
        path: 'LeaveTypes',
        name: 'LeaveTypes',
        component: () => import('../views/LeaveTypes/LeaveTypes.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'LeaveTypes/NewLeaveType',
        name: 'NewLeaveType',
        component: () => import('../views/LeaveTypes/NewLeaveType.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'LeaveTypes/:id',
        name: 'ViewLeaveType',
        component: () => import('../views/LeaveTypes/ViewLeaveType.vue'),
        meta: { requiresAuth: true }
      },
      {
        path: 'LeaveTypes/Edit/:id',
        name: 'EditLeaveType',
        component: () => import('../views/LeaveTypes/EditLeaveTypes.vue'),
        meta: { requiresAuth: true }
      },
            // Leaves routes
            {
              path: 'Leaves/EditLeaves',
              name: 'EditLeaves',
              component: () => import('../views/Leaves/EditLeave.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Leaves/NewLeave',
              name: 'NewLeave',
              component: () => import('../views/Leaves/NewLeave.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Leaves',
              name: 'Leaves',
              component: () => import('../views/Leaves/Leaves.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Leaves/AllLeaves',
              name: 'AllLeaves',
              component: () => import('../views/Leaves/AllLeaves.vue'),
              meta: { requiresAuth: true }
            },
            // {
            //   path: 'Leaves/:id',
            //   name: 'ViewLeaveType',
            //   component: () => import('../views/Leaves/ViewLeaveType.vue'),
            //   meta: { requiresAuth: true }
            // },
            // {
            //   path: 'Leaves/Edit/:id',
            //   name: 'EditLeaveType',
            //   component: () => import('../views/Leaves/EditLeaves.vue'),
            //   meta: { requiresAuth: true }
            // },
      
      {
        path: '/Login',
        name: 'Login',
        component: () => import('../views/Login.vue')
      },
      {
        path: 'test',
        name: 'test',
        component: () => import('../views/test/test.vue'),
        meta: { requiresAuth: true }

      },
    ]
  },
  {
    path: '/Login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/Login'
  }
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

// Navigation guard
router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
    next('/login');
  } else {
    next();
  }
});

export default router;
