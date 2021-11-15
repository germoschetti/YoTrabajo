import { Component, OnInit } from '@angular/core';
import { HostListener } from '@angular/core';
import { BlogService } from 'src/app/services/blog.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  video:any;
  verticalOffset:any;
  firstUrl:string;
  src:string;
  play:boolean;
  posts:any

  constructor(
    private _blogService: BlogService
  ) {
    this.play = false;
    this.firstUrl = "https://www.youtube.com/embed/onOEns_MnC4"
    this.src = this.firstUrl
    this.posts = [];
    this.getFourPosts()
  }

  ngOnInit(): void {
    this.video = document.querySelector('iframe')
    this.videoAutoPlay()
  }



  
/* AUTOPLAY VIDEO */
@HostListener("window:scroll", []) onWindowScroll() {
  this.verticalOffset = window.pageYOffset
  this.videoAutoPlay()
}

  videoAutoPlay() {
    let heightBrowser = window.innerHeight
    let heigthVideo = this.video.offsetHeight
    let min =  (this.getOffset(this.video).top - heightBrowser) + (heigthVideo / 1.5)
    let max =  this.getOffset(this.video).top + (heigthVideo / 2.7)
    let url = this.src + '?autoplay=1&mute=1'


    if( this.verticalOffset >= min && this.verticalOffset < max){
      if(this.play == false){
        this.src =  url
        this.play = true
      }
    }else{
      this.play = false
      this.src = this.firstUrl
    }
  }

  getOffset(el:any) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }

  getFourPosts(){
    this._blogService.getAllPosts().subscribe(data=>{
      for(let i = 0; i <= 3; i++){
        this.posts.push(data[i])
      }
    })
  }




}
