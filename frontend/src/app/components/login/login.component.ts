import { Component, OnInit } from '@angular/core';
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
  constructor(private _userService: UserService) {
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
    if (this.username.trim() == '') {
      alert('El nombre de usuario es un campo requerido');
    }
    else if (this.email.trim() == '') {
      alert('El email es un campo requerido');
    }
    else if (this.password.trim() == '') {
      alert('La contraseña es un campo requerido');
    }
    else {
      this.user = new User(this.email, this.password, this.username);
      this._userService.registerUser(this.user).subscribe(data => {
        form.reset();
      }, err => {
        if (err.error.email) {
          this._userService.setError('There is already a registered user with this email');
        }
        if (err.error.username) {
          this._userService.setError('This username is already in use');
        }
      })

    }
  }

  loginUser(form: any) {
    if (this.loginEmail.trim() == '') {
      alert('El email es un campo requerido')
    }
    else if (this.loginPassword.trim() == '') {
      alert('La contraseña es un campo requerido')
    }
    else {
      this.user = new User(this.loginEmail, this.loginPassword)
      this._userService.loginUser(this.user).subscribe(data => {
        this._userService.setToken(data.access)
        this.getActualUser()
        form.reset()
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
