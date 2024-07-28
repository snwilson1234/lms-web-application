import { Component, Input, OnInit } from '@angular/core';
import { CourseInfo } from '../../interface/course-info';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../service/api.service';

@Component({
  selector: 'app-course',
  standalone: true,
  imports: [],
  templateUrl: './course.component.html',
  styleUrl: './course.component.scss'
})
export class CourseComponent implements OnInit {
  
  @Input() courseId!: number;
  
  courseInfo!: CourseInfo;

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService
  ) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.courseId = Number(params.get('courseId'))!;
    });

    this.apiService.getCourse(this.courseId).subscribe({
      next: (data) => {
        this.courseInfo = data;
      },
      error: (error) => {
        console.error(error);
      }
    })

  }
  
}
