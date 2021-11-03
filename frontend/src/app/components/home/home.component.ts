import { Component, OnInit } from '@angular/core';
import { HostListener } from '@angular/core';

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

  constructor(
  ) {
    this.play = false;
    this.firstUrl = "https://www.youtube.com/embed/onOEns_MnC4"
    this.src = this.firstUrl
  }

  ngOnInit(): void {
    this.video = document.querySelector('iframe')
    this.videoAutoPlay()
  }

  @HostListener("window:scroll", []) onWindowScroll() {
    this.verticalOffset = window.pageYOffset
    console.log('SRC ACTUAL: ', this.verticalOffset)
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
    console.log(
      ' MIN: ',min + '\n', 
      'MAX: ',max)
  }

  getOffset(el:any) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }




}
