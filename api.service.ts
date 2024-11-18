import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:8000'; // FastAPI URL

  constructor(private http: HttpClient) {}

  getRootMessage(): Observable<any> {
    return this.http.get(`${this.apiUrl}/`);
  }
}