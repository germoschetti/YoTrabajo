import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-error',
  templateUrl: './error.component.html',
  styleUrls: ['./error.component.css']
})
export class ErrorComponent implements OnInit {

  error: string;
  mostrar: boolean;
  subscription: Subscription;
  constructor(private _userService: UserService) {
    this.error = '';
    this.mostrar = false;
    
    this.subscription = this._userService.getError().subscribe(data => {
      this.error = data;
      this.showMessage();
    })
  }

  ngOnInit(): void {
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  showMessage() {
    this.mostrar = true;
    setTimeout(() => {
      this.mostrar = false;
    }, 3000);
  }

}
