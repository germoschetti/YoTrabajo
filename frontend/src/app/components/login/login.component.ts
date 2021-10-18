import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
/*   sign_in_btn = document.querySelector('#sign-in-btn')
  sign_up_btn = document.querySelector('#sign-up-btn')
  container = document.querySelector('.container') */
  constructor() { }

  ngOnInit(): void {
  }

  signUpMode(){
    document.querySelector('.container')?.classList.add("sign-up-mode")
  }

  signInMode(){
    document.querySelector('.container')?.classList.remove("sign-up-mode")
  }
  
  }
