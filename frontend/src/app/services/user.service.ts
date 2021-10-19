import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { User } from '../models/user/user.module';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  url: string;
  error$: Subject<string>;
  access$: Subject<string>;
  accessHeader:HttpHeaders;
  token:string;

  constructor(private http:HttpClient) { 
    this.url = 'http://127.0.0.1:8000/api/';
    this.error$ = new Subject<string>();
    this.access$ = new Subject<string>();
    this.accessHeader = new HttpHeaders;
    this.token = '';
  }

  registerUser(user:User):Observable<any>{
    return this.http.post(this.url + 'auth/register/', user);
  }

  loginUser(user:any):Observable<any>{
    return this.http.post(this.url + 'auth/login/', user);
  }

  getActaulUser(): Observable<any> {
    this.token = `${localStorage.getItem('token')}`;
    this.accessHeader = new HttpHeaders({'Authorization': 'Bearer '+this.token});
    return this.http.get(this.url + 'auth/me/', {headers: this.accessHeader});
  }

  /* Set shared variables as observable */
  setError(message: string): void {
    this.error$.next(message);
  }

  getError(): Observable<string> {
    return this.error$.asObservable();
  }

  setToken(token: string): void {
    localStorage.setItem('token', token);
    this.access$.next(token);
  }

  getToken(): Observable<string> {
    return this.access$.asObservable();
  }
}
