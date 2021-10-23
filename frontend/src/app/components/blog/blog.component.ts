import { Component, OnInit } from '@angular/core';
import { BlogService } from 'src/app/services/blog.service';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css']
})
export class BlogComponent implements OnInit {
  posts: any;
  categories:any;
  category:string;
  postDetail:any;
  constructor(
    private _blogService: BlogService
  ) {
    this.category = 'All';
  }

  ngOnInit(): void {
    this.getAllPosts();
    this.getAllCategories();
  }

  getAllPosts(){
    this._blogService.getAllPosts().subscribe(data=>{
      this.posts = data;
    })
  }

  getAllCategories(){
    this._blogService.getAllCategories().subscribe(data=>{
     this.categories = data;
    })
  }

  getPostsByCategory(category:any){
    this._blogService.getPostsByCategory(category).subscribe(data=>{
      this.posts = data
    });
  }

  getPostById(post:number){
    this._blogService.getPostById(post).subscribe(data=>{
    this.postDetail = data
    console.log(this.postDetail)
  })
  }

  showPost(post:number){
    this.getPostById(post)
    document.querySelector(".post")?.classList.add('post-active');
  }
  hidePost(){
    document.querySelector(".post")?.classList.remove('post-active');
  }

  /* UI */
  linkActive(e:any){
    let actualLi = e.target;
    this.category = actualLi.innerHTML;
    let li = document.querySelectorAll('.filter-links');
    for(let i = 0; i < li.length; i++){
      li[i].classList.remove('filter-container-active');
    }
    actualLi.classList.add('filter-container-active');
  }

}
