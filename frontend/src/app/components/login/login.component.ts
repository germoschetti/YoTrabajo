import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { User } from 'src/app/models/user/user.module';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string;
  email: string;
  password: string;
  loginEmail: string;
  loginPassword: string;
  user: User
  subscription: Subscription
  actualUser: string;
  token: string;
  constructor(
    private _userService: UserService,
    private router:Router) {
    this.username = '';
    this.email = '';
    this.password = '';
    this.loginEmail = '';
    this.loginPassword = '';
    this.user = new User('', '', '');
    this.token='';
    this.actualUser='';
    /* GET ACTUAL TOKEN */
    this.subscription = this._userService.getToken().subscribe(data => {
      this.token = data;
    });
  }

  ngOnInit(): void {
  }

  registerUser(form: any) {
    if (this.username.trim() == '' || this.email.trim() == '' || this.password.trim() == '') {
      this._userService.setError('All fields are required');
    }

    else {
      this.user = new User(this.email, this.password, this.username);
      this._userService.registerUser(this.user).subscribe(data => {
        this._userService.setSuccess('Your account has been created successfully');
        form.reset();
        
      }, err => {
        console.log('err', err.error)
        if (err.error.username) {
          this._userService.setError('This username is already in use');
        }
        else if (err.error.email[0] == 'Enter a valid email address.') {
          this._userService.setError('Enter a valid email address.');
        }
        else if (err.error.email) {
          console.log(err.error.email);
          this._userService.setError('There is already a registered user with this email');
        }
      })

    }
  }

  loginUser(form: any) {
    if (this.loginEmail.trim() == '' || this.loginPassword.trim() == '') {
      this._userService.setError('All fields are required');
    }
     else {
      this.user = new User(this.loginEmail, this.loginPassword)
      this._userService.loginUser(this.user).subscribe(data => {
        this._userService.setToken(data.access)
        this.getActualUser()
        form.reset()
        this.router.navigate(['home'])
      }, err => {
        console.log("THE ERROR IS:", err)
        this._userService.setError('The credentials are wrong')
      })

    }

  }

  getActualUser() {
    this._userService.getActaulUser().subscribe(data => {
      this.actualUser = data.username;
    }, err => {
      console.log(err.error);
    })
  }

  logOut() {
    localStorage.removeItem('token');
    this.subscription.unsubscribe();
    this.actualUser = '';
  }
  /* UI */
  signUpMode() {
    document.querySelector('.container')?.classList.add("sign-up-mode");
  }

  signInMode() {
    document.querySelector('.container')?.classList.remove("sign-up-mode");
  }


}
