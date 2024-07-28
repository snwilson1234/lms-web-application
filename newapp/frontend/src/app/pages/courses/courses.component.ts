import { Component, OnInit } from '@angular/core';
import { CourseInfo } from '../../interface/course-info';
import { CommonModule, NgFor } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [
    CommonModule,
    NgFor,
    MatCardModule,
    MatIconModule
  ],
  templateUrl: './courses.component.html',
  styleUrl: './courses.component.scss'
})
export class CoursesComponent implements OnInit {
  courses: Array<CourseInfo> = []

  ngOnInit(): void {
    this.courses = [
      {
        title : 'placeholder1',
        term  : 'Spring'
      },
      {
        title : 'placeholder2',
        term  : 'Spring'
      },
      {
        title : 'placeholder3',
        term  : 'Spring'
      },
    ]
  }

}
