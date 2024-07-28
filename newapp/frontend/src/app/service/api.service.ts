import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, tap, throwError } from 'rxjs';


@Injectable({ providedIn: 'root'})
export class ApiService {
    private readonly apiUrl = 'http://localhost:8000';

    // // inject HttpClient into category service
    constructor(private http: HttpClient) { }
    

    // // Courses
    public getCourses(): Observable<any> {
        return this.http.get(`${this.apiUrl}/courses/`)
    }

    // // public postCourse(purchase: any): Observable<any> {
    // //     return this.http.post<Purchase>(`${this.apiUrl}/courses/`, course);
    // // }


}