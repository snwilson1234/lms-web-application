import { Routes } from '@angular/router';
import { CoursesComponent } from './pages/courses/courses.component';
import { CourseComponent } from './pages/course/course.component';

export const routes: Routes = [
    {
        path: '',
        redirectTo: '/courses',
        pathMatch: 'full'
    },
    {
        path: 'courses',
        component: CoursesComponent,
    },
    {
        path: 'course/:courseId',
        component: CourseComponent
    }
];
