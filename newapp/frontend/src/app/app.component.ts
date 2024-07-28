import { Component } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { AppHeaderComponent } from './shared/header/app-header.component';
import { CommonModule, NgFor } from '@angular/common';
import { ApiService } from './service/api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    AppHeaderComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = "";

  constructor(
    private router: Router,
    private apiService: ApiService
  ) {}

  setHeader() {
    let path = this.router.url.split('/')[1];
    if (path === "courses") {
      this.title = "Dashboard";
    } 
    else if (path === "course") {
      let courseId = this.router.url.split('/')[2];
      this.apiService.getCourse(Number(courseId)).subscribe({
        next: (data) => {
          this.title = data['title'];
        },
        error: (error) => {
          console.error(error);
        }
      })
    }
    else {
      this.title = "ERROR";
    }
  }
}
