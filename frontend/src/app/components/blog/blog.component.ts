import { Component, OnInit } from '@angular/core';
import { BlogService } from 'src/app/services/blog.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css']
})
export class BlogComponent implements OnInit {
  posts: any;
  currentPost: number;
  comments: any;
  categories: any;
  category: string;
  postDetail: any;
  contentPost: any;
  content: string;
  isLogged: boolean;
  constructor(
    private _blogService: BlogService,
    private _userService: UserService
  ) {
    this.category = 'All';
    this.currentPost = 0;
    this.content = '';
    this.isLogged = false
  }

  ngOnInit(): void {
    this.getAllPosts();
    this.getAllCategories();
  }

  getAllPosts() {
    this._blogService.getAllPosts().subscribe(data => {
      this.posts = data;
    })
  }

  getAllCategories() {
    this._blogService.getAllCategories().subscribe(data => {
      this.categories = data;
    })
  }

  getPostsByCategory(category: any) {
    if (category.value == 'All') {
      this.getAllPosts();
    } else {
      if (typeof (category) != 'number') {
        category = category.value;
      }
      this._blogService.getPostsByCategory(category).subscribe(data => {
        this.posts = data;
      });
    }

  }

  getPostById(post: number) {
    this._blogService.getPostById(post).subscribe(data => {
      this.postDetail = data
      this.contentPost = this.postDetail.content.split('~~')
    })
  }

  getComments() {
    this._blogService.getComments(this.currentPost).subscribe(data => {
      this.comments = data
    })
  }

  createComment(form:any) {
    let comment = {
      content: this.content,
      post: this.currentPost
    }
    if (this.content.trim() == '') {
      this._userService.setError('To make a comment you must write something in the comment box')
    } else {
      this._blogService.createComments(comment).subscribe(data => {
        this._userService.setSuccess('Your comment has been created successfully');
        form.reset()
        this.getComments()
      },
        err => {
          if (err.statusText == 'Unauthorized') {
            this._userService.setError('To make a comment you must be logged in')
          }
        })

    }

  }

  logged() {
    this._userService.getActaulUser().subscribe(data => {
      this.isLogged = true;
    }, err => {
      this._userService.setError('To make a comment you must be logged in')
    })
  }


  showPost(post: number) {
    this.currentPost = post;
    this.getPostById(post);
    this.getComments();
    document.querySelector(".post")?.classList.add('post-active');
  }
  hidePost() {
    document.querySelector(".post")?.classList.remove('post-active');
  }

  /* UI */
  linkActive(e: any) {
    let actualLi = e.target;
    this.category = actualLi.innerHTML;
    let li = document.querySelectorAll('.filter-links');
    for (let i = 0; i < li.length; i++) {
      li[i].classList.remove('filter-container-active');
    }
    actualLi.classList.add('filter-container-active');
  }

}
