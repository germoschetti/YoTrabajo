import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  url:string;
  post$: Subject<number>;
  token:string
  accessHeader: any;
 
  constructor(
    private http:HttpClient,
    private _userService: UserService) {
    this.url = 'http://127.0.0.1:8000/api/';
    this.post$ = new Subject<number>();
    this.token = '';
   }

  getAllPosts(): Observable<any>{
    return this.http.get(this.url + 'posts/')
  }

  getPostById(id:number):Observable<object>{
    return this.http.get(this.url + 'posts/'+ id + '/')
  }

  getAllCategories(): Observable<any>{
    return this.http.get(this.url + 'categories/')
  }

  getPostsByCategory(id:number): Observable<any>{
    return this.http.get(this.url + `posts/?category=${id}`)
  }

  getComments(id:number): Observable<any>{
    return this.http.get(this.url+ `comments/?post=${id}`)
  }

  createComments(comment:any): Observable<any>{
    let currentSession = this._userService.currentSession()
    console.log(currentSession)
    this.accessHeader = new HttpHeaders({'Authorization': 'Bearer '+ currentSession});
    return this.http.post(this.url+ 'comments/', comment, {headers:this.accessHeader})
  }


  setPost(post: number): void {
    this.post$.next(post);
   
  }

  getPost(): Observable<number> {
    console.log('Desde el service devuelvo: ', this.post$)
    return this.post$.asObservable();
  }


}
