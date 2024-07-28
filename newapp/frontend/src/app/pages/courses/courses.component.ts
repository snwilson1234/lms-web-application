import { Component, OnInit } from '@angular/core';
import { CourseInfo } from '../../interface/course-info';
import { CommonModule, NgFor } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { ApiService } from '../../service/api.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [
    CommonModule,
    NgFor,
    MatCardModule,
    MatIconModule,
  ],
  templateUrl: './courses.component.html',
  styleUrl: './courses.component.scss',
  providers: [
    ApiService,
  ]
})
export class CoursesComponent implements OnInit {
  courses: Array<CourseInfo> = []

  constructor(
    private apiSerivce: ApiService
  ) {}

  private reformatCourseData(courseData: Array<CourseInfo>):
  Array<CourseInfo> {
    for (let course of courseData) {
      if (course.term === "SP") {
        course.term = "Spring";
      }
      else if (course.term === "SU") {
        course.term = "Summer";
      }
      else if (course.term == "FA") {
        course.term = "Fall";
      }
    }
    return courseData;
  }

  ngOnInit(): void {
    this.apiSerivce.getCourses().subscribe({
      next: (data) => {
        console.log("data received:", data);
        this.courses = this.reformatCourseData(data);
      },
      error: (error) => {
        console.error(error);
      },
      complete: () => {
        console.log("attempted to fetch courses");
      }
    });
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
