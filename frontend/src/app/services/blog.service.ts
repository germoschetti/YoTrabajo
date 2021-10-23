import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  url:string;
  post$: Subject<number>;
  constructor(private http:HttpClient) {
    this.url = 'http://127.0.0.1:8000/api/';
    this.post$ = new Subject<number>();
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


  setPost(post: number): void {
    this.post$.next(post);
   
  }

  getPost(): Observable<number> {
    console.log('Desde el service devuelvo: ', this.post$)
    return this.post$.asObservable();
  }


}
