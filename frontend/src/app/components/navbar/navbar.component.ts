import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  user:string;
  constructor(
    private _userService: UserService
  ) {
    this.user = '';
    this._userService.getActaulUser().subscribe(data=>{
      this.user = data.username
    })
   }

  ngOnInit(): void {
  }
  showAndHideMenu() {
    const menuItems = document.querySelector('.menu-items');
    menuItems?.classList.toggle('show');
  }

}
