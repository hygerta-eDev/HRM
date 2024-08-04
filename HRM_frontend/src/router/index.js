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
        meta: { requiresAuth: true}

      },
      {
        path: 'Companies/NewCompany',
        name: 'NewCompany',
        component: () => import('../views/Companies/NewCompany.vue'),
        // meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Companies/:id',
        name: 'ViewCompany',
        component: () => import('../views/Companies/ViewCompany.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Companies/Edit/:id',
        name: 'EditCompany',
        component: () => import('../views/Companies/EditCompany.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      // Departments routes
      {
        path: 'Departments',
        name: 'Departments',
        component: () => import('../views/Departments/Departments.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Departments/NewDepartment',
        name: 'NewDepartment',
        component: () => import('../views/Departments/NewDepartment.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Departments/:id',
        name: 'ViewDepartment',
        component: () => import('../views/Departments/ViewDepartment.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Departments/Edit/:id',
        name: 'EditDepartment',
        component: () => import('../views/Departments/EditDepartment.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      // JobPositions routes
      {
        path: 'JobPositions',
        name: 'JobPositions',
        component: () => import('../views/JobPositions/JobPositions.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'JobPositions/NewJobPosition',
        name: 'NewJobPosition',
        component: () => import('../views/JobPositions/NewJobPosition.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'JobPositions/:id',
        name: 'ViewJobPosition',
        component: () => import('../views/JobPositions/ViewJobPosition.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'JobPositions/Edit/:id',
        name: 'EditJobPosition',
        component: () => import('../views/JobPositions/EditJobPosition.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      // Qualifications routes
      {
        path: 'Qualifications',
        name: 'Qualifications',
        component: () => import('../views/Qualifications/Qualifications.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Qualifications/NewQualifications',
        name: 'NewQualifications',
        component: () => import('../views/Qualifications/NewQualifications.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Qualifications/:id',
        name: 'ViewQualifications',
        component: () => import('../views/Qualifications/ViewQualifications.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Qualifications/Edit/:id',
        name: 'EditQualifications',
        component: () => import('../views/Qualifications/EditQualifications.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      // Ethnicities routes
      {
        path: 'Ethnicities',
        name: 'Ethnicities',
        component: () => import('../views/Ethnicities/Ethnicities.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Ethnicities/NewEthnicity',
        name: 'NewEthnicity',
        component: () => import('../views/Ethnicities/NewEthnicity.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Ethnicities/:id',
        name: 'ViewEthnicity',
        component: () => import('../views/Ethnicities/ViewEthnicity.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'Ethnicities/Edit/:id',
        name: 'EditEthnicity',
        component: () => import('../views/Ethnicities/EditEthnicity.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      // LeaveTypes routes
      {
        path: 'LeaveTypes',
        name: 'LeaveTypes',
        component: () => import('../views/LeaveTypes/LeaveTypes.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'LeaveTypes/NewLeaveType',
        name: 'NewLeaveType',
        component: () => import('../views/LeaveTypes/NewLeaveType.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'LeaveTypes/:id',
        name: 'ViewLeaveType',
        component: () => import('../views/LeaveTypes/ViewLeaveType.vue'),
        meta: { requiresAuth: true, roles:[1]}

      },
      {
        path: 'LeaveTypes/Edit/:id',
        name: 'EditLeaveType',
        component: () => import('../views/LeaveTypes/EditLeaveTypes.vue'),
        meta: { requiresAuth: true, roles:[1]}

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
              path: 'Documents',
              name: 'Documents',
              component: () => import('../views/Documents/Documents.vue'),
              meta: { requiresAuth: true }
            },
            // {
            //   path: 'Ethnicities/NewEthnicity',
            //   name: 'NewEthnicity',
            //   component: () => import('../views/Ethnicities/NewEthnicity.vue'),
            //   meta: { requiresAuth: true }
            // },
            // {
            //   path: 'Ethnicities/:id',
            //   name: 'ViewEthnicity',
            //   component: () => import('../views/Ethnicities/ViewEthnicity.vue'),
            //   meta: { requiresAuth: true }
            // },
            // {
            //   path: 'Ethnicities/Edit/:id',
            //   name: 'EditEthnicity',
            //   component: () => import('../views/Ethnicities/EditEthnicity.vue'),
            //   meta: { requiresAuth: true }
            // },
            {
              path: 'Trainings',
              name: 'Trainings',
              component: () => import('../views/Trainings/Trainings.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Trainings/NewTraining',
              name: 'NewTraining',
              component: () => import('../views/Trainings/NewTraining.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Trainings/:id',
              name: 'ViewTraining',
              component: () => import('../views/Trainings/ViewTraining.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Trainings/Edit/:id',
              name: 'EditTraining',
              component: () => import('../views/Trainings/EditTraining.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Assessments',
              name: 'Assessments',
              component: () => import('../views/Assessments/Assessments.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Assessments/NewAssessment/:id',
              name: 'NewAssessment',
              component: () => import('../views/Assessments/NewAssessment.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Assessments/:id',
              name: 'ViewAssessment',
              component: () => import('../views/Assessments/ViewAssessment.vue'),
              meta: { requiresAuth: true }
            },
            {
              path: 'Assessments/Edit/:id',
              name: 'EditAssessment',
              component: () => import('../views/Assessments/EditAssessment.vue'),
              meta: { requiresAuth: true }
            },
            
      
      {
        path: '/Login',
        name: 'Login',
        component: () => import('../views/Login.vue')
      },
      {
        path: 'test',
        name: 'test',
        component: () => import('../views/test/test.vue'),
        // meta: { requiresAuth: true }

      },{
      path: 'Profile',
      name: 'Profile',
      component: () => import('../views/Profile/Profile.vue'),
      // meta: { requiresAuth: true }

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

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  const userRoles = JSON.parse(localStorage.getItem('roles') || '[]').map(Number);

  // console.log('isAuthenticated:', isAuthenticated);
  // console.log('userRoles:', userRoles);

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      // console.log('Not authenticated, redirecting to login');
      next('/login');
    } else {
      const requiredRoles = to.meta.roles || [];
      if (requiredRoles.length === 0 || requiredRoles.some(role => userRoles.includes(role))) {
        // console.log('Permission granted, proceeding to route');
        next();
      } else {
        // console.log('No permission, redirecting to unauthorized');
        next('/unauthorized');
      }
    }
  } else {
    next();
  }
});

export default router;