import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-success',
  templateUrl: './success.component.html',
  styleUrls: ['./success.component.css']
})
export class SuccessComponent implements OnInit {
  success: string;
  show: boolean;
  subscription: Subscription;
  
  constructor(private _userService: UserService) {
    this.success = '';
    this.show = false;
    
    this.subscription = this._userService.getSuccess().subscribe(data => {
      this.success = data;
      this.showMessage();
    })
  }

  ngOnInit(): void {
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  showMessage() {
    this.show = true;
    document.querySelector('#alert-success')?.classList.add('success-alert')
    setTimeout(() => {
      this.show = false;
      document.querySelector('#alert-success')?.classList.remove('success-alert')
    }, 3000);
  }
}
