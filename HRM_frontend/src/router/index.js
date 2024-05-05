import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import DepartmentsView from '../views/DepartmentsView.vue'
import CreateDepartment from '../pages/Departments/CreateDepartment.vue'
import DepartmentDetails from '../pages/Departments/DepartmentDetails.vue'
import EditDepartment from '../pages/Departments/EditDepartment.vue'
import QualificationsView from '../views/QualificationsView.vue'
import CreateQualification from '../pages/Qualifications/CreateQualification.vue'
import QualificationDetails from '../pages/Qualifications/QualificationDetails.vue'
import EditQualification from '../pages/Qualifications/EditQualification.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/departments',
      component: DepartmentsView,
      children: [
        {
          path: '', 
          name: 'Departments',
          component: DepartmentsView
        }
      ]
    },
    {
      path: '/departments/create-department',
      name: 'CreateDepartment',
      component: CreateDepartment
    },
    {
      path: '/departments/edit-department/:id',
      name: 'EditDepartment',
      component: EditDepartment
    },
    {
      path: '/departments/departmentDetails/:id',
      name: 'DepartmentDetails',
      component: DepartmentDetails
    },
    {
      path: '/qualifications',
      component: QualificationsView,
      children: [
        {
          path: '', 
          name: 'Qualifications',
          component: QualificationsView
        }
      ]
    },
    {
      path: '/qualifications/create-qualification',
      name: 'CreateQualification',
      component: CreateQualification
    },
    {
      path: '/qualifications/edit-qualification/:id',
      name: 'EditQualification',
      component: EditQualification
    },
    {
      path: '/qualifications/qualificationDetails/:id',
      name: 'QualificationDetails',
      component: QualificationDetails
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
